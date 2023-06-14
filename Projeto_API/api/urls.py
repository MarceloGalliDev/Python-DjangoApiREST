from django.urls import path, include
from rest_framework import routers
from .views import company_view, programmer_view


router = routers.DefaultRouter()
#o r'', serve para formatar o path, pois se usarmos um /n ele interpreta como pular linha
router.register(r'programmers', programmer_view.ProgrammerViewSet)

urlpatterns = [
  path('', include(router.urls))
  # path('companies/', company_view.CompanyView.as_view(), name='companies_list'),
  # path('companies/<int:id>', company_view.CompanyView.as_view(), name='companies_process'),
  # path('', programmer_view.ProgrammerViewSet.as_view(), name='')
]
