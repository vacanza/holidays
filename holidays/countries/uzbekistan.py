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

from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Uzbekistan(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    https://www.officeholidays.com/countries/uzbekistan
    """

    country = "UZ"

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year
        self._add_new_years_day("New Year")

        # Women's Day
        self._add_womens_day("Women's Day")

        # Nauryz Holiday
        self._add_holiday_mar_21("Nauryz")

        # Ramadan Khait
        # Date of observance is announced yearly, This is an estimate.
        self._add_eid_al_fitr_day("Ramadan Khait")

        # Memorial Day
        self._add_world_war_two_victory_day("Memorial Day")

        # Kurban Khait
        # Date of observance is announced yearly, This is an estimate.
        self._add_eid_al_adha_day("Kurban Khait")

        # Independence Day
        self._add_holiday_sep_1("Independence Day")

        # Teacher's Day
        self._add_holiday_oct_1("Teacher's Day")

        # Constitution Day
        self._add_holiday_dec_8("Constitution Day")


class UZ(Uzbekistan):
    pass


class UZB(Uzbekistan):
    pass
