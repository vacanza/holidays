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
    """

    country = "NP"
    # %s (estimated).
    estimated_label = "%s (estimated)"

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
        # Prithvi Jayanti.
        self._add_holiday_jan_11("Prithvi Jayanti")

        # Martyr's Day.
        self._add_holiday_jan_30("Martyr's Day")

        # National Democracy Day.
        self._add_holiday_feb_19("National Democracy Day")

        # Women's Day.
        self._add_womens_day("Women's Day")

        # Nepal New Year (Vikram Sambat).
        self._add_vaisakhi("Nepali New Year (Vikram Sambat)")

        # Labor Day.
        self._add_labor_day("Labor Day")

        # Republic Day.
        self._add_holiday_may_29("Republic Day")

        # Constitution Day.
        self._add_holiday_sep_19("Constitution Day")

        # Christmas.
        self._add_christmas_day("Christmas")

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

        # Ram Navami.
        self._add_ram_navami("Ram Navami")

        # Buddha Jayanti.
        self._add_buddha_purnima("Buddha Jayanti")

        # Ghatasthapana.
        self._add_sharad_navratri("Ghatasthapana")

        # Phulpati.
        self._add_maha_saptami("Phulpati")

        # Maha Ashtami.
        self._add_maha_ashtami("Maha Ashtami")

        # Maha Navami.
        self._add_maha_navami("Maha Navami")

        # Vijayadashami.
        self._add_dussehra("Vijayadashami")

        # Ekadashi(Dashain).
        self._add_papankusha_ekadashi("Ekadashi (Dashain)")

        # Duwadashi(Dashain).
        self._add_papankusha_duwadashi("Duwadashi (Dashain)")

        # Janai Purnima.
        self._add_raksha_bandhan("Janai Purnima")

        # Shree Krishna Janmashtami.
        self._add_janmashtami("Shree Krishna Janmashtami")

        # Lakshmi Puja.
        self._add_diwali_india("Lakshmi Puja")

        # Gai Tihar.
        self._add_gau_krida("Gai Tihar")

        # Bhai Tika.
        self._add_bhai_dooj("Bhai Tika")

        # Govardhan Puja
        self._add_govardhan_puja("Govardhan Puja")

        # Mha Puja.
        self._add_govardhan_puja("Mha Puja")

        # Tihar holiday.
        self._add_tihar_holiday("Tihar Holiday")

        # Chhath Parwa.
        self._add_chhath_puja("Chhath Parwa")

        # Islamic holidays.

        # Eid al-Fitr.
        self._add_eid_al_fitr_day("Id-ul-Fitr")

        # Eid al-Adha.
        self._add_eid_al_adha_day("Bakrid")


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


class NepalStaticHolidays:
    """Nepal Special Holidays.

    References:
       * [Death of HM King Husayn bin Talal of Jordan](https://web.archive.org/web/20170710193530/https://www.qppstudio.net/public-holidays-news/1999/nepal-declares-february-9-public-holiday-001911.htm)
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
        1999: (FEB, 9, name_day_of_national_mourning),
        2011: (MAR, 6, name_day_of_national_mourning),
        2016: (FEB, 10, name_day_of_national_mourning),
        2023: (
            (JAN, 16, name_day_of_national_mourning),
            # People War's Day.
            (FEB, 13, "People War's Day"),
            (SEP, 14, name_day_of_national_mourning),
        ),
    }
