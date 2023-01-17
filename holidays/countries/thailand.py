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

from dateutil.relativedelta import relativedelta as rd

from holidays.constants import FEB, MAR, APR, MAY, JUN, JUL, AUG, OCT, DEC, SAT
from holidays.holiday_base import HolidayBase
from holidays.utils import _ChineseLuniSolar


class Thailand(HolidayBase):
    """
    Thailand holidays.

    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Thailand
    """

    country = "TH"

    def __init__(self, **kwargs):
        self.cnls = _ChineseLuniSolar()
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        def add_holiday(dt, holiday_name):
            if dt.year != year:
                return

            self[dt] = holiday_name
            if self.observed and self._is_weekend(dt):
                in_lieu = dt + rd(days=2 if dt.weekday() == SAT else 1)
                while in_lieu.year == year and in_lieu in self:
                    in_lieu += rd(days=+1)

                add_holiday(in_lieu, f"{holiday_name} (in lieu)")

        super()._populate(year)

        # New Year's Day.
        add_holiday(date(year, 1, 1), "New Year's Day")

        # Magha Pujab.
        # TODO(ark): research Buddhist calendar options.
        magha_puja = {
            2016: (FEB, 22),
            2017: (FEB, 11),
            2018: (MAR, 1),
            2019: (FEB, 19),
            2020: (FEB, 26),
            2021: (FEB, 26),
            2022: (FEB, 16),
            2023: (MAR, 6),
        }
        if year in magha_puja:
            add_holiday(date(year, *magha_puja[year]), "Makha Bucha")

        # Chakri Memorial Day.
        add_holiday(date(year, APR, 6), "Chakri Memorial Day")

        # Songkran Festival.
        songkran_festival = "Songkran Festival"
        add_holiday(date(year, APR, 13), songkran_festival)
        add_holiday(date(year, APR, 14), songkran_festival)
        add_holiday(date(year, APR, 15), songkran_festival)

        # Labour day.
        add_holiday(date(year, MAY, 1), "Labour Day")

        # Buddha's Birthday.
        add_holiday(self.cnls.vesak_may_date(year), "Buddha's Birthday")

        # Coronation Day.
        if year <= 2016:
            add_holiday(date(year, MAY, 5), "Coronation Day")
        elif year >= 2020:
            add_holiday(date(year, MAY, 4), "Coronation Day")

        # Queen's Birthday.
        add_holiday(date(year, JUN, 3), "Queen Suthida's Birthday")

        # King's Birthday.
        add_holiday(date(year, JUL, 28), "King's Birthday")

        # Asalha Puja.
        asalha_puja = {
            2006: (JUL, 11),
            2007: (JUN, 30),
            2008: (JUL, 18),
            2009: (JUL, 7),
            2010: (JUL, 25),
            2011: (JUL, 15),
            2012: (AUG, 2),
            2013: (JUL, 30),
            2014: (JUL, 13),
            2015: (JUL, 30),
            2016: (JUL, 15),
            2017: (JUL, 9),
            2018: (JUL, 29),
            2019: (JUL, 16),
            2020: (JUL, 5),
            2021: (JUL, 24),
            2022: (JUL, 13),
            2023: (JUL, 3),
            2024: (JUL, 21),
            2025: (JUL, 10),
        }
        if year in asalha_puja:
            add_holiday(date(year, *asalha_puja[year]), "Asalha Puja")

        # Beginning of Vassa.
        vassa = {
            2006: (JUL, 12),
            2007: (JUL, 31),
            2008: (JUL, 19),
            2009: (JUL, 8),
            2010: (JUL, 27),
            2011: (JUL, 16),
            2012: (AUG, 3),
            2013: (JUL, 23),
            2014: (JUL, 13),
            2015: (AUG, 1),
            2016: (JUL, 20),
            2017: (JUL, 9),
            2018: (JUL, 28),
            2019: (JUL, 17),
            2020: (JUL, 6),
            2021: (JUL, 25),
            2022: (JUL, 14),
            2023: (AUG, 2),
            2024: (JUL, 21),
            2025: (JUL, 23),
        }
        if year in vassa:
            add_holiday(date(year, *vassa[year]), "Beginning of Vassa")

        # The Queen Sirikit's Birthday.
        add_holiday(date(year, AUG, 12), "The Queen Mother's Birthday")

        # Anniversary for the Death of King Bhumibol Adulyadej.
        add_holiday(
            date(year, OCT, 13), "King Bhumibol Adulyadej Memorial Day"
        )

        # King Chulalongkorn Day
        add_holiday(date(year, OCT, 23), "King Chulalongkorn Day")

        # King Bhumibol Adulyadej's Birthday Anniversary.
        add_holiday(date(year, DEC, 5), "King Bhumibol Adulyadej's Birthday")

        # Constitution Day.
        add_holiday(date(year, DEC, 10), "Constitution Day")

        # New Year's Eve.
        add_holiday(date(year, DEC, 31), "New Year's Eve")


class TH(Thailand):
    pass


class THA(Thailand):
    pass
