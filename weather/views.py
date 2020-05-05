import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    if request.method == 'POST':
        name=request.POST['name']
        url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={use api id here}'
        #url='http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid='
        r = requests.get(url.format(name)).json()
        print(r)
        city_weather = {
            'city' : name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data = []
        weather_data.append(city_weather)
        context = {'weather_data' :weather_data}
        return render(request, 'weather/index.html',context)
    else:
        return render(request, 'weather/index.html')
