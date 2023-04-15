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

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV, DEC
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import InternationalHolidays, IslamicHolidays


class Pakistan(HolidayBase, InternationalHolidays, IslamicHolidays):
    country = "PK"

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        if year <= 1947:
            return None
        super()._populate(year)

        # Kashmir Solidarity Day
        if year >= 1990:
            self._add_holiday("Kashmir Solidarity Day", FEB, 5)

        # Pakistan Day
        if year >= 1956:
            self._add_holiday("Pakistan Day", MAR, 23)

        # Labour Day
        if year >= 1972:
            self._add_labor_day("Labour Day")

        # Independence Day
        self._add_holiday("Independence Day", AUG, 14)

        # Iqbal Day
        if year <= 2014 or year >= 2022:
            self._add_holiday("Iqbal Day", NOV, 9)

        # Quaid-e-Azam Day
        self._add_holiday("Quaid-e-Azam Day", DEC, 25)

        # Eid-ul-Fitr
        # https://www.timeanddate.com/holidays/pakistan/eid-ul-fitr-1
        dates_obs = {
            2005: ((NOV, 4),),
            2006: ((OCT, 24),),
            2007: ((OCT, 13),),
            2008: ((OCT, 2),),
            2009: ((SEP, 21),),
            2010: ((SEP, 10),),
            2011: ((AUG, 31),),
            2012: ((AUG, 19),),
            2013: ((AUG, 8),),
            2014: ((JUL, 29),),
            2015: ((JUL, 17),),
            2016: ((JUL, 6),),
            2017: ((JUN, 26),),
            2018: ((JUN, 16),),
            2019: ((JUN, 5),),
            2020: ((MAY, 24),),
            2021: ((MAY, 13),),
            2022: ((MAY, 3),),
        }
        name = "Eid-ul-Fitr"
        if year in dates_obs:
            for yr in (year - 1, year):
                for hol_date in dates_obs.get(yr, ()):
                    dt = date(yr, *hol_date)
                    self._add_holiday(name, dt)
                    self._add_holiday(name, dt + td(days=+1))
                    self._add_holiday(name, dt + td(days=+2))
        else:
            name = f"{name}* (*estimated)"
            self._add_eid_al_fitr_day(name)
            self._add_eid_al_fitr_day_two(name)
            self._add_eid_al_fitr_day_three(name)

        # Eid-ul-Adha
        # https://www.timeanddate.com/holidays/pakistan/eid-ul-azha
        dates_obs = {
            2005: ((JAN, 21),),
            2006: ((JAN, 10), (DEC, 31)),
            2007: ((DEC, 20),),
            2008: ((DEC, 9),),
            2009: ((NOV, 28),),
            2010: ((NOV, 17),),
            2011: ((NOV, 7),),
            2012: ((OCT, 26),),
            2013: ((OCT, 15),),
            2014: ((OCT, 6),),
            2015: ((SEP, 24),),
            2016: ((SEP, 12),),
            2017: ((SEP, 2),),
            2018: ((AUG, 22),),
            2019: ((AUG, 12),),
            2020: ((JUL, 31),),
            2021: ((JUL, 21),),
            2022: ((JUL, 10),),
        }
        name = "Eid-ul-Adha"
        if year in dates_obs:
            for yr in (year - 1, year):
                for hol_date in dates_obs.get(yr, ()):
                    dt = date(yr, *hol_date)
                    self._add_holiday(name, dt)
                    self._add_holiday(name, dt + td(days=+1))
                    self._add_holiday(name, dt + td(days=+2))
        else:
            name = f"{name}* (*estimated)"
            self._add_eid_al_adha_day(name)
            self._add_eid_al_adha_day_two(name)
            self._add_eid_al_adha_day_three(name)

        # Eid Milad-un-Nabi, Birth of the Prophet
        # https://www.timeanddate.com/holidays/pakistan/eid-milad-un-nabi
        dates_obs = {
            2005: ((APR, 22),),
            2006: ((APR, 11),),
            2007: ((MAR, 31),),
            2008: ((MAR, 21),),
            2009: ((MAR, 9),),
            2010: ((MAR, 1),),
            2011: ((FEB, 17),),
            2012: ((FEB, 5),),
            2013: ((JAN, 24),),
            2014: ((JAN, 14),),
            2015: ((JAN, 4),),
            2016: ((DEC, 12),),
            2017: ((DEC, 1),),
            2018: ((NOV, 21),),
            2019: ((NOV, 10),),
            2020: ((OCT, 30),),
            2021: ((OCT, 19),),
            2022: ((OCT, 9),),
        }
        name = "Eid Milad-un-Nabi"
        if year in dates_obs:
            for hol_date in dates_obs[year]:
                dt = date(year, *hol_date)
                self._add_holiday(name, dt)
        else:
            self._add_mawlid_day(f"{name}* (*estimated)")

        # Ashura
        # https://www.timeanddate.com/holidays/pakistan/first-day-ashura
        dates_obs = {
            2005: ((FEB, 18),),
            2006: ((FEB, 8),),
            2007: ((JAN, 28),),
            2008: ((JAN, 18),),
            2009: ((JAN, 6), (DEC, 26)),
            2010: ((DEC, 16),),
            2011: ((DEC, 5),),
            2012: ((NOV, 23),),
            2013: ((NOV, 13),),
            2014: ((NOV, 3),),
            2015: ((OCT, 23),),
            2016: ((OCT, 11),),
            2017: ((SEP, 30),),
            2018: ((SEP, 21),),
            2019: ((SEP, 9),),
            2020: ((AUG, 29),),
            2021: ((AUG, 18),),
            2022: ((AUG, 9),),
        }
        name = "Ashura"
        if year in dates_obs:
            for yr in (year - 1, year):
                for hol_date in dates_obs.get(yr, ()):
                    dt = date(yr, *hol_date)
                    self._add_holiday(name, dt)
                    self._add_holiday(name, dt + td(days=+1))
        else:
            name = f"{name}* (*estimated)"
            for dt in self._add_ashura_day(name):
                self._add_holiday(name, dt + td(days=+1))


class PK(Pakistan):
    pass


class PAK(Pakistan):
    pass
