from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from sistem.views import search, sign_up, contact, index, aboutUs
# from Pages.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('sign_up/', sign_up, name='signUp'),
    path('contact/', contact, name='contact'),
    path('search/', search, name='search'),
    path('UserAdmin/', include('UserAdmin.urls')),
    path('Messages/', include('Messages.urls')),
    path('AboutUs/', aboutUs, name ='aboutUs'),
    path('Pages/', include('Pages.urls')),
    # path('Pages/', get_pages, name ='viewPages'),
    # path('Page/create', create_page, name ='createPage'),
    # path('Page/delete/<int:id>', delete_page, name='deletePage'),
    # path('Page/update/<int:id>', update_page, name='updatePage'),
    # path('Page/view/<int:id>' , get_page, name='viewPage')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)