from django.urls import path

from . import views

urlpatterns = [
    path('', views.projects_list, name='projects-list'),
]