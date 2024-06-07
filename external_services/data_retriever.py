import sys

import aiohttp
import asyncio
from db.db import session
# from db.models import CityTemperature, City
import os
from dotenv import load_dotenv

from models.models import Temperature

# Load the environment variables from the .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv('API_KEY')
secret_key = os.getenv('API_NAME')


class DataRetriever:

    cities = ["New Delhi", "İstanbul", "New York", "Paris"]


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
            days_list = get_past_7_days()
            tasks = []
            for city in self.cities:
                for day in days_list:
                    tasks.append(self.fetch_weather_data(session, city,
                                                    f"https://api.weatherapi.com/v1/history.json?key={api_key}&q={city}&dt={day}"))
            return await asyncio.gather(*tasks)

retriever = DataRetriever()
weather_hist_data = asyncio.run(retriever.fetch_historic_weather_data())
hist = {}
for i in weather_hist_data:
    hist["city"] = i["location"]["name"]

    hist["date"] = i["forecast"]["forecastday"][0]["date"]
    hist["temp_c"] = i["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
    hist["temp_f"] = i["forecast"]["forecastday"][0]["day"]["avgtemp_f"]

    session.add(Temperature(**hist))
session.commit()

curr = {}
weather_current_data = asyncio.run(retriever.fetch_current_weather_data())
for i in weather_current_data:
    curr["city"] = i["location"]["name"]
    curr["date"] = "current"
    curr["temp_c"] = i["current"]["temp_c"]
    curr["temp_f"] = i["current"]["temp_f"]
    session.add(Temperature(**curr))
session.commit()

weather_forecast_data = asyncio.run(retriever.fetch_forecast_weather_data())

forecast = {}

for i in weather_forecast_data:
    for j in i["forecast"]["forecastday"]:
        forecast["city"] = i["location"]["name"]
        forecast["date"] = j["date"]
        forecast["temp_c"] = j["day"]["avgtemp_c"]
        forecast["temp_f"] = j["day"]["avgtemp_f"]

        session.add(Temperature(**forecast))

session.commit()


session.close()