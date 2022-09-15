Aplicación de manejo de usuario

Funciones implementadas:

login: http://localhost:8000/UserAdmin/login

logout: http://localhost:8000/UserAdmin/logout

Visualización de perfil http://localhost:8000/UserAdmin/view_profile


Desde la visualización del perfil se pueden modificar los datos del usuario separados en tres grupos:

Cambio de imagen:
desde: http://localhost:8000/UserAdmin/edit_image

Edición de datos básicos de usuario (username, first_name, last_name y email):
desde: http://localhost:8000/UserAdmin/edit_user

Edición de datos de perfil (webpage, description):
desde: desde: http://localhost:8000/UserAdmin/edit_profile

Cambio de contraseña:
desde: http://localhost:8000/UserAdmin/edit_password

TODO:

-Mejorar estética de view_profile
-Incluir info de usuario logueado y navegación en la barra de navegación
-Opcional, agregar mas campos al perfil: edad, fecha de nacimiento, país etc.

