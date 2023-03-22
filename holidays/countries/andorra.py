#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from datetime import timedelta as td

from dateutil.easter import easter

from holidays.calendars import _get_nth_weekday_from, _get_nth_weekday_of_month
from holidays.constants import JAN, MAR, MAY, JUL, AUG, SEP, NOV, DEC, FRI, SAT
from holidays.holiday_base import HolidayBase


class Andorra(HolidayBase):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Andorra
      - https://www.holsdb.com/public-holidays/ad
    """

    country = "AD"
    subdivisions = [
        "02",  # Canillo.
        "03",  # Encamp.
        "04",  # La Massana.
        "05",  # Ordino.
        "06",  # Sant Julià de Lòria.
        "07",  # Andorra la Vella.
        "08",  # Escaldes-Engordany.
    ]

    def _populate(self, year: int) -> None:
        super()._populate(year)

        # New Year's Day.
        self[date(year, JAN, 1)] = "New Year's Day"

        # Epiphany.
        self[date(year, JAN, 6)] = "Epiphany"

        easter_sunday = easter(year)

        # Carnival.
        self[easter_sunday + td(days=-47)] = "Carnival"

        # Constitution Day.
        self[date(year, MAR, 14)] = "Constitution Day"

        # Good Friday.
        self[easter_sunday + td(days=-2)] = "Good Friday"

        # Easter Sunday.
        self[easter_sunday + td(days=+1)] = "Easter Monday"

        # Labour Day.
        self[date(year, MAY, 1)] = "Labour Day"

        # Whit Monday.
        self[easter_sunday + td(days=+50)] = "Whit Monday"

        # Assumption Day.
        self[date(year, AUG, 15)] = "Assumption Day"

        # National Day.
        self[date(year, SEP, 8)] = "National Day"

        # All Saints' Day.
        self[date(year, NOV, 1)] = "All Saints' Day"

        # Immaculate Conception Day.
        self[date(year, DEC, 8)] = "Immaculate Conception Day"

        # Christmas Day.
        self[date(year, DEC, 25)] = "Christmas Day"

        # Saint Stephen's Day.
        self[date(year, DEC, 26)] = "Saint Stephen's Day"

        # Parish local holidays.
        third_sat_of_july = _get_nth_weekday_of_month(3, SAT, JUL, year)
        last_fri_of_july = _get_nth_weekday_from(-1, FRI, date(year, JUL, 29))
        first_sat_of_august = _get_nth_weekday_of_month(1, SAT, AUG, year)

        parish_holidays_mapping = {
            "02": ((third_sat_of_july, 3, "Canillo Annual Festival"),),
            "03": ((date(year, AUG, 15), 2, "Encamp Annual Festival"),),
            "04": ((date(year, AUG, 15), 2, "La Massana Annual Festival"),),
            "05": ((date(year, AUG, 15), 2, "Ordino Annual Festival"),),
            "06": (
                (
                    last_fri_of_july,
                    4,
                    "Sant Julià de Lòria Annual Festival",
                ),
            ),
            "07": (
                (
                    first_sat_of_august,
                    3,
                    "Andorra la Vella Annual Festival",
                ),
            ),
            "08": (
                (date(year, JUL, 25), 2, "Escaldes–Engordany Annual Festival"),
            ),
        }

        if self.subdiv:
            for (
                holiday_date,
                num_days,
                holiday_name,
            ) in parish_holidays_mapping[self.subdiv]:
                for delta in range(num_days):
                    self[holiday_date + td(days=delta)] = holiday_name


class AD(Andorra):
    pass


class AND(Andorra):
    pass
