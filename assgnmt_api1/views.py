from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict


from assgnmt_api1.serializers import SlotValidationResult, valueFormSerializer 
from assgnmt_api1 import serializers

# Create your views here.
class finiteValidator(APIView):

    serializer_class = serializers.finiteSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return JsonResponse(model_to_dict(SlotValidationResult))
        else:
            print(serializer.errors)

    

