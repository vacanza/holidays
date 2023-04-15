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

from holidays.constants import JAN, MAR, APR, JUL, AUG, OCT
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import InternationalHolidays, IslamicHolidays


class Tunisia(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    Holidays here are estimates, it is common for the day to be pushed
    if falls in a weekend, although not a rule that can be implemented.
    Holidays after 2020: the following four moving date holidays whose exact
    date is announced yearly are estimated (and so denoted):
    - Eid El Fetr
    - Eid El Adha
    - Arafat Day
    - Moulad El Naby
    """

    country = "TN"

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self._add_new_years_day("New Year's Day")

        # Revolution and Youth Day - January 14
        self._add_holiday("Revolution and Youth Day - January 14", JAN, 14)

        # Independence Day
        self._add_holiday("Independence Day", MAR, 20)

        # Martyrs' Day
        self._add_holiday("Martyrs' Day", APR, 9)

        # Labour Day
        self._add_labor_day("Labour Day")

        # Republic Day
        self._add_holiday("Republic Day", JUL, 25)

        # Women's Day
        self._add_holiday("Women's Day", AUG, 13)

        # Evacuation Day
        self._add_holiday("Evacuation Day", OCT, 15)

        # Eid al-Fitr - Feast Festive
        # date of observance is announced yearly, This is an estimate since
        # having the Holiday on Weekend does change the number of days,
        # deceided to leave it since marking a Weekend as a holiday
        # wouldn't do much harm.
        name = "Eid al-Fitr"
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(f"{name} Holiday")
        self._add_eid_al_fitr_day_three(f"{name} Holiday")

        # Arafat Day & Eid al-Adha - Scarfice Festive
        # date of observance is announced yearly
        name = "Eid al-Adha"
        self._add_arafah_day("Arafat Day")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(f"{name} Holiday")
        self._add_eid_al_adha_day_three(f"{name} Holiday")

        # Islamic New Year - (hijari_year, 1, 1)
        self._add_islamic_new_year_day("Islamic New Year")

        # Prophet Muhammad's Birthday - (hijari_year, 3, 12)
        self._add_mawlid_day("Prophet Muhammad's Birthday")


class TN(Tunisia):
    pass


class TUN(Tunisia):
    pass
