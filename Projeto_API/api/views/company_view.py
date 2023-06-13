from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from django.http.response import JsonResponse
from django.shortcuts import render
from ..models import Company
from django.views import View
from ..serializers import company_serializer

class CompanyView(View):
  
  def get(self, request):
    companies = list(Company.objects.values())
    if len(companies) > 0:
      data = {'message': 'Sucess', 'companies':companies}
    else:
      data = {'message': 'Companies not found...'}
    return JsonResponse(data)
  
  def post(self, request, format=None):
    pass
  
  def put(self, request, format=None):
    pass
  
  def delete(self, request, format=None):
    pass
  
