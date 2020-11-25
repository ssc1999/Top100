from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . import views

def index (request) :
    return render(request, "index.html")

def contact (request) :
    return render(request, "contact.html")

def blog (request) :
    return render(request, "blog.html")

def album (request) :
    return render(request, "album.html")

def about (request) :
    return render(request, "about.html")