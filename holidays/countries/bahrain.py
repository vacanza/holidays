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

from datetime import date
from datetime import timedelta as td

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
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Labour day.
        self._add_labor_day("Labour Day")

        # Eid Al Fitr.
        eid_al_fitr = "Eid Al Fitr"
        eid_al_fitr_mapping = {
            2022: ((MAY, 2),),
        }
        if year in eid_al_fitr_mapping:
            for dt in eid_al_fitr_mapping[year]:
                eid_al_fitr_day = date(year, *dt)
                self._add_holiday(eid_al_fitr, eid_al_fitr_day)
                self._add_holiday(
                    f"{eid_al_fitr} Holiday", eid_al_fitr_day + td(days=+1)
                )
                self._add_holiday(
                    f"{eid_al_fitr} Holiday", eid_al_fitr_day + td(days=+2)
                )
        else:
            self._add_eid_al_fitr_day(f"{eid_al_fitr}* (*estimated)")
            self._add_eid_al_fitr_day_two(
                f"{eid_al_fitr} Holiday* (*estimated)"
            )
            self._add_eid_al_fitr_day_three(
                f"{eid_al_fitr} Holiday* (*estimated)"
            )

        # Eid Al Adha.
        eid_al_adha = "Eid Al Adha"
        eid_al_adha_mapping = {
            2022: ((JUL, 9),),
        }
        if year in eid_al_adha_mapping:
            for dt in eid_al_adha_mapping[year]:
                eid_al_adha_day = date(year, *dt)
                self._add_holiday(eid_al_adha, eid_al_adha_day)
                self._add_holiday(
                    f"{eid_al_adha} Holiday", eid_al_adha_day + td(days=+1)
                )
                self._add_holiday(
                    f"{eid_al_adha} Holiday", eid_al_adha_day + td(days=+2)
                )
        else:
            self._add_eid_al_adha_day(f"{eid_al_adha}* (*estimated)")
            self._add_eid_al_adha_day_two(f"{eid_al_adha}* (*estimated)")
            self._add_eid_al_adha_day_three(f"{eid_al_adha}* (*estimated)")

        # Al Hijra New Year.
        hijri_new_year = "Al Hijra New Year"
        hijri_new_year_mapping = {
            2022: ((JUL, 30),),
        }
        if year in hijri_new_year_mapping:
            for dt in hijri_new_year_mapping[year]:
                self._add_holiday(hijri_new_year, date(year, *dt))
        else:
            self._add_islamic_new_year_day(f"{hijri_new_year}* (*estimated)")

        # Ashura.
        ashura = "Ashura"
        ashura_mapping = {
            2022: ((AUG, 7),),
        }
        if year in ashura_mapping:
            for dt in ashura_mapping[year]:
                ashura_day = date(year, *dt)
                self._add_holiday(ashura, ashura_day)
                self._add_holiday(
                    f"{ashura} Holiday", ashura_day + td(days=+1)
                )
        else:
            for ashura_dt in self._add_ashura_day(
                f"{ashura} Holiday* (*estimated)"
            ):
                self._add_holiday(
                    f"{ashura}* (*estimated)", ashura_dt + td(days=-1)
                )

        # Prophets Birthday.
        mawlud = "Prophets Birthday"
        mawlud_mapping = {2022: ((OCT, 8),)}
        if year in mawlud_mapping:
            for dt in mawlud_mapping[year]:
                self._add_holiday(mawlud, date(year, *dt))
        else:
            self._add_mawlid_day(f"{mawlud}* (*estimated)")

        # National Day.
        national_day = "National Day"
        self._add_holiday(national_day, DEC, 16)
        self._add_holiday(national_day, DEC, 17)


class BH(Bahrain):
    pass


class BAH(Bahrain):
    pass
