# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)


from convertdate import gregorian, hebrew
from convertdate.holidays import (
    hanukkah,
    lag_baomer,
    passover,
    purim,
    rosh_hashanah,
    shavuot,
    sukkot,
    yom_kippur,
)
from datetime import date
from dateutil.relativedelta import relativedelta as rd

from holidays.holiday_base import HolidayBase


class Israel(HolidayBase):
    def __init__(self, **kwargs):
        self.country = "IL"

        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # Passover
        name = "Passover I"
        year, month, day = passover(year, eve=True)
        passover_start_dt = date(year, month, day)
        self[passover_start_dt] = name + " - Eve"
        self[passover_start_dt + rd(days=1)] = name

        name = "Passover"
        for offset in range(2, 6):
            self[passover_start_dt + rd(days=offset)] = name + " - Chol HaMoed"

        name = "Passover VII"
        self[passover_start_dt + rd(days=6)] = name + " - Eve"
        self[passover_start_dt + rd(days=7)] = name

        # Memorial Day
        name = "Memorial Day"
        year, month, day = gregorian.from_jd(
            hebrew.to_jd_gregorianyear(year, hebrew.IYYAR, 3)
        )
        self[date(year, month, day) + rd(days=1)] = name

        observed_delta = 0
        if self.observed:
            day_in_week = date(year, month, day).weekday()
            if day_in_week in (2, 3):
                observed_delta = -(day_in_week - 1)
            elif 2004 <= year and day_in_week == 5:
                observed_delta = 1

            if observed_delta != 0:
                self[date(year, month, day) + rd(days=observed_delta + 1)] = (
                    name + " (Observed)"
                )

        # Independence Day
        name = "Independence Day"
        self[date(year, month, day) + rd(days=2)] = name

        if self.observed and observed_delta != 0:
            self[date(year, month, day) + rd(days=observed_delta + 2)] = (
                name + " (Observed)"
            )

        # Lag Baomer
        name = "Lag B'Omer"
        year, month, day = lag_baomer(year, eve=False)
        self[date(year, month, day)] = name

        # Shavuot
        name = "Shavuot"
        year, month, day = shavuot(year, eve=True)
        self[date(year, month, day)] = name + " - Eve"
        self[date(year, month, day) + rd(days=1)] = name

        # Rosh Hashana
        name = "Rosh Hashanah"
        year, month, day = rosh_hashanah(year, eve=True)
        self[date(year, month, day)] = name + " - Eve"
        self[date(year, month, day) + rd(days=1)] = name
        self[date(year, month, day) + rd(days=2)] = name

        # Yom Kippur
        name = "Yom Kippur"
        year, month, day = yom_kippur(year, eve=True)
        self[date(year, month, day)] = name + " - Eve"
        self[date(year, month, day) + rd(days=1)] = name

        # Sukkot
        name = "Sukkot I"
        year, month, day = sukkot(year, eve=True)
        sukkot_start_dt = date(year, month, day)
        self[sukkot_start_dt] = name + " - Eve"
        self[sukkot_start_dt + rd(days=1)] = name

        name = "Sukkot"
        for offset in range(2, 7):
            self[sukkot_start_dt + rd(days=offset)] = name + " - Chol HaMoed"

        name = "Sukkot VII"
        self[sukkot_start_dt + rd(days=7)] = name + " - Eve"
        self[sukkot_start_dt + rd(days=8)] = name

        # Hanukkah
        name = "Hanukkah"
        year, month, day = hanukkah(year, eve=False)
        for offset in range(8):
            self[date(year, month, day) + rd(days=offset)] = name

        # Purim
        name = "Purim"
        year, month, day = purim(year, eve=True)
        self[date(year, month, day)] = name + " - Eve"
        self[date(year, month, day) + rd(days=1)] = name
        self[date(year, month, day) + rd(days=2)] = "Shushan Purim"


class IL(Israel):
    pass


class ISR(Israel):
    pass
