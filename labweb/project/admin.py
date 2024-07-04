from django.contrib import admin
from .models import Projects, ProjectPhoto

class ProjectPhotoInline(admin.TabularInline):
    model = ProjectPhoto
    extra = 1  # 추가할 수 있는 사진 수

class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjectPhotoInline]

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(ProjectPhoto)
