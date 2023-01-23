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
#  Copyright: Kateryna Golovanova <kate@kgthreads.com>, 2022

from datetime import date
from datetime import timedelta as td

from dateutil.easter import easter

from holidays.constants import AUG, DEC, FEB, JAN, MAR, MAY, NOV, SEP
from holidays.holiday_base import HolidayBase


class Liechtenstein(HolidayBase):
    """
    Liechtenstein holidays.
    See https://en.wikipedia.org/wiki/Public_holidays_in_Liechtenstein
    for details.
    """

    country = "LI"

    def _populate(self, year):
        # New Year's Day.
        self[date(year, JAN, 1)] = "Neujahr"

        # Saint Berchtold's Day.
        self[date(year, JAN, 2)] = "Berchtoldstag"

        # Epiphany.
        self[date(year, JAN, 6)] = "Drei Könige"

        # Candlemas.
        self[date(year, FEB, 2)] = "Mariä Lichtmess"

        easter_date = easter(year)
        # Shrove Tuesday.
        self[easter_date + td(days=-47)] = "Fasnachtsdienstag"

        # Saint Joseph's Day.
        self[date(year, MAR, 19)] = "Josefstag"

        # Good Friday.
        self[easter_date + td(days=-2)] = "Karfreitag"

        # Easter.
        self[easter_date] = "Ostersonntag"

        # Easter Monday.
        self[easter_date + td(days=+1)] = "Ostermontag"

        # Labor Day.
        self[date(year, MAY, 1)] = "Tag der Arbeit"

        # Ascension Day.
        self[easter_date + td(days=+39)] = "Auffahrt"

        # Pentecost.
        self[easter_date + td(days=+49)] = "Pfingstsonntag"

        # Whit Monday.
        self[easter_date + td(days=+50)] = "Pfingstmontag"

        # Corpus Christi.
        self[easter_date + td(days=+60)] = "Fronleichnam"

        # National Day.
        self[date(year, AUG, 15)] = "Staatsfeiertag"

        # Nativity of Mary.
        self[date(year, SEP, 8)] = "Maria Geburt"

        # All Saints Day.
        self[date(year, NOV, 1)] = "Allerheiligen"

        # Feast of the Immaculate Conception.
        self[date(year, DEC, 8)] = "Maria Empfängnis"

        # Christmas Eve.
        self[date(year, DEC, 24)] = "Heiliger Abend"

        # Christmas Day.
        self[date(year, DEC, 25)] = "Weihnachten"

        # St. Stephen's Day.
        self[date(year, DEC, 26)] = "Stefanstag"

        # New Year's Eve.
        self[date(year, DEC, 31)] = "Silvester"


class LI(Liechtenstein):
    pass


class LIE(Liechtenstein):
    pass
