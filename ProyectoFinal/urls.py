from django.contrib import admin 
from django.urls import path
from sistem.views import search, sign_up, contact, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='home'),
    path('sign_up/', sign_up, name='signUp'),
    path('contact/', contact, name='contact'),
    path('search/',search,name='search'),
]
