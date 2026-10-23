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
from holidays.holiday_base import HolidayBase


class Euronext(HolidayBase, ChristianHolidays, InternationalHolidays):
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
        if type(self) is not Euronext and not kwargs.get("subdiv"):
            kwargs["subdiv"] = self.market
        super().__init__(*args, **kwargs)

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
        # (see the corresponding subdivision public holidays). No half
        # trading day is observed when they fall on a weekend (for Dublin
        # see the subdivision half day holidays below).
        if self.subdiv in ("XMIL", "XOSL"):
            return None

        # Christmas Eve.
        if not self._is_weekend(date(self._year, DEC, 24)):
            self._add_christmas_eve("Christmas Eve")

        # New Year's Eve.
        if not self._is_weekend(date(self._year, DEC, 31)):
            self._add_new_years_eve("New Year's Eve")

    def _populate_subdiv_xdub_public_holidays(self):
        # Irish May Bank Holiday.
        self._add_holiday_1st_mon_of_may("Irish May Bank Holiday")

        # When New Year's Day, Christmas Day or St Stephen's Day fall on a
        # weekend, Euronext Dublin is closed on the following weekday
        # instead (e.g., if Christmas Day falls on a Sunday, the market is
        # closed on Tuesday, since Monday is St Stephen's Day itself).
        fixed_dates = (
            date(self._year, JAN, 1),
            date(self._year, DEC, 25),
            date(self._year, DEC, 26),
        )
        observed_dates = set()
        for dt, name in (
            (date(self._year, JAN, 1), "New Year's Day"),
            (date(self._year, DEC, 25), "Christmas Day"),
            (date(self._year, DEC, 26), "St Stephen's Day"),
        ):
            if dt.weekday() == 5:  # Saturday.
                substitute_dt = _timedelta(dt, +2)
            elif dt.weekday() == 6:  # Sunday.
                substitute_dt = _timedelta(dt, +1)
            else:
                continue

            while substitute_dt in fixed_dates or substitute_dt in observed_dates:
                substitute_dt = _timedelta(substitute_dt, +1)

            observed_dates.add(substitute_dt)
            self._add_holiday(name, substitute_dt)

    def _populate_subdiv_xdub_half_day_holidays(self):
        # When Christmas Eve or New Year's Eve fall on a weekend, the half
        # trading day is observed on the preceding Friday instead.
        for day, name in ((24, "Christmas Eve"), (31, "New Year's Eve")):
            dt = date(self._year, DEC, day)
            if self._is_weekend(dt):
                self._add_holiday(name, _timedelta(dt, -1 if dt.weekday() == 5 else -2))

    def _populate_subdiv_xmil_public_holidays(self):
        # Milan is included in the Euronext holiday calendars from 2023.
        if self._year < 2023:
            return None

        # Assumption Day (Ferragosto).
        self._add_assumption_of_mary_day("Assumption Day")

        # Christmas Eve.
        self._add_christmas_eve("Christmas Eve")

        # New Year's Eve.
        self._add_new_years_eve("New Year's Eve")

    def _populate_subdiv_xosl_public_holidays(self):
        # Maundy Thursday.
        self._add_holy_thursday("Maundy Thursday")

        # Ascension Day.
        self._add_ascension_thursday("Ascension Day")

        # Constitution Day.
        self._add_holiday("Constitution Day", MAY, 17)

        # Whit Monday.
        self._add_pentecost_monday("Whit Monday")

        # Christmas Eve.
        self._add_christmas_eve("Christmas Eve")

        # New Year's Eve.
        self._add_new_years_eve("New Year's Eve")

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
