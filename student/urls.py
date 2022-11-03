from django.urls import include, path
from .views import xyz

urlpatterns = [
  path('xyz', xyz),
]
