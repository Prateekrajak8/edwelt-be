from django.contrib import admin

from university.models import University

# Register your models here.
@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "description", "created_at", "updated_at"]
    search_fields = ["name"]
