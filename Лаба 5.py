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

    print(f"Температура: {cur_temp} градусов по Цельсию\n"
          f"Влажность: {cur_hum}%\n"
          f"Давление: {cur_press} мм рт ст\n"
          f"Скорость ветра: {cur_wind} м/c")
def city_weather():
    city = input("Введите название города: ")
    get_weather(city, open_weather_token)

city_weather()
print('')

response = requests.get('https://vk.com')
print(f'Status code: {response.status_code}')


print('1. Nubmersapi.com API')
num = int(input('Input number: '))
res = requests.get(f'http://numbersapi.com/{num}')
print(res.text, '\n')

def get_word_info():
    print('3. Online dictionary API (meanings of words).')
    word = input('Input word: ')
    result = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    if result.status_code == 200:
        response = result.json()
        count = 0

        print('Meanings:')
        for i in response[0]["meanings"]:
            for j in i["definitions"]:
                count += 1
                print(f'{count}. {j["definition"]}')
    else:
        print('You typed something wrong')


get_word_info()
