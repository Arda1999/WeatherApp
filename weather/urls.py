from django.urls import path
from .views import WeatherView, WeatherView5
app_name = "weather"

urlpatterns = [
    path('', WeatherView, name='weather'),
    path('weather5/', WeatherView5, name="weather5"),
]
