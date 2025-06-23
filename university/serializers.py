from rest_framework import serializers
from .models import University, Exam

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'  # Or pick specific fields if needed

class UniversitySerializer(serializers.ModelSerializer):
    exams = ExamSerializer(many=True, read_only=True)

    class Meta:
        model = University
        fields = '__all__'