from django.urls import path

from . import views

urlpatterns = [
        path ('', views.index, name = 'index'),
        path ('contact', views.contact, name = 'contact'),
        path ('genre', views.genre, name = 'genre'),
        path ('album', views.album, name = 'album'),
        path ('about', views.about, name = 'about'),
        path ('author', views.author, name = 'author'),
        path ('genre/<int:genre_id>/', views.genre_details, name = 'genre_details'),
        path ('author/<int:author_id>/', views.author_details, name = 'author_details')
]
