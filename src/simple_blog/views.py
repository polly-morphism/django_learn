from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.http import Http404
# Create your views here.

def blog_post_detail_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_post_detail_page.html"
    context = {"object": obj,}
    return render(request, template_name, context)
