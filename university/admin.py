from django.contrib import admin

from university.models import University

# Register your models here.
@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "description", "banner_image_url", "logo_image_url", "brochure_url", "created_at", "updated_at"]
    search_fields = ["name"]
