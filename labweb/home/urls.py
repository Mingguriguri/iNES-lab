from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # ex: /projects/name
]