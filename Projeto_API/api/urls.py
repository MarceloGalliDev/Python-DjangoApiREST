from django.urls import path, include
from rest_framework import routers
from .views import company_view, programmer_view


router = routers.DefaultRouter()
router.register(r'programmers', programmer_view.ProgrammerViewSet)

urlpatterns = [
  path('companies/', company_view.CompanyView.as_view(), name='companies_list'),
  path('companies/<int:id>', company_view.CompanyView.as_view(), name='companies_process'),
  path('', programmer_view.ProgrammerViewSet.as_view(), name='')
]
