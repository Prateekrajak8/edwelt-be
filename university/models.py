from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    tambnail_url = models.TextField(blank=True)
    banner_image_url = models.TextField(blank=True)
    logo_image_url = models.TextField(blank=True)
    brochure_url = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name