import requests
from django.shortcuts import render
from .models import City
# Create your views here.
from .forms import CityForm
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4c09b25b72ade06d1df302223086097a'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities  = City.objects.all()
    weather_data = []
    for city in cities:

        res =  requests.get(url.format(city)).json()
       # print (res)
        city_weather = {
            'city': city,
            'temperature': res['main']['temp'],
            'description': res['weather'][0]['description'],
            'icon':  res['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)