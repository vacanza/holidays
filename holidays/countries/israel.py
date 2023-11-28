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

from datetime import timedelta as td

from holidays.calendars import _HebrewLunisolar
from holidays.constants import OPTIONAL, PUBLIC, SCHOOL
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    MON_TO_NEXT_TUE,
    THU_TO_PREV_WED,
    FRI_TO_PREV_WED,
    FRI_TO_PREV_THU,
    SAT_TO_PREV_THU,
    SAT_TO_NEXT_SUN,
    SUN_TO_NEXT_MON,
)


class Israel(ObservedHolidayBase):
    country = "IL"
    observed_label = "%s (Observed)"
    supported_categories = (OPTIONAL, PUBLIC, SCHOOL)

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("observed_rule", FRI_TO_PREV_THU + SAT_TO_PREV_THU)
        super().__init__(*args, **kwargs)

    def _get_holiday(self, holiday: str):
        return _HebrewLunisolar.hebrew_holiday_date(self._year, holiday)

    def _populate_public_holidays(self):
        if self._year <= 1947:
            return None

        if self._year >= 2101:
            raise NotImplementedError

        # Rosh Hashanah
        rosh_hashanah_dt = self._get_holiday("ROSH_HASHANAH")
        name = "Rosh Hashanah"
        self._add_holiday(name, rosh_hashanah_dt)
        self._add_holiday(name, rosh_hashanah_dt + td(days=+1))

        # Yom Kippur
        self._add_holiday("Yom Kippur", self._get_holiday("YOM_KIPPUR"))

        # Sukkot
        sukkot_dt = self._get_holiday("SUKKOT")
        self._add_holiday("Sukkot", sukkot_dt)
        self._add_holiday("Simchat Torah / Shemini Atzeret", sukkot_dt + td(days=+7))

        # Passover
        passover_dt = self._get_holiday("PASSOVER")
        self._add_holiday("Passover", passover_dt)
        self._add_holiday("Seventh day of Passover", passover_dt + td(days=+6))

        # Independence Day
        name = "Independence Day"
        independence_day_dt = self._get_holiday("INDEPENDENCE_DAY")
        rule = FRI_TO_PREV_THU + SAT_TO_PREV_THU
        if self._year >= 2004:
            rule += MON_TO_NEXT_TUE
        is_obs, _ = self._add_observed(independence_day_dt, name, rule)
        if not is_obs:
            self._add_holiday(name, independence_day_dt)

        # Shavuot
        self._add_holiday("Shavuot", self._get_holiday("SHAVUOT"))

    def _populate_optional_holidays(self):
        if self._year <= 1947:
            return None

        if self._year >= 2101:
            raise NotImplementedError

        # Sukkot Chol HaMoed
        sukkot_dt = self._get_holiday("SUKKOT")
        for offset in range(1, 6):
            self._add_holiday("Sukkot", sukkot_dt + td(days=offset))

        if self._year >= 2008:
            # Sigd
            self._add_holiday("Sigd", self._get_holiday("YOM_KIPPUR") + td(days=+49))

        # Purim
        self._add_holiday("Purim", self._get_holiday("PURIM"))

        # Passover (Chol HaMoed Pesach)
        passover_dt = self._get_holiday("PASSOVER")
        for offset in range(1, 6):
            self._add_holiday("Passover", passover_dt + td(days=offset))

        # Memorial Day
        if self._year >= 1963:
            name = "Memorial Day"
            memorial_day_dt = self._get_holiday("INDEPENDENCE_DAY") + td(days=-1)
            rule = THU_TO_PREV_WED + FRI_TO_PREV_WED
            if self._year >= 2004:
                rule += SUN_TO_NEXT_MON
            is_obs, _ = self._add_observed(memorial_day_dt, name, rule)
            if not is_obs:
                self._add_holiday(name, memorial_day_dt)

        # Jerusalem Day
        self._add_holiday("Jerusalem Day", self._get_holiday("LAG_BAOMER") + td(days=+10))

        # Tisha B'Av
        name = "Tisha B'Av"
        tisha_bav_dt = self._get_holiday("TISHA_BAV")
        is_obs, _ = self._add_observed(tisha_bav_dt, name, SAT_TO_NEXT_SUN)
        if not is_obs:
            self._add_holiday(name, tisha_bav_dt)

    def _populate_school_holidays(self):
        if self._year <= 1947:
            return None

        if self._year >= 2101:
            raise NotImplementedError

        # Sukkot Chol HaMoed
        sukkot_dt = self._get_holiday("SUKKOT")
        for offset in range(1, 6):
            self._add_holiday("Sukkot", sukkot_dt + td(days=offset))

        # Hanukkah
        for yr in (self._year - 1, self._year):
            hanukkah_dt = _HebrewLunisolar.hebrew_holiday_date(yr, "HANUKKAH")
            for offset in range(8):
                self._add_holiday("Hanukkah", hanukkah_dt + td(days=offset))

        # Fast of Esther
        name = "Fast of Esther"
        purim_dt = self._get_holiday("PURIM")
        taanit_ester_dt = purim_dt + td(days=-1)
        is_obs, _ = self._add_observed(taanit_ester_dt, name, SAT_TO_PREV_THU)
        if not is_obs:
            self._add_holiday(name, taanit_ester_dt)

        # Purim
        self._add_holiday("Purim", purim_dt)

        # Passover (Chol HaMoed Pesach)
        passover_dt = self._get_holiday("PASSOVER")
        for offset in range(1, 6):
            self._add_holiday("Passover", passover_dt + td(days=offset))

        # Lag BaOmer
        self._add_holiday("Lag BaOmer", self._get_holiday("LAG_BAOMER"))


class IL(Israel):
    pass


class ISR(Israel):
    pass
