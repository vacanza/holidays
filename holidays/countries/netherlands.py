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

from datetime import date
from gettext import gettext as tr

from holidays.calendars.gregorian import APR, AUG, _timedelta
from holidays.constants import OPTIONAL, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Netherlands(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:

    - https://en.wikipedia.org/wiki/Public_holidays_in_the_Netherlands
    - https://nl.wikipedia.org/wiki/Feestdagen_in_Nederland
    - http://www.iamsterdam.com/en/plan-your-trip/practical-info/public-holidays
    """

    country = "NL"
    default_language = "nl"
    supported_categories = (OPTIONAL, PUBLIC)
    supported_languages = ("en_US", "nl", "uk")
    start_year = 1801

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Nieuwjaarsdag"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Eerste paasdag"))

        # Easter Monday.
        self._add_easter_monday(tr("Tweede paasdag"))

        # King's / Queen's day
        if self._year >= 1891:
            name = (
                # King's Day.
                tr("Koningsdag")
                if self._year >= 2014
                # Queen's Day.
                else tr("Koninginnedag")
            )
            if self._year >= 2014:
                dt = date(self._year, APR, 27)
            elif self._year >= 1949:
                dt = date(self._year, APR, 30)
            else:
                dt = date(self._year, AUG, 31)
            if self._is_sunday(dt):
                dt = _timedelta(dt, -1 if self._year >= 1980 else +1)
            self._add_holiday(name, dt)

        if self._year >= 1950 and self._year % 5 == 0:
            # Liberation Day.
            self._add_holiday_may_5(tr("Bevrijdingsdag"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Hemelvaartsdag"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Eerste Pinksterdag"))

        # Whit Monday.
        self._add_whit_monday(tr("Tweede Pinksterdag"))

        # Christmas Day.
        self._add_christmas_day(tr("Eerste Kerstdag"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Tweede Kerstdag"))

    def _populate_optional_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Goede Vrijdag"))

        if self._year >= 1990:
            # Liberation Day.
            self._add_holiday_may_5(tr("Bevrijdingsdag"))


class NL(Netherlands):
    pass


class NLD(Netherlands):
    pass
