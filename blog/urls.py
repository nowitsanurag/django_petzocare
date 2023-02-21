from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("postComment/", views.postComment, name="postComment"),
    path('blog/', views.index,name="BlogHome"),
    # path('<slug:slug>/', views.blogPost, name="blogPost"),
    path("blog/blogpost/<int:id>", views.blogPost, name="blogPost"),
]
