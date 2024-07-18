from django.contrib import admin
from django import forms
from .models import Projects, ProjectPhoto

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
        help_texts = {
            'name': '프로젝트 이름을 입력하세요. (필수)',
            'description': '프로젝트에 대한 개요를 입력하세요. 비워두면 화면에 표시되지 않습니다. (선택사항)',
            'start_date': '프로젝트 시작 날짜를 선택하세요. 비워두면 화면에 표시되지 않습니다. (선택사항)',
            'end_date': '프로젝트 종료 날짜를 선택하세요. 비워두면 화면에 표시되지 않습니다. (선택사항)',
            'project_lead': '프로젝트 리더가 있다면 선택하세요. 비워두면 화면에 표시되지 않습니다. (선택사항)',
            'members': '프로젝트에 참여하는 멤버들을 선택하세요. (필수)',
            'areas': '연구 분야를 선택하세요. (선택사항)',
            'keywords': '프로젝트의 키워드가 있다면 "쉼표"로 구분하여 입력하세요. (선택사항)',
            'github_link': 'Github 링크를 입력하세요. 비워두면 화면에 표시되지 않습니다. (선택사항)',
            'paper_link': '논문 링크를 입력하세요. 비워두면 화면에 표시되지 않습니다. (선택사항)',
            'other_link': '추가 링크를 입력하세요. 비워두면 화면에 표시되지 않습니다. (선택사항)',
        }

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
    form = ProjectForm
    inlines = [ProjectPhotoInline]
    list_display = ('team', 'name', 'start_date', 'end_date')
    list_filter = ('team', 'areas', 'keywords')
    search_fields = ('team', 'name', 'description')
    filter_horizontal = ('members', 'areas')
    ordering = ('-start_date', '-end_date', 'name')

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(ProjectPhoto)
