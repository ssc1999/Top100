from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import ContactForm
from .models import Contact, Genre, Author, Song, Album
from . import views

def index (request) :
    songs_date = get_list_or_404(Song.objects.order_by('date')[: 4])
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contacto = Contact()
            contacto.name = form.cleaned_data["name"]
            contacto.phone = form.cleaned_data["phone"]
            contacto.mail = form.cleaned_data["mail"]
            contacto.message = form.cleaned_data["message"]
            contacto.save()
        return HttpResponseRedirect(reverse(views.index))
    context = {
        'song_date_list' : songs_date,
        'form' : form
    }
    return render(request, "index.html", context)

def contact (request) :
    songs_date = get_list_or_404(Song.objects.order_by('date')[: 4])
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contacto = Contact()
            contacto.name = form.cleaned_data["name"]
            contacto.phone = form.cleaned_data["phone"]
            contacto.mail = form.cleaned_data["mail"]
            contacto.message = form.cleaned_data["message"]
            contacto.save()
        return HttpResponseRedirect(reverse(views.contact))
    context = {
        'song_date_list' : songs_date,
        'form' : form
    }
    return render(request, "contact.html", context)

def genre (request) :
    genres = get_list_or_404(Genre.objects.order_by('name'))
    songs_date = get_list_or_404(Song.objects.order_by('date')[: 4])
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contacto = Contact()
            contacto.name = form.cleaned_data["name"]
            contacto.phone = form.cleaned_data["phone"]
            contacto.mail = form.cleaned_data["mail"]
            contacto.message = form.cleaned_data["message"]
            contacto.save()
        return HttpResponseRedirect(reverse(views.index))
    context = {
        'genre_list': genres,
        'song_date_list' : songs_date,
        'form' : form
    }
    return render(request, "genre.html", context)

def author (request) :
    authors = get_list_or_404(Author.objects.order_by('name'))
    songs_date = get_list_or_404(Song.objects.order_by('date')[: 4])
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contacto = Contact()
            contacto.name = form.cleaned_data["name"]
            contacto.phone = form.cleaned_data["phone"]
            contacto.mail = form.cleaned_data["mail"]
            contacto.message = form.cleaned_data["message"]
            contacto.save()
        return HttpResponseRedirect(reverse(views.index))
    context = {
        'author_list': authors,
        'song_date_list' : songs_date,
        'form' : form
    }
    return render(request, "author.html", context)

def album (request) :
    albums = get_list_or_404(Album.objects.order_by('name'))
    songs_date = get_list_or_404(Song.objects.order_by('date')[: 4])
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contacto = Contact()
            contacto.name = form.cleaned_data["name"]
            contacto.phone = form.cleaned_data["phone"]
            contacto.mail = form.cleaned_data["mail"]
            contacto.message = form.cleaned_data["message"]
            contacto.save()
        return HttpResponseRedirect(reverse(views.index))
    context = {
        'album_list': albums,
        'song_date_list' : songs_date,
        'form' : form
    }
    return render(request, "album.html", context)

def about (request) :
    songs_date = get_list_or_404(Song.objects.order_by('date')[: 4])
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contacto = Contact()
            contacto.name = form.cleaned_data["name"]
            contacto.phone = form.cleaned_data["phone"]
            contacto.mail = form.cleaned_data["mail"]
            contacto.message = form.cleaned_data["message"]
            contacto.save()
        return HttpResponseRedirect(reverse(views.index))
    context = {
        'song_date_list' : songs_date,
        'form' : form
    }
    return render(request, "about.html", context)

def genre_details(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    song = Song.objects.filter(genre=get_object_or_404(Genre, pk=genre_id)).order_by('name')
    songs_date = get_list_or_404(Song.objects.order_by('date')[: 4])
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contacto = Contact()
            contacto.name = form.cleaned_data["name"]
            contacto.phone = form.cleaned_data["phone"]
            contacto.mail = form.cleaned_data["mail"]
            contacto.message = form.cleaned_data["message"]
            contacto.save()
        return HttpResponseRedirect(reverse(views.index))
    context = {
        'genre': genre,
        'song_list' : song,
        'song_date_list' : songs_date,
        'form' : form
    }
    return render(request, "genre_details.html", context)

def author_details(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    song = Song.objects.filter(author=get_object_or_404(Author, pk=author_id)).order_by('name')
    songs_date = get_list_or_404(Song.objects.order_by('date')[: 4])
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contacto = Contact()
            contacto.name = form.cleaned_data["name"]
            contacto.phone = form.cleaned_data["phone"]
            contacto.mail = form.cleaned_data["mail"]
            contacto.message = form.cleaned_data["message"]
            contacto.save()
        return HttpResponseRedirect(reverse(views.index))
    context = {
        'author': author,
        'song_list' : song,
        'song_date_list' : songs_date,
        'form' : form
    }
    return render(request, "author_details.html", context)

def song_details(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    songs_date = get_list_or_404(Song.objects.order_by('date')[: 4])
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contacto = Contact()
            contacto.name = form.cleaned_data["name"]
            contacto.phone = form.cleaned_data["phone"]
            contacto.mail = form.cleaned_data["mail"]
            contacto.message = form.cleaned_data["message"]
            contacto.save()
        return HttpResponseRedirect(reverse(views.index))
    context = {
        'song': song,
        'song_date_list' : songs_date,
        'form' : form
    }
    return render(request, "song_details.html", context)