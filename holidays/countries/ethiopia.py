#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: vacanza team (https://github.com/orgs/vacanza/teams) (c) 2023-2024
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from calendar import isleap
from gettext import gettext as tr

from holidays.calendars.gregorian import SEP
from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Ethiopia(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    country = "ET"
    default_language = "am"
    estimated_label = tr("%s (ግምት)")
    supported_languages = ("am", "ar", "en_US")

    def _is_leap_year(self):
        """
        Ethiopian leap years are coincident with leap years in the Gregorian
        calendar until the end of February 2100. It starts earlier from new
        year of western calendar.
        Ethiopian leap year starts on Sep 11, so it has an effect on
        holidays between Sep 11 and Jan 1. Therefore, here on the following
        function we intentionally add 1 to the leap year to offset the
        difference.
        """
        return isleap(self._year + 1)

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day
        # The Ethiopian New Year is called Kudus Yohannes in Ge'ez and
        # Tigrinya, while in Amharic,
        # the official language of Ethiopia it is called Enkutatash.
        # It occurs on September 11 in the Gregorian Calendar;
        # except for the year preceding a leap year, when it occurs on
        # September 12.

        # Ethiopian New Year.
        self._add_holiday(tr("አዲስ ዓመት እንቁጣጣሽ"), SEP, 12 if self._is_leap_year() else 11)

        # Finding of True Cross.
        self._add_holiday(tr("መስቀል"), SEP, 28 if self._is_leap_year() else 27)

        # Orthodox Christmas.
        self._add_christmas_day(tr("ገና"))

        # Orthodox Epiphany.
        self._add_epiphany_day(tr("ጥምቀት"))

        # Orthodox Good Friday.
        self._add_good_friday(tr("ስቅለት"))

        # Orthodox Easter Sunday.
        self._add_easter_sunday(tr("ፋሲካ"))

        if self._year > 1896:
            # Adwa Victory Day.
            self._add_holiday_mar_2(tr("አድዋ"))

        # Labour Day.
        self._add_labor_day(tr("የሰራተኞች ቀን"))

        if self._year > 1941:
            # Patriots Day.
            self._add_holiday_may_5(tr("የአርበኞች ቀን"))

        if self._year > 1991:
            # Downfall of Dergue Regime Day.
            self._add_holiday_may_28(tr("ደርግ የወደቀበት ቀን"))

        if self._year < 1991 and self._year > 1974:
            # Downfall of King Haile Selassie.
            self._add_holiday(tr("ደርግ የመጣበት ቀን"), SEP, 13 if self._is_leap_year() else 12)

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("ኢድ አልፈጥር"))

        # Eid al-Adha.
        name = tr("አረፋ")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)

        # Prophet Muhammad's Birthday.
        name = tr("መውሊድ")
        self._add_mawlid_day(name)
        self._add_mawlid_day_two(name)


class ET(Ethiopia):
    pass


class ETH(Ethiopia):
    pass
