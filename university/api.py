from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from university.models import Course, University, UniversityPlacement, counsellingPrograms, counsellingTimelines
from .serializers import UniversitySerializer
from django.shortcuts import get_object_or_404

class UniversityListCreateAPIView(APIView):
    def get(self, request):
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UniversityDetailAPIView(APIView):
    def get(self, request, pk):
        university = get_object_or_404(University, pk=pk)
        serializer = UniversitySerializer(university)
        return Response(serializer.data)

    def put(self, request, pk):
        university = get_object_or_404(University, pk=pk)
        serializer = UniversitySerializer(university, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        university = get_object_or_404(University, pk=pk)
        university.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CourseByUniversityView(APIView):
    def get(self, request, university_id):
        courses = Course.objects.filter(university__id=university_id)

        data = []
        for course in courses:
            data.append({
                "id": course.id,
                "university": course.university.id,
                "name": course.name,
                "course_type": course.course_type,
                "level": course.level,
                "certificate_program": course.certificate_program,
                "duration": course.duration,
                "total_fees": course.total_fees,
                "seats": course.seats,
                "exams": [
                    {
                        "id": exam.id,
                        "name": exam.name,
                        "application_start_date": exam.application_start_date,
                        "application_end_date": exam.application_end_date
                    }
                    for exam in course.exams.all()
                ],
                "about": course.about,
                "created_at": course.created_at,
                "updated_at": course.updated_at,
            })

        return Response(data, status=status.HTTP_200_OK)
    
class UniversityPlacementByUniversityView(APIView):
    def get(self, request, university_id):
        placements = UniversityPlacement.objects.filter(university__id=university_id)

        data = []
        for placement in placements:
            data.append({
                "id": placement.id,
                "university": placement.university.id,
                "level": placement.level,
                "year_span": placement.year_span,
                "gender": placement.gender,
                "details": placement.details,
                "about": placement.about,
                "key_highlights": placement.key_highlights,
                "created_at": placement.created_at,
                "updated_at": placement.updated_at,
            })

        return Response(data, status=status.HTTP_200_OK)
    
class CounsellingView(APIView):
    def get(self, request):
        exam_type = request.GET.get('exam_type')
        if not exam_type:
            return Response({'error': 'exam_type parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        programs = counsellingPrograms.objects.filter(exam_type=exam_type, is_active=True).values('id', 'program', 'exam_type', 'is_active')
        return Response(list(programs), status=status.HTTP_200_OK)
        
    def post(self, request):
        data = request.data
        program = data.get('program')
        exam_type = data.get('exam_type')
        if not program or not exam_type:
            return Response({'error': 'Both program and exam_type are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        counselling_timelines = counsellingTimelines.objects.filter(program__program=program, program__exam_type=exam_type, is_active=True)
        return Response(counselling_timelines, status=status.HTTP_200_OK)