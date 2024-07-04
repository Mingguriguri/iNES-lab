from django.contrib import admin
from .models import Area

'''
목록 보기: list_display
필터: list_filter
검색: search_fields
'''
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('team', 'area_name')
    list_filter = ('team', 'area_name')
    search_fields = ('team', 'area_name')
    
