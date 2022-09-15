from django.contrib.auth.views import LogoutView
from django.urls import path
from UserAdmin.views import *

urlpatterns = [
    path('login/', login_request, name='UserLogin'),
    path('register/', register, name='UserRegister'),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='UserLogout'),
    path('view_profile', view_profile, name='ViewProfile'),
    path('edit_user', edit_user, name='EditUser'),
    path('edit_profile', edit_profile, name='EditProfile'),
    path('edit_image', edit_image, name='EditImage'),
    path('change_password', change_password, name='ChangePassword'),
]