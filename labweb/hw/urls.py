from django.urls import path
from awards import views as awards_view
from area import views as area_views
from gallery import views as gallery_views
from member import views as member_views
from notice import views as notice_views
from project import views as project_views
from publications import views as publications_views

urlpatterns = [
    path('awards/', awards_view.hw_award, name='hw_award'),
    path('research_topic/', area_views.hw_research_topic, name='hw_research_topic'),
    path('gallery/', gallery_views.hw_gallery, name='hw_gallery'),
    path('members/', member_views.hw_members, name='hw_members'),
    path('members/filter/', member_views.hw_filter_by_degree, name='hw_filter_by_degree'),
    path('notices/', notice_views.hw_notice_list, name='hw_notice_list'),
    path('notices/<int:notice_id>/', notice_views.hw_notice_detail, name='hw_notice_detail'),    
    path('projects/', project_views.hw_projects_list, name='hw_projects_list'),
    path('projects/<int:project_id>/', project_views.project_detail, name='project_detail'),
    path('publications/<str:pub_type>/', publications_views.hw_publications, name='hw_publications'),
]
