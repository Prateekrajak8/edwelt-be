from django.urls import path

from university.api import CounsellingView, CourseByUniversityView, UniversityDetailAPIView, UniversityListCreateAPIView, UniversityPlacementByUniversityView

urlpatterns = [
    path('universities/', UniversityListCreateAPIView.as_view(), name='university-list-create'),
    path('universities/<int:pk>/', UniversityDetailAPIView.as_view(), name='university-detail'),
    path('universities/<int:university_id>/placements/', UniversityPlacementByUniversityView.as_view(), name='placements-by-university'),
    path('universities/<int:university_id>/courses/', CourseByUniversityView.as_view(), name='courses-by-university'),
    path('api/programs/', CounsellingView.as_view(), name='get_all_programs'),
    path('api/timelines/', CounsellingView.as_view(), name='get_timelines_by_program'),
]