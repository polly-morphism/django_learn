from django.contrib import admin
from django.urls import path
from simple_blog.views import *
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/<str:slug>/', blog_post_detail_page),
    path('about/', about_page),
    path('contact/', contact_page),
    path('', home_page),
]
