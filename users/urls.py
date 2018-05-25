"""leaning_logs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

"""Определяет схемы URL для learning_logs."""
app_name = 'users'

from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    #Страница входа
    path(r'login/', login, {'template_name': 'users/login.html'}, name='login'),
    #Страница выхода
    path(r'logout/', views.logout_view, name='logout'),
    #Страница регистрации
    path(r'register/', views.register, name='register')
]
