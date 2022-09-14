from django.shortcuts import render, redirect
from Messages.forms import SendMessageForm, SearchUserForm
from django.db.models import Q
from Messages.models import Messages
from django.contrib.auth.models import User
from datetime import datetime


# Create your views here.
from UserAdmin.models import Profile


def messenger(request, user_id):

    current_usr = request.user
    other_usr = User.objects.get(id=user_id)

    if request.method == 'POST':
        if 'send_message' in request.POST:
            form = SendMessageForm(request.POST)

            if form.is_valid():
                info = form.cleaned_data
                message = Messages(timestamp=datetime.now(), sender=current_usr, receiver=other_usr, message=info['message'])
                message.save()
                return redirect('MessagesMessenger', user_id=other_usr.id)

    """
    Q objects can be combined using the &, |, and ^ operators. When an operator is used on two Q objects, it yields a new Q object.
    For example, this statement yields a single Q object that represents the “OR” of two "question__startswith" queries:
    Q(question__startswith='Who') | Q(question__startswith='What')This is equivalent to the following SQL WHERE clause:
    WHERE question LIKE 'Who%' OR question LIKE 'What%'
    """
    if request.POST and 'search_user' in request.POST:
        form = SearchUserForm(request.POST)

        if form.is_valid():
            filter_string = form.cleaned_data['user_name']
            filtered = True
            search_form = SearchUserForm({'user_name': filter_string})
            users = User.objects.filter(Q(first_name__icontains=filter_string) | Q(last_name__icontains=filter_string))

    else:
        filtered = False
        search_form = SearchUserForm()
        users = User.objects.select_related('profile').exclude(id=current_usr.id)

    messages = Messages.objects.filter((Q(receiver=current_usr.id) & Q(sender=other_usr.id)) | (Q(receiver=other_usr.id) & Q(sender=current_usr.id))).order_by('timestamp')


    contexto = {
        'users': users,
        'messages': messages,
        'current_usr': current_usr,
        'other_usr': other_usr,
        'message_form': SendMessageForm(),
        'search_form': search_form,
        'filtered': filtered,
    }
    return render(request, 'Messages/messenger.html', contexto)