import sys

import aiohttp
import asyncio
from db.db import session, engine
# from db.models import CityTemperature, City
import os
from dotenv import load_dotenv

from models.models import Temperature
from utils.utils import get_past_days_date

# Load the environment variables from the .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv('API_KEY')
secret_key = os.getenv('API_NAME')


class DataRetriever:

    cities = ["New Delhi", "İstanbul", "New York", "Paris"]

    def __init__(self):
        Temperature.__table__.create(bind=engine, checkfirst=True)

    async def fetch_weather(self, session, url):
        async with session.get(url) as response:
            return await response.json()


    async def fetch_weather_data(self, session, city, API_URL):
        url = API_URL.format(city=city, api_key=api_key)
        async with session.get(url) as response:
            return await response.json()


    async def fetch_current_weather_data(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_weather_data(session, city,
                                        f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no") for
                     city in self.cities]
            return await asyncio.gather(*tasks)


    async def fetch_forecast_weather_data(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_weather_data(session, city,
                                        f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=7&aqi=no&alerts=no")
                     for city in self.cities]
            return await asyncio.gather(*tasks)


    async def fetch_historic_weather_data(self):
        async with aiohttp.ClientSession() as session:
            days_list = get_past_days_date()
            tasks = []
            for city in self.cities:
                for day in days_list:
                    tasks.append(self.fetch_weather_data(session, city,
                                                    f"https://api.weatherapi.com/v1/history.json?key={api_key}&q={city}&dt={day}"))
            return await asyncio.gather(*tasks)

