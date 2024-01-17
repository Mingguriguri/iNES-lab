from django.contrib import admin
from .models import Projects

# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'project_lead']  # Admin 목록에 표시할 필드
    filter_horizontal = ('members', 'areas',)  # 멤버와 영역을 수평으로 필터링


admin.site.register(Projects)
