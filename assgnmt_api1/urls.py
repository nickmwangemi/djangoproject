from django.urls import path
from assgnmt_api1 import views

urlpatterns = [
    path('finite-value', views.finiteValidator.as_view()),
]