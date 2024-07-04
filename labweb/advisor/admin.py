from django.contrib import admin
from .models import Advisor, EducationExperience

class EducationExperienceInline(admin.TabularInline):
    model = EducationExperience
    extra = 1

@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    inlines = [EducationExperienceInline]
    list_display = ('team', 'name')
    list_filter = ('team',)
