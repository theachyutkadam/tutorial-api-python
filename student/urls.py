from django.urls import include, path
from .views import xyz

from rest_framework.urlpatterns import format_suffix_patterns
from student import views

urlpatterns = [
  path('student/', views.student_list),
  path('student/<int:pk>/', views.student_detail),
  path('xyz', xyz),
]
urlpatterns = format_suffix_patterns(urlpatterns)
