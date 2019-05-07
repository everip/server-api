import json
import requests

from django.shortcuts import render
from .models import Object, Attribute, Property
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .serializers import ObjectSerializer
# Create your views here.

class ObjectSerializer(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializers_class = ContinentSerializer

