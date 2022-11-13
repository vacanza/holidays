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
from dateutil.relativedelta import SU

from holidays.holiday_base import HolidayBase


class Madagascar(HolidayBase):
    """
    https://www.officeholidays.com/countries/madagascar
    https://www.timeanddate.com/holidays/madagascar/
    """

    country = "MG"

    def _populate(self, year):
        super()._populate(year)

        # Observed since 1947
        if year <= 1946:
            return

        self[date(year, 1, 1)] = "Taom-baovao"
        self[date(year, 3, 8)] = "Fetin'ny vehivavy"
        self[date(year, 3, 29)] = "Fetin'ny mahery fo"
        self[date(year, 11, 1)] = "Fetin'ny olo-masina"
        self[date(year, 12, 25)] = "Fetin'ny noely"
        self[easter(year)] = "fetin'ny paska"
        self[easter(year) + rd(days=1)] = "Alatsinain'ny paska"
        self[easter(year) + rd(days=49)] = "Pentekosta"
        self[easter(year) + rd(days=50)] = "Alatsinain'ny pentekosta"
        self[date(year, 6, 1) + rd(day=1, weekday=SU(3))] = "Fetin'ny ray"
        self[
            easter(year) + rd(days=39)
        ] = "Fiakaran'ny Jesosy kristy tany an-danitra"
        self[date(year, 8, 15)] = "Fiakaran'ny Masina Maria tany an-danitra"

        if easter(year) + rd(days=49) == date(year, 5, 1) + rd(
            day=31, weekday=SU(-1)
        ):
            self[
                date(year, 5, 1) + rd(day=31, weekday=SU(-1)) + rd(days=7)
            ] = "Fetin'ny Reny"
        else:
            self[
                date(year, 5, 1) + rd(day=31, weekday=SU(-1))
            ] = "Fetin'ny Reny"


class MG(Madagascar):
    pass


class MDG(Madagascar):
    pass
