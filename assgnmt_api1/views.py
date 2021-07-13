import json

from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from assgnmt_api1 import serializers
from assgnmt_api1.serializers import (FiniteSerializer)


# Create your views here.
class FiniteValidatorList(APIView):

    serializer_class = serializers.FiniteSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            print(serializer)
            return Response(serializer.data)
        else:
            print(serializer.errors)

    def get(self,request):
        if request.method == 'GET': # 
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                return Response(serializer)
        return Response(serializer.errors)
    
# req -> body -> method: GET/POST/PUT



