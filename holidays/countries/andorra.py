#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, MAY, JUL, AUG, SEP, NOV, DEC
from holidays.holiday_base import HolidayBase


class Andorra(HolidayBase):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Andorra
    """

    country = "AD"
    subdivisions = [
        "AD-02",  # Canillo.
        "AD-03",  # Encamp.
        "AD-04",  # La Massana.
        "AD-05",  # Ordino.
        "AD-06",  # Sant Julià de Lòria.
        "AD-07",  # Andorra la Vella.
        "AD-08",  # Escaldes-Engordany.
    ]

    def _populate(self, year: int) -> None:
        super()._populate(year)

        # New Year's Day.
        self[date(year, JAN, 1)] = "New Year's Day"

        # Epiphany.
        self[date(year, JAN, 6)] = "Epiphany"

        easter_sunday = easter(year)

        # Carnival.
        self[easter_sunday + rd(days=-47)] = "Carnival"

        # Constitution Day.
        self[date(year, MAR, 14)] = "Constitution Day"

        # Good Friday.
        self[easter_sunday + rd(days=-2)] = "Good Friday"

        # Easter Sunday.
        self[easter_sunday + rd(days=+1)] = "Easter Monday"

        # Labour Day.
        self[date(year, MAY, 1)] = "Labour Day"

        # Whit Monday.
        self[easter_sunday + rd(days=+50)] = "Whit Monday"

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
        parish_holidays_mapping = {
            "AD-02": (
                (date(year, JUL, 21), "Canillo Annual Festival"),
                (date(year, JUL, 22), "Canillo Annual Festival"),
                (date(year, JUL, 23), "Canillo Annual Festival"),
            ),
            "AD-03": (
                (date(year, AUG, 15), "Encamp Annual Festival"),
                (date(year, AUG, 16), "Encamp Annual Festival"),
            ),
            "AD-04": (
                (date(year, AUG, 15), "La Massana Annual Festival"),
                (date(year, AUG, 16), "La Massana Annual Festival"),
            ),
            "AD-05": (
                (date(year, AUG, 15), "Ordino Annual Festival"),
                (date(year, AUG, 16), "Ordino Annual Festival"),
            ),
            "AD-06": (
                (date(year, JUL, 27), "Sant Julià de Lòria Annual Festival"),
                (date(year, JUL, 28), "Sant Julià de Lòria Annual Festival"),
                (date(year, JUL, 29), "Sant Julià de Lòria Annual Festival"),
                (date(year, JUL, 30), "Sant Julià de Lòria Annual Festival"),
            ),
            "AD-07": (
                (date(year, AUG, 4), "Andorra la Vella Annual Festival"),
                (date(year, AUG, 5), "Andorra la Vella Annual Festival"),
                (date(year, AUG, 6), "Andorra la Vella Annual Festival"),
            ),
            "AD-08": (
                (date(year, JUL, 25), "Escaldes–Engordany Annual Festival"),
                (date(year, JUL, 26), "Escaldes–Engordany Annual Festival"),
            ),
        }

        if self.subdiv:
            for holiday_date, holiday_name in parish_holidays_mapping[
                self.subdiv
            ]:
                self[holiday_date] = holiday_name


class AD(Andorra):
    pass


class AND(Andorra):
    pass
