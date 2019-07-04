from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.http import Http404
from .forms import *
# Create your views here.


def blog_post_list_view(request):
    #lists out objects
    qs = BlogPost.objects.all() #list of python objects
    #can be filtered .filter(...)
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

#CRUD create-retrieve-update-dalete


#@login_required
@staff_member_required
# Because of the decorators request.user will return smth
def blog_post_create_view(request):
    #create objects
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        form.save() #can't use it unless it's a model
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context)


def blog_post_retrieve_view(request, slug):
    #detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/retrieve.html'
    context = {"object": obj,}
    return render(request, template_name, context)



@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {"title": f"Update {obj.title}", "form": form,}
    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('/blog')
    context = {"object": obj,}
    return render(request, template_name, context)
