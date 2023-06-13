from django.shortcuts import render
from rest_framework.views import APIView
from .models import Company

class CompanyView(APIView):
  
  def get(self, request, format=None):
    companies=Company.objects.all()
    if len(companies)>0:
      data={'message': 'Companies not found...'}
  
  def post(self, request, format=None):
    pass
  
  def put(self, request, format=None):
    pass
  
  def delete(self, request, format=None):
    pass
  
