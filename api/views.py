import requests
import json
from django.http import HttpResponse, JsonResponse
# from . import models, serializers

# 대륙 목록을 반환하는 함수입니다.
def getContinents(request):
    if '' == request.GET:
        return HttpResponse(status=400)

    try:
        return JsonResponse(
            data = serializers.ObjectSerializers(
                models.Object.objects.all(),
                many=True
                ).data,
            safe=False,
            json_dumps_params={'ensure_ascii': False}
        )
    except:
        return HttpResponse(status=500)

# 특정 대륙과 관련된 정보를 반환하는 함수입니다.
def getContinent(request, continent):
    if '' == request.GET:
        return HttpResponse(status=400)
    
    try:
        return JsonResponse(
            data =  serializers.ObjectSerializers(
                models.Object.objects.all(),
                many=True
                ).data,
            safe=False,
            json_dumps_params={'ensure_ascii': False}
        )
    except:
        return JsonResponse()

# 특정 대륙에 속한 나라 목록을 반환하는 함수입니다.
def getCountries(request, continent):
    return JsonResponse()

# 특정 나라와 관련된 정보를 반환하는 함수입니다.
def getCountry(request, continent, country):
    return JsonResponse()

# 특정 나라에 속한 도시 목록을 반환하는 함수입니다.
def getCities(request, continent, country):
    return JsonResponse()

# 특정 도시와 관련된 정보를 반환하는 함수입니다.
def getCity(request, continent, country, city):
    return JsonResponse()

# 특정 도시에 속한 관광지 목록을 반환하는 함수입니다.
def getSights(request, continent, country, city):
    return JsonResponse()

# 특정 관광지와 관련된 정보를 반환하는 함수입니다.
def getSight(request, continent, country, city, sight):
    return JsonResponse()
