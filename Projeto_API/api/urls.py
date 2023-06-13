from django.urls import path
from .views.company_view import CompanyView

urlpatterns = [
  path('companies/', CompanyView.as_view(), name='companies_list')
]
