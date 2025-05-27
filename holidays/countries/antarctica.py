#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2025
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date, timedelta
from holidays.constants import PUBLIC
from holidays.holiday_base import HolidayBase
from gettext import gettext as tr

from holidays.calendars.gregorian import (
    JAN, FEB, MAR, APR, MAY, JUN, JUL, SEP, OCT, NOV, DEC
)
from holidays.calendars.gregorian import _get_nth_weekday_from
from holidays.calendars.gregorian import MON, FRI

class Antarctica(HolidayBase):
    """
    Antarctica holidays.

    Based on community, research station, and historical conventions.
    """

    country = "AQ"
    default_language = "en_US"
    supported_categories = (PUBLIC,)
    supported_languages = ("en_US",)
    subdivisions = ()
    subdivisions_aliases = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        year = self._year

        # Fixed-date holidays
        self._add_holiday_jan_1(tr("New Year's Day"))
        self._add_holiday_jan_27(tr("Bellingshausen Day"))

        self._add_holiday_jul_1(tr("Dominion Day"))
        self._add_holiday_nov_11(tr("Remembrance Day"))
        self._add_holiday_dec_14(tr("Amundsen Day"))
        self._add_holiday_dec_24(tr("Christmas Eve"))
        self._add_christmas_day(tr("Christmas Day"))
        self._add_holiday_dec_26(tr("Boxing Day"))
        self._add_holiday_dec_31(tr("New Year's Eve"))

        # 1st Friday of February - Election Day
        feb_first = date(year, FEB, 1)
        first_friday_feb = feb_first + timedelta(days=(FRI - feb_first.weekday()) % 7)
        self._add_holiday(first_friday_feb, tr("Election Day"))

        # 1st Monday of March - March Bank Holiday
        mar_first = date(year, MAR, 1)
        first_monday_mar = mar_first + timedelta(days=(MON - mar_first.weekday()) % 7)
        self._add_holiday(first_monday_mar, tr("March Bank Holiday"))

        # Good Friday, Easter Sunday, Easter Monday
        self._add_good_friday(tr("Good Friday"))
        self._add_easter_sunday(tr("Easter Sunday"))
        self._add_easter_monday(tr("Easter Monday"))

        # Monday before May 25 - Victoria Day
        may_25 = date(year, MAY, 25)
        victoria_day = may_25 - timedelta(days=(may_25.weekday() + 1) % 7 + 1)
        # Find the Monday before May 25
        while victoria_day.weekday() != 0 or victoria_day >= may_25:
            victoria_day -= timedelta(days=1)
        self._add_holiday(victoria_day, tr("Victoria Day"))

        # June Solstice - Midwinter Bank Holiday (typically June 20, 21, or 22)
        # We'll use astronomical calculation for solstice; for most practical purposes, June 21.
        self._add_holiday_jun_21(tr("Midwinter Bank Holiday"))

        # 1st Monday of September - Labour Day
        sep_first = date(year, SEP, 1)
        first_monday_sep = sep_first + timedelta(days=(MON - sep_first.weekday()) % 7)
        self._add_holiday(first_monday_sep, tr("Labour Day"))

        # 2nd Monday of October - Thanksgiving
        oct_first = date(year, OCT, 1)
        first_monday_oct = oct_first + timedelta(days=(MON - oct_first.weekday()) % 7)
        second_monday_oct = first_monday_oct + timedelta(days=7)
        self._add_holiday(second_monday_oct, tr("Thanksgiving"))

        # Last Monday of November - November Bank Holiday
        nov_last = date(year, NOV, 30)
        last_monday_nov = nov_last - timedelta(days=(nov_last.weekday() - MON) % 7)
        self._add_holiday(last_monday_nov, tr("November Bank Holiday"))

    # Helper method for holidays on an exact date
    def _add_holiday(self, dt, name):
        self._add_holiday_date(dt, name)

    def _add_holiday_date(self, dt, name):
        self[dt] = name

    def _add_holiday_jan_1(self, name):
        self._add_holiday(date(self._year, JAN, 1), name)

    def _add_holiday_jan_27(self, name):
        self._add_holiday(date(self._year, JAN, 27), name)

    def _add_holiday_jul_1(self, name):
        self._add_holiday(date(self._year, JUL, 1), name)

    def _add_holiday_nov_11(self, name):
        self._add_holiday(date(self._year, NOV, 11), name)

    def _add_holiday_dec_14(self, name):
        self._add_holiday(date(self._year, DEC, 14), name)

    def _add_holiday_dec_24(self, name):
        self._add_holiday(date(self._year, DEC, 24), name)

    def _add_holiday_dec_26(self, name):
        self._add_holiday(date(self._year, DEC, 26), name)

    def _add_holiday_dec_31(self, name):
        self._add_holiday(date(self._year, DEC, 31), name)

    def _add_holiday_jun_21(self, name):
        self._add_holiday(date(self._year, JUN, 21), name)

class AQ(Antarctica):
    pass

class ATA(Antarctica):
    pass