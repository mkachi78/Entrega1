from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from UserAdmin.forms import UserRegisterForm, ProfileEditForm, UserEditForm, ImageEditForm, UserLoginForm
from UserAdmin.models import Profile


def login_request(request):

    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')
                return redirect('home')
            else:
                messages.info(request, 'inicio de sesion fallido!')
                return redirect('UserLogin')
        else:
            messages.info(request, 'inicio de sesion fallido!')
            return redirect('UserLogin')

    contexto = {
        'form': UserLoginForm(),
        'user_cmd': 'Ingreso de usuario'
    }
    return render(request, 'UserAdmin/login.html', contexto)


def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            reg_user = form.save()
            profile = Profile(user=reg_user, imagen='profile/default.jpg', webpage='', description='')
            profile.save()
            messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
            return redirect('home')

        else:

            messages.info(request, 'Tu usuario no pudo ser registrado!')
            messages.info(request, form.error_messages)
            return redirect('UserRegister')

    contexto = {
        'form': UserRegisterForm(),
        'user_cmd': 'Registro de Usuario'
    }

    return render(request, 'UserAdmin/login.html', contexto)

@login_required
def edit_user(request):

    user = request.user

    if request.method == 'POST':

        form = UserEditForm(request.POST, request.FILES)

        if form.is_valid():

            #Datos que se modificaran
            info = form.cleaned_data

            user.first_name = info['first_name']
            user.last_name = info['last_name']
            user.email = info['email']
            user.save()

            messages.info(request, 'Perfil actualizado correctamente!')
            return redirect('ViewProfile')

        else:
            messages.info(request, 'El perfil no pudo ser actualizado!')
            #messages.info(request, form.error_messages)
            return redirect('EditUser')

    user = request.user
    contexto = {
            'form': UserEditForm(
                {'first_name': user.first_name,
                 'last_name': user.last_name,
                 'email': user.email}),
            'title': 'Editar Usuario'
                }
    return render(request, 'UserAdmin/edit_profile.html', contexto)


@login_required
def edit_profile(request):

    user = request.user

    if request.method == 'POST':

        form = ProfileEditForm(request.POST, request.FILES)

        if form.is_valid():

            #Datos que se modificaran
            info = form.cleaned_data

            user.profile.webpage = info['webpage']
            user.profile.description = info['description']
            user.profile.save()

            messages.info(request, 'Perfil actualizado correctamente!')
            return redirect('ViewProfile')

        else:
            messages.info(request, 'El perfil no pudo ser actualizado!')
            #messages.info(request, form.error_messages)
            return redirect('EditProfile')

    user = request.user
    contexto = {
            'form': ProfileEditForm(
                {'webpage': user.profile.webpage,
                'description': user.profile.description}),
                'title': 'Editar perfil'
                }
    return render(request, 'UserAdmin/edit_profile.html', contexto)

@login_required
def edit_image(request):

    user = request.user

    if request.method == 'POST':

        form = ImageEditForm(request.POST, request.FILES)

        if form.is_valid():

            #Datos que se modificaran
            info = form.cleaned_data

            user.profile.imagen = info['imagen']
            user.profile.save()

            messages.info(request, 'Perfil actualizado correctamente!')
            return redirect('ViewProfile')

        else:
            #messages.info(request, 'El perfil no pudo ser actualizado!')
            #messages.info(request, form.error_messages)
            return redirect('EditImage')

    user = request.user
    contexto = {
            'form': ImageEditForm(
                {'imagen': user.profile.imagen}),
            'title': 'Editar Imagen'
                }
    return render(request, 'UserAdmin/edit_profile.html', contexto)

@login_required
def view_profile(request):

    return render(request, 'UserAdmin/view_profile.html')


@login_required
def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.info(request, 'Password modificado con éxito')
            return redirect('ViewProfile')

        else:
            messages.info(request, 'Error al cambiar el password!')
            messages.info(request, form.error_messages)
            return redirect('ChangePassword')

    contexto = {
        'form': PasswordChangeForm(user=request.user),
        'title': 'Cambio de Password'
    }
    return render(request, 'UserAdmin/edit_profile.html', contexto)

