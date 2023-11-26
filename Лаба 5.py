import requests
from pprint import pprint
from config1 import open_weather_token


def get_weather(city, open_weather_token):
    r = requests .get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
    data = r.json()
    city = data['name']
    cur_temp = data['main']['temp']
    cur_hum = data['main']['humidity']
    cur_press = round((data['main']['pressure'] * 10**2) /133)
    cur_wind = data['wind']['speed']

    print(f"Погода в городе {city} в данный момент:\n"
          f"Температура: {cur_temp} градусов по Цельсию\n"
          f"Влажность: {cur_hum}%\n"
          f"Давление: {cur_press} мм рт ст\n"
          f"Скорость ветра: {cur_wind} м/c")
def city_weather():
    city = input("Введите название города: ")
    get_weather(city, open_weather_token)

city_weather()
print('')

