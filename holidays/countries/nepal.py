#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import (
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
)
from holidays.holiday_base import HolidayBase


class Nepal(
    HolidayBase, ChristianHolidays, HinduCalendarHolidays, InternationalHolidays, IslamicHolidays
):
    """Nepal holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Nepal>
        * <https://narayanilawfirm.org.np/list-of-public-holidays-in-nepal-2079/>
        * <https://www.timeanddate.com/holidays/nepal/>
    """

    country = "NP"

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=NepalIslamicHolidays, show_estimated=islamic_show_estimated
        )
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # https://www.timeanddate.com/holidays/nepal/gyalpo-losar
        gyalpo_losar_dates = {
            2016: (MAR, 9),
            2017: (FEB, 27),
            2018: (FEB, 16),
            2019: (MAR, 7),
            2020: (FEB, 24),
            2021: (MAR, 14),
            2022: (MAR, 3),
            2023: (FEB, 21),
            2024: (MAR, 11),
            2025: (FEB, 28),
            2026: (FEB, 18),
            2027: (FEB, 7),
            2028: (FEB, 26),
            2029: (FEB, 14),
            2030: (MAR, 5),
            2031: (FEB, 22),
            2032: (FEB, 12),
            2033: (MAR, 2),
            2034: (FEB, 19),
            2035: (FEB, 9),
        }

        # https://www.timeanddate.com/holidays/nepal/sonam-losar
        sonam_losar_dates = {
            2016: (FEB, 9),
            2017: (JAN, 28),
            2018: (JAN, 18),
            2019: (FEB, 5),
            2020: (JAN, 25),
            2021: (FEB, 12),
            2022: (FEB, 2),
            2023: (JAN, 22),
            2024: (FEB, 10),
            2025: (JAN, 30),
            2026: (JAN, 19),
            2027: (FEB, 7),
            2028: (FEB, 26),
            2029: (JAN, 15),
            2030: (FEB, 3),
            2031: (JAN, 24),
            2032: (FEB, 12),
            2033: (JAN, 31),
            2034: (JAN, 21),
            2035: (FEB, 9),
        }

        # Prithvi Jayanti.
        self._add_holiday_jan_11("Prithvi Jayanti")

        # Martyr's Day.
        self._add_holiday_jan_30("Martyr's Day")

        # National Democracy Day.
        self._add_holiday_feb_19("National Democracy Day")

        # Republic Day.
        self._add_holiday_may_29("Republic Day")

        # Constitution Day.
        self._add_holiday_sep_19("Constitution Day")

        # Tamu Losar.
        self._add_holiday_dec_30("Tamu Losar")

        if self._year in gyalpo_losar_dates:
            # Gyalpo Losar.
            self._add_holiday("Gyalpo Losar", gyalpo_losar_dates[self._year])

        # Labor Day.
        self._add_labor_day("Labor Day")

        # Nepal New Year (Vikram Sambat).
        self._add_vaisakhi("Nepali New Year (Vikram Sambat)")

        if self._year in sonam_losar_dates:
            # Sonam Losar.
            self._add_holiday("Sonam Losar", sonam_losar_dates[self._year])

        # Women's Day.
        self._add_womens_day("Women's Day")

        # Christian holidays.

        # Christmas.
        self._add_christmas_day("Christmas")

        # Hindu holidays.

        # Bhai Tika.
        self._add_bhai_dooj("Bhai Tika")

        # Buddha Jayanti.
        self._add_buddha_purnima("Buddha Jayanti")

        # Chhath Parwa.
        self._add_chhath_puja("Chhath Parwa")

        # Duwadashi(Dashain).
        self._add_papankusha_duwadashi("Duwadashi(Dashain)")

        # Ekadashi(Dashain).
        self._add_papankusha_ekadashi("Ekadashi(Dashain)")

        # Gai Tihar.
        self._add_gau_krida("Gai Tihar")

        # Ghatasthapana.
        self._add_sharad_navratri("Ghatasthapana")

        # Govardhan Puja
        self._add_govardhan_puja("Govardhan Puja")

        # Holi(Mountain & Hilly)
        self._add_nepal_holi("Holi(Mountain & Hilly)")

        # Holi(Terai)
        self._add_holi("Holi(Terai)")

        # Janai Purnima.
        self._add_raksha_bandhan("Janai Purnima")

        # Krishna Janmashtami.
        self._add_janmashtami("Krishna Janmashtami")

        # Lakshmi Puja.
        self._add_diwali_india("Lakshmi Puja")

        # Maghe Sankranti.
        self._add_makar_sankranti("Maghe Sankranti")

        # Maha Ashtami.
        self._add_maha_ashtami("Maha Ashtami")

        # Maha Navami.
        self._add_maha_navami("Maha Navami")

        # Maha Shivaratri.
        self._add_maha_shivaratri("Maha Shivaratri")

        # Mha Puja.
        self._add_govardhan_puja("Mha Puja")

        # Phulpati.
        self._add_maha_saptami("Phulpati")

        # Ram Navami.
        self._add_ram_navami("Ram Navami")

        # Tihar holiday.
        self._add_tihar_holiday("Tihar Holiday")

        # Vijayadashami.
        self._add_dussehra("Vijayadashami")

        # Islamic holidays.

        # Eid al-Adha.
        self._add_eid_al_adha_day("Bakrid")

        # Eid al-Fitr.
        self._add_eid_al_fitr_day("Id-ul-Fitr")


class NepalIslamicHolidays(_CustomIslamicHolidays):
    # Bakrid / Eid-al-Adha.
    EID_AL_ADHA_DATES = {
        2001: (MAR, 6),
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 2),
        2005: (JAN, 21),
        2006: ((JAN, 11), (DEC, 31)),
        2007: (DEC, 20),
        2008: (DEC, 9),
        2009: (NOV, 28),
        2010: (NOV, 17),
        2011: (NOV, 7),
        2012: (OCT, 27),
        2013: (OCT, 16),
        2014: (OCT, 6),
        2015: (SEP, 25),
        2016: (SEP, 13),
        2017: (SEP, 2),
        2018: (AUG, 22),
        2019: (AUG, 12),
        2020: (AUG, 1),
        2021: (JUL, 21),
        2022: (JUL, 10),
        2023: (JUN, 29),
        2024: (JUN, 17),
        2025: (JUN, 7),
    }

    # Id-ul-Fitr / Eid-al-Fitr.
    EID_AL_FITR_DATES = {
        2001: (DEC, 17),
        2002: (DEC, 6),
        2003: (NOV, 26),
        2004: (NOV, 14),
        2005: (NOV, 3),
        2006: (OCT, 24),
        2007: (OCT, 13),
        2008: (OCT, 2),
        2009: (SEP, 21),
        2010: (SEP, 10),
        2011: (AUG, 31),
        2012: (AUG, 20),
        2013: (AUG, 8),
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
        2018: (JUN, 16),
        2019: (JUN, 5),
        2020: (MAY, 25),
        2021: (MAY, 14),
        2022: (MAY, 3),
        2023: (APR, 22),
        2024: (APR, 11),
        2025: (MAR, 31),
    }


class NP(Nepal):
    pass


class NPL(Nepal):
    pass
