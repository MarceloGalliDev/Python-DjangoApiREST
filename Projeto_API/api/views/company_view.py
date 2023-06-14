from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.shortcuts import render
from ..models import Company
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from ..serializers import company_serializer
import json

class CompanyView(APIView):
  
  
  #criando CSRF protection
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
  
  
  # def get(self, request, id=0):
  #   if(id > 0):
  #     companies = list(Company.objects.filter(id=id).values())
  #     if len(companies) > 0:
  #       company = companies[0]
  #       data = {'message':'Sucess', 'companies':company}
  #     else:
  #       data = {'message': 'Companies not found...'}
  #     return JsonResponse(data)
  #   else:
  #     companies = list(Company.objects.values())
  #     if len(companies) > 0:
  #       data = {'message':'Sucess', 'companies':companies}
  #     else:
  #       data = {'message':'Companies not found...'}
  #     return JsonResponse(data)
  
  @api_view(['GET'])
  @permission_classes((permissions.AllowAny,))
  def get(self, request, format=None):
    serializer_company = company_serializer.CompanySerializer(data=request.data, context={'request': request})
    
    if serializer_company.is_valid():
      serializer_company.save()
      return Response(serializer_company.data, status=status_http.HTTP_200_OK)
    return Response(serializer_company.errors, status=status_http.HTTP_400_BAD_REQUEST)
    
  
  def post(self, request):
    jd = json.loads(request.body)
    # print(request.body)
    # print(jd)
    
    Company.objects.create(
      name=jd['name'], 
      website=jd['website'],
      foundation=jd['foundation'],
    )
    
    data = {'message': 'Success'}
    return JsonResponse(data)
  
  def put(self, request, id):
    jd = json.loads(request.body)
    companies = list(Company.objects.filter(id=id).values())
    if len(companies) > 0:
      company = Company.objects.get(id=id)
      company.name = jd['name']
      company.website = jd['website']
      company.foundation = jd['foundation']
      company.save()
      data = {'message': 'Success'}
    else:
      data = {'message':'Companies not found...'}
    return JsonResponse(data)
      
      
  def delete(self, request, id):
    companies = list(Company.objects.filter(id=id).values())
    if len(companies) > 0:
      Company.objects.filter(id=id).delete()
      data = {'message': 'Success'}
    else:
      data = {'message':'Companies not found...'}
    return JsonResponse(data)
  
