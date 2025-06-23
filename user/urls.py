from django.urls import path

from university.api import UniversityDetailAPIView, UniversityListCreateAPIView
from user.api import RegisterUserAPIView


urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register_user'),
]