from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=acf2fda418d037c666dfcee794470ce4'
    cities = City.objects.all()
    city = 'Las Vegas'
    form = CityForm
    city_weather = requests.get(url.format(city)).json()
    weather_data = []
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'app_w/index.html', context)
