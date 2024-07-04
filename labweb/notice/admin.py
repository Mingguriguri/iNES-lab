from django.contrib import admin
from .models import Notice

'''
목록 보기: list_display
필터: list_filter
검색: search_fields
정렬: ordering
'''
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('team', 'title', 'author', 'created_at', 'updated_at')
    list_filter = ('team', 'created_at', 'author')
    search_fields = ('title', 'contents')
    ordering = ('-created_at', 'updated_at')