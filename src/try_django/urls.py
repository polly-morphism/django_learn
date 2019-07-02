from django.contrib import admin
from django.urls import path, include
from simple_blog.views import blog_post_create_view
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog-new/', blog_post_create_view),
    path('about/', about_page),
    path('contact/', contact_page),
    path('', home_page),
    path('blog/', include('simple_blog.urls')),
]
