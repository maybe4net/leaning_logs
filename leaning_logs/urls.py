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
app_name = 'learning_logs'

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # Домашняя страница
    path(r'', views.index, name='index'),
    #Вывод всех тем
    path(r'topics/', views.topics, name='topics'),
    #Страница с подробной информацией по отдельной теме
    path(r'topics/<int:topic_id>/', views.topic, name='topic'),
    # Страница для добавления новой темы
    path(r'new_topic/', views.new_topic, name='new_topic'),
    # Страница для добавления новой записи
    path(r'new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Страница для редактирования записи
    path(r'edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]
