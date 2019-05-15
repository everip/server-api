from django.urls import path
from . import views

urlpatterns = [
    path('continents', views.getContinents),
    path('<str:continent>', views.getContinent),

    path('<str:continent>/countries', views.getCountries),
    path('<str:continent>/<str:country>', views.getCountry),
    
    path('<str:continent>/<str:country>/cities', views.getCities),
    path('<str:continent>/<str:country>/<str:city>', views.getCity),

    path('<str:continent>/<str:country>/<str:city>/sights', views.getSights),
    path('<str:continent>/<str:country>/<str:city>/<str:sight>', views.getSight),
]