# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeacherSerializer, StudentSerializer, SubjectSerializer
from .models import Teacher, Student, Subject

class TeacherSerializer(viewsets.ModelViewSet):
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer

class StudentSerializer(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class SubjectSerializer(viewsets.ModelViewSet):
  queryset = Subject.objects.all()
  serializer_class = SubjectSerializer

def xyz(request):
  print("+++++++++++1111111")
