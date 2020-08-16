from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from ..models import Subject, Course
from .serializers import SubjectSerializer, CourseSerializer


class SubjectListView(generics.ListAPIView):
    """Генерация ответа в виде JSON о всех предметах"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    """Генерация ответа в виде JSON о конкретном предмете по pk из url'а"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


# этот Класс был замененм функцией enroll в классе CourseViewSet, и ссылка туда также автогенерируется используя имя метода
# class CourseEnrollView(APIView):
#     """Запись на курсы"""
#     # пользователи будут идентифицированы по перереданному http хэдэру Authorization содержащему логин и пароль
#     authentication_classes = (BasicAuthentication,)
#     # доступ только для авторизованных пользователей
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request, pk, format=None):  # Вьюха работает только с POST запросами, pk идет и url'а
#         course = get_object_or_404(Course, id=pk)
#         course.students.add(request.user)
#         return Response({'enrolled': True})


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение списка курсов и конкретного кураса динамически"""
    # viewsets.ReadOnlyModelViewSet это как простой APIView,
    # только динамически создает ссылки на лист и на конкретный объект в файле urls.py с помощью router
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True,  # detail - параметр говорит что работаем с одним объектом
            methods=['post'],
            authentication_classes=[BasicAuthentication],
            permission_classes=(IsAuthenticated))
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})

