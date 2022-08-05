from django.urls import path
from .views import CompanyViews

urlpatterns = [
  path('companies/', CompanyViews.as_view(), name='companies_list'),
  path('companies/<int:id>', CompanyViews.as_view(), name='companies_process')
]