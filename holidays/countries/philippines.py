#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from holidays.groups import (
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
)
from holidays.holiday_base import HolidayBase


class Philippines(
    HolidayBase, ChineseCalendarHolidays, ChristianHolidays, InternationalHolidays, IslamicHolidays
):
    """
    Philippines holidays.

    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_the_Philippines
    """

    country = "PH"

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Chinese New Year.
        self._add_chinese_new_years_day("Chinese New Year")

        # People Power Anniversary.
        self._add_holiday_feb_25("EDSA Revolution Anniversary")

        # Day of Valor.
        self._add_holiday_apr_9("Day of Valor")

        # Maundy Thursday.
        self._add_holy_thursday("Maundy Thursday")
        # Good Friday.
        self._add_good_friday("Good Friday")
        # Black Saturday.
        self._add_holy_saturday("Black Saturday")

        # Labour Day.
        self._add_labor_day("Labour Day")

        # Eid al-Fitr.
        self._add_eid_al_fitr_day("Eid'l Fitr")

        # Independence Day.
        self._add_holiday_jun_12("Independence Day")

        # Eid al-Adha.
        self._add_eid_al_adha_day("Eid'l Adha")

        # Ninoy Aquino Day.
        self._add_holiday_aug_21("Ninoy Aquino Day")

        # National Heroes Day.
        self._add_holiday_last_mon_of_aug("National Heroes Day")

        # All Saints' Day.
        self._add_all_saints_day("All Saints' Day")

        # Bonifacio Day.
        self._add_holiday_nov_30("Bonifacio Day")

        # Immaculate Conception Day.
        self._add_immaculate_conception_day("Immaculate Conception Day")

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

        # Rizal Day.
        self._add_holiday_dec_30("Rizal Day")

        # New Year's Eve.
        self._add_new_years_eve("New Year's Eve")


class PH(Philippines):
    pass


class PHL(Philippines):
    pass
