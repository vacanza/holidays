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
from holidays.constants import JAN, MAR, MAY, JUN, AUG, NOV, DEC, SUN
from holidays.holiday_base import HolidayBase


class Madagascar(HolidayBase):
    """
    https://www.officeholidays.com/countries/madagascar
    https://www.timeanddate.com/holidays/madagascar/
    """

    country = "MG"

    def _populate(self, year):
        # Observed since 1947
        if year <= 1946:
            return None

        super()._populate(year)

        self[date(year, JAN, 1)] = "Taom-baovao / New Year's Day"
        self[date(year, MAR, 8)] = "Fetin'ny vehivavy / Women's Day"
        self[date(year, MAR, 29)] = "Fetin'ny mahery fo / Martyrs' Day"
        self[date(year, MAY, 1)] = "Labour Day"
        self[
            _get_nth_weekday_of_month(3, SUN, JUN, year)
        ] = "Fetin'ny ray / Father's Day"

        if year >= 1960:
            self[date(year, JUN, 26)] = "Independence Day"

        self[
            date(year, AUG, 15)
        ] = "Fiakaran'ny Masina Maria tany an-danitra / Assumption Day"

        self[date(year, NOV, 1)] = "Fetin'ny olo-masina / All Saints' Day"

        if year >= 2011:
            self[date(year, DEC, 11)] = "Republic Day"

        self[date(year, DEC, 25)] = "Fetin'ny noely / Christmas Day"

        easter_date = easter(year)
        self[easter_date] = "Fetin'ny paska / Easter Sunday"
        self[easter_date + td(days=+1)] = "Alatsinain'ny paska / Easter Monday"
        self[
            easter_date + td(days=+39)
        ] = "Fiakaran'ny Jesosy kristy tany an-danitra / Ascension Day"

        whit_sunday = easter_date + td(days=+49)
        self[whit_sunday] = "Pentekosta / Whit Sunday"

        self[
            easter_date + td(days=+50)
        ] = "Alatsinain'ny pentekosta / Whit Monday"

        dt = _get_nth_weekday_of_month(-1, SUN, MAY, year)
        if dt == whit_sunday:
            dt += td(days=+7)
        self[dt] = "Fetin'ny Reny / Mother's Day"


class MG(Madagascar):
    pass


class MDG(Madagascar):
    pass
