import requests
import datetime
from config import tg_bot_token
from config import weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.message):
    await message.reply('Привет! Напиши мне название города и Я пришлю сводку погоды! ')


@dp.message_handler()
async def get_weather(message: types.message):
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
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric&lang=ru'
        )

        data = r.json()
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
        await message.reply(f'Погода в Городе {city}: {wm}\n'
                            f'Температура: {temp}°C\n'
                            f'Скорость Ветра: {wind} м/с\n'
                            f'Влажность: {humidity}%\n'
                            f''
                            )

    except:
        await message.reply('\U00002757 Проверьте название Города!')


if __name__ == '__main__':
    executor.start_polling(dp)
