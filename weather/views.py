import requests
import json
from django.contrib.auth.decorators import login_required

from django.shortcuts import render





@login_required()
def WeatherView(request):
    return render(request, 'weather.html')


@login_required()
def WeatherView5(request):
    return render(request, 'weather5.html')


def get_weather_data(city, duration):
  
    api_key = "169ce696d0924eb38ec80224232701"
    query_str = "http://api.worldweatheronline.com/premium/v1/weather.ashx?key={api_key}&q={city}+&num_of_days={duration}&format=json"
    response = requests.get(query_str.format(
        api_key=api_key, city=city, duration=duration))
    my_response = json.loads(response.text)
    return my_response['data']

