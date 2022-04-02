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

from datetime import date, datetime

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import MON, TUE, SUN
from holidays.constants import JAN, FEB, APR, MAY, AUG, DEC
from holidays.holiday_base import HolidayBase


class Zimbabwe(HolidayBase):
    country = "ZW"

    def __init__(self, **kwargs):
        # https://en.wikipedia.org/wiki/Robert_Mugabe
        # https://en.wikipedia.org/wiki/Public_holidays_in_Zimbabwe
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        if year > 1987:
            self[date(year, JAN, 1)] = "New Year's Day"

            if year > 2017:
                # https://en.wikipedia.org/wiki/Robert_Gabriel_Mugabe_National_Youth_Day
                self[
                    date(year, FEB, 21)
                ] = "Robert Gabriel Mugabe National Youth Day"

            e = easter(year)
            good_friday = e - rd(days=2)
            easter_saturday = e - rd(days=1)
            easter_monday = e + rd(days=1)
            self[good_friday] = "Good Friday"
            self[easter_saturday] = "Easter Saturday"
            self[easter_monday] = "Easter Monday"

            self[date(year, APR, 18)] = "Independence Day"

            self[date(year, MAY, 1)] = "Workers' Day"
            self[date(year, MAY, 25)] = "Africa Day"

            # 2nd Monday of August
            # Find the date of the 2nd Monday
            # for the given year
            zimbabwe_heroes_day = date(year, AUG, 8)
            while zimbabwe_heroes_day.isoweekday() != MON and (
                8 <= zimbabwe_heroes_day.day <= 14
            ):
                zimbabwe_heroes_day = zimbabwe_heroes_day + rd(days=1)

            self[zimbabwe_heroes_day] = "Zimbabwe Heroes' Day"

            # 2nd Tuesday of August
            # Find the date of the 2nd Tuesday
            # for the given year
            defence_forces_day = datetime(year, AUG, 8)
            while defence_forces_day.isoweekday() != TUE and (
                8 <= defence_forces_day.day <= 14
            ):
                defence_forces_day = defence_forces_day + rd(days=1)

            self[defence_forces_day] = "Defense Forces Day"

            self[date(year, DEC, 22)] = "Unity Day"
            self[date(year, DEC, 25)] = "Christmas Day"
            self[date(year, DEC, 26)] = "Boxing Day"

            for k, v in list(self.items()):
                if self.observed and k.weekday() == SUN and k.year == year:
                    add_days = 1
                    while self.get(k + rd(days=add_days)) is not None:
                        add_days += 1
                    self[k + rd(days=add_days)] = v + " (Observed)"


class ZW(Zimbabwe):
    pass


class ZWE(Zimbabwe):
    pass
