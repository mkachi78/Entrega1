from django.urls import path
from Messages.views import *

urlpatterns = [
    path('messenger/<int:user_id>', messenger, name='MessagesMessenger'),
]


