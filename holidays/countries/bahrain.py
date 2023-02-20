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

from holidays.calendars import _islamic_to_gre
from holidays.constants import FRI, SAT, JAN, MAY, JUL, AUG, OCT, DEC
from holidays.holiday_base import HolidayBase


class Bahrain(HolidayBase):
    """
    Bahrain holidays.

    References:
      - https://www.cbb.gov.bh/official-bank-holidays/
      - https://www.officeholidays.com/countries/bahrain/
    """

    country = "BH"
    weekend = {FRI, SAT}

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self[date(year, JAN, 1)] = "New Year's Day"

        # Labour day.
        self[date(year, MAY, 1)] = "Labour Day"

        # Eid Al Fitr.
        eid_al_fitr = "Eid Al Fitr"
        eid_al_fitr_mapping = {
            2022: ((MAY, 2),),
        }
        if year in eid_al_fitr_mapping:
            for dt in eid_al_fitr_mapping[year]:
                eid_al_fitr_day = date(year, *dt)
                self[eid_al_fitr_day] = eid_al_fitr
                self[eid_al_fitr_day + td(days=+1)] = f"{eid_al_fitr} Holiday"
                self[eid_al_fitr_day + td(days=+2)] = f"{eid_al_fitr} Holiday"
        else:
            for eid_al_fitr_day in _islamic_to_gre(year, 10, 1):
                self[eid_al_fitr_day] = f"{eid_al_fitr}* (*estimated)"
                self[
                    eid_al_fitr_day + td(days=+1)
                ] = f"{eid_al_fitr} Holiday* (*estimated)"
                self[
                    eid_al_fitr_day + td(days=+2)
                ] = f"{eid_al_fitr} Holiday* (*estimated)"

        # Eid Al Adha.
        eid_al_adha = "Eid Al Adha"
        eid_al_adha_mapping = {
            2022: ((JUL, 9),),
        }
        if year in eid_al_adha_mapping:
            for dt in eid_al_adha_mapping[year]:
                eid_al_adha_day = date(year, *dt)
                self[eid_al_adha_day] = eid_al_adha
                self[eid_al_adha_day + td(days=+1)] = f"{eid_al_adha} Holiday"
                self[eid_al_adha_day + td(days=+2)] = f"{eid_al_adha} Holiday"
        else:
            for eid_al_adha_day in _islamic_to_gre(year, 12, 9):
                self[
                    eid_al_adha_day + td(days=+1)
                ] = f"{eid_al_adha}* (*estimated)"
                self[
                    eid_al_adha_day + td(days=+2)
                ] = f"{eid_al_adha}* (*estimated)"
                self[
                    eid_al_adha_day + td(days=+3)
                ] = f"{eid_al_adha}* (*estimated)"

        # Al Hijra New Year.
        hijri_new_year = "Al Hijra New Year"
        hijri_new_year_mapping = {
            2022: ((JUL, 30),),
        }
        if year in hijri_new_year_mapping:
            for dt in hijri_new_year_mapping[year]:
                self[date(year, *dt)] = hijri_new_year
        else:
            for dt in _islamic_to_gre(year, 1, 1):
                self[dt] = f"{hijri_new_year}* (*estimated)"

        # Ashura.
        ashura = "Ashura"
        ashura_mapping = {
            2022: ((AUG, 7),),
        }
        if year in ashura_mapping:
            for dt in ashura_mapping[year]:
                ashura_day = date(year, *dt)
                self[ashura_day] = ashura
                self[ashura_day + td(days=+1)] = f"{ashura} Holiday"
        else:
            for ashura_day in _islamic_to_gre(year, 1, 9):
                self[ashura_day] = f"{ashura}* (*estimated)"
                self[
                    ashura_day + td(days=+1)
                ] = f"{ashura}* Holiday* (*estimated)"

        # Prophets Birthday.
        mawlud = "Prophets Birthday"
        mawlud_mapping = {2022: ((OCT, 8),)}
        if year in mawlud_mapping:
            for dt in mawlud_mapping[year]:
                self[date(year, *dt)] = mawlud
        else:
            for dt in _islamic_to_gre(year, 3, 12):
                self[dt] = f"{mawlud}* (*estimated)"

        # National Day.
        national_day = "National Day"
        self[date(year, DEC, 16)] = national_day
        self[date(year, DEC, 17)] = national_day


class BH(Bahrain):
    pass


class BAH(Bahrain):
    pass
