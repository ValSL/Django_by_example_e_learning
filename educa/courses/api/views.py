from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from ..models import Subject, Course
from .serializers import SubjectSerializer


class SubjectListView(generics.ListAPIView):
    """Генерация ответа в виде JSON о всех предметах"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    """Генерация ответа в виде JSON о конкретном предмете по pk из url'а"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseEnrollView(APIView):
    """Запись на курсы"""
    # пользователи будут идентифицированы по перереданному http хэдэру Authorization содержащему логин и пароль
    authentication_classes = (BasicAuthentication,)
    # доступ только для авторизованных пользователей
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):  # Вьюха работает только с POST запросами, pk идет и url'а
        course = get_object_or_404(Course, id=pk)
        course.students.add(request.user)
        return Response({'enrolled': True})
