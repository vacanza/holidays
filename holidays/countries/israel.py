#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars import _HebrewLunisolar
from holidays.calendars.gregorian import _timedelta, FRI, SAT
from holidays.calendars.hebrew import (
    HANUKKAH,
    INDEPENDENCE_DAY,
    LAG_BAOMER,
    PASSOVER,
    PURIM,
    ROSH_HASHANAH,
    SHAVUOT,
    SUKKOT,
    YOM_KIPPUR,
)
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
    """
    Israel holidays.

    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Israel
      - https://web.archive.org/web/20190923042619/https://www.knesset.gov.il/laws/special/heb/jerusalem_day_law.htm
    """

    country = "IL"
    default_language = "he"
    # %s (observed).
    observed_label = tr("(נצפה) %s")
    supported_categories = (OPTIONAL, PUBLIC, SCHOOL)
    supported_languages = ("en_US", "he", "uk")
    weekend = {FRI, SAT}

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("observed_rule", FRI_TO_PREV_THU + SAT_TO_PREV_THU)
        super().__init__(*args, **kwargs)

    def _get_holiday(self, holiday: str):
        return _HebrewLunisolar._get_holiday(holiday, self._year)

    def _populate_public_holidays(self):
        if self._year <= 1947:
            return None

        if self._year >= 2101:
            raise NotImplementedError

        # Rosh Hashanah (New Year).
        name = tr("ראש השנה")
        rosh_hashanah_dt = self._get_holiday(ROSH_HASHANAH)
        self._add_holiday(name, rosh_hashanah_dt)
        self._add_holiday(name, _timedelta(rosh_hashanah_dt, +1))

        # Yom Kippur (Day of Atonement).
        self._add_holiday(tr("יום כיפור"), self._get_holiday(YOM_KIPPUR))

        # Sukkot (Feast of Tabernacles).
        name = tr("סוכות")
        sukkot_dt = self._get_holiday(SUKKOT)
        self._add_holiday(name, sukkot_dt)
        # Simchat Torah / Shemini Atzeret.
        self._add_holiday(tr("שמחת תורה/שמיני עצרת"), _timedelta(sukkot_dt, +7))

        passover_dt = self._get_holiday(PASSOVER)
        # Pesach (Passover).
        self._add_holiday(tr("פסח"), passover_dt)
        # Shvi'i shel Pesach (Seventh day of Passover)
        self._add_holiday(tr("שביעי של פסח"), _timedelta(passover_dt, +6))

        # Yom Ha-Atzmaut (Independence Day).
        name = tr("יום העצמאות")
        independence_day_dt = self._get_holiday(INDEPENDENCE_DAY)
        rule = FRI_TO_PREV_THU + SAT_TO_PREV_THU
        if self._year >= 2004:
            rule += MON_TO_NEXT_TUE
        is_observed, _ = self._add_observed(independence_day_dt, name, rule)
        if not is_observed:
            self._add_holiday(name, independence_day_dt)

        # Shavuot.
        self._add_holiday(tr("שבועות"), self._get_holiday(SHAVUOT))

    def _populate_optional_holidays(self):
        if self._year <= 1947:
            return None

        if self._year >= 2101:
            raise NotImplementedError

        sukkot_dt = self._get_holiday(SUKKOT)
        for offset in range(1, 6):
            # Chol HaMoed Sukkot (Feast of Tabernacles holiday).
            self._add_holiday(tr("חול המועד סוכות"), _timedelta(sukkot_dt, offset))

        if self._year >= 2008:
            # Sigd.
            self._add_holiday(tr("סיגד"), _timedelta(self._get_holiday(YOM_KIPPUR), +49))

        # Purim.
        self._add_holiday(tr("פורים"), self._get_holiday(PURIM))

        passover_dt = self._get_holiday(PASSOVER)
        for offset in range(1, 6):
            # Chol HaMoed Pesach (Passover holiday).
            self._add_holiday(tr("חול המועד פסח"), _timedelta(passover_dt, offset))

        if self._year >= 1963:
            # Yom Hazikaron (Fallen Soldiers and Victims of Terrorism Remembrance Day).
            name = tr("יום הזיכרון לחללי מערכות ישראל ונפגעי פעולות האיבה")
            remembrance_day_dt = _timedelta(self._get_holiday(INDEPENDENCE_DAY), -1)
            rule = THU_TO_PREV_WED + FRI_TO_PREV_WED
            if self._year >= 2004:
                rule += SUN_TO_NEXT_MON
            is_observed, _ = self._add_observed(remembrance_day_dt, name, rule)
            if not is_observed:
                self._add_holiday(name, remembrance_day_dt)

        if self._year >= 1998:
            # Yom Yerushalayim (Jerusalem Day).
            self._add_holiday(tr("יום ירושלים"), _timedelta(self._get_holiday(LAG_BAOMER), +10))

        # Tisha B'Av (Tisha B'Av, fast).
        name = tr("תשעה באב")
        tisha_bav_dt = self._get_holiday("TISHA_BAV")
        is_observed, _ = self._add_observed(tisha_bav_dt, name, SAT_TO_NEXT_SUN)
        if not is_observed:
            self._add_holiday(name, tisha_bav_dt)

    def _populate_school_holidays(self):
        if self._year <= 1947:
            return None

        if self._year >= 2101:
            raise NotImplementedError

        sukkot_dt = self._get_holiday(SUKKOT)
        for offset in range(1, 6):
            # Chol HaMoed Sukkot (Feast of Tabernacles holiday).
            self._add_holiday(tr("חול המועד סוכות"), _timedelta(sukkot_dt, offset))

        for year in (self._year - 1, self._year):
            hanukkah_dt = _HebrewLunisolar._get_holiday(HANUKKAH, year)
            for offset in range(8):
                # Hanukkah.
                self._add_holiday(tr("חנוכה"), _timedelta(hanukkah_dt, offset))

        # Ta`anit Ester (Fast of Esther).
        name = tr("תענית אסתר")
        purim_dt = self._get_holiday(PURIM)
        taanit_ester_dt = _timedelta(purim_dt, -1)
        is_observed, _ = self._add_observed(taanit_ester_dt, name, SAT_TO_PREV_THU)
        if not is_observed:
            self._add_holiday(name, taanit_ester_dt)

        # Purim.
        self._add_holiday(tr("פורים"), purim_dt)

        passover_dt = self._get_holiday(PASSOVER)
        for offset in range(1, 6):
            # Chol HaMoed Pesach (Passover holiday).
            self._add_holiday(tr("חול המועד פסח"), _timedelta(passover_dt, offset))

        # Lag Ba'omer (Lag BaOmer).
        self._add_holiday(tr('ל"ג בעומר'), self._get_holiday(LAG_BAOMER))


class IL(Israel):
    pass


class ISR(Israel):
    pass
