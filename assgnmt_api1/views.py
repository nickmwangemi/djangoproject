from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.forms.models import model_to_dict


from assgnmt_api1.serializers import SlotValidationResult, valueFormSerializer 
from assgnmt_api1 import serializers

# Create your views here.
class finiteValidator(APIView):

    serializer_class = serializers.finiteSerializer

    def post(self,request):
        data = JSONParser().parse(request)
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        new_dict = {}
        new_dict['results'] = SlotValidationResult
        return JsonResponse(json.dumps(new_dict))

    def get(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return JsonResponse(model_to_dict(SlotValidationResult))



    

