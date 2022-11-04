from django.urls import include, path
from .views import xyz
from rest_framework.urlpatterns import format_suffix_patterns
from student import views
urlpatterns = [
  path('xyz', xyz),
  # path('student/', views.TeacherList.as_view()),
  # path('student/<int:pk>/', views.TeacherDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
