from rest_framework import viewsets
from ..serializers import programmer_serializer
from ..models import Programmer
from rest_framework import permissions


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = programmer_serializer.ProgrammerSerializer
    permission_classes = [permissions.IsAuthenticated]