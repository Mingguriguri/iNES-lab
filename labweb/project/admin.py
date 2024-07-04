from django.contrib import admin
from .models import Projects, ProjectPhoto

class ProjectPhotoInline(admin.TabularInline):
    model = ProjectPhoto
    extra = 10  # 추가할 수 있는 사진 수


'''
목록 보기: list_display
필터: list_filter
검색: search_fields
정렬: ordering
'''
class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjectPhotoInline]
    list_display = ('team', 'name', 'start_date', 'end_date')
    list_filter = ('team', 'areas', 'keywords')
    search_fields = ('team', 'title', 'contents')
    filter_horizontal = ('members', 'areas')
    ordering = ('-start_date', '-end_date', 'name')

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(ProjectPhoto)
