import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c2514daffcbd261b8f9940d30fc01d0a'

    if request.method == "POST":
        pass
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    form = CityForm()
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r["main"]["temp"],
            'description': r["weather"][0]["description"],
            'icon': r["weather"][0]["icon"],
        }
        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather.html', context)