from rest_framework import serializers
from ..models import Programmer

class ProgrammerSerializer(serializers.Serializer):
  class Meta:
    model=Programmer
    fields= '__all__'