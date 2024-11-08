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

from holidays.calendars.gregorian import _timedelta, FRI, SAT
from holidays.constants import OPTIONAL, PUBLIC, SCHOOL
from holidays.groups import HebrewCalendarHolidays
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


class Israel(ObservedHolidayBase, HebrewCalendarHolidays):
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
    start_year = 1948

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("observed_rule", FRI_TO_PREV_THU + SAT_TO_PREV_THU)
        super().__init__(*args, **kwargs)

    def _add_observed(self, dt, name, rule):
        is_observed, _ = super()._add_observed(dt, name, rule)
        if not is_observed:
            self._add_holiday(name, dt)

    def _populate_public_holidays(self):
        # Rosh Hashanah (New Year).
        self._add_hebrew_holiday(tr("ראש השנה"), self._rosh_hashanah_date, range(2))

        # Yom Kippur (Day of Atonement).
        self._add_hebrew_holiday(tr("יום כיפור"), self._yom_kippur_date)

        # Sukkot (Feast of Tabernacles).
        self._add_hebrew_holiday(tr("סוכות"), self._sukkot_date)
        # Simchat Torah / Shemini Atzeret.
        self._add_hebrew_holiday(tr("שמחת תורה/שמיני עצרת"), self._sukkot_date, +7)

        # Pesach (Passover).
        self._add_hebrew_holiday(tr("פסח"), self._passover_date)
        # Shvi'i shel Pesach (Seventh day of Passover)
        self._add_hebrew_holiday(tr("שביעי של פסח"), self._passover_date, +6)

        rule = FRI_TO_PREV_THU + SAT_TO_PREV_THU
        if self._year >= 2004:
            rule += MON_TO_NEXT_TUE
        # Yom Ha-Atzmaut (Independence Day).
        self._add_observed(self._israel_independence_date, tr("יום העצמאות"), rule)

        # Shavuot.
        self._add_hebrew_holiday(tr("שבועות"), self._shavuot_date)

    def _populate_optional_holidays(self):
        # Chol HaMoed Sukkot (Feast of Tabernacles holiday).
        self._add_hebrew_holiday(tr("חול המועד סוכות"), self._sukkot_date, range(1, 6))

        if self._year >= 2008:
            # Sigd.
            self._add_hebrew_holiday(tr("סיגד"), self._yom_kippur_date, +49)

        # Purim.
        self._add_hebrew_holiday(tr("פורים"), self._purim_date)

        # Chol HaMoed Pesach (Passover holiday).
        self._add_hebrew_holiday(tr("חול המועד פסח"), self._passover_date, range(1, 6))

        if self._year >= 1963:
            rule = THU_TO_PREV_WED + FRI_TO_PREV_WED
            if self._year >= 2004:
                rule += SUN_TO_NEXT_MON
            self._add_observed(
                _timedelta(self._israel_independence_date, -1),
                # Yom Hazikaron (Fallen Soldiers and Victims of Terrorism Remembrance Day).
                tr("יום הזיכרון לחללי מערכות ישראל ונפגעי פעולות האיבה"),
                rule,
            )

        if self._year >= 1998:
            # Yom Yerushalayim (Jerusalem Day).
            self._add_hebrew_holiday(tr("יום ירושלים"), self._lag_baomer_date, +10)

        # Tisha B'Av (Tisha B'Av, fast).
        self._add_observed(self._tisha_bav_date, tr("תשעה באב"), SAT_TO_NEXT_SUN)

    def _populate_school_holidays(self):
        # Chol HaMoed Sukkot (Feast of Tabernacles holiday).
        self._add_hebrew_holiday(tr("חול המועד סוכות"), self._sukkot_date, range(1, 6))

        for hanukkah_dt in self._hanukkah_date:
            # Hanukkah.
            self._add_hebrew_holiday(tr("חנוכה"), hanukkah_dt, range(8))

        # Ta`anit Ester (Fast of Esther).
        self._add_observed(_timedelta(self._purim_date, -1), tr("תענית אסתר"), SAT_TO_PREV_THU)

        # Purim.
        self._add_hebrew_holiday(tr("פורים"), self._purim_date)

        # Chol HaMoed Pesach (Passover holiday).
        self._add_hebrew_holiday(tr("חול המועד פסח"), self._passover_date, range(1, 6))

        # Lag Ba'omer (Lag BaOmer).
        self._add_hebrew_holiday(tr('ל"ג בעומר'), self._lag_baomer_date)


class IL(Israel):
    pass


class ISR(Israel):
    pass
