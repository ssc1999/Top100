from django.urls import path, include
from . import views

urlpatterns = [
        path('i18n/', include('django.conf.urls.i18n')),
        path ('', views.index, name = 'index'),
        path ('contact', views.contact, name = 'contact'),
        path ('genre', views.genre, name = 'genre'),
        path ('album', views.album, name = 'album'),
        path ('about', views.about, name = 'about'),
        path ('author', views.author, name = 'author'),
        path ('genre/<int:genre_id>/', views.genre_details, name = 'genre_details'),
        path ('author/<int:author_id>/', views.author_details, name = 'author_details'),
        path ('song/<int:song_id>/', views.song_details, name = 'song_details'),
        path ('album/<int:album_id>/', views.album_details, name = 'album_details'),
]
