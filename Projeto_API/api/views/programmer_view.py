from rest_framework import viewsets
from ..serializers import programmer_serializer
from ..models import Programmer

class ProgrammerViewSet(viewsets.ModelViewSet):
  queryset = Programmer.objects.all()
  serializer_class = programmer_serializer.ProgrammerSerializer