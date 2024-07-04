from django.contrib import admin
from .models import member_list

'''
목록 보기: list_display
필터: list_filter
검색: search_fields
정렬: ordering
'''
@admin.register(member_list)
class member_listAdmin(admin.ModelAdmin):
    list_display = ('team', 'name', 'degree', 'status', 'email')
    list_filter = ('team', 'degree', 'status')
    search_fields = ('team', 'name', 'degree', 'status', 'motto')
    ordering = ('-status', 'team', 'name',)
    