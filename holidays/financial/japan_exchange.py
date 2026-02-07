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

from datetime import date, timedelta

from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
    MON,
)
from holidays.groups import InternationalHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class JapanExchange(HolidayBase, InternationalHolidays, StaticHolidays):
    """Japan Exchange Group (JPX) holidays.

    References:
        * https://www.jpx.co.jp/english/corporate/about-jpx/calendar/index.html
        * https://en.wikipedia.org/wiki/Public_holidays_in_Japan
        * https://www.japaneselawtranslation.go.jp/en/laws/view/4846/en
    """

    market = "JPX"
    start_year = 2013

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, JapanExchangeStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Fixed date holidays
        self._add_new_years_day("New Year's Day")
        self._add_feb_11("National Foundation Day")
        self._add_apr_29("Showa Day")
        self._add_may_3("Constitution Memorial Day")
        self._add_may_4("Greenery Day")
        self._add_may_5("Children's Day")
        self._add_aug_11("Mountain Day")
        self._add_nov_3("Culture Day")
        self._add_nov_23("Labor Thanksgiving Day")
        self._add_dec_23_or_feb_23("Emperor's Birthday")

        # Movable holidays (Happy Monday System)
        self._add_coming_of_age_day()
        self._add_marine_day()
        self._add_respect_for_the_aged_day()
        self._add_sports_day()

        # Equinox holidays
        self._add_vernal_equinox_day()
        self._add_autumnal_equinox_day()

        # Year-end market holidays (non-national holidays)
        self._add_market_holidays()

        # Apply substitute holiday rules
        self._apply_substitute_holidays()

        # Apply bridge holiday rules
        self._apply_bridge_holidays()

    def _add_feb_11(self, name):
        """February 11 - National Foundation Day"""
        if self._year >= 1948:
            self._add_holiday(name, date(self._year, FEB, 11))

    def _add_apr_29(self, name):
        """April 29 - Showa Day"""
        if self._year >= 2007:
            self._add_holiday(name, date(self._year, APR, 29))
        elif self._year >= 1989:
            self._add_holiday("Greenery Day", date(self._year, APR, 29))
        elif self._year >= 1948:
            self._add_holiday("Emperor's Birthday", date(self._year, APR, 29))

    def _add_may_3(self, name):
        """May 3 - Constitution Memorial Day"""
        if self._year >= 1948:
            self._add_holiday(name, date(self._year, MAY, 3))

    def _add_may_4(self, name):
        """May 4 - Greenery Day"""
        if self._year >= 2007:
            self._add_holiday(name, date(self._year, MAY, 4))
        elif self._year >= 1985:
            self._add_holiday("National Holiday", date(self._year, MAY, 4))

    def _add_may_5(self, name):
        """May 5 - Children's Day"""
        if self._year >= 1948:
            self._add_holiday(name, date(self._year, MAY, 5))

    def _add_aug_11(self, name):
        """August 11 - Mountain Day"""
        if self._year >= 2016:
            self._add_holiday(name, date(self._year, AUG, 11))

    def _add_nov_3(self, name):
        """November 3 - Culture Day"""
        if self._year >= 1948:
            self._add_holiday(name, date(self._year, NOV, 3))

    def _add_nov_23(self, name):
        """November 23 - Labor Thanksgiving Day"""
        if self._year >= 1948:
            self._add_holiday(name, date(self._year, NOV, 23))

    def _add_dec_23_or_feb_23(self, name):
        """Emperor's Birthday - Dec 23 (1989-2018) or Feb 23 (2020+)"""
        if 1989 <= self._year <= 2018:
            self._add_holiday(name, date(self._year, DEC, 23))
        elif self._year >= 2020:
            self._add_holiday(name, date(self._year, FEB, 23))

    def _add_coming_of_age_day(self):
        """Second Monday of January - Coming of Age Day"""
        if self._year >= 2000:
            self._add_holiday("Coming of Age Day", self._get_nth_weekday_of_month(2, MON, JAN))
        elif self._year >= 1948:
            self._add_holiday("Coming of Age Day", date(self._year, JAN, 15))

    def _add_marine_day(self):
        """Third Monday of July - Marine Day"""
        if self._year >= 2003:
            self._add_holiday("Marine Day", self._get_nth_weekday_of_month(3, MON, JUL))
        elif self._year >= 1996:
            self._add_holiday("Marine Day", date(self._year, JUL, 20))

    def _add_respect_for_the_aged_day(self):
        """Third Monday of September - Respect for the Aged Day"""
        if self._year >= 2003:
            self._add_holiday(
                "Respect for the Aged Day", self._get_nth_weekday_of_month(3, MON, SEP)
            )
        elif self._year >= 1966:
            self._add_holiday("Respect for the Aged Day", date(self._year, SEP, 15))

    def _add_sports_day(self):
        """Second Monday of October - Sports Day"""
        if self._year >= 2000:
            self._add_holiday("Sports Day", self._get_nth_weekday_of_month(2, MON, OCT))
        elif self._year >= 1966:
            self._add_holiday("Sports Day", date(self._year, OCT, 10))

    def _add_vernal_equinox_day(self):
        """Vernal Equinox Day (March 20 or 21)"""
        equinox_date = self._calculate_equinox(self._year, vernal=True)
        if equinox_date:
            self._add_holiday("Vernal Equinox Day", equinox_date)

    def _add_autumnal_equinox_day(self):
        """Autumnal Equinox Day (September 22 or 23)"""
        equinox_date = self._calculate_equinox(self._year, vernal=False)
        if equinox_date:
            self._add_holiday("Autumnal Equinox Day", equinox_date)

    def _add_market_holidays(self):
        """Non-national market holidays: Jan 2-3, Dec 31"""
        # January 2
        jan2 = date(self._year, JAN, 2)
        if jan2.weekday() < 5:  # Weekday
            self._add_holiday("Market Holiday", jan2)

        # January 3
        jan3 = date(self._year, JAN, 3)
        if jan3.weekday() < 5:  # Weekday
            self._add_holiday("Market Holiday", jan3)

        # December 31
        dec31 = date(self._year, DEC, 31)
        if dec31.weekday() < 5:  # Weekday
            self._add_holiday("Market Holiday", dec31)

    def _apply_substitute_holidays(self):
        """Apply substitute holiday rule (Article 3, Paragraph 2)"""
        current_holidays = list(self.keys())

        for holiday_date in sorted(current_holidays):
            if holiday_date.weekday() == 6:  # Sunday
                candidate = holiday_date + timedelta(days=1)
                # Find next available weekday
                while candidate in self or candidate.weekday() >= 5:
                    candidate += timedelta(days=1)
                self._add_holiday("Substitute Holiday", candidate)

    def _apply_bridge_holidays(self):
        """Apply bridge holiday rule (Article 3, Paragraph 3)"""
        current_holidays = sorted(self.keys())

        for i in range(len(current_holidays) - 1):
            date1 = current_holidays[i]
            date2 = current_holidays[i + 1]

            if (date2 - date1).days == 2:  # Exactly one day gap
                bridge_day = date1 + timedelta(days=1)
                if bridge_day.weekday() < 5:  # Weekday
                    self._add_holiday("Citizens' Holiday", bridge_day)

    def _calculate_equinox(self, year, *, vernal=True):
        """Calculate equinox date based on astronomical formula"""
        # Simplified calculation - in production should use precise astronomical algorithms
        if vernal:  # Vernal Equinox (March)
            if year < 2000:
                # Historical formula
                day = int(20.8357 + 0.242194 * (year - 1980) - int((year - 1980) / 4))
            else:
                # Modern formula
                day = int(20.8431 + 0.242194 * (year - 1980) - int((year - 1980) / 4))
            return date(year, MAR, min(max(day, 20), 21))
        else:  # Autumnal Equinox (September)
            if year < 2000:
                # Historical formula
                day = int(23.2588 + 0.242194 * (year - 1980) - int((year - 1980) / 4))
            else:
                # Modern formula
                day = int(23.2488 + 0.242194 * (year - 1980) - int((year - 1980) / 4))
            return date(year, SEP, min(max(day, 22), 23))

    def _get_nth_weekday_of_month(self, n, weekday, month):
        """Get nth weekday of month (e.g., 2nd Monday of January)"""
        first_day = date(self._year, month, 1)
        # Find first occurrence of the weekday
        days_to_first = (weekday - first_day.weekday()) % 7
        first_weekday = first_day + timedelta(days=days_to_first)
        # Add (n-1) weeks
        return first_weekday + timedelta(weeks=n - 1)


class JPX(JapanExchange):
    """Japan Exchange Group (alias)."""

    pass


class TSE(JapanExchange):
    """Tokyo Stock Exchange (alias)."""

    pass


class OSE(JapanExchange):
    """Osaka Exchange (alias)."""

    pass


class JapanExchangeStaticHolidays:
    """Static overrides for special cases."""

    special_public_holidays = {
        2019: (
            (APR, 30, "Bridge Holiday (Imperial Accession)"),
            (MAY, 1, "Coronation Day"),
            (MAY, 2, "Bridge Holiday (Imperial Accession)"),
            (MAY, 6, "Children's Day Observed"),
        ),
        2020: (
            (JUL, 23, "Marine Day (Olympic Shift)"),
            (JUL, 24, "Sports Day (Olympic Shift)"),
            (AUG, 10, "Mountain Day (Olympic Shift)"),
        ),
        2021: (
            (JUL, 22, "Marine Day (Olympic Shift)"),
            (JUL, 23, "Sports Day (Olympic Shift)"),
            (AUG, 9, "Mountain Day Observed (Olympic Shift)"),
        ),
        2022: ((FEB, 24, "Emperor's Birthday Observed"),),
        2025: (
            (FEB, 24, "Emperor's Birthday Observed"),
            (MAY, 6, "Greenery Day Observed"),
            (NOV, 24, "Labor Thanksgiving Day Observed"),
        ),
        2026: ((SEP, 22, "Citizens' Holiday (Silver Week)"),),
    }
