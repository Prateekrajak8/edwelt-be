from django.db import models

# Create your models here.
class University(models.Model):
    name = models.TextField()
    location = models.TextField(blank=True)
    description = models.TextField(blank=True)
    tambnail_image = models.ImageField(upload_to='tambnails/', null=True, blank=True)
    banner_image = models.ImageField(upload_to='banners/', null=True, blank=True)
    logo_image = models.ImageField(upload_to='logos/', null=True, blank=True)
    brochure = models.FileField(upload_to='brochures/', null=True, blank=True)
    highlights = models.JSONField(default=dict, blank=True)
    applygrad_rankings = models.JSONField(default=dict, blank=True)
    map_url = models.CharField(max_length=1000, null=True, blank=True)
    exams = models.ManyToManyField('Exam', related_name='university')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class UniversityPlacement(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    LEVEL_CHOICES = (
        ('pg', 'PG'),
        ('ug', 'UG'),
    )

    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='placements')
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    year_span = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    details = models.JSONField(default=dict)
    about = models.TextField()
    key_highlights = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.university.name} - {self.level} ({self.year_span}) [{self.gender}]"
    
class Course(models.Model):
    LEVEL_CHOICES = (
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('Doctoral', 'Doctoral'),
    )

    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=255)  # e.g., "MBBS", "DM Neurology"
    course_type = models.CharField(max_length=50, default="Full Time")  # Optional
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    certificate_program = models.BooleanField(default=False)
    duration = models.CharField(max_length=50)  # e.g., "5Y 6M"
    total_fees = models.CharField(max_length=50)  # e.g., "6.79K INR"
    seats = models.PositiveIntegerField()
    exams = models.ManyToManyField('Exam', related_name='courses')  # e.g., "NEET", "AIIMS PG", etc.
    about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.university.name}"
    
class Exam(models.Model):
    name = models.CharField(max_length=255, unique=True)
    application_start_date = models.DateField(null=True, blank=True)
    application_end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
class counsellingPrograms(models.Model):
    exam_choices = (
        ('NEET PG', 'NEET PG'),
        ('NEET UG', 'NEET UG'),
    )
    exam_type = models.CharField(max_length=255, choices=exam_choices)
    program = models.CharField(max_length=1000, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.program

class counsellingTimelines(models.Model):
    program = models.ForeignKey(counsellingPrograms, on_delete=models.CASCADE, related_name='timelines')
    date = models.DateField()
    round_number = models.CharField(max_length=100)
    stage = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['round_number', 'date']
    def __str__(self):
        return f"{self.program.program} - {self.date}"