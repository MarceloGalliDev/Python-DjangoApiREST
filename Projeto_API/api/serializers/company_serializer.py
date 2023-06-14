from rest_framework import serializers
from django.db import models
from django.urls import reverse
from ..models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
