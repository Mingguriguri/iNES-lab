from django.contrib import admin
from django import forms
from .models import Advisor, EducationExperience

class EducationExperienceForm(forms.ModelForm):
    class Meta:
        model = EducationExperience
        fields = '__all__'
        help_texts = {
            'date_range': '기간을 입력해주세요. (e.g. 2023 - 2024) (필수)',
            'institution': '소속을 입력해주세요. (필수)',
            'position': '직책을 입력해주세요. (필수)'
        }

class AdvisorForm(forms.ModelForm):
    class Meta:
        model = Advisor
        fields = '__all__'
        help_texts = {
            'affiliation': '소속을 입력해주세요. (필수)',
            'position': '직위를 입력해주세요. (필수)',
            'research_fields': '연구분야를 입력하세요. 비워두면 화면에 표시되지 않습니다. (선택사항)',
            'specialty': '전공분야를 입력하세요. 비워두면 화면에 표시되지 않습니다. (선택사항)',
            'introduction': '소개글을 작성해주세요. (필수)',
            'keywords': '키워드가 있다면 "쉼표"로 구분하여 입력하세요. (필수)',
            'photo': '대표할 이미지를 넣어주세요. 비워두면 화면에 표시되지 않습니다. (선택사항)'
        }

class EducationExperienceInline(admin.TabularInline):
    form = EducationExperienceForm
    model = EducationExperience
    extra = 1

@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    form = AdvisorForm
    inlines = [EducationExperienceInline]
    list_display = ('team', 'name')
    list_filter = ('team',)
