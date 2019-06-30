from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    title = 'Home page <3'
    return render(request, "home.html", {'title':title,})

def about_page(request):
    return render(request, "about.html", {'title':'about us',})

def contact_page(request):
    return render(request, "hello_world.html", {'title':'contact us',})
