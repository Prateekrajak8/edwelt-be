from django.contrib import admin
from .models import Exam, University, UniversityPlacement, Course, counsellingPrograms, counsellingTimelines

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'created_at', 'updated_at')
    search_fields = ('name', 'location')
    list_filter = ('created_at', 'updated_at')
    filter_horizontal = ('exams',) 
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
    search_fields = ('name', 'university__name', 'exams__name')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('exams',) 

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'application_start_date', 'application_end_date', 'created_at', 'updated_at')
    list_filter = ('name', 'application_start_date')
    search_fields = ('name', 'application_start_date')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(counsellingPrograms)
class CounsellingProgramAdmin(admin.ModelAdmin):
    list_display = ('exam_type', 'program', 'is_active', 'created_at', 'updated_at')
    search_fields = ('exam_type',)
    list_filter = ('exam_type', 'is_active')

@admin.register(counsellingTimelines)
class CounsellingTimelineAdmin(admin.ModelAdmin):
    list_display = ('program', 'round_number', 'stage', 'date', 'is_active', 'created_at', 'updated_at')
    search_fields = ('program__program', 'stage',)
    list_filter = ('program__exam_type', 'program__program', 'round_number')
