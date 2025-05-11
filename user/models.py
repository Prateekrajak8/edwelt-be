from django.db import models

class UserRegistration(models.Model):
    CATEGORY_CHOICES = [
        ('12th_pass', '12th Pass'),
        ('graduate', 'Graduate'),
        ('parent', 'Parent'),
        ('nri', 'NRI')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    neet_rank = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.phone_number}"
