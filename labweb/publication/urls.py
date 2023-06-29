from django.urls import path

from . import views

urlpatterns = [
    path('journal/', views.index, name='publications'),
    # ex: /projects/name
    path('<int:pub_id>/', views.detail, name="detail"), 
    path('conference/', views.conference, name='conference'),
]