#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from holidays.calendars import _CustomIslamicHolidays, _CustomHinduHolidays
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
        * <https://english.hamropatro.com/calendar>
        * <https://www.ashesh.com.np/nepali-calendar/>
        * <https://www.bolpatra.gov.np/egp/openDateConverter>
        * <https://www.moha.gov.np/en/page/holidays>
    """

    country = "NP"
    # %s (estimated).
    estimated_label = "%s (estimated)"
    start_year = 2010
    supported_categories = (PUBLIC, WORKDAY)

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self, cls=NepalHinduHolidays)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=NepalIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, cls=NepalStaticHolidays)
        super().__init__(*args, **kwargs)

    def _add_non_continuous_holidays(self, is_workday: bool = False):
        """Holidays removed by MoHA between 2019-2020."""
        if (2019 <= self._year <= 2020) == is_workday:
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
                2019: (JAN, 30),
                2020: (JAN, 30),
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
            if self._year in martyrs_day_dates:
                # Martyr's Day.
                self._add_holiday("Martyr's Day", martyrs_day_dates[self._year])

            democracy_day_dates = {
                2010: (FEB, 19),
                2011: (FEB, 19),
                2012: (FEB, 19),
                2013: (FEB, 18),
                2014: (FEB, 19),
                2015: (FEB, 19),
                2016: (FEB, 19),
                2017: (FEB, 18),
                2018: (FEB, 19),
                2019: (FEB, 19),
                2020: (FEB, 19),
                2021: (FEB, 19),
                2022: (FEB, 19),
                2023: (FEB, 19),
                2024: (FEB, 19),
                2025: (FEB, 19),
                2026: (FEB, 19),
                2027: (FEB, 19),
                2028: (FEB, 19),
                2029: (FEB, 19),
                2030: (FEB, 19),
                2031: (FEB, 20),
                2032: (FEB, 20),
                2033: (FEB, 19),
            }
            if self._year in democracy_day_dates:
                # National Democracy Day.
                self._add_holiday("National Democracy Day", democracy_day_dates[self._year])

            republic_day_dates = {
                2010: (MAY, 29),
                2011: (MAY, 29),
                2012: (MAY, 28),
                2013: (MAY, 29),
                2014: (MAY, 29),
                2015: (MAY, 29),
                2016: (MAY, 28),
                2017: (MAY, 29),
                2018: (MAY, 29),
                2019: (MAY, 29),
                2020: (MAY, 28),
                2021: (MAY, 29),
                2022: (MAY, 29),
                2023: (MAY, 29),
                2024: (MAY, 28),
                2025: (MAY, 28),
                2026: (MAY, 29),
                2027: (MAY, 29),
                2028: (MAY, 28),
                2029: (MAY, 28),
                2030: (MAY, 29),
                2031: (MAY, 29),
                2032: (MAY, 28),
            }
            if self._year in republic_day_dates:
                # Established in 2009.
                # Republic Day.
                self._add_holiday("Republic Day", republic_day_dates[self._year])

            # Hindu Holidays.

            # Ram Navami.
            self._add_ram_navami("Ram Navami")

            # Janai Poornima.
            self._add_raksha_bandhan("Janai Poornima")

            # Shree Krishna Janmashtami.
            self._add_janmashtami("Shree Krishna Janmashtami")

            # Ghatasthapana.
            self._add_sharad_navratri("Ghatasthapana")

            # Duwadashi (Dashain).
            self._add_papankusha_duwadashi("Duwadashi (Dashain)")

    def _populate_public_holidays(self):
        if self._year >= 2023:
            # Prithvi Jayanti.
            self._add_holiday_jan_11("Prithvi Jayanti")

        # International Women's Day.
        self._add_womens_day("International Women's Day")

        # Nepal New Year.
        self._add_vaisakhi("Nepali New Year")

        # International Labour Day.
        self._add_labor_day("International Labour Day")

        constitution_day_dates = {
            2016: (SEP, 19),
            2017: (SEP, 19),
            2018: (SEP, 19),
            2019: (SEP, 20),
            2020: (SEP, 19),
            2021: (SEP, 19),
            2022: (SEP, 19),
            2023: (SEP, 20),
            2024: (SEP, 19),
            2025: (SEP, 19),
            2026: (SEP, 19),
            2027: (SEP, 19),
            2028: (SEP, 18),
            2029: (SEP, 19),
            2030: (SEP, 19),
            2031: (SEP, 19),
            2032: (SEP, 19),
        }
        if self._year in constitution_day_dates:
            # Constitution Day.
            self._add_holiday("Constitution Day", constitution_day_dates[self._year])

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

        # Hindu holidays.

        # Maghe Sankranti.
        self._add_makar_sankranti("Maghe Sankranti")

        # Sonam Lhochhar.
        self._add_sonam_losar("Sonam Lhochhar")

        # Maha Shivaratri.
        self._add_maha_shivaratri("Maha Shivaratri")

        # Gyalpo Lhosar.
        self._add_gyalpo_losar("Gyalpo Lhosar")

        # Fagu Poornima.
        self._add_nepal_holi("Fagu Poornima")

        # Fagu Poornima (Terai).
        self._add_holi("Fagu Poornima (Terai)")

        # Buddha Jayanti.
        self._add_buddha_purnima("Buddha Jayanti")

        # Fulpati.
        self._add_maha_saptami("Fulpati")

        # Maha Ashtami.
        self._add_maha_ashtami("Maha Ashtami")

        # Maha Navami.
        self._add_maha_navami("Maha Navami")

        # Bijaya Dashami.
        self._add_dussehra("Bijaya Dashami")

        # Ekadashi (Dashain).
        self._add_papankusha_ekadashi("Ekadashi (Dashain)")

        # Laxmi Pooja.
        self._add_diwali_india("Laxmi Pooja")

        # Gai Tihar.
        self._add_gau_krida("Gai Tihar")

        # Gobardhan Pooja.
        self._add_govardhan_puja("Gobardhan Pooja")

        # Mha Pooja.
        self._add_govardhan_puja("Mha Pooja")

        # Bhai Tika.
        self._add_bhai_dooj("Bhai Tika")

        # Chhath Parva.
        self._add_chhath_puja("Chhath Parva")

        # Tamu Lhochhar.
        self._add_tamu_losar("Tamu Lhochhar")

        # Islamic holidays.

        # Eid al-Fitr.
        self._add_eid_al_fitr_day("Id-ul-Fitr")

        # Eid al-Adha.
        self._add_eid_al_adha_day("Bakrid")

        # Removed by MoHA between 2019-2020.
        self._add_non_continuous_holidays()

    def _populate_workday_holidays(self):
        self._add_non_continuous_holidays(is_workday=True)


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


class NepalHinduHolidays(_CustomHinduHolidays):
    # Maghe Sankranti.
    MAKAR_SANKRANTI_DATES = {
        2022: (JAN, 15),
        2023: (JAN, 15),
        2024: (JAN, 15),
        2026: (JAN, 15),
    }

    # Fagu Poornima (Terai).
    HOLI_DATES = {
        2023: (MAR, 7),
        2026: (MAR, 3),
    }

    # Ram Navami.
    RAM_NAVAMI_DATES = {
        2026: (MAR, 27),
    }

    # Nepal New Year.
    VAISAKHI_DATES = {
        2025: (APR, 14),
    }

    # Janai Punima.
    RAKSHA_BANDHAN_DATES = {
        2022: (AUG, 12),
        2023: (AUG, 31),
    }

    # Shree Krishna Janmashtami.
    JANMASHTAMI_DATES = {
        2023: (SEP, 6),
    }

    # Maha Ashtami.
    MAHA_ASHTAMI_DATES = {
        2020: (OCT, 24),
    }

    # Maha Navami.
    MAHA_NAVAMI_DATES = {
        2020: (OCT, 25),
    }

    # Bijaya Dashami.
    DUSSEHRA_DATES = {
        2020: (OCT, 26),
    }

    # Gobardhan Pooja.
    GOVARDHAN_PUJA_DATES = {
        2020: (NOV, 16),
        2022: (OCT, 26),
        2023: (NOV, 14),
    }

    # Chhath Parva.
    CHHATH_PUJA_DATES = {
        2025: (OCT, 27),
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

    # Tihar Holiday.
    name_tihar_holiday = "Tihar Holiday"

    special_public_holidays = {
        2011: (MAR, 6, name_day_of_national_mourning),
        2016: (FEB, 10, name_day_of_national_mourning),
        2021: (NOV, 7, name_tihar_holiday),
        2022: (OCT, 28, name_tihar_holiday),
        2023: (
            (JAN, 16, name_day_of_national_mourning),
            # People War's Day.
            (FEB, 13, "People War's Day"),
            (SEP, 14, name_day_of_national_mourning),
            (NOV, 16, name_tihar_holiday),
        ),
        2024: (NOV, 4, name_tihar_holiday),
        2025: (OCT, 24, name_tihar_holiday),
    }
