from django.contrib import admin
from .models import University, UniversityPlacement, Course

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'created_at', 'updated_at')
    search_fields = ('name', 'location')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(UniversityPlacement)
class UniversityPlacementAdmin(admin.ModelAdmin):
    list_display = ('university', 'level', 'year_span', 'gender', 'created_at', 'updated_at')
    list_filter = ('university', 'level', 'gender', 'created_at')
    search_fields = ('university__name', 'year_span')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'level', 'duration', 'total_fees', 'seats', 'created_at', 'updated_at')
    list_filter = ('level', 'university', 'created_at')
    search_fields = ('name', 'university__name', 'exams')
    readonly_fields = ('created_at', 'updated_at')
