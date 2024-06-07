"""This file starts app."""
import json
from datetime import datetime, timedelta
import logging
from typing import Any


from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import uvicorn

from external_services.retriever_execution import data_retriever_execution
from models.models import Temperature
from schemas.current_temperatures import CurrentTemperatures
from db.db import session, engine
from crud.crud_manager import Crud


crud = Crud()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    Temperature.__table__.drop(bind=engine, checkfirst=True)
    await data_retriever_execution()
@app.get("/status")
async def status() -> Any:
    """Check if app is running."""
    return {"success": True}

@app.get("/get_current_temperatures")
def get_current_temperatures(inputs: CurrentTemperatures):
    """returns fahreneight or celcius temperatures"""
    city = inputs.city
    date = inputs.date
    temp_type = inputs.temperature_type
    temp = crud.get_current_temps(date, city, temp_type)

    return temp


@app.get("/past_days_temperatures")
def get_past_days_temperatures(inputs: CurrentTemperatures):
    city = inputs.city

    temp_type = inputs.temperature_type
    days = inputs.days
    temp_list = crud.get_past_days_temp(city, temp_type, days)
    print(temp_list)
    return temp_list

@app.get("/next_days_temperatures")
def get_past_days_temperatures(inputs: CurrentTemperatures):
    city = inputs.city
    temp_type = inputs.temperature_type
    days = inputs.days
    temp_list = crud.get_next_days_temp(city, temp_type, days)
    print(temp_list)
    return temp_list



if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )
