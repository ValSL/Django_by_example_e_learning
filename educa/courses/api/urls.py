from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()  # инициализация роутера
router.register('courses', views.CourseViewSet)  # динамическое создание ссылок на лист и объект,
# в данном случае courses/ и courses/<pk>


app_name = 'courses'
urlpatterns = [
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/<pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
    path('courses/<pk>/enroll/', views.CourseEnrollView.as_view(), name='course_enroll'),
    path('', include(router.urls))
]
