import requests
import datetime
import json
from django.http import HttpResponse, JsonResponse
from . import utils
from . import config


def instagram(request):
    if '' == request.GET.get('sight', ''):
        return HttpResponse(status=400)

    sight = utils.fromSpaceToUnderLine(request.GET['sight'])
    URL = f"https://www.instagram.com/explore/tags/{sight}/?__a=1"
    undistilled = {}
    distilled = {}

    try:
        undistilled = requests.get(URL).json(
        )['graphql']['hashtag']['edge_hashtag_to_top_posts']['edges']
        distilled = []

        for datum in undistilled:
            distilled.append({
                'thumbnail': datum['node']['thumbnail_src'],
                'liked': datum['node']['edge_liked_by']['count'],
                'published': datetime.date.fromtimestamp(datum['node']['taken_at_timestamp']).isoformat(),
                'url': f"https://www.instagram.com/p/{datum['node']['shortcode']}"
            })

        return JsonResponse(
            distilled,
            safe=False,
            json_dumps_params={'ensure_ascii': False}
        )
    except:
        return HttpResponse(status=500)


def weather(request):
    if '' == request.GET.get('country', '') and '' == request.GET.get('city', ''):
        return HttpResponse(status=400)

    country = request.GET['country']
    city = request.GET['city']
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={config.OpenWeatherMap['secret']}"
    undistilled = {}
    distilled = {}

    try:
        undistilled = requests.get(URL).json()
        distilled = {
            'icon': utils.formatByWeather(undistilled['weather'][0]['main']),
            'text': undistilled['weather'][0]['description'],
            'temperature': {
                'min': utils.formatByTemperature(undistilled['main']['temp_min']),
                'max': utils.formatByTemperature(undistilled['main']['temp_max']),
                'now': utils.formatByTemperature(undistilled['main']['temp']),
            },
            'humidity': undistilled['main']['humidity'],
            'wind': {
                'way': utils.formatByCardinal(undistilled['wind']['deg']),
                'speed': undistilled['wind']['speed'],
            },
        }

        return JsonResponse(
            distilled,
            safe=False,
            json_dumps_params={'ensure_ascii': False}
        )
    except:
        return HttpResponse(status=500)


def naver(request):
    if '' == request.GET.get('value', ''):
        return HttpResponse(status=400)

    value = request.GET['value']
    URL = f"https://openapi.naver.com/v1/search/blog.json?query={value}"
    undistilled = {}
    distilled = {}

    try:
        undistilled = requests.get(URL, headers={
            'X-Naver-Client-Id': config.Naver['appid'],
            'X-Naver-Client-Secret': config.Naver['secret']
        }).json()['items']
        distilled = []

        for datum in undistilled:
            distilled.append({
                'url': datum['link'],
                'title': utils.removeTag(datum['title']),
                'description': utils.removeTag(datum['description']),
                'published': datetime.datetime.strptime(datum['postdate'], '%Y%m%d').date().isoformat(),
            })

        return JsonResponse(
            distilled,
            safe=False,
            json_dumps_params={'ensure_ascii': False}
        )
    except:
        return HttpResponse(status=500)
