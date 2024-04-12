from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'), # 현재 사용중인 버전
    # ex: /projects/name
]