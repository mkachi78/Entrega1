from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, loader
from sistem.forms import *
from sistem.models import *
from django.db.models import Q

def sign_up(request):
    
    if request.method == 'POST':
        form_sign = UserForm(request.POST)

        if form_sign.is_valid():
            data = form_sign.cleaned_data
            user = User(name=data.get('name'), last_name=data.get('last_name'), age=data.get('age'), email=data.get('email'))
            user.save()
        
    context = {
            'user_form': UserForm()
        }    

    return render(request, 'apps/signUp.html', context)

def contact(request):

    if request.method == 'POST':
        form_contact = ContactForm(request.POST)

        if form_contact.is_valid():
            data = form_contact.cleaned_data
            contact = Contact(name=data.get('full_name'), email=data.get('email'), subject=data.get('subject'), message=data.get('message'))
            contact.save()
        
    context = {
            'contact_form': ContactForm()
        } 

    return render(request, 'apps/contact.html', context)

def index(request):
    if request.method == 'POST':
            form_publication = PublicationForm(request.POST)

            if form_publication.is_valid():
                data = form_publication.cleaned_data
                publication = Publication(author=data.get('author'), subject=data.get('subject'), content=data.get('content'))
                publication.save()
    publications = Publication.objects.all()    
    context = {
            'publication_list': publications,
            'publication_form': PublicationForm()
        } 

    return render(request, 'index.html', context)

def search(request):
    post_search = set()
    if request.method == 'POST':
        content = request.POST.get('search_values')
        post_search= Publication.objects.filter(Q (author__icontains=content) | Q(subject__icontains=content)  | Q(content__icontains=content))
   
    context={
         'myForm':SearchForm(),
        'posts':post_search,
        }
    return render( request ,'apps/search.html',context)


def aboutUs(request):
    return render (request, 'apps/about.html')