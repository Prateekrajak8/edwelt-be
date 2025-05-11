from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NewsHighlight

class NewsHighlightListView(APIView):
    def get(self, request):
        university_id = request.GET.get('university_id')
        if not university_id:
            return Response({'error': 'university_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        news = NewsHighlight.objects.filter(university_id=university_id).order_by('-published_at')
        data = [
            {
                "id": n.id,
                "title": n.title,
                "summary": n.summary,
                "url": n.url,
                "published_at": n.published_at,
            }
            for n in news
        ]
        return Response(data)
