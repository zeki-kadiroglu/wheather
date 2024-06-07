import json
import pytest
import requests

# Base URL of the API
BASE_URL = "http://localhost:8000"


def test_get_current_temperatures_endpoint():
    payload = {
        "city": "Paris",
        "date": "current",
        "temperature_type": "F"
    }
    response = requests.get(f"{BASE_URL}/get_current_temperatures", data=json.dumps(payload))

    assert response.status_code == 200
    assert type(response.json()) == float


def test_get_past_days_temperatures_endpoint():
    payload = {
        "city": "Paris",
        "temperature_type": "C",
        "days": 3
    }
    response = requests.get(f"{BASE_URL}/past_days_temperatures", data=json.dumps(payload))
    print(response.json())
    assert response.status_code == 200
    assert type(response.json()) == list
    assert type(response.json()[0][0]) == float




def test_get_next_days_temperatures_endpoint():
    payload = {
        "city": "Paris",
        "temperature_type": "F",
        "days": 5
    }
    response = requests.get(f"{BASE_URL}/next_days_temperatures", data=json.dumps(payload))
    assert response.status_code == 200
    assert type(response.json()) == list
    assert type(response.json()[0][0]) == float



def test_invalid_endpoint():
    response = requests.post(f"{BASE_URL}/invalidEndpoint")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not Found"


def test_get_current_temperatures_endpoint_unprocessible_entity():
    payload = {

    }
    response = requests.get(f"{BASE_URL}/get_current_temperatures", data=json.dumps(payload))

    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Field required"
