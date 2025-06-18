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

from holidays.calendars.gregorian import NOV
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SUN_TO_NEXT_MON,
    SAT_TO_PREV_FRI,
    SUN_TO_NEXT_TUE,
    SUN_TO_PREV_SAT,
)


class SintMaarten(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Sint Maarten holidays.

    References:
        * <https://web.archive.org/web/20250606191248/https://en.wikipedia.org/wiki/Sint_Maarten>
        * <https://web.archive.org/web/20250529071040/https://en.wikipedia.org/wiki/Public_holidays_in_Sint_Maarten>
        * <https://web.archive.org/web/20250425015159/https://www.qppstudio.net/public-holidays/sint_maarten.htm>
        * [AB 2012 no. 19](https://web.archive.org/web/20250615040244/https://www.sintmaartengov.org/Documents/Official%20Publications/AB%2019%20Lvo%20Dag%20van%20Bevrijding.pdf)
        * [AB 2015 no. 24](https://web.archive.org/web/20250615035932/https://www.sintmaartengov.org/Documents/Official%20Publications/AB%2024%20Landsverordening%20Constitution%20Day.pdf)
        * [2014-2023](https://web.archive.org/web/20230307083630/https://www.sintmaartengov.org/government/VSA/labour/Pages/Public-Holiday-Schedule.aspx)
        * [2024-Present](https://web.archive.org/web/20250212071023/https://www.sintmaartengov.org/Pages/Public-Holiday-Schedule.aspx)
    """

    country = "SX"
    default_language = "en_US"
    supported_languages = ("en_US",)
    # Sint Maarten became a constituent country on October 10, 2010.
    start_year = 2011

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("New Year's Day"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Easter Sunday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        if self._year >= 2014:
            self._move_holiday(
                # King's Day (April 27 or April 26 if 27 is a Sunday).
                self._add_holiday_apr_27(tr("King's Day")),
                rule=SUN_TO_PREV_SAT,
            )

        if self._year >= 2011:
            self._move_holiday(
                # Carnival Day.
                self._add_holiday_apr_30(tr("Carnival Day")),
                rule=SAT_TO_PREV_FRI + SUN_TO_NEXT_TUE,
            )

        # Labour Day.
        self._add_labor_day(tr("Labour Day"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Ascension Day"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Whit Sunday"))

        # Established on June 13th, 2012.
        if self._year >= 2012:
            # Emancipation Day.
            self._add_observed(self._add_holiday_jul_1(tr("Emancipation Day")))

        # Established on September 28th, 2015.
        if self._year >= 2015:
            # Constitution Day.
            self._add_holiday_2nd_mon_of_oct(tr("Constitution Day"))

        if self._year >= 2011:
            self._move_holiday(
                # Kingdom Day on 15th December (If a Sunday, on Monday 16 December).
                self._add_holiday_dec_15(tr("Kingdom Day")),
                rule=SUN_TO_NEXT_MON,
            )

        if self._year >= 2011:
            # All Saints' Day.
            self._add_holiday(tr("All Saints' Day"), date(self._year, NOV, 1))

        if self._year >= 2011:
            # Sint Maarten Day.
            self._add_holiday(tr("Sint Maarten Day"), date(self._year, NOV, 11))

        # Christmas Day.
        self._add_christmas_day(tr("Christmas Day"))

        # Second day of Christmas.
        self._add_christmas_day_two(tr("Second day of Christmas"))


class SX(SintMaarten):
    pass


class SXM(SintMaarten):
    pass
