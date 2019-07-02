from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.http import Http404
# Create your views here.


def blog_post_list_view(request):
    #lists out objects
    qs = BlogPost.objects.all() #list of python objects
    #can be filtered .filter(...)
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

#CRUD create-retrieve-update-dalete

def blog_post_create_view(request):
    #create objects
    template_name = 'blog/create.html'
    context = {'form': None}
    return render(request, template_name, context)


def blog_post_retrieve_view(request, slug):
    #detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/retrieve.html'
    context = {"object": obj,}
    return render(request, template_name, context)


def blog_post_update_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/update.html'
    context = {"object": obj, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = {"object": obj,}
    return render(request, template_name, context)
