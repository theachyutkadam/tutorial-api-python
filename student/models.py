from django.db import models

# Create your models here.
class Teacher(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  birth_date = models.CharField(max_length=10)
  qulification = models.CharField(max_length=10)
  contact = models.CharField(max_length=10)
  is_active = models.BooleanField()

class Subject(models.Model):
  name = models.CharField(max_length=30)
  department = models.CharField(max_length=30)
  chapter_count = models.CharField(max_length=5)
  is_active = models.BooleanField()
  teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

class Student(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  birth_date = models.CharField(max_length=10)
  contact = models.CharField(max_length=10)
  is_active = models.BooleanField()
  subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
