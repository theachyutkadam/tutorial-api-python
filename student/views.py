# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TeacherSerializer, StudentSerializer, SubjectSerializer
from .models import Teacher, Student, Subject

class TeacherSerializer(viewsets.ModelViewSet):
  queryset = Teacher.objects.all().order_by('id')
  serializer_class = TeacherSerializer
  permission_classes = [permissions.IsAuthenticated]

class StudentSerializer(viewsets.ModelViewSet):
  queryset = Student.objects.all().order_by('id')
  serializer_class = StudentSerializer
  permission_classes = [permissions.IsAuthenticated]

class SubjectSerializer(viewsets.ModelViewSet):
  queryset = Subject.objects.all().order_by('id')
  serializer_class = SubjectSerializer
  permission_classes = [permissions.IsAuthenticated]

def xyz(request):
  print("+++++++++++1111111")
