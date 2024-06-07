import asyncio

from daily_scheduler import set_daily_scheduler
from db.db import session
from external_services.data_retriever import DataRetriever
from models.models import Temperature


def daily_module():
    """Run daily the modules in the function. In order update data source everyday."""
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

