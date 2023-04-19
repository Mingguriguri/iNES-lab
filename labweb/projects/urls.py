from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='projects'),
    # ex: /projects/name
    path('<int:article_id>/', views.detail, name="detail"), 
]