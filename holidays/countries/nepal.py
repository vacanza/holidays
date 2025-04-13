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
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV
from holidays.constants import PUBLIC, WORKDAY
from holidays.groups import (
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.holiday_base import HolidayBase


class Nepal(
    HolidayBase,
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
):
    """Nepal holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Nepal>
        * <https://narayanilawfirm.org.np/list-of-public-holidays-in-nepal-2079/>
        * <https://www.timeanddate.com/holidays/nepal/>
        * <https://kathmandupost.com/national/2018/03/29/government-trims-public-holidays-by-22-days>
        * <https://kathmandupost.com/national/2021/02/13/two-years-after-shortening-public-holiday-list-government-starts-adding-to-it-again>
        * <https://english.hamropatro.com/nepali-public-holidays>
        * <https://www.ashesh.com.np/nepali-calendar/ >
    """

    country = "NP"
    supported_categories = (PUBLIC, WORKDAY)
    # %s (estimated).
    estimated_label = "%s (estimated)"
    start_year = 2010

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=NepalIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, cls=NepalStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # https://www.bolpatra.gov.np/egp/openDateConverter
        martyrs_day_dates = {
            2010: (JAN, 30),
            2011: (JAN, 30),
            2012: (JAN, 30),
            2013: (JAN, 29),
            2014: (JAN, 30),
            2015: (JAN, 30),
            2016: (JAN, 30),
            2017: (JAN, 29),
            2018: (JAN, 30),
            2021: (JAN, 29),
            2022: (JAN, 30),
            2023: (JAN, 30),
            2024: (JAN, 30),
            2025: (JAN, 29),
            2026: (JAN, 29),
            2027: (JAN, 29),
            2028: (JAN, 29),
            2029: (JAN, 29),
            2030: (JAN, 29),
            2031: (JAN, 30),
            2032: (JAN, 30),
            2033: (JAN, 29),
        }
        if self._year >= 2023:
            # Prithvi Jayanti.
            self._add_holiday_jan_11("Prithvi Jayanti")

        # Women's Day.
        self._add_womens_day("Women's Day")

        # Nepal New Year.
        self._add_vaisakhi("Nepali New Year")

        # Labor Day.
        self._add_labor_day("Labor Day")

        # Constitution Day.
        self._add_holiday_sep_19("Constitution Day")

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

        # Tamu Losar.
        self._add_holiday_dec_30("Tamu Losar")

        # Hindu holidays.

        # Maghe Sankranti.
        self._add_makar_sankranti("Maghe Sankranti")

        # Sonam Losar.
        self._add_sonam_losar("Sonam Losar")

        # Gyalpo Losar.
        self._add_gyalpo_losar("Gyalpo Losar")

        # Maha Shivaratri.
        self._add_maha_shivaratri("Maha Shivaratri")

        # Holi (Mountain & Hilly).
        self._add_nepal_holi("Holi (Mountain & Hilly)")

        # Holi (Terai).
        self._add_holi("Holi (Terai)")

        # Buddha Jayanti.
        self._add_buddha_purnima("Buddha Jayanti")

        # Phulpati.
        self._add_maha_saptami("Phulpati")

        # Maha Ashtami.
        self._add_maha_ashtami("Maha Ashtami")

        # Maha Navami.
        self._add_maha_navami("Maha Navami")

        # Vijayadashami.
        self._add_dussehra("Vijayadashami")

        # Ekadashi (Dashain).
        self._add_papankusha_ekadashi("Ekadashi (Dashain)")

        # Lakshmi Puja.
        self._add_diwali_india("Lakshmi Puja")

        # Gai Tihar.
        self._add_gau_krida("Gai Tihar")

        # Govardhan Puja.
        self._add_govardhan_puja("Govardhan Puja")

        # Mha Puja.
        self._add_govardhan_puja("Mha Puja")

        # Bhai Tika.
        self._add_bhai_dooj("Bhai Tika")

        # Tihar Holiday.
        self._add_tihar_holiday("Tihar Holiday")

        # Chhath Parwa.
        self._add_chhath_puja("Chhath Parwa")

        # Islamic holidays.

        # Eid al-Fitr.
        self._add_eid_al_fitr_day("Id-ul-Fitr")

        # Eid al-Adha.
        self._add_eid_al_adha_day("Bakrid")

        # Removed by MoHA between 2019-2020.

        if self._year not in {2019, 2020}:
            if self._year in martyrs_day_dates:
                # Martyr's Day.
                self._add_holiday("Martyr's Day", martyrs_day_dates[self._year])

            # National Democracy Day.
            self._add_holiday_feb_19("National Democracy Day")

            # Republic Day.
            self._add_holiday_may_29("Republic Day")

            # Hindu Holidays.

            # Ram Navami.
            self._add_ram_navami("Ram Navami")

            # Janai Purnima.
            self._add_raksha_bandhan("Janai Purnima")

            # Shree Krishna Janmashtami.
            self._add_janmashtami("Shree Krishna Janmashtami")

            # Ghatasthapana.
            self._add_sharad_navratri("Ghatasthapana")

            # Duwadashi (Dashain).
            self._add_papankusha_duwadashi("Duwadashi (Dashain)")

    def _populate_workday_holidays(self):
        # https://www.bolpatra.gov.np/egp/openDateConverter
        martyrs_day_dates = {
            2019: (JAN, 30),
            2020: (JAN, 30),
        }

        if 2019 <= self._year <= 2020:
            # Prithvi Jayanti.
            self._add_holiday_jan_11("Prithvi Jayanti")

            if self._year in martyrs_day_dates:  # pragma: no cover
                # Martyr's Day.
                self._add_holiday("Martyr's Day", martyrs_day_dates[self._year])

            # National Democracy Day.
            self._add_holiday_feb_19("National Democracy Day")

            # Republic Day.
            self._add_holiday_may_29("Republic Day")

            # Hindu holidays.

            # Ram Navami.
            self._add_ram_navami("Ram Navami")

            # Janai Purnima.
            self._add_raksha_bandhan("Janai Purnima")

            # Shree Krishna Janmashtami.
            self._add_janmashtami("Shree Krishna Janmashtami")

            # Ghatasthapana.
            self._add_sharad_navratri("Ghatasthapana")

            # Duwadashi (Dashain).
            self._add_papankusha_duwadashi("Duwadashi (Dashain)")


class NepalIslamicHolidays(_CustomIslamicHolidays):
    # Bakrid / Eid-al-Adha.
    EID_AL_ADHA_DATES = {
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


class NepalStaticHolidays:
    """Nepal special holidays.

    References:
        * [Death of Krishna Prasad Bhattarai](https://myrepublica.nagariknetwork.com/news/27618/)
        * [Death of Sushil Koirala](https://kathmandupost.com/miscellaneous/2016/02/09/cabinet-decision-koirala-to-be-honoured-with-state-funeral)
        * [Crash of Yeti Airlines Flight 691](https://edition.cnn.com/2023/01/15/asia/nepal-yeti-airlines-crash-intl-hnk/index.html)
        * [People's War Day Instituted](https://kathmandupost.com/national/2023/02/12/government-announces-public-holiday-on-monday-to-mark-people-s-war-day)
        * [People's War Day Annulled](https://kathmandupost.com/national/2023/12/29/supreme-court-annuls-public-holiday-on-people-s-war-day)
        * [Death of Subas Chandra Nembang](https://en.nepalkhabar.com/news/detail/6023/)
    """

    # Day of National Mourning.
    name_day_of_national_mourning = "Day of National Mourning"

    special_public_holidays = {
        2011: (MAR, 6, name_day_of_national_mourning),
        2016: (FEB, 10, name_day_of_national_mourning),
        2023: (
            (JAN, 16, name_day_of_national_mourning),
            # People War's Day.
            (FEB, 13, "People War's Day"),
            (SEP, 14, name_day_of_national_mourning),
        ),
    }
