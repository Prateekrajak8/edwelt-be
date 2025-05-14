from django.urls import path

from university.api import CourseByUniversityView, UniversityDetailAPIView, UniversityListCreateAPIView, UniversityPlacementByUniversityView

urlpatterns = [
    path('universities/', UniversityListCreateAPIView.as_view(), name='university-list-create'),
    path('universities/<int:pk>/', UniversityDetailAPIView.as_view(), name='university-detail'),
    path('universities/<int:university_id>/placements/', UniversityPlacementByUniversityView.as_view(), name='placements-by-university'),
    path('universities/<int:university_id>/courses/', CourseByUniversityView.as_view(), name='courses-by-university'),
]