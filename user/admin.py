from django.contrib import admin

from user.models import UserRegistration

# Register your models here.
@admin.register(UserRegistration)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone_number", "category", "neet_rank", "created_at"]
    search_fields = ["phone_number"]
