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

from holidays.groups import IslamicHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Turkey(HolidayBase, IslamicHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Turkey
    """

    country = "TR"

    def __init__(self, *args, **kwargs):
        IslamicHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        self._add_new_years_day("New Year's Day")

        self._add_holiday_apr_23("National Sovereignty and Children's Day")

        self._add_labor_day("Labour Day")

        self._add_holiday_may_19("Commemoration of Ataturk, Youth and Sports Day")

        # Became a national holiday after 2016 Turkish coup d'état attempt.
        if year > 2016:
            self._add_holiday_jul_15("Democracy and National Unity Day")

        self._add_holiday_aug_30("Victory Day")

        self._add_holiday_oct_29("Republic Day")

        # Ramadan Feast.
        self._add_eid_al_fitr_day("Ramadan Feast")
        self._add_eid_al_fitr_day_two("Ramadan Feast Holiday")
        self._add_eid_al_fitr_day_three("Ramadan Feast Holiday")

        # Sacrifice Feast.
        self._add_eid_al_adha_day("Sacrifice Feast")
        self._add_eid_al_adha_day_two("Sacrifice Feast Holiday")
        self._add_eid_al_adha_day_three("Sacrifice Feast Holiday")
        self._add_eid_al_adha_day_four("Sacrifice Feast Holiday")


class TR(Turkey):
    pass


class TUR(Turkey):
    pass
