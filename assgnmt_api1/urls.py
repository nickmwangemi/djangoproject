from django.urls import path
from assgnmt_api1 import views

urlpatterns = [
    path('finite-value', views.FiniteValidatorList.as_view()),
]