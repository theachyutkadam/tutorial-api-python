"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from quickstart import views as quick_start_view
from student import views as student_view
from hobby import views as hobby_view

router = routers.DefaultRouter()
router.register(r'users', quick_start_view.UserViewSet)
router.register(r'groups', quick_start_view.GroupViewSet)
router.register(r'hobby', hobby_view.HobbySerializer)

router.register(r'teacher', student_view.TeacherSerializer)
router.register(r'student', student_view.StudentSerializer)
router.register(r'subject', student_view.SubjectSerializer)

urlpatterns = [
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#   path('star-wars/', include('student.urls')),
]
