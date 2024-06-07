## wheather
* Python version: `Python3.9`
* In order to run the project, firstly create a python `virtual environment`.
* Secondly, install the requirement.txt, by using `pip install -r requirements.txt`
* Then use this command under the wheather directory: `python3 main.py`

## Clarification:
* `External Service module` retrieves data from remote URL.
* Whenever starts the app, DataBase is updated thanks to this module. 

## Test Endpoints:
* There are 3 different end points. They can be tested on `Postman`
### Used body request entities and their definition
* `city`: String, one of the cities in that list, [Paris, New Delhi, Istanbul, New York]
* `date`: String(Optional), `current` represents today's date, Apart from that in `DataBase` you can access 7 days previous and 7 days later data on following format -->  2024-06-07 (String value) 
* `temperature_type`: String, It has 2 different values. `C: celcius` and `F: fahrenheit`. This will provide celcius or fahrenheit temperature value.
* `days`: Integer, Not bigger than `7` value. It can be changed. For example, if `days` is `5`, response will return 5 days data according to endpoint.


### End Points


    `GET`: (http://localhost:8000/get_current_temperatures) --> sample body request: {"city":"Paris", "date": "current","temperature_type":"F"}
    Info: This endpoint will return current temperature of the selected city
    Response: 57.2

     `GET`: (http://localhost:8000/past_days_temperatures) --> sample body request: {"city":"Paris","temperature_type": "C","days":3}
    Info: This endpoint will return past 3 days, temperatures and date.
    Response: [[15.6,"2024-06-07"],[14.6,"2024-06-06"],[15.6,"2024-06-05"]]


    `GET`: (http://localhost:8000/next_days_temperatures) --> sample body request: {"city":"Paris","temperature_type": "F","days":6}
    Info: This endpoint will return next 3 days, temperatures and date.
    Response: [[15.6,"2024-06-07"],[14.6,"2024-06-06"],[15.6,"2024-06-05"]]

### Unit tests
* Under the `test` directory, run this command `pytest test_app_api.py`.


    
