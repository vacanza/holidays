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

from convertdate import gregorian, hebrew
from convertdate.holidays import hanukkah, lag_baomer, passover, purim
from convertdate.holidays import rosh_hashanah, shavuot, sukkot, yom_kippur

from holidays.holiday_base import HolidayBase


class Israel(HolidayBase):
    country = "IL"

    def _populate(self, year):
        super()._populate(year)

        # Passover
        name = "Passover I"
        passover_start_dt = date(*passover(year, eve=True))
        self[passover_start_dt] = name + " - Eve"
        self[passover_start_dt + td(days=+1)] = name

        name = "Passover"
        for offset in range(2, 6):
            self[passover_start_dt + td(days=offset)] = name + " - Chol HaMoed"

        name = "Passover VII"
        self[passover_start_dt + td(days=+6)] = name + " - Eve"
        self[passover_start_dt + td(days=+7)] = name

        # Memorial Day
        name = "Memorial Day"
        memorial_day_dt = date(
            *gregorian.from_jd(
                hebrew.to_jd_gregorianyear(year, hebrew.IYYAR, 3)
            )
        )
        self[memorial_day_dt + td(days=+1)] = name

        observed_delta = 0
        if self.observed:
            day_in_week = memorial_day_dt.weekday()
            if self._is_wednesday(memorial_day_dt) or self._is_thursday(
                memorial_day_dt
            ):
                observed_delta = -(day_in_week - 1)
            elif 2004 <= year and self._is_saturday(memorial_day_dt):
                observed_delta = 1

            if observed_delta != 0:
                self[memorial_day_dt + td(days=observed_delta + 1)] = (
                    name + " (Observed)"
                )

        # Independence Day
        name = "Independence Day"
        self[memorial_day_dt + td(days=+2)] = name

        if self.observed and observed_delta != 0:
            self[memorial_day_dt + td(days=observed_delta + 2)] = (
                name + " (Observed)"
            )

        # Lag Baomer
        name = "Lag B'Omer"
        lag_baomer_dt = date(*lag_baomer(year, eve=False))
        self[lag_baomer_dt] = name

        # Shavuot
        name = "Shavuot"
        shavuot_dt = date(*shavuot(year, eve=True))
        self[shavuot_dt] = name + " - Eve"
        self[shavuot_dt + td(days=+1)] = name

        # Rosh Hashana
        name = "Rosh Hashanah"
        rosh_hashanah_dt = date(*rosh_hashanah(year, eve=True))
        self[rosh_hashanah_dt] = name + " - Eve"
        self[rosh_hashanah_dt + td(days=+1)] = name
        self[rosh_hashanah_dt + td(days=+2)] = name

        # Yom Kippur
        name = "Yom Kippur"
        yom_kippur_dt = date(*yom_kippur(year, eve=True))
        self[yom_kippur_dt] = name + " - Eve"
        self[yom_kippur_dt + td(days=+1)] = name

        # Sukkot
        name = "Sukkot I"
        sukkot_start_dt = date(*sukkot(year, eve=True))
        self[sukkot_start_dt] = name + " - Eve"
        self[sukkot_start_dt + td(days=+1)] = name

        name = "Sukkot"
        for offset in range(2, 7):
            self[sukkot_start_dt + td(days=offset)] = name + " - Chol HaMoed"

        name = "Sukkot VII"
        self[sukkot_start_dt + td(days=+7)] = name + " - Eve"
        self[sukkot_start_dt + td(days=+8)] = name

        # Hanukkah
        name = "Hanukkah"
        hk_start_date = date(*hanukkah(year, eve=False))
        for offset in range(8):
            hk_date = hk_start_date + td(days=offset)
            if hk_date.year == year:
                self[hk_date] = name
        # Some o prior's year Hannukah may fall in current year.
        hk_start_date = date(*hanukkah(year - 1, eve=False))
        for offset in range(8):
            hk_date = hk_start_date + td(days=offset)
            if hk_date.year == year:
                self[hk_date] = name

        # Purim
        name = "Purim"
        purim_date = date(*purim(year, eve=True))
        self[purim_date] = name + " - Eve"
        self[purim_date + td(days=+1)] = name
        self[purim_date + td(days=+2)] = "Shushan Purim"


class IL(Israel):
    pass


class ISR(Israel):
    pass
