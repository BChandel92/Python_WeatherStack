import requests
def get_weather_forecast():
    #Connecting to weather API
    url="http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22"
    weather_request=requests.get(url)
    weather_json=weather_request.json()
    #Parsing JSON
    description=weather_json["weather"][0]['description']
    temp_min=weather_json["main"]['temp_min']
    temp_max=weather_json["main"]['temp_max']

    #Creating the Forecasting String
    forecast="The Circus forecast for today is "
    forecast+=description+ ' with a high of '+str(int(temp_max))
    forecast+=" and a low of "+str(int(temp_min))
    return forecast
    #print(forecast)