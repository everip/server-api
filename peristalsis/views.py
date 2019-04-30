import requests
import datetime
import json
from django.http import HttpResponse, JsonResponse
from . import utils
from . import config


def instagram(request):
    sight = utils.fromSpaceToUnderLine(request.GET['sight'])
    URL = f"https://www.instagram.com/explore/tags/{sight}/?__a=1"
    undistilled = {}
    distilled = {}

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


def weather(request):
    city = request.GET['city']
    country = request.GET['country']
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={config.OpenWeatherMap['secret']}"
    undistilled = {}
    distilled = {}

    undistilled = requests.get(URL).json()
    distilled = {
        'weather': {
            'icon': utils.formatByWeather(undistilled['weather'][0]['main']),
            'text': undistilled['weather'][0]['description'],
        },
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


def naver(request):
    value = request.GET['value']
    URL = f"https://openapi.naver.com/v1/search/blog.json?query={value}"
    undistilled = {}
    distilled = {}

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
