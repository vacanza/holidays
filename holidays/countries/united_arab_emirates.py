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

from holidays.constants import APR, MAY, JUN, JUL, AUG, SEP, NOV, DEC, FRI, SAT
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import InternationalHolidays, IslamicHolidays


class UnitedArabEmirates(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    Holidays are regulated by the Article 74
    of Federal Law No. 08 for the year 1980:
    https://www.ilo.org/dyn/natlex/docs/ELECTRONIC/11956/69376/F417089305/ARE11956.pdf
    However the law is not applied literally,
    and was amended often in the past few years.
    Sources:
    2017: https://www.khaleejtimes.com/nation/uae-official-public-holidays-list-2017   # noqa: E501
    2018: https://www.thenational.ae/uae/government/uae-public-holidays-2018-announced-by-abu-dhabi-government-1.691393  # noqa: E501
    2019: https://www.thenational.ae/uae/government/uae-public-holidays-for-2019-and-2020-announced-by-cabinet-1.833425  # noqa: E501
    2020: https://u.ae/en/information-and-services/public-holidays-and-religious-affairs/public-holidays  # noqa: E501

    Holidays based on the Islamic Calendar are estimated (and so denoted),
    as are announced each year and based on moon sightings:
    - Eid al-Fitr
    - Eid al-Adha
    - Arafat (Hajj) Day
    - Al-Hijra (Islamic New Year
    - Mawlud al-Nabi (Prophet Mohammad's Birthday)
    - Leilat al-Miraj (Ascension of the Prophet), suspended after 2018.
    """

    country = "AE"
    weekend = {FRI, SAT}

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self._add_new_years_day("New Year's Day")

        # Commemoration Day
        if year >= 2015:
            dt = (DEC, 1) if year >= 2019 else (NOV, 30)
            self._add_holiday("Commemoration Day", *dt)

        # National Day
        self._add_holiday("National Day", DEC, 2)
        self._add_holiday("National Day Holiday", DEC, 3)

        # Eid al-Fitr
        # Date is announced each year. Usually stretches along 3 or 4 days,
        # in some instances prepending/appending a day or two
        # before/after the official holiday.
        dates_obs = {
            2017: ((JUN, 25),),
            2018: ((JUN, 14),),
            2019: ((JUN, 3),),
            2020: ((MAY, 24),),
        }
        name = "Eid al-Fitr"
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self._add_holiday(name, hol_date)
                self._add_holiday(f"{name} Holiday", hol_date + td(days=+1))
                self._add_holiday(f"{name} Holiday", hol_date + td(days=+2))
        else:
            self._add_eid_al_fitr_day(f"{name}* (*estimated)")
            self._add_eid_al_fitr_day_two(f"{name}* (*estimated)")
            self._add_eid_al_fitr_day_three(f"{name}* (*estimated)")

        # Arafat Day & Eid al-Adha
        dates_obs = {  # Eid al-Adha 1st day
            2017: ((SEP, 1),),
            2018: ((AUG, 21),),
            2019: ((AUG, 11),),
            2020: ((JUL, 31),),
        }
        pre_name = "Arafat (Hajj) Day"
        name = "Eid al-Adha"
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self._add_holiday(pre_name, hol_date + td(days=-1))
                self._add_holiday(name, hol_date)
                self._add_holiday(f"{name} Holiday", hol_date + td(days=+1))
                self._add_holiday(f"{name} Holiday", hol_date + td(days=+2))
        else:
            self._add_arafah_day(f"{pre_name}* (*estimated)")
            self._add_eid_al_adha_day(f"{name}* (*estimated)")
            self._add_eid_al_adha_day_two(f"{name}* Holiday* (*estimated)")
            self._add_eid_al_adha_day_three(f"{name}* Holiday* (*estimated)")

        # Islamic New Year - (hijari_year, 1, 1)
        dates_obs = {
            2017: ((SEP, 22),),
            2018: ((SEP, 11),),
            2019: ((AUG, 31),),
            2020: ((AUG, 23),),
        }
        name = "Al Hijra - Islamic New Year"
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                self._add_holiday(name, *date_obs)
        else:
            self._add_islamic_new_year_day(f"{name}* (*estimated)")

        # Leilat al-Miraj - The Prophet's ascension (hijari_year, 7, 27)
        if year <= 2018:  # starting from 2019 the UAE government removed this
            dates_obs = {
                2017: ((APR, 23),),
                2018: ((APR, 13),),
            }
            name = "Leilat al-Miraj - The Prophet's ascension"
            if year in dates_obs:
                for date_obs in dates_obs[year]:
                    self._add_holiday(name, *date_obs)
            else:
                self._add_isra_and_miraj_day(f"{name}* (*estimated)")

        # Prophet Muhammad's Birthday - (hijari_year, 3, 12)
        if year <= 2019:  # starting from 2020 the UAE government removed this
            dates_obs = {
                2017: ((NOV, 30),),
                2018: ((NOV, 19),),
                2019: ((NOV, 9),),
            }
            name = "Mawlud al-Nabi - Prophet Mohammad's Birthday"
            if year in dates_obs:
                for date_obs in dates_obs[year]:
                    self._add_holiday(name, *date_obs)
            else:
                self._add_mawlid_day(f"{name}* (*estimated)")


class AE(UnitedArabEmirates):
    pass


class ARE(UnitedArabEmirates):
    pass
