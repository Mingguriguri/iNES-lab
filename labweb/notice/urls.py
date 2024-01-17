from django.urls import path

from . import views

urlpatterns = [
    path('', views.notice_list, name='notice_list'),
]

