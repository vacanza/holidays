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

from holidays.calendars.gregorian import APR, OCT, JUL, NOV
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class SintMaarten(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Sint Maarten holidays.

    References:
        * <https://web.archive.org/web/20250606191248/https://en.wikipedia.org/wiki/Sint_Maarten>
        * <https://web.archive.org/web/20250529071040/https://en.wikipedia.org/wiki/Public_holidays_in_Sint_Maarten>
        * <https://web.archive.org/web/20250425015159/https://www.qppstudio.net/public-holidays/sint_maarten.htm>
        * <https://web.archive.org/web/20250212071023/https://www.sintmaartengov.org/Pages/Public-Holiday-Schedule.aspx>
    """

    country = "SX"
    default_language = "en_US"
    supported_languages = ("en_US",)
    # OCT 2010: Autonomous State status in the Kingdom of the Netherlands.
    start_year = 2010

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day
        self._add_new_years_day(tr("New Year's Day"))

        # Good Friday
        self._add_good_friday(tr("Good Friday"))

        # Easter Sunday
        self._add_easter_sunday(tr("Easter Sunday"))

        # Easter Monday
        self._add_easter_monday(tr("Easter Monday"))

        # King's Day (April 27 or April 26 if 27 is a Sunday)
        if self._year >= 2014:
            if date(self._year, APR, 27).weekday() == 6:  # Sunday
                self._add_holiday(tr("King's Day"), date(self._year, APR, 26))
            else:
                self._add_holiday(tr("King's Day"), date(self._year, APR, 27))
        
        # Carnival Day
        self._add_holiday(tr("Carnival Day"), date(self._year, APR, 30))

        # Labour Day
        self._add_labor_day(tr("Labour Day"))

        # Ascension Day
        self._add_ascension_thursday(tr("Ascension Day"))

        # Whit Sunday
        self._add_whit_sunday(tr("Whit Sunday"))

        # Emancipation Day
        if self._year >= 2020:
            self._add_holiday(tr("Emancipation Day"), date(self._year, JUL, 1))
        
        # Constitution Day
        if self._year >= 2010:
            self._add_holiday(tr("Constitution Day"), date(self._year, OCT, 10))
        
        # Sint Maarten Day
        self._add_holiday(tr("Sint Maarten Day"), date(self._year, NOV, 11))

        # Christmas Day
        self._add_christmas_day(tr("Christmas Day"))

        # Second day of Christmas
        self._add_christmas_day_two(tr("Second day of Christmas"))


class SX(SintMaarten):
    pass


class SXM(SintMaarten):
    pass