from dataclasses import fields
from rest_framework import serializers
from .models import Student, Teacher, Subject

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Teacher
    fields = ('id', 'url', 'first_name', 'last_name', 'birth_date', 'qulification', 'contact', 'is_active')

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
  # teacher = TeacherSerializer()
  class Meta:
    model = Subject
    fields = ('id', 'url', 'name', 'department', 'chapter_count', 'is_active', 'teacher')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
  # subject = SubjectSerializer()
  class Meta:
    model = Student
    fields = ('id', 'url', 'first_name', 'last_name', 'birth_date', 'contact', 'is_active', 'subject', 'image')
