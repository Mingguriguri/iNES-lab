from django.contrib import admin
from django import forms
from .models import Area

'''
목록 보기: list_display
필터: list_filter
검색: search_fields
'''
class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'
        help_texts = {
            'area_name': '연구분야를 입력해주세요. (필수)',
            'area_description': '연구분야에 대한 구체적인 내용을 입력해주세요. 추후에 사용될 예정입니다. 없으면 온점을 입력해주세요.(필수)',
            'photo': '대표할 이미지를 넣어주세요. 비워두면 화면에 표시되지 않습니다. (선택사항)'
        }

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    form = AreaForm
    list_display = ('team', 'area_name')
    list_filter = ('team', 'area_name')
    search_fields = ('team', 'area_name')
    
