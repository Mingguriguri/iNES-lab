from django.urls import path
from awards import views as awards_view

urlpatterns = [
    path('awards/', awards_view.ai_award, name='ai_award'),
    # path('projects/', project_views.ai_projects, name='ai_projects'),
    # path('notices/', notice_views.ai_notices, name='ai_notices'),
    # path('gallery/', gallery_views.ai_gallery, name='ai_gallery'),
]
