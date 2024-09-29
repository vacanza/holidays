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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class ElSalvador(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
    - https://www.transparencia.gob.sv/institutions/gd-usulutan/documents/192280/download
    - https://www.timeanddate.com/holidays/el-salvador
    - https://www.officeholidays.com/countries/el-salvador
    """

    country = "SV"
    subdivisions = (
        "AH",  # Ahuachapán
        "CA",  # Cabañas
        "CH",  # Chalatenango
        "CU",  # Cuscatlán
        "LI",  # La Libertad
        "MO",  # Morazán
        "PA",  # La Paz
        "SA",  # Santa Ana
        "SM",  # San Miguel
        "SO",  # Sonsonate
        "SS",  # San Salvador
        "SV",  # San Vicente
        "UN",  # La Unión
        "US",  # Usulután
    )

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Maundy Thursday.
        self._add_holy_thursday("Maundy Thursday")

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Holy Saturday.
        self._add_holy_saturday("Holy Saturday")

        # Labor Day.
        self._add_labor_day("Labor Day")

        if self._year >= 2016:
            # Legislative Decree #399 from Apr 14, 2016
            # Mothers' Day.
            self._add_holiday_may_10("Mothers' Day")

        if self._year >= 2013:
            # Legislative Decree #208 from Jun 17, 2012
            # Fathers' Day.
            self._add_holiday_jun_17("Fathers' Day")

        # Feast of San Salvador.
        self._add_holiday_aug_6("Feast of San Salvador")

        # Independence Day.
        self._add_holiday_sep_15("Independence Day")

        # All Souls' Day.
        self._add_all_souls_day("All Souls' Day")

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

    def _populate_subdiv_ss_public_holidays(self):
        # San Salvador Day 1.
        self._add_holiday_aug_3("San Salvador Day 1")

        # San Salvador Day 2.
        self._add_holiday_aug_5("San Salvador Day 2")


class SV(ElSalvador):
    pass


class SLV(ElSalvador):
    pass
