from django.contrib import admin
from django.urls import path,include
from . import views as post_views
urlpatterns = [
    path('addpost/',post_views.PostCreateView.as_view(),name="add_post"),
    path('viewpost/<int:pk>',post_views.display_post,name="view_post"),
    path('viewall/',post_views.viewall)
]