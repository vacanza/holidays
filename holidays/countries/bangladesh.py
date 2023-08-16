#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           tasnim<tasnimislam1999@gmail.com>
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.groups import InternationalHolidays
from holidays.holiday_base import HolidayBase


class Bangladesh(HolidayBase, InternationalHolidays):
    """
    https://mopa.gov.bd/sites/default/files/files/mopa.gov.bd/public_holiday/61c35b73_e335_462a_9bcf_4695b23b6d82/reg4-2019-212.PDF
    https://en.wikipedia.org/wiki/Public_holidays_in_Bangladesh
    """

    country = "BD"

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # International Mother's language Day.
        self._add_holiday_feb_21("International Mother's language Day")

        # Sheikh Mujibur Rahman's Birthday and Children's Day.
        self._add_holiday_mar_17("Sheikh Mujibur Rahman's Birthday and Children's Day")

        # Independence Day.
        self._add_holiday_mar_26("Independence Day")

        # Bengali New Year's Day.
        self._add_holiday_apr_14("Bengali New Year's Day")

        # May Day.
        self._add_labor_day("May Day")

        # National Mourning Day.
        self._add_holiday_aug_15("National Mourning Day")

        # Victory Day.
        self._add_holiday_dec_16("Victory Day")


class BD(Bangladesh):
    pass


class BGD(Bangladesh):
    pass
