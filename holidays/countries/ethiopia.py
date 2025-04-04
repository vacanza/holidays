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

from calendar import isleap
from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV
from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Ethiopia(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Ethiopia holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Ethiopia>
    """

    country = "ET"
    default_language = "am"
    # %s (estimated).
    estimated_label = tr("%s (ግምት)")
    supported_languages = ("am", "ar", "en_US")
    start_year = 1898

    def _is_leap_year(self):
        """Determine if the Ethiopian calendar year is a leap year.

        Ethiopian leap years generally align with Gregorian leap years until
        February 2100. However, the Ethiopian calendar starts earlier (on September 11),
        which affects holidays between September 11 and January 1.

        To account for this shift, the method checks whether next year is a leap year
        in the Gregorian calendar.

        Returns:
            `True` if the Ethiopian year is a leap year, `False` otherwise.
        """

        return isleap(self._year + 1)

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=EthiopiaIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Christmas Day.
        self._add_christmas_day(tr("ገና"))

        # Epiphany.
        self._add_holiday(tr("ጥምቀት"), JAN, 20 if super()._is_leap_year() else 19)

        # Adwa Victory Day.
        self._add_holiday_mar_2(tr("አድዋ"))

        # Good Friday.
        self._add_good_friday(tr("ስቅለት"))

        # Easter Sunday.
        self._add_easter_sunday(tr("ፋሲካ"))

        # Workers' Day.
        self._add_labor_day(tr("የሰራተኞች ቀን"))

        if self._year >= 1942:
            # Patriots' Day.
            self._add_holiday_may_5(tr("የአርበኞች ቀን"))

        if self._year >= 1992:
            # Downfall of Dergue Regime Day.
            self._add_holiday_may_28(tr("ደርግ የወደቀበት ቀን"))

        # Ethiopian New Year.
        self._add_holiday(tr("እንቁጣጣሽ"), SEP, 12 if self._is_leap_year() else 11)

        # Finding of True Cross.
        self._add_holiday(tr("መስቀል"), SEP, 28 if self._is_leap_year() else 27)

        if 1975 <= self._year <= 1990:
            # Revolution Day.
            self._add_holiday(tr("የአብዮት ቀን"), SEP, 13 if self._is_leap_year() else 12)

            # October Revolution Day.
            self._add_holiday_nov_7(tr("የጥቅምት አብዮት ቀን"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("ኢድ አልፈጥር"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("አረፋ"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("መውሊድ"))


class ET(Ethiopia):
    pass


class ETH(Ethiopia):
    pass


class EthiopiaIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2018: (AUG, 22),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
    }

    EID_AL_FITR_DATES = {
        2018: (JUN, 15),
        2019: (JUN, 4),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 21),
        2024: (APR, 10),
    }

    MAWLID_DATES = {
        2018: (NOV, 21),
        2019: (NOV, 10),
        2020: (OCT, 29),
        2021: (OCT, 18),
        2022: (OCT, 8),
        2023: (SEP, 27),
    }
