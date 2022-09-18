from django.shortcuts import render
from Pages.forms import *
from Pages.models import *
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import datetime


def index(request):
    publications = Pages.objects.all()
    context = {
            'publication_list': get_pages,
            'publication_form': publications
        } 
    return render(request, 'index.html', context)

def get_pages(request):
    publications = Pages.objects.all()
    context = {
            'publication_list': publications
        } 
    return render(request, 'Pages/Pages.html', context)

def get_page(request, id):
    publication = Pages.objects.get(id=id)
    context = {
        'publication': publication
    } 

    return render(request, 'Pages/view.html', context)

@login_required
def delete_page(request,id):
    Pages.objects.get(id=id).delete()
    return redirect('viewPages')

@login_required
def update_page(request, id):

    page = Pages.objects.get(id=id)
    

    if request.method == 'POST':
        page_form = PagesForm(request.POST, request.FILES)

        if page_form.is_valid():
            data = page_form.cleaned_data
            page.title = data.get('title')
            page.subject = data.get('subject')
            page.imagen = data.get('imagen')
            page.content = data.get('content')
            page.save()
            return redirect('viewPages')

    page_form_context = PagesForm(
        initial={
            'title': page.title, 
            'imagen': page.imagen, 
            'subject': page.subject, 
            'content': page.content
        }
    )
    context = {
        'publication_form': page_form_context
    } 

    return render(request, 'Pages/update.html', context)


@login_required
def create_page(request):
    user = request.user
    if request.method == 'POST':
        form_publication = PagesForm(request.POST, request.FILES)

        if form_publication.is_valid():
            
            data = form_publication.cleaned_data
            page = Pages(title=data.get('title'), subject=data.get('subject'), imagen=data.get('imagen'), content=data.get('content'), author_id=user.id, date_create = datetime.datetime.now().strftime("%Y-%m-%d"))
            page.save()
            return redirect('viewPages')
            

    publication_form = PagesForm({'author':user.username})
    context = {
        'publication_form': publication_form
    } 

    return render(request, 'Pages/create.html', context)