from django.urls import path
from awards import views as awards_view
from area import views as area_views
from gallery import views as gallery_views
from member import views as member_views
from notice import views as notice_views
from project import views as project_views
from publications import views as publications_views
from advisor import views as advisor_views

urlpatterns = [
    path('advisors/', advisor_views.advisor_list, {'team': 'ai'}, name='ai_advisors'),
    path('awards/', awards_view.ai_award, name='ai_award'),
    path('research_topic/', area_views.ai_research_topic, name='ai_research_topic'),
    path('gallery/', gallery_views.ai_gallery, name='ai_gallery'),
    path('members/', member_views.ai_members, name='ai_members'),
    path('members/filter/', member_views.ai_filter_by_degree, name='ai_filter_by_degree'),
    path('notices/', notice_views.ai_notice_list, name='ai_notice_list'),
    path('notices/<int:notice_id>/', notice_views.ai_notice_detail, name='ai_notice_detail'),
    path('projects/', project_views.ai_projects_list, name='ai_projects_list'),
    path('projects/<int:project_id>/', project_views.project_detail, name='project_detail'),
    path('publications/<str:pub_type>/', publications_views.ai_publications, name='ai_publications'),
]
