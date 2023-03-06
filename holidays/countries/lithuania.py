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

from holidays.calendars import _get_nth_weekday_of_month
from holidays.constants import JAN, FEB, MAR, MAY, JUN, AUG, DEC, SUN, JUL, NOV
from holidays.holiday_base import HolidayBase


class Lithuania(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Lithuania
    https://www.kalendorius.today/
    """

    country = "LT"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self[date(year, JAN, 1)] = "Naujieji metai"

        # Day of Restoration of the State of Lithuania (1918)
        if year >= 1918:
            self[date(year, FEB, 16)] = "Lietuvos valstybės " "atkūrimo diena"

        # Day of Restoration of Independence of Lithuania
        # (from the Soviet Union, 1990)
        if year >= 1990:
            self[date(year, MAR, 11)] = (
                "Lietuvos nepriklausomybės " "atkūrimo diena"
            )

        # Easter
        easter_date = easter(year)
        self[easter_date] = "Velykos"

        # Easter 2nd day
        self[easter_date + td(days=+1)] = "Velykų antroji diena"

        # International Workers' Day
        self[date(year, MAY, 1)] = "Tarptautinė darbo diena"

        # Mother's day. First Sunday in May
        self[_get_nth_weekday_of_month(1, SUN, MAY, year)] = "Motinos diena"

        # Fathers's day. First Sunday in June
        self[_get_nth_weekday_of_month(1, SUN, JUN, year)] = "Tėvo diena"

        # St. John's Day [Christian name],
        # Day of Dew [original pagan name]
        if year >= 2003:
            self[date(year, JUN, 24)] = "Joninės, Rasos"

        # Statehood Day
        if year >= 1991:
            self[date(year, JUL, 6)] = (
                "Valstybės (Lietuvos "
                "karaliaus Mindaugo "
                "karūnavimo) diena"
            )

        # Assumption Day
        self[date(year, AUG, 15)] = (
            "Žolinė (Švč. Mergelės " "Marijos ėmimo į dangų diena)"
        )

        # All Saints' Day
        self[date(year, NOV, 1)] = "Visų šventųjų diena (Vėlinės)"

        # All Souls' Day
        if year >= 2020:
            self[date(year, NOV, 2)] = "Mirusiųjų atminimo diena (Vėlinės)"

        # Christmas Eve
        self[date(year, DEC, 24)] = "Šv. Kūčios"

        # Christmas 1st day
        self[date(year, DEC, 25)] = "Šv. Kalėdų pirma diena"

        # Christmas 2nd day
        self[date(year, DEC, 26)] = "Šv. Kalėdų antra diena"


class LT(Lithuania):
    pass


class LTU(Lithuania):
    pass
