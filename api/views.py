import requests
import json
from django.http import HttpResponse, JsonResponse
from api.serializers import ObjectSerializers
from api.models import Object, Property, Attribute
# 대륙 목록을 반환하는 함수입니다.
def getContinents(request):
    if '' == request.GET:
        return HttpResponse(status=400)

    try:
        queryset = Object.objects.filter(Type = 0)
        serializer = ObjectSerializers(queryset, many=True)
        return HttpResponse(serializer.data)
    except:
        return HttpResponse(status=500)

# 특정 대륙과 관련된 정보를 반환하는 함수입니다.
def getContinent(request, continent):
    if '' == request.GET:
        return HttpResponse(status=400)

    try:
        queryset = Object.objects.get(Name = continent)
        serializer = ObjectSerializers(queryset, many=True)
        return HttpResponse(serializer.data)
    except:
        return HttpResponse(status=500)

# 특정 대륙에 속한 나라 목록을 반환하는 함수입니다.
def getCountries(request, continent):
    if '' == request.GET:
        return HttpResponse(status=400)

    try:
        queryset = Object.objects.filter(Name = continent, Type = 1)
        serializer = ObjectSerializers(queryset, many=True)
        return HttpResponse(serializer.data)
    except:
        return HttpResponse(status=500)
# 특정 나라와 관련된 정보를 반환하는 함수입니다.
def getCountry(request, continent, country):
    if '' == request.GET:
        return HttpResponse(status=400)

    try:
        queryset = Object.objects.filter(Name = continent and cuntry)
        serializer = ObjectSerializers(queryset, many=True)
        return HttpResponse(serializer.data)
    except:
        return HttpResponse(status=500)

# 특정 나라에 속한 도시 목록을 반환하는 함수입니다.
def getCities(request, continent, country):
    if '' == request.GET:
        return HttpResponse(status=400)

    try:
        queryset = Object.objects.filter(Name = continent and country, Type = 2)
        serializer = ObjectSerializers(queryset, many=True)
        return HttpResponse(serializer.data)
    except:
        return HttpResponse(status=500)

# 특정 도시와 관련된 정보를 반환하는 함수입니다.
def getCity(request, continent, country, city):
    if '' == request.GET:
        return HttpResponse(status=400)

    try:
        queryset = Object.objects.filter(Name = continent and country and city)
        serializer = ObjectSerializers(queryset, many=True)
        return HttpResponse(serializer.data)
    except:
        return HttpResponse(status=500)

# 특정 도시에 속한 관광지 목록을 반환하는 함수입니다.
def getSights(request, continent, country, city):
    if '' == request.GET:
        return HttpResponse(status=400)

    try:
        queryset = Object.objects.filter(Name = continent and country and city, Type = 3)
        serializer = ObjectSerializers(queryset, many=True)
        return HttpResponse(serializer.data)
    except:
        return HttpResponse(status=500)

# 특정 관광지와 관련된 정보를 반환하는 함수입니다.
def getSight(request, continent, country, city, sight):
    if '' == request.GET:
        return HttpResponse(status=400)

    try:
        queryset = Object.objects.filter(Name = continent and country and city and sight)
        serializer = ObjectSerializers(queryset, many=True)
        return HttpResponse(serializer.data)
    except:
        return HttpResponse(status=500)
