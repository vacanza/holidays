#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars.gregorian import _timedelta
from holidays.constants import PUBLIC, UNOFFICIAL
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Aland(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Aland Islands holidays.

    References:
        * https://en.wikipedia.org/wiki/Public_holidays_in_%C3%85land
        * https://date.nager.at/PublicHoliday/%C3%85land-Islands/2025
        * https://www.bank-holidays.com/country/Aland-Islands_194.htm
    """

    country = "AX"
    default_language = "sv"
    supported_languages = ("en_US",)
    supported_categories = (PUBLIC, UNOFFICIAL)
    start_year = 1920

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Nyårsdagen"))

        # Epiphany.
        self._add_epiphany_day(tr("Trettondedag jul"))

        # Good Friday.
        self._add_good_friday(tr("Långfredagen"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Påskdagen"))

        # Easter Monday.
        self._add_easter_monday(tr("Annandag påsk"))

        if self._year >= 1939:
            # May Day.
            self._add_labor_day(tr("Första maj"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Kristi himmelsfärdsdag"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Pingstdagen"))

        # Autonomy Day
        self._add_holiday_jun_9(tr("Självstyrelsedagen"))

        # Midsummer Eve.
        name = tr("Midsommarafton")
        dt = (
            self._add_holiday_1st_fri_from_jun_19(name)
            if self._year >= 1953
            else self._add_holiday_jun_23(name)
        )

        # Midsummer Day.
        self._add_holiday(tr("Midsommardagen"), _timedelta(dt, +1))

        # All Saints' Day.
        self._add_holiday_1st_sat_from_oct_31(tr("Alla helgons dag"))

        if self._year >= 1917:
            # Finnish Independence Day.
            self._add_holiday_dec_6(tr("Självständighetsdagen"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Julafton"))

        # Christmas Day.
        self._add_christmas_day(tr("Juldagen"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Annandag jul"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Nyårsafton"))


class AX(Aland):
    """Alternative name for the Åland Islands holidays (ISO 3166-1 alpha-2 code)."""

    pass


class ALA(Aland):
    """Alternative name for the Åland Islands holidays (ISO 3166-1 alpha-3 code)."""

    pass
