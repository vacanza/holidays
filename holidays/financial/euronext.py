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

from holidays.calendars.gregorian import DEC, JAN, MAY, _timedelta
from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import (
    SAT_SUN_TO_NEXT_WORKDAY,
    SAT_SUN_TO_NONE,
    SAT_SUN_TO_PREV_FRI,
    ObservedHolidayBase,
)

# Holiday names shared by several Euronext markets.
_CHRISTMAS_EVE = "Christmas Eve"
_NEW_YEARS_EVE = "New Year's Eve"


class Euronext(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Euronext holidays.

    Euronext cash and derivatives markets (Amsterdam, Brussels, Dublin,
    Lisbon, Milan, Oslo and Paris) share a common holiday calendar with a
    small number of market-specific closures. Christmas Eve and New Year's
    Eve are half trading days in all markets except Milan and Oslo, where
    they are full-day closures. Milan market holidays are included from
    2023, the first year Milan appears in the Euronext holiday calendars.

    References:
        * <https://www.euronext.com/en/trading-calendars-hours>
        * [2026 Holiday Calendar for Euronext's Cash and Derivatives markets]
            (https://connect2.euronext.com/sites/default/files/2025-11/IF251107CADE%202026%20Holiday%20Calendar%20for%20Euronexts%20Cash%20and%20Derivatives%20markets_1.pdf?VersionId=3ehe2.c9cMxv1K36.i6o4tz.5CAJmuw2)
    """

    market = "XPAR"
    subdivisions = ("XAMS", "XBRU", "XDUB", "XLIS", "XMIL", "XOSL", "XPAR")
    supported_categories = (HALF_DAY, PUBLIC)
    start_year = 2021

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        # Market subclasses (e.g., XOSL) default to their own subdivision,
        # so their market-specific holidays are included when the subclass
        # is used directly (e.g., via financial_holidays("XOSL"), which
        # passes subdiv=None).
        if type(self) is not Euronext and not any(
            kwargs.get(key) for key in ("subdiv", "prov", "state")
        ):
            if len(args) < 4:
                kwargs["subdiv"] = self.market
            elif args[3] is None:
                # A null positional subdivision gets the market default too.
                args = (*args[:3], self.market, *args[4:])
        # The observed arguments are passed to ObservedHolidayBase in its
        # own leading positions, keeping the HolidayBase positional
        # arguments (years, expand, observed, subdiv, ...) intact.
        super().__init__(
            kwargs.pop("observed_rule", None),
            kwargs.pop("observed_since", None),
            *args,
            **kwargs,
        )

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # Labour Day.
        self._add_labor_day("Labour Day")

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

        # St Stephen's Day.
        self._add_christmas_day_two("St Stephen's Day")

    def _populate_half_day_holidays(self):
        # Christmas Eve and New Year's Eve are half trading days in all
        # markets except Milan and Oslo, where they are full-day closures
        # (see the corresponding subdivision public holidays). There is no
        # half trading day when they fall on a weekend (for Dublin see the
        # subdivision half day holidays below).
        if self.subdiv in ("XMIL", "XOSL"):
            return None

        # Christmas Eve.
        self._move_holiday_forced(
            self._add_christmas_eve(_CHRISTMAS_EVE),
            rule=SAT_SUN_TO_NONE,
        )

        # New Year's Eve.
        self._move_holiday_forced(
            self._add_new_years_eve(_NEW_YEARS_EVE),
            rule=SAT_SUN_TO_NONE,
        )

    def _populate_subdiv_xdub_public_holidays(self):
        # Irish May Bank Holiday.
        self._add_holiday_1st_mon_of_may("Irish May Bank Holiday")

        # When New Year's Day, Christmas Day or St Stephen's Day fall on a
        # weekend, Euronext Dublin is closed on the following workday
        # instead (e.g., if Christmas Day falls on a Sunday, the market is
        # closed on Tuesday, since Monday is St Stephen's Day itself).
        for dt in (
            date(self._year, JAN, 1),
            date(self._year, DEC, 25),
            date(self._year, DEC, 26),
        ):
            self._add_observed(dt, rule=SAT_SUN_TO_NEXT_WORKDAY)

    def _populate_subdiv_xdub_half_day_holidays(self):
        # When Christmas Eve or New Year's Eve fall on a weekend, the half
        # trading day is observed on the preceding Friday instead.
        self._move_holiday_forced(
            self._add_christmas_eve(_CHRISTMAS_EVE),
            rule=SAT_SUN_TO_PREV_FRI,
        )
        self._move_holiday_forced(
            self._add_new_years_eve(_NEW_YEARS_EVE),
            rule=SAT_SUN_TO_PREV_FRI,
        )

    def _add_eves_as_full_day_holidays(self):
        """Add Christmas Eve and New Year's Eve as full-day holidays."""
        # Christmas Eve.
        self._add_christmas_eve(_CHRISTMAS_EVE)

        # New Year's Eve.
        self._add_new_years_eve(_NEW_YEARS_EVE)

    def _populate_subdiv_xmil_public_holidays(self):
        # Milan is included in the Euronext holiday calendars from 2023.
        if self._year < 2023:
            return None

        # Assumption Day (Ferragosto).
        self._add_assumption_of_mary_day("Assumption Day")

        # Christmas Eve and New Year's Eve are full-day closures.
        self._add_eves_as_full_day_holidays()

    def _populate_subdiv_xosl_public_holidays(self):
        # Maundy Thursday.
        self._add_holy_thursday("Maundy Thursday")

        # Ascension Day.
        self._add_ascension_thursday("Ascension Day")

        # Constitution Day.
        self._add_holiday("Constitution Day", MAY, 17)

        # Whit Monday.
        self._add_pentecost_monday("Whit Monday")

        # Christmas Eve and New Year's Eve are full-day closures.
        self._add_eves_as_full_day_holidays()

    def _populate_subdiv_xosl_half_day_holidays(self):
        # Wednesday before Easter.
        self._add_holiday("Wednesday before Easter", _timedelta(self._easter_sunday, -4))


class XPAR(Euronext):
    market = "XPAR"


class XAMS(Euronext):
    market = "XAMS"


class XBRU(Euronext):
    market = "XBRU"


class XDUB(Euronext):
    market = "XDUB"


class XLIS(Euronext):
    market = "XLIS"


class XMIL(Euronext):
    market = "XMIL"


class XOSL(Euronext):
    market = "XOSL"
