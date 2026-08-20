#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date
from gettext import gettext as tr

from holidays.calendars.gregorian import _timedelta, FRI, SAT, SUN, JAN, MAR, OCT, NOV
from holidays.constants import PUBLIC, HALF_DAY
from holidays.groups import HebrewCalendarHolidays, StaticHolidays
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


class TelAvivStockExchange(ObservedHolidayBase, HebrewCalendarHolidays, StaticHolidays):
    """Tel Aviv Stock Exchange (TASE) holidays.

    References:
        * [2013](https://web.archive.org/web/20251117170334/https://content.tase.co.il/media/pqrowxtp/file_0010_vacation_schedule_2013_eng.pdf)
        * [2014](https://web.archive.org/web/20251117170321/https://content.tase.co.il/media/1yrj4yn5/file_0010_vacation_schedule_2014_eng.pdf)
        * [2015](https://web.archive.org/web/20251117170319/https://content.tase.co.il/media/dp0kghj1/file_0010_vacation_schedule_2015_eng.pdf)
        * [2016](https://web.archive.org/web/20251117170511/https://content.tase.co.il/media/p2gm0s3f/file_0010_vacation_schedule_2016_eng.pdf)
        * [2017](https://web.archive.org/web/20251117170325/https://content.tase.co.il/media/ax5jgq31/file_0010_vacation_schedule_2017_eng.pdf)
        * [2018](https://web.archive.org/web/20251117170332/https://content.tase.co.il/media/fz0nyrzy/file_0010_vacation_schedule_2018_eng.pdf)
        * [2019](https://web.archive.org/web/20251117170336/https://content.tase.co.il/media/n2hl3q50/file_0010_vacation_schedule_2019_eng.pdf)
        * [2020](https://web.archive.org/web/20251117170318/https://content.tase.co.il/media/hk4pgzy4/file_0010_vacation_schedule_2020_eng.pdf)
        * [2021](https://web.archive.org/web/20251117170340/https://content.tase.co.il/media/hh2ilipi/file_0010_vacation_schedule_2021_eng.pdf)
        * [2022](https://web.archive.org/web/20251117170332/https://content.tase.co.il/media/vyolzrvu/file_0010_vacation_schedule_2022_eng.pdf)
        * [2023](https://web.archive.org/web/20260813161147/https://content.tase.co.il/media/iqcijli2/file_0010_vacation_schedule_2023_eng.pdf)
        * [2024](https://web.archive.org/web/20251117170328/https://content.tase.co.il/media/33xjyi00/file_0010_vacation_schedule_2024_eng.pdf)
        * [2025](https://web.archive.org/web/20260813161220/https://content.tase.co.il/media/ob4blknd/file_0010_vacation_schedule_2025_eng.pdf)
        * [2026](https://web.archive.org/web/20260418172343/https://www.tase.co.il/en/content/knowledge_center/trading_vacation_schedule/)
    """

    market = "XTAE"
    default_language = "he"
    observed_label = "%s"
    supported_categories = (PUBLIC, HALF_DAY)
    supported_languages = ("en_US", "he")
    start_year = 2013

    def __init__(self, *args, **kwargs):
        HebrewCalendarHolidays.__init__(self)
        StaticHolidays.__init__(self, TelAvivStockExchangeStaticHolidays)
        super().__init__(*args, **kwargs)

    def _get_weekend(self, dt) -> set[int]:
        # TASE shifted to a Saturday/Sunday weekend in 2026
        return {SAT, SUN} if dt >= date(2026, JAN, 5) else {FRI, SAT}

    def _add_observed(self, dt, name, rule):
        is_observed, _ = super()._add_observed(dt, name, rule=rule)
        if not is_observed:
            self._add_holiday(name, dt)

    def _populate_public_holidays(self):
        eve_dts = set()

        # Purim.
        self._add_purim(tr("פורים"))

        if 2022 <= self._year <= 2023:
            # Shushan Purim.
            self._add_purim(tr("שושן פורים"), +1)

        # Passover Eve.
        eve_dts.update(self._add_passover(tr("ערב פסח"), -1))

        # Passover
        self._add_passover(tr("פסח"))

        # Passover II Eve.
        eve_dts.update(self._add_passover(tr("ערב שביעי של פסח"), +5))

        # Passover II.
        self._add_passover(tr("שביעי של פסח"), +6)

        self._add_observed(
            _timedelta(self._hebrew_calendar.israel_independence_date(self._year), -1),
            # Memorial Day.
            tr("יום הזיכרון"),
            THU_TO_PREV_WED + FRI_TO_PREV_WED + SUN_TO_NEXT_MON,
        )

        self._add_observed(
            self._hebrew_calendar.israel_independence_date(self._year),
            # Independence Day.
            tr("יום העצמאות"),
            FRI_TO_PREV_THU + SAT_TO_PREV_THU + MON_TO_NEXT_TUE,
        )

        shavuot_dt = self._hebrew_calendar.shavuot_date(self._year)
        # Shavuot Eve.
        eve_dts.add(self._add_holiday(tr("ערב שבועות"), _timedelta(shavuot_dt, -1)))

        # Shavuot.
        self._add_shavuot(tr("שבועות"))

        self._add_observed(
            self._hebrew_calendar.tisha_bav_date(self._year),
            # Fast Day (Tisha B'Av).
            tr("תשעה באב"),
            SAT_TO_NEXT_SUN,
        )

        # Jewish New Year Eve.
        eve_dts.update(self._add_rosh_hashanah(tr("ערב ראש השנה"), -1))

        # Jewish New Year.
        self._add_rosh_hashanah(tr("ראש השנה"), range(2))

        # Yom Kippur Eve.
        self._add_yom_kippur(tr("ערב יום כיפור"), -1)

        # Yom Kippur.
        self._add_yom_kippur(tr("יום כיפור"))

        # Sukkoth Eve.
        eve_dts.update(self._add_sukkot(tr("ערב סוכות"), -1))

        # Sukkoth
        self._add_sukkot(tr("סוכות"))

        # Simchat Tora Eve.
        eve_dts.update(self._add_sukkot(tr("ערב שמחת תורה"), +6))

        # Simchat Torah / Shemini Atzeret.
        self._add_sukkot(tr("שמחת תורה/שמיני עצרת"), +7)

        # %s (Friday before holiday).
        bridge_label = tr("%s (שישי לפני חג)")
        for dt, name in tuple(self.items()):
            if dt.year != self._year:
                continue

            if dt.weekday() == SAT:
                self.pop(dt)

            elif dt.weekday() == SUN and self._year >= 2026:
                if dt in eve_dts:
                    self.pop(dt)
                else:
                    fri_dt = _timedelta(dt, -2)
                    if fri_dt not in self:
                        self._add_holiday(self._format_holiday_name(bridge_label, name), fri_dt)

    def _populate_half_day_holidays(self):
        # %s (Half trading day).
        half_day_label = tr("%s (חצי יום מסחר)")

        passover_dt = self._hebrew_calendar.passover_date(self._year)
        for i in range(1, 5):
            dt = _timedelta(passover_dt, i)
            if not self._is_weekend(dt):
                self._add_holiday(
                    # Chol HaMoed Passover.
                    self._format_holiday_name(half_day_label, tr("חול המועד פסח")),
                    dt,
                )

        sukkot_dt = self._hebrew_calendar.sukkot_date(self._year)
        for i in range(1, 6):
            dt = _timedelta(sukkot_dt, i)
            if not self._is_weekend(dt):
                self._add_holiday(
                    # Chol HaMoed Sukkoth.
                    self._format_holiday_name(half_day_label, tr("חול המועד סוכות")),
                    dt,
                )


class XTAE(TelAvivStockExchange):
    pass


class TASE(TelAvivStockExchange):
    pass


class TelAvivStockExchangeStaticHolidays:
    special_public_holidays = {
        # Knesset Election Day.
        2013: (JAN, 22, tr("יום בחירות")),
        # Knesset Election Day.
        2015: (MAR, 17, tr("יום בחירות")),
        # Municipal Election Day.
        2018: (OCT, 30, tr("יום בחירות לרשויות המקומיות")),
        # Knesset Election Day.
        2021: (MAR, 23, tr("יום בחירות")),
        # Knesset Election Day.
        2022: (NOV, 1, tr("יום בחירות")),
        # Municipal Election Day.
        2023: (OCT, 31, tr("יום בחירות לרשויות המקומיות")),
        # Knesset Election Day.
        2026: (OCT, 27, tr("יום בחירות")),
    }
