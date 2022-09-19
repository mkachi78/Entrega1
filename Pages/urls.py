from django.urls import path
from Pages.views import *

urlpatterns = [
    path('', get_pages, name ='viewPages'),
    path('view/myPages/userId/<int:id>', get_my_pages, name ='viewMyPages'),
    path('create', create_page, name ='createPage'),
    path('delete/<int:id>', delete_page, name='deletePage'),
    path('update/<int:id>', update_page, name='updatePage'),
    path('view/<int:id>' , get_page, name='viewPage')
]