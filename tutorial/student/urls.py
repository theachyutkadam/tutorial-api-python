from django.urls import include, path
from rest_framework import routers
from student.views import TeacherViewSet, StudentViewSet, SubjectViewSet

router = routers.DefalutRouter()
router.register(r'teacher', TeacherViewSet)
router.register(r'student', StudentViewSet)
router.register(r'subject', SubjectViewSet)

urlpatterns = [
  path('', include(router.urls)),
]

