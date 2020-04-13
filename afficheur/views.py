import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from Search.search import *
# Create your views here.

def index(request):

    search = ''
    dict = {}

    if request.method == 'POST':
            search = request.POST.get('search')
            print(search)

    form = CityForm()

    if search is not None:
       dict = retrieveCandidate(search)

    # cities = City.objects.all()
    cities = dict
    weather_data = []

    for city in cities:

        city_weather = {
            'name': city.email,
            'email': city.name,
            'description': city.phone,
            'url' : city.url,
        }

        weather_data.append(city_weather)

    print(weather_data)

    context = {'weather_data' : weather_data,'form':form}
    return render(request, 'afficheur/new.html', context)


