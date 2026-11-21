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

from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    JUN,
    SEP,
    OCT,
    NOV,
    FRI,
    SAT,
    SUN,
    _timedelta,
)
from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import HebrewCalendarHolidays, StaticHolidays
from holidays.helpers import tr
from holidays.observed_holiday_base import (
    FRI_TO_PREV_THU,
    FRI_TO_PREV_WED,
    MON_TO_NEXT_TUE,
    SAT_TO_NEXT_SUN,
    SAT_TO_PREV_THU,
    SAT_SUN_TO_PREV_FRI,
    SUN_TO_NEXT_MON,
    THU_TO_PREV_WED,
    ObservedHolidayBase,
)


class TelAvivStockExchange(ObservedHolidayBase, HebrewCalendarHolidays, StaticHolidays):
    """Tel Aviv Stock Exchange (TASE) holidays.

    References:
        * [TASE Trading and Vacation Schedules](https://web.archive.org/web/20261114073950/https://www.tase.co.il/en/content/knowledge_center/trading_vacation_schedule/)
        * [Vacation Schedule 2013](https://web.archive.org/web/20260630182118/https://content.tase.co.il/media/musikfp3/file_0010_vacation_schedule_2013_heb.pdf)
        * [Vacation Schedule 2020](https://web.archive.org/web/20251117170318/https://content.tase.co.il/media/hk4pgzy4/file_0010_vacation_schedule_2020_eng.pdf)
        * [Vacation Schedule 2022](https://web.archive.org/web/20251117170332/https://content.tase.co.il/media/vyolzrvu/file_0010_vacation_schedule_2022_eng.pdf)
        * [Vacation Schedule 2023](https://web.archive.org/web/20261114073732/https://content.tase.co.il/media/iqcijli2/file_0010_vacation_schedule_2023_eng.pdf)
        * [Trading on Shushan Purim 2023](https://web.archive.org/web/20260118174913/https://www.tase.co.il/en/content/news-lobby/20230308_pr/)
        * [Vacation Schedule 2024](https://web.archive.org/web/20251117170328/https://content.tase.co.il/media/33xjyi00/file_0010_vacation_schedule_2024_eng.pdf)
    """

    market = "XTAE"
    default_language = "he"
    # %s (observed).
    observed_label = tr("%s (נצפה)")
    supported_languages = ("en_US", "he")
    # Earliest available official vacation schedule.
    start_year = 2013
    supported_categories = (HALF_DAY, PUBLIC)

    def __init__(self, *args, **kwargs):
        HebrewCalendarHolidays.__init__(self)
        StaticHolidays.__init__(self, TelAvivStockExchangeStaticHolidays)
        super().__init__(*args, **kwargs)

    def _add_observed(self, dt, name, rule):
        is_observed, _ = super()._add_observed(dt, name, rule=rule)
        if not is_observed:
            self._add_holiday(name, dt)

    def _get_weekend(self, dt: date) -> set[int]:
        # January 4, 2026 was the first non-trading Sunday.
        return {SAT, SUN} if dt >= date(2026, JAN, 4) else {FRI, SAT}

    def _populate_common_holidays(self):
        super()._populate_common_holidays()
        if PUBLIC not in self.categories:
            return

        # Fridays during Chol HaMoed follow the regular Friday schedule.
        chol_hamoed = {
            _timedelta(dt, delta)  # type: ignore[arg-type]
            for dt, days in (
                (self._hebrew_calendar.passover_date(self._year), 5),
                (self._hebrew_calendar.sukkot_date(self._year), 6),
            )
            for delta in range(1, days + 1)
        }
        for dt in tuple(self):
            if dt.year != self._year:
                continue
            if (
                self._year >= 2026
                and self._is_sunday(dt)
                and (friday := self._get_observed_date(dt, SAT_SUN_TO_PREV_FRI)) not in self
                and friday not in chol_hamoed
            ):
                super()._add_observed(
                    dt,
                    # Market Holiday.
                    tr("יום חופשה בבורסה"),
                    rule=SAT_SUN_TO_PREV_FRI,
                    force_observed=True,
                    show_observed_label=False,
                )
            if self._is_weekend(dt):
                self.pop(dt)

    def _populate_half_day_holidays(self):
        def shortened_session_offsets(dt: date, eve_offset: int) -> tuple[int, ...]:
            # Exclude the full-day eve and Fridays, which use regular Friday hours.
            return tuple(
                offset
                for offset in range(1, eve_offset)
                if not self._is_weekend(day := _timedelta(dt, offset)) and not self._is_friday(day)
            )

        self._add_passover(
            # Chol HaMoed Pesach (Passover holiday).
            tr("חול המועד פסח"),
            shortened_session_offsets(
                self._hebrew_calendar.passover_date(self._year),  # type: ignore[arg-type]
                5,
            ),
        )
        self._add_sukkot(
            # Chol HaMoed Sukkot (Feast of Tabernacles holiday).
            tr("חול המועד סוכות"),
            shortened_session_offsets(
                self._hebrew_calendar.sukkot_date(self._year),  # type: ignore[arg-type]
                6,
            ),
        )

    def _populate_public_holidays(self):
        # Purim.
        self._add_purim(tr("פורים"))

        # Pesach Eve.
        self._add_passover(tr("ערב פסח"), -1)
        # Pesach.
        self._add_passover(tr("פסח"))
        # Eve of the Seventh Day of Pesach.
        self._add_passover(tr("ערב שביעי של פסח"), +5)
        # Seventh day of Pesach.
        self._add_passover(tr("שביעי של פסח"), +6)

        self._add_observed(
            _timedelta(self._hebrew_calendar.israel_independence_date(self._year), -1),
            # Remembrance Day.
            tr("יום הזיכרון לחללי מערכות ישראל ונפגעי פעולות האיבה"),
            THU_TO_PREV_WED + FRI_TO_PREV_WED + SUN_TO_NEXT_MON,
        )

        self._add_observed(
            self._hebrew_calendar.israel_independence_date(self._year),
            # Independence Day.
            tr("יום העצמאות"),
            FRI_TO_PREV_THU + SAT_TO_PREV_THU + MON_TO_NEXT_TUE,
        )

        # Shavuot Eve.
        self._add_shavuot(tr("ערב שבועות"), -1)
        # Shavuot.
        self._add_shavuot(tr("שבועות"))

        self._add_observed(
            self._hebrew_calendar.tisha_bav_date(self._year),
            # Tisha B'Av.
            tr("תשעה באב"),
            SAT_TO_NEXT_SUN,
        )

        # Rosh Hashanah Eve.
        self._add_rosh_hashanah(tr("ערב ראש השנה"), -1)
        # Rosh Hashanah.
        self._add_rosh_hashanah(tr("ראש השנה"), range(2))

        # Yom Kippur Eve.
        self._add_yom_kippur(tr("ערב יום כיפור"), -1)
        # Yom Kippur.
        self._add_yom_kippur(tr("יום כיפור"))

        # Sukkot Eve.
        self._add_sukkot(tr("ערב סוכות"), -1)
        # Sukkot.
        self._add_sukkot(tr("סוכות"))
        # Simchat Torah Eve.
        self._add_sukkot(tr("ערב שמחת תורה"), +6)
        # Simchat Torah / Shemini Atzeret.
        self._add_sukkot(tr("שמחת תורה/שמיני עצרת"), +7)


class XTAE(TelAvivStockExchange):
    pass


class TelAvivStockExchangeStaticHolidays:
    """Tel Aviv Stock Exchange special holidays.

    References:
        * [Vacation Schedule 2015](https://web.archive.org/web/20260630182118/https://content.tase.co.il/media/punlviyp/file_0010_vacation_schedule_2015_heb.pdf)
        * [Vacation Schedule 2018](https://web.archive.org/web/20260630182118/https://content.tase.co.il/media/5cmh154f/file_0010_vacation_schedule_2018_heb.pdf)
        * [Vacation Schedule 2019](https://web.archive.org/web/20260630182118/https://content.tase.co.il/media/qsyberat/file_0010_vacation_schedule_2019_heb.pdf)
        * [September 2019 election closure](https://web.archive.org/web/20191016132948/https://en.globes.co.il/en/article-mon-tase-flat-as-delek-decline-continues-1001300994)
        * [March 2020 election closure](https://web.archive.org/web/20250126033838/https://www.timesofisrael.com/tel-aviv-stock-exchange-continues-slide-as-virus-outbreak-batters-global-markets/)
        * [June 2020 labor dispute closure](https://web.archive.org/web/20220223003921/https://en.globes.co.il/en/article-no-trading-on-tase-as-workers-apply-sanctions-1001331393)
        * [Vacation Schedule 2021](https://web.archive.org/web/20260630182118/https://content.tase.co.il/media/phbhzlw0/file_0010_vacation_schedule_2021_heb.pdf)
        * [Municipal elections 2024](https://web.archive.org/web/20250720201133/https://en.globes.co.il/en/article-Mon-TASE-edges-higher-despite-no-rate-cut-1001472244)
    """

    # Knesset Election Day.
    knesset_election_day = tr("יום הבחירות לכנסת")
    # Municipal Election Day.
    municipal_election_day = tr("יום הבחירות לרשויות המקומיות")

    special_public_holidays = {
        2013: (JAN, 22, knesset_election_day),
        2015: (MAR, 17, knesset_election_day),
        2018: (OCT, 30, municipal_election_day),
        2019: (
            (APR, 9, knesset_election_day),
            (SEP, 17, knesset_election_day),
        ),
        2020: (
            (MAR, 2, knesset_election_day),
            # Market Holiday.
            (JUN, 7, tr("יום חופשה בבורסה")),
        ),
        2021: (MAR, 23, knesset_election_day),
        2022: (NOV, 1, knesset_election_day),
        2024: (FEB, 27, municipal_election_day),
        2026: (OCT, 27, knesset_election_day),
    }
