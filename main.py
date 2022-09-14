import requests
# from pprint import pprint
from config import weather_token


def get_weather(city, weather_token):

    smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00001F327",
        "Grizzle": "Дождь \U00001F327",
        "Thunderstorm": "Гроза \U00001F329",
        "Snow": "Снег \U00001F328",
        "Mist": "Туман \U00001F32B"
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric&lang=ru'
        )
        data = r.json()
        # pprint(data)

        weather_main = data['weather'][0]['main']
        if weather_main in smile:
            wm = smile[weather_main]
        else:
            wm = '\U00001F52E'

        city = data['name']
        temp = data['main']['temp']
        temp = float('{:.1f}'.format(temp))
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        print(f'Погода в Городе {city}: {wm}\n'
              f'Температура: {temp}°C\n'
              f'Скорость Ветра: {wind} м/с\n'
              f'Влажность: {humidity}%\n'
              f''
              )

    except Exception:
        print('Проверьте название Города!')


def main():
    city = input('Пожалуйста, Введите Город: ')
    get_weather(city, weather_token)


if __name__ == '__main__':
    main()
