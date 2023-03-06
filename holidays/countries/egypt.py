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

from holidays.calendars import JULIAN_CALENDAR
from holidays.constants import JAN, APR, JUN, JUL, OCT
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, IslamicHolidays
from holidays.holiday_groups import InternationalHolidays


class Egypt(
    HolidayBase, ChristianHolidays, IslamicHolidays, InternationalHolidays
):
    # Holidays here are estimates, it is common for the day to be pushed
    # if falls in a weekend, although not a rule that can be implemented.
    # Holidays after 2020: the following four moving date holidays whose exact
    # date is announced yearly are estimated (and so denoted):
    # - Eid El Fetr*
    # - Eid El Adha*
    # - Arafat Day*
    # - Moulad El Naby*
    # *only if hijri-converter library is installed, otherwise a warning is
    #  raised that this holiday is missing. hijri-converter requires
    #  Python >= 3.6
    # is_weekend function is there, however not activated for accuracy.

    country = "EG"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)

        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self._add_new_years_day("New Year's Day - Bank Holiday")

        # Coptic Christmas
        self._add_christmas_day("Coptic Christmas")

        # 25th of Jan
        if year >= 2012:
            self._add_holiday("Revolution Day - January 25", JAN, 25)
        elif year >= 2009:
            self._add_holiday("Police Day", JAN, 25)

        # Coptic Easter - Orthodox Easter
        self._add_easter_sunday("Coptic Easter Sunday")
        self._add_easter_monday("Sham El Nessim")  # Spring Festival

        # Sinai Libration Day
        if year > 1982:
            self._add_holiday("Sinai Liberation Day", APR, 25)

        # Labour Day
        self._add_labour_day("Labour Day")

        # Armed Forces Day
        self._add_holiday("Armed Forces Day", OCT, 6)

        # 30 June Revolution Day
        if year >= 2014:
            self._add_holiday("30 June Revolution Day", JUN, 30)

        # Revolution Day
        if year > 1952:
            self._add_holiday("Revolution Day", JUL, 23)

        # Eid al-Fitr - Feast Festive
        self._add_eid_al_fitr_day("Eid al-Fitr")
        self._add_eid_al_fitr_day_two("Eid al-Fitr Holiday")
        self._add_eid_al_fitr_day_three("Eid al-Fitr Holiday")

        self._add_arafah_day("Arafat Day")

        # Arafat Day & Eid al-Adha - Scarfice Festive
        self._add_eid_al_adha_day("Eid al-Adha")
        self._add_eid_al_adha_day_two("Eid al-Adha Holiday")
        self._add_eid_al_adha_day_three("Eid al-Adha Holiday")

        self._add_islamic_new_year_day("Islamic New Year")

        self._add_mawlid_day("Prophet Muhammad's Birthday")


class EG(Egypt):
    pass


class EGY(Egypt):
    pass
