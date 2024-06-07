

from datetime import datetime, timedelta
from typing import Optional


def get_past_days_date(days: Optional[int]=7):
    # Given date
    given_date = datetime.now()

    # List to hold previous 7 days
    previous_days = []

    # Loop to get the previous 7 days
    for i in range(days):
        day = given_date - timedelta(days=i)
        previous_days.append(day)

    day_list = []
    # Print the previous 7 days
    for day in previous_days:
        day = day.strftime('%Y-%m-%d')
        day_list.append(day)

    return day_list

def get_next_days_date(days: int):
    # Given date
    given_date = datetime.now()

    # List to hold previous 7 days
    previous_days = []

    # Loop to get the previous 7 days
    for i in range(days):
        day = given_date + timedelta(days=i)
        previous_days.append(day)

    day_list = []
    # Print the previous 7 days
    for day in previous_days:
        day = day.strftime('%Y-%m-%d')
        day_list.append(day)

    return day_list