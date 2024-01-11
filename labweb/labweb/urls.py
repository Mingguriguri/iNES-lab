"""labweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('member/', include('member.urls')),
    path('projects/', include('projects.urls')),
    path('project/', include('project.urls')),
    path('topic/', include('area.urls')),
    path('contact/', include('contact.urls')),
    path('demo/', include('demo.urls')),
    path('gallery/', include('gallery.urls')),
    path('publications/', include('publications.urls')),
    path('publication/', include('publication.urls')),
    path('history/', include('history_of_ines.urls')),
    path('awards/', include('awards.urls')),
    path('admin/', admin.site.urls),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)