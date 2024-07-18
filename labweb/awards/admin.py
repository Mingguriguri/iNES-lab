from django.contrib import admin
from .models import Awards

'''
목록 보기: list_display
필터: list_filter
검색: search_fields
향상된 Many-to-Many 관리: filter_horizontal
정렬: ordering
'''

@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('team', 'title', 'award_dates')
    list_filter = ('team', 'award_dates')
    search_fields = ('title', 'contents')
    filter_horizontal = ('member',)
    ordering = ('award_dates', 'team',)
