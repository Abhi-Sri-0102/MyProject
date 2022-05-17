from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
# Create your views here.

@api_view(["POST"])
def IdealWeight(heightdata):
    try:
        obj=json.loads(heightdata.body)
        ret={}
        def flatten(x,flattened_key=""):
            if type(x) is dict:
                for current_key in x:
                    flatten(x[current_key],flattened_key+current_key+'__')
            else:
                ret[flattened_key[:-2]]=x
        flatten(obj)
        return Response(ret)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)