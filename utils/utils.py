

from datetime import datetime, timedelta

def get_past_7_days():
    # Given date
    given_date = datetime.now()

    # List to hold previous 7 days
    previous_7_days = []

    # Loop to get the previous 7 days
    for i in range(1, 8):
        day = given_date - timedelta(days=i)
        previous_7_days.append(day)

    day_list = []
    # Print the previous 7 days
    for day in previous_7_days:
        day = day.strftime('%Y-%m-%d')
        day_list.append(day)

    return day_list