from dataclasses import fields
from rest_framework import serializers
from .models import Student, Teacher, Subject

class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = ('first_name', 'last_name', 'birth_date', 'qulification', 'contact', 'is_active')

class SubjectSerializer(serializers.ModelSerializer):
  # teacher = TeacherSerializer()
  class Meta:
    model = Subject
    fields = ('name', 'department', 'chapter_count', 'is_active', 'teacher')

class StudentSerializer(serializers.ModelSerializer):
  # subject = SubjectSerializer()
  class Meta:
    model = Student
    fields = ('first_name', 'last_name', 'birth_date', 'contact', 'is_active', 'subject')
