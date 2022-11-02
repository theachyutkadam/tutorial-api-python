from django.urls import include, path
from rest_framework import routers
from .views import TeacherSerializer, StudentSerializer, SubjectSerializer, xyz
# from tutorial import student

# router = routers.DefalutRouter()
# router.register(r'teacher', TeacherSerializer)
# router.register(r'student', StudentSerializer)
# router.register(r'subject', SubjectSerializer)

urlpatterns = [
  path('xyz', xyz),
]
