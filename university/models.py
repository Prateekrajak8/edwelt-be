from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    tambnail_image = models.ImageField(upload_to='tambnails/', null=True, blank=True)
    banner_image = models.ImageField(upload_to='banners/', null=True, blank=True)
    logo_image = models.ImageField(upload_to='logos/', null=True, blank=True)
    brochure = models.FileField(upload_to='brochures/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name