from django.contrib import admin
from django import forms
from .models import member_list

'''
목록 보기: list_display
필터: list_filter
검색: search_fields
정렬: ordering
'''
class MemberListForm(forms.ModelForm):
    class Meta:
        model = member_list
        fields = '__all__'
        help_texts = {
            'main_photo': '증명사진과 같은 공식적인 사진을 넣어주세요. (필수)',
            'hobby_photo': '취미와 관련된 사진을 넣어주세요. 넣고 싶지 않을 경우 main_photo와 같은 사진을 넣어주세요. (필수)',
        }

@admin.register(member_list)
class member_listAdmin(admin.ModelAdmin):
    form = MemberListForm
    list_display = ('team', 'name', 'degree', 'status', 'email')
    list_filter = ('team', 'degree', 'status')
    search_fields = ('team', 'name', 'degree', 'status', 'motto')
    ordering = ('-status', 'team', 'name',)
    