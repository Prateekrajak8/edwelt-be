from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from university.models import University
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