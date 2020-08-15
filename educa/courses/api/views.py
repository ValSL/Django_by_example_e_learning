from rest_framework import generics
from ..models import Subject
from .serializers import SubjectSerializer


class SubjectListView(generics.ListAPIView):
    """Генерация ответа в виде JSON о всех предметах"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    """Генерация ответа в виде JSON о конкретном предмете по pk из url'а"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
