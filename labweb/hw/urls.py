from django.urls import path
from awards import views as awards_view
from area import views as area_views

urlpatterns = [
    path('awards/', awards_view.hw_award, name='hw_award'),
    path('research_topic/', area_views.hw_research_topic, name='hw_research_topic'),

    # path('projects/', project_views.ai_projects, name='ai_projects'),
    # path('notices/', notice_views.ai_notices, name='ai_notices'),
    # path('gallery/', galleㄴry_views.ai_gallery, name='ai_gallery'),
]
