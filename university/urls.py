from django.urls import path

from university.api import UniversityDetailAPIView, UniversityListCreateAPIView

urlpatterns = [
    path('universities/', UniversityListCreateAPIView.as_view(), name='university-list-create'),
    path('universities/<int:pk>/', UniversityDetailAPIView.as_view(), name='university-detail'),
]