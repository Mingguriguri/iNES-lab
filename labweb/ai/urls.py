from django.urls import path
from awards import views as awards_view
from area import views as area_views
from gallery import views as gallery_views

urlpatterns = [
    path('awards/', awards_view.ai_award, name='ai_award'),
    path('research_topic/', area_views.ai_research_topic, name='ai_research_topic'),
    path('gallery/', gallery_views.ai_gallery, name='ai_gallery'),

    # path('projects/', project_views.ai_projects, name='ai_projects'),
    # path('notices/', notice_views.ai_notices, name='ai_notices'),
]
