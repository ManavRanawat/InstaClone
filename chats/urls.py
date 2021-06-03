from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views as chat_views
# from . views import Graph
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('chat/', chat_views.view_chats, name='view_chats'),
    path('detail_chats/<str:username>', chat_views.detail_chat, name='detail_chats'),
    path('new_chat/', TemplateView.as_view(template_name="new_chat.html") , name='new_chat'),
    path('graphs/', chat_views.make_graph, name='graphs'),
]