from django.shortcuts import render
import requests
import datetime
import ipinfo

# Create your views here.
def index(request):
    print(request.POST)
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        # response = requests.get('http://ipinfo.io/json')
        # data = json.loads(response.text)
        access_token = '62850ee40de8c6' #collected from -> https://ipinfo.io/

        handler = ipinfo.getHandler(access_token)
        data = handler.getDetails()
        
        city = data.city

    appid = '614292ec1c4f55c22a7de859d174f10c'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMETER = {'q': city, 'appid': appid, 'units': 'metric'}

    r = requests.get(url=URL, params=PARAMETER)
    res = r.json()
    weather_details = {
        'description': res['weather'][0]['description'],
        'icon': res['weather'][0]['icon'],
        'temp': res['main']['temp'],
        'feels_like': res['main']['feels_like'],
        'wind_speed': res['wind']['speed'],
        'day': datetime.date.today(),
        'city': city
    }
    return render(request, 'weather_finder/index.html', { 'weather': weather_details })
