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

from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.helpers import tr
from holidays.mixins.child_entity import ChildEntity
from holidays.observed_holiday_base import (
    SAT_SUN_TO_NEXT_WORKDAY,
    SAT_SUN_TO_NONE,
    SAT_SUN_TO_PREV_FRI,
    ObservedHolidayBase,
)


class Euronext(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Euronext holidays.

    Euronext cash and derivatives markets (Amsterdam, Brussels, Dublin,
    Lisbon, Milan, Oslo and Paris) share a common holiday calendar with a
    small number of market-specific closures. Christmas Eve and New Year's
    Eve are half trading days in all markets except Milan and Oslo, where
    they are full-day closures. On half trading days the Amsterdam,
    Brussels, Lisbon and Paris cash markets close by 14:05 CET, while
    Euronext Dublin equities close at 12:30 Dublin time. Euronext Dublin
    has been closed on May Day since 2021. Milan market holidays are
    included from 2023, the first year Milan appears in the Euronext
    holiday calendars.

    References:
        * <https://www.euronext.com/en/trading-calendars-hours>
        * [2026 Holiday Calendar for Euronext's Cash and Derivatives markets]
            (https://connect2.euronext.com/sites/default/files/2025-11/IF251107CADE%202026%20Holiday%20Calendar%20for%20Euronexts%20Cash%20and%20Derivatives%20markets_1.pdf?VersionId=3ehe2.c9cMxv1K36.i6o4tz.5CAJmuw2)
        * [Trading hours and holidays (archived 18 December 2019)]
            (https://web.archive.org/web/20191218011504/https://www.euronext.com/en/trade/trading-hours-holidays)
        * [Trading hours and holidays (archived 5 December 2020)]
            (https://web.archive.org/web/20201205035823/https://www.euronext.com/en/trade/trading-hours-holidays)
        * [Trading calendars and hours (archived 25 March 2019)]
            (https://web.archive.org/web/20190325100632/https://www.euronext.com/en/trading-calendars-hours)
    """

    # Euronext Paris is the group's largest market by market
    # capitalization, so XPAR is the default market.
    market = "XPAR"
    default_language = "en_GB"
    supported_languages = ("en_GB", "en_US", "fr", "it", "nl", "no", "pt_PT")
    supported_categories = (HALF_DAY, PUBLIC)
    subdivisions: tuple[str, ...] = (
        "XAMS",  # Amsterdam.
        "XBRU",  # Brussels.
        "XDUB",  # Dublin.
        "XLIS",  # Lisbon.
        "XMIL",  # Milan.
        "XOSL",  # Oslo.
        "XPAR",  # Paris.
    )
    start_year = 2019

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        self._move_holiday_forced(
            # New Year's Day.
            self._add_new_years_day(tr("New Year's Day")),
            rule=SAT_SUN_TO_NONE,
        )

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Labour Day.
        self._move_holiday_forced(self._add_labor_day(tr("Labour Day")), rule=SAT_SUN_TO_NONE)

        self._move_holiday_forced(
            # Christmas Day.
            self._add_christmas_day(tr("Christmas Day")),
            rule=SAT_SUN_TO_NONE,
        )

        self._move_holiday_forced(
            # St Stephen's Day.
            self._add_christmas_day_two(tr("St Stephen's Day")),
            rule=SAT_SUN_TO_NONE,
        )

    def _populate_half_day_holidays(self):
        # Christmas Eve and New Year's Eve are half trading days in all
        # markets except Milan and Oslo, where they are full-day closures
        # (see the corresponding subdivision public holidays). There is no
        # half trading day when they fall on a weekend (for Dublin see the
        # subdivision half day holidays below).
        if self.subdiv in ("XMIL", "XOSL"):
            return None

        # %s (markets close at 2:05pm CET).
        close_2_05pm_label = tr("%s (markets close at 2:05pm CET)")
        # %s (markets close at 12:30pm).
        close_12_30pm_label = tr("%s (markets close at 12:30pm)")
        # On Euronext Dublin, equities close at 12:30 Dublin time.
        close_label = close_12_30pm_label if self.subdiv == "XDUB" else close_2_05pm_label

        # Christmas Eve.
        self._move_holiday_forced(
            self._add_christmas_eve(self._format_holiday_name(close_label, tr("Christmas Eve"))),
            rule=SAT_SUN_TO_NONE,
        )

        # New Year's Eve.
        self._move_holiday_forced(
            self._add_new_years_eve(self._format_holiday_name(close_label, tr("New Year's Eve"))),
            rule=SAT_SUN_TO_NONE,
        )

    def _populate_subdiv_xdub_public_holidays(self):
        # Euronext Dublin has been closed on May Day since 2021.
        if self._year >= 2021:
            # Irish May Bank Holiday.
            self._add_holiday_1st_mon_of_may(tr("Irish May Bank Holiday"))

        # When New Year's Day, Christmas Day or St Stephen's Day fall on a
        # weekend, Euronext Dublin is closed on the following workday
        # instead (e.g., if Christmas Day falls on a Sunday, the market is
        # closed on Tuesday, since Monday is St Stephen's Day itself).
        # New Year's Day.
        self._move_holiday(
            self._add_new_years_day(tr("New Year's Day")), rule=SAT_SUN_TO_NEXT_WORKDAY
        )

        # Christmas Day.
        self._move_holiday(
            self._add_christmas_day(tr("Christmas Day")), rule=SAT_SUN_TO_NEXT_WORKDAY
        )

        # St Stephen's Day.
        self._move_holiday(
            self._add_christmas_day_two(tr("St Stephen's Day")),
            rule=SAT_SUN_TO_NEXT_WORKDAY,
        )

    def _populate_subdiv_xdub_half_day_holidays(self):
        # When Christmas Eve or New Year's Eve fall on a weekend, the half
        # trading day is observed on the preceding Friday instead.
        # %s (markets close at 12:30pm).
        close_12_30pm_label = tr("%s (markets close at 12:30pm)")

        self._move_holiday_forced(
            self._add_christmas_eve(
                self._format_holiday_name(close_12_30pm_label, tr("Christmas Eve"))
            ),
            rule=SAT_SUN_TO_PREV_FRI,
        )
        self._move_holiday_forced(
            self._add_new_years_eve(
                self._format_holiday_name(close_12_30pm_label, tr("New Year's Eve"))
            ),
            rule=SAT_SUN_TO_PREV_FRI,
        )

    def _add_eves_as_full_day_holidays(self):
        """Add Christmas Eve and New Year's Eve as full-day holidays."""
        self._move_holiday_forced(
            # Christmas Eve.
            self._add_christmas_eve(tr("Christmas Eve")),
            rule=SAT_SUN_TO_NONE,
        )

        self._move_holiday_forced(
            # New Year's Eve.
            self._add_new_years_eve(tr("New Year's Eve")),
            rule=SAT_SUN_TO_NONE,
        )

    def _populate_subdiv_xmil_public_holidays(self):
        # Milan is included in the Euronext holiday calendars from 2023.
        if self._year < 2023:
            return None

        # Assumption Day (Ferragosto).
        self._move_holiday_forced(
            # Assumption Day.
            self._add_assumption_of_mary_day(tr("Assumption Day")),
            rule=SAT_SUN_TO_NONE,
        )

        # Christmas Eve and New Year's Eve are full-day closures.
        self._add_eves_as_full_day_holidays()

    def _populate_subdiv_xosl_public_holidays(self):
        # Maundy Thursday.
        self._add_holy_thursday(tr("Maundy Thursday"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Ascension Day"))

        self._move_holiday_forced(
            # Constitution Day.
            self._add_holiday_may_17(tr("Constitution Day")),
            rule=SAT_SUN_TO_NONE,
        )

        # Whit Monday.
        self._add_pentecost_monday(tr("Whit Monday"))

        # Christmas Eve and New Year's Eve are full-day closures.
        self._add_eves_as_full_day_holidays()

    def _populate_subdiv_xosl_half_day_holidays(self):
        # %s (markets close at 1:00pm CET).
        close_1pm_label = tr("%s (markets close at 1:00pm CET)")

        self._add_holiday_4_days_prior_easter(
            # Wednesday before Easter.
            self._format_holiday_name(close_1pm_label, tr("Wednesday before Easter"))
        )


class XPAR(ChildEntity, Euronext):
    country = None  # type: ignore[assignment]
    market = "XPAR"
    parent_entity = Euronext
    parent_entity_subdivision_code = "XPAR"


class XAMS(ChildEntity, Euronext):
    country = None  # type: ignore[assignment]
    market = "XAMS"
    parent_entity = Euronext
    parent_entity_subdivision_code = "XAMS"


class XBRU(ChildEntity, Euronext):
    country = None  # type: ignore[assignment]
    market = "XBRU"
    parent_entity = Euronext
    parent_entity_subdivision_code = "XBRU"


class XDUB(ChildEntity, Euronext):
    country = None  # type: ignore[assignment]
    market = "XDUB"
    parent_entity = Euronext
    parent_entity_subdivision_code = "XDUB"


class XLIS(ChildEntity, Euronext):
    country = None  # type: ignore[assignment]
    market = "XLIS"
    parent_entity = Euronext
    parent_entity_subdivision_code = "XLIS"


class XMIL(ChildEntity, Euronext):
    country = None  # type: ignore[assignment]
    market = "XMIL"
    parent_entity = Euronext
    parent_entity_subdivision_code = "XMIL"


class XOSL(ChildEntity, Euronext):
    country = None  # type: ignore[assignment]
    market = "XOSL"
    parent_entity = Euronext
    parent_entity_subdivision_code = "XOSL"
