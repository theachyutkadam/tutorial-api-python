from dataclasses import fields
from rest_framework import serializers
from student.models import Student, Teacher, Subject

class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = ('first_name', 'last_name', 'birth_date', 'qulification', 'contact', 'is_active')

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ('first_name', 'last_name', 'birth_date', 'contact', 'is_active', 'subject')

class SubjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subject
    fields = ('name', 'department', 'chapter_count', 'is_active', 'teacher')
