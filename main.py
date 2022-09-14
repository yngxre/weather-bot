import requests
from pprint import pprint
from config import weather_token


def get_weather(city, weather_token):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric'
        )
        data = r.json()
        # pprint(data)

        city = data['name']
        temp = data['main']['temp']
        weather = data['weather']['description']
        print(f'Погода в Городе {city}°C : {temp}\nweather')


    except Exception as ex:
        print('ex')
        print('Check City Name!')



def main():
    city = input('Please, input name of the City: ')
    get_weather(city, weather_token)


if __name__ == '__main__':
    main()
