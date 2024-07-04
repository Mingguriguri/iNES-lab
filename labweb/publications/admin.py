from django.contrib import admin
from .models import Publication

'''
목록 보기: title, team, pub_type, published_date, publisher 표시.
필터: 사이드바에 team, pub_type, published_date 필터 제공.
검색: title과 citation_text, publisher 검색 가능.
향상된 Many-to-Many 관리: authors와 areas에 대해 filter_horizontal 사용.
'''
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'team', 'pub_type', 'published_date', 'publisher')
    list_filter = ('team', 'pub_type', 'published_date')
    search_fields = ('title', 'citation_text', 'publisher')
    filter_horizontal = ('authors', 'areas')

