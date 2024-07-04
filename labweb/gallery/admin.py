from django.contrib import admin
from .models import Gallery

'''
목록 보기: list_display
필터: list_filter
검색: search_fields
정렬: ordering
'''
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('team', 'title', 'upload_date')
    list_filter = ('team', 'upload_date')
    search_fields = ('title', 'contents')
    ordering = ('-upload_date',)