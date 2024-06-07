
from sqlalchemy import Table, select, and_

from db.db import session, engine
from models.models import Temperature, Base
from utils.utils import get_past_days_date, get_next_days_date


class Crud:

    def _get_table(self, table_name: str) -> Table:
        """:return Table object.

        :param: table_name is a table which call for query.
        """
        return Table(
            table_name,
            Base.metadata,
            autoload_with=engine,
        )
    def get_current_temps(self, date, city, temp_type):
        """This query prevents redundant if else lines."""
        if temp_type == "C":
            results = session.query(Temperature.temp_c).filter(Temperature.date == date, Temperature.city == city).all()
            for temp in results:
                return temp.temp_c

        elif temp_type == "F":
            results = session.query(Temperature.temp_f).filter(Temperature.date == date, Temperature.city == city).all()

            for temp in results:
                return temp.temp_f

    def get_past_days_temp(self, city, temp_type, days):
        date_list = get_past_days_date(days)
        print(date_list)
        if temp_type == "C":
            results = session.query(Temperature.temp_c, Temperature.date).filter(Temperature.date.in_(date_list), Temperature.city == city).limit(days).all()

            return [(temp.temp_c, temp.date) for temp in results]

        elif temp_type == "F":
            results = session.query(Temperature.temp_f, Temperature.date).filter(Temperature.date.in_(date_list), Temperature.city == city).limit(days).all()

            return [(temp.temp_f, temp.date) for temp in results]


    def get_next_days_temp(self, city, temp_type, days):
        date_list = get_next_days_date(days)
        print(date_list)
        if temp_type == "C":
            results = session.query(Temperature.temp_c, Temperature.date).filter(Temperature.date.in_(date_list), Temperature.city == city).limit(days).all()

            return [(temp.temp_c, temp.date) for temp in results]

        elif temp_type == "F":
            results = session.query(Temperature.temp_f, Temperature.date).filter(Temperature.date.in_(date_list), Temperature.city == city).limit(days).all()
            # result order is different
            return [(temp.temp_f, temp.date) for temp in results]


