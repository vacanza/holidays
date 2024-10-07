#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from holidays.calendars.gregorian import FRI, SAT
from holidays.groups import InternationalHolidays
from holidays.holiday_base import HolidayBase


class Bangladesh(HolidayBase, InternationalHolidays):
    """
    References:
        - https://mopa.gov.bd/sites/default/files/files/mopa.gov.bd/public_holiday/61c35b73_e335_462a_9bcf_4695b23b6d82/reg4-2019-212.PDF
        - https://en.wikipedia.org/wiki/Public_holidays_in_Bangladesh
    """

    country = "BD"
    weekend = {FRI, SAT}

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
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
