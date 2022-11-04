from rest_framework import viewsets
# from rest_framework import permissions
from .serializers import HobbySerializer
from .models import Hobby
# Create your views here.

class HobbySerializer(viewsets.ModelViewSet):
  queryset = Hobby.objects.all().order_by('id')
  serializer_class = HobbySerializer
  # permission_classes = [permissions.IsAuthenticated]
