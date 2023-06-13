from django.urls import path
from .views import CompanyView

urlpatterns = [
  path('companies/', CompanyView.as_views(), name='companies_list')
]
