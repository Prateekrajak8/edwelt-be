from django.db import models
from django.contrib.postgres.fields import ArrayField
from university.models import University

class NewsHighlight(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='news_highlights')
    title = models.CharField(max_length=500)
    summary = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        default=list
    )
    url = models.URLField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title