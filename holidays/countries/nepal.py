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

from holidays.calendars.gregorian import JAN, FEB
from holidays.groups import ChristianHolidays, HinduCalendarHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Nepal(HolidayBase, ChristianHolidays, HinduCalendarHolidays, InternationalHolidays):
    """Nepal holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Nepal>
        * <https://www.calendarlabs.com/holidays/nepal/2025>
        * <https://www.timeanddate.com/holidays/nepal/>
    """

    country = "NP"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
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


class NP(Nepal):
    pass


class NPL(Nepal):
    pass
