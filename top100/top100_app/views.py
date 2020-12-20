from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import ContactForm
from .models import Contact, Genre, Author, Song, Album
from . import views

def index (request) :
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
        'form' : form
    }
    return render(request, "index.html", context)

def contact (request) :
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
        'form' : form
    }
    return render(request, "contact.html", context)

def genre (request) :
    genres = get_list_or_404(Genre.objects.order_by('name'))
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
        'form' : form
    }
    return render(request, "genre.html", context)

def author (request) :
    authors = get_list_or_404(Author.objects.order_by('name'))
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
        'form' : form
    }
    return render(request, "author.html", context)

def album (request) :
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
        'form' : form
    }
    return render(request, "album.html", context)

def about (request) :
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
        'form' : form
    }
    return render(request, "about.html", context)

def genre_details(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
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
    song = Song.objects.filter(genre=get_object_or_404(Genre, pk=genre_id)).order_by('name')
    context = {
        'genre': genre,
        'form' : form,
        'song_list' : song
    }
    return render(request, "genre_details.html", context)

def author_details(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
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
    song = Song.objects.filter(author=get_object_or_404(Author, pk=author_id)).order_by('name')
    context = {
        'author': author,
        'form' : form,
        'song_list' : song
    }
    return render(request, "author_details.html", context)

def song_details(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
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
        'form' : form,
    }
    return render(request, "song_details.html", context)