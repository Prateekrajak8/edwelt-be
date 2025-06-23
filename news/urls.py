from django.urls import path

from news.api import NewsHighlightListView

urlpatterns = [
    path('highlights/', NewsHighlightListView.as_view(), name='news-highlights'),
]
