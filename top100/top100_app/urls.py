from django.urls import path

from . import views

urlpatterns = [
        path ('', views.index, name = 'index'),
        path ('index.html', views.index, name = 'index'),
        path ('contact.html', views.contact, name = 'contact'),
        path ('genero.html', views.genero, name = 'genero'),
        path ('album.html', views.album, name = 'album'),
        path ('about.html', views.about, name = 'about'),

]
