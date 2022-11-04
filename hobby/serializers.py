from rest_framework import serializers
from .models import Hobby

class HobbySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Hobby
    fields = ('id', 'url', 'name', 'is_active')
