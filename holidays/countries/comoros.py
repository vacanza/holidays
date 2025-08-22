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

from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, APR, OCT
from holidays.groups import (
    ChristianHolidays,
    IslamicHolidays,
    InternationalHolidays,
    StaticHolidays,
)
from holidays.holiday_base import HolidayBase


class Comoros(
    HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """Comoros holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_the_Comoros>
        * [Décret N°24-056PR](https://web.archive.org/web/20250717033820/https://munganyo.km/decrees/225)
        * [Décret N°25-008PR](https://web.archive.org/web/20250715223159/https://munganyo.km/decrees/374)

    """

    country = "KM"
    # %s (estimated).
    estimated_label = "%s (estimated)"
    # Independence from France on July 6, 1975.
    start_year = 1976

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=ComorosIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, ComorosStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Cheikh al Maarouf.
        self._add_holiday_mar_18("Cheikh al Maarouf")

        # Labour Day.
        self._add_labor_day("Labour Day")

        # National Day.
        self._add_holiday_jul_6("National Day")

        if self._year >= 2006:
            # Maore Day.
            self._add_holiday_nov_12("Maore Day")

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

        # Eid al-Fitr.
        name = tr("Eid al-Fitr")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)

        # Eid al-Adha.
        name = tr("Eid al-Adha")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)

        # Islamic New Year.
        self._add_islamic_new_year_day("Islamic New Year")

        # The Prophet's Birthday.
        self._add_mawlid_day("The Prophet's Birthday")

        # The Prophet's Ascension.
        self._add_isra_and_miraj_day("The Prophet's Ascension")


class KM(Comoros):
    pass


class COM(Comoros):
    pass


class ComorosIslamicHolidays(_CustomIslamicHolidays):
    MAWLID_DATES_CONFIRMED_YEARS = (2021, 2021)
    MAWLID_DATES = {
        2021: (OCT, 19),
    }


class ComorosStaticHolidays:
    # Public Holiday.
    special_public_holidays = {
        2024: (APR, 13, "National Holiday"),
        2025: (JAN, 30, "Election Partial Day Holiday"),
    }
