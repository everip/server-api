import re


def fromSpaceToUnderLine(value):
    return value.replace(' ', '_')


def removeTag(value):
    return re.sub(re.compile('<.*?>'), '', value)


def formatByWeather(value):
    value = value.lower()
    if value == 'clear':
        return 'sun'
    elif value == 'clouds':
        return 'cloud'
    elif value == 'thunderstorm':
        return 'storm'
    # elif value == 'snow':
    #   return 'snow'
    # elif value == 'tornado':
    #   return 'tornado'
    elif value in ('rain', 'drizzle'):
        return 'rain'
    elif value in ('fog', 'haze', 'mise', 'smoke', 'dust', 'sand', 'ash', 'squall'):
        return 'fog'
    else:
        return value


def formatByCardinal(value):
    if value == 0:
        return '북풍'
    elif value < 90:
        return '북동풍'
    elif value == 90:
        return '동풍'
    elif value < 180:
        return '남동풍'
    elif value == 180:
        return '남풍'
    elif value < 270:
        return '남서풍'
    elif value == 270:
        return '서풍'
    elif value < 360:
        return '북서풍'
    else:
        return ''


def formatByTemperature(value):
    return round(value - 273.15, 1)
