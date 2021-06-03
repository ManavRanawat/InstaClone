"""instaclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import urls
<<<<<<< HEAD
from posts import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    path('',include('posts.urls')),
=======

from chats import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),

    path('',include('chats.urls')),
>>>>>>> 80bb199a7a6259f7ebe3116dfcfdb2d4f8cc776a
]
