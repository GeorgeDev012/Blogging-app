"""Defines URL patterns for learning_logs."""

from django.urls import path, re_path

from . import views

app_name='blogs'

urlpatterns = [
    # Home page
    re_path(r'^$', views.index, name='index'),

    # Show blog posts
    re_path(r'^post/(?P<blog_post_id>\d+)$', views.blog_post, name='blog_post'),
    
    # Page for adding a new blog post
    re_path(r'^new_blog_post/$', views.new_blog_post, name='new_blog_post'),

    # Page for editing a blog post
    re_path(r'^edit_blog_post/(?P<blog_post_id>\d+)/$', views.edit_blog_post, name='edit_blog_post'),
    ]