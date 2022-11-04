# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TeacherSerializer, StudentSerializer, SubjectSerializer
from .models import Teacher, Student, Subject


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def student_list(request):
  """
  """
  print("List all code students, or create a new student.")
  if request.method == 'GET':
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
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
