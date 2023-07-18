from django.urls import path

from . import views

urlpatterns = [
    path('', views.filter_by_degree, name='index'),
    path('filter/', views.filter_by_degree, name='filter_by_degree'),  # Add this line

]