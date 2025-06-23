from django.contrib import admin
from .models import NewsHighlight

@admin.register(NewsHighlight)
class NewsHighlightAdmin(admin.ModelAdmin):
    list_display = ('title', 'university', 'published_at')
    list_filter = ('university', 'published_at')
    search_fields = ('title', 'summary', 'university__name')
    ordering = ('-published_at',)