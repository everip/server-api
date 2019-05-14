import json
import requests
from django.shortcuts import render
from .models import Object, Attribute, Property
from django.http import HttpResponse, JsonResponse


# Create your views here.

def continent(request):

    if '' == request.GET.get('value', ''):
        return HttpResponse(status=400)

    value = request.GET['value']
    data = {}
    try:
        data = []
        if value == 'continents':
            object_data = Object.objects.all()
            lenod = len(object_data)
            for i in range(lenod):
                property_data = Property.objects.filter('index' = object_data[i][index])
                attribute_data = Attribute.objects.filter('index' = property_data[i][attribute])
                data.append({
                    "name" : object_data[i][name],
                    "attribute" : attribute_data[i][value]
                })            


            
        else:
            object_data = Object.objects.filter('name' = value)
            property_data = Property.objects.filter('index' = object_data[0][index])
            attribute_data = Attribute.objects.filter('index' = property_data[0][attribute])
            data.append({
                "name" : object_data[0][name],
                "attributes" : attribute_data[0][value]
            })
        return JsonResponse(
            data,
            safe=False,
            json_dumps_params={'ensure_ascii': False}
        )
    except:
        return HttpResponse(statsu=500)
    