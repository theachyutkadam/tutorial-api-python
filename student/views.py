# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Teacher, Student, Subject
from .serializers import TeacherSerializer, StudentSerializer, SubjectSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# class TeacherSerializer(viewsets.ModelViewSet):
#   queryset = Teacher.objects.all().order_by('id')
#   serializer_class = TeacherSerializer
#   permission_classes = [permissions.IsAuthenticated]
class TeacherList(APIView):
  """
  List all teachers, or create a new teacher.
  """
  def get(self, request, format=None):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetail(APIView):
  """
  Retrieve, update or delete a teacher instance.
  """
  def get_object(self, pk):
    try:
      return Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    teacher = self.get_object(pk)
    serializer = TeacherSerializer(teacher)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    teacher = self.get_object(pk)
    serializer = TeacherSerializer(teacher, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    teacher = self.get_object(pk)
    teacher.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)










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
