from django.urls import path
from . import views


urlpatterns = [
    path('weather', views.weather),
    path('instagram', views.instagram),
    path('naver', views.naver)
]
