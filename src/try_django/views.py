from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
def home_page(request):
    title = 'Home page <3'
    return render(request, "home.html", {'title':title,})

def about_page(request):
    return render(request, "about.html", {'title':'about us',})

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
    'title':'contact us', 'form': form
    }
    return render(request, "form.html", context)
