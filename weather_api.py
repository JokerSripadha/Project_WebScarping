# -*- coding: utf-8 -*-
"""Weather API.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rA6g_yMx2nfrx9ydD0vvDRaiAB8XQxgX
"""

import requests

api_key = 'a6397a3666834e188b7162940242002'

def get_weather(city, api_key):
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city, api_key)

    if 'error' in weather_data:
        print("Error:", weather_data['error']['message'])
    else:
        print(f"Weather in {city}:")
        print("Condition:", weather_data['current']['condition']['text'])
        print("Temperature (C):", weather_data['current']['temp_c'])
        print("Feels like (C):", weather_data['current']['feelslike_c'])
        print("Humidity:", weather_data['current']['humidity'])
        print("Wind (km/h):", weather_data['current']['wind_kph'])
        print("Wind Direction:", weather_data['current']['wind_dir'])
        print("Cloud :", weather_data['current']['cloud'])

        if 'alert' in weather_data['current']:
            print("Alert Headline:", weather_data['current']['alert']['headline'])
        else:
            print("No alerts")


if __name__ == "__main__":
    main()