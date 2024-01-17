from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ver3/', views.ver3, name='ver3'),
    # ex: /projects/name
]