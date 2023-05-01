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

from holidays.calendars import _CustomCalendar, _IslamicLunar
from holidays.constants import FRI, SAT, MAY, JUL, AUG, OCT, DEC
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import InternationalHolidays, IslamicHolidays


class Bahrain(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    Bahrain holidays.

    References:
      - https://www.cbb.gov.bh/official-bank-holidays/
      - https://www.officeholidays.com/countries/bahrain/
    """

    country = "BH"
    weekend = {FRI, SAT}

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, calendar=BahrainIslamicCalendar())
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Labour day.
        self._add_labor_day("Labour Day")

        # Eid Al Fitr.
        eid_al_fitr = "Eid Al Fitr"
        self._add_eid_al_fitr_day(eid_al_fitr)
        self._add_eid_al_fitr_day_two(f"{eid_al_fitr} Holiday")
        self._add_eid_al_fitr_day_three(f"{eid_al_fitr} Holiday")

        # Eid Al Adha.
        eid_al_adha = "Eid Al Adha"
        self._add_eid_al_adha_day(eid_al_adha)
        self._add_eid_al_adha_day_two(f"{eid_al_adha} Holiday")
        self._add_eid_al_adha_day_three(f"{eid_al_adha} Holiday")

        # Al Hijra New Year.
        hijri_new_year = "Al Hijra New Year"
        self._add_islamic_new_year_day(hijri_new_year)

        # Ashura.
        ashura = "Ashura"
        self._add_ashura_eve(f"{ashura} Holiday")
        self._add_ashura_day(ashura)

        # Prophets Birthday.
        self._add_mawlid_day("Prophets Birthday")

        # National Day.
        national_day = "National Day"
        self._add_holiday(national_day, DEC, 16)
        self._add_holiday(national_day, DEC, 17)


class BH(Bahrain):
    pass


class BAH(Bahrain):
    pass


class BahrainIslamicCalendar(_CustomCalendar, _IslamicLunar):
    ASHURA_DATES = {
        2022: ((AUG, 8),),
    }

    EID_AL_ADHA = {
        2022: ((JUL, 9),),
    }

    EID_AL_FITR_DATES = {
        2022: ((MAY, 2),),
    }

    HIJRI_NEW_YEAR_DATES = {
        2022: ((JUL, 30),),
    }

    MAWLID_DATES = {
        2022: ((OCT, 8),),
    }
