#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.groups import ChristianHolidays, IslamicHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class NorthMacedonia(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_North_Macedonia
    """

    country = "MK"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        self._add_new_years_day("New Year's Day")

        self._add_christmas_day("Christmas Day (Orthodox)")

        self._add_easter_monday("Easter Monday (Orthodox)")

        self._add_labor_day("Labour Day")

        self._add_holiday_may_24("Saints Cyril and Methodius Day")

        self._add_holiday_aug_2("Republic Day")

        self._add_holiday_sep_8("Independence Day")

        self._add_holiday_oct_11("Day of Macedonian Uprising in 1941")

        self._add_holiday_oct_23("Day of the Macedonian Revolutionary Struggle")

        self._add_holiday_dec_8("Saint Clement of Ohrid Day")

        self._add_eid_al_fitr_day("Eid al-Fitr")


class MK(NorthMacedonia):
    pass


class MKD(NorthMacedonia):
    pass
