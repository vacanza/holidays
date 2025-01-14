#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.constants import BANK, PUBLIC
from holidays.groups import (
    InternationalHolidays,
    IslamicHolidays,
    ChristianHolidays,
    HinduCalendarHolidays,
    BuddhistCalendarHolidays,
)
from holidays.holiday_base import HolidayBase


class SriLanka(
    HolidayBase,
    InternationalHolidays,
    IslamicHolidays,
    ChristianHolidays,
    HinduCalendarHolidays,
    BuddhistCalendarHolidays,
):
    """
    https://en.wikipedia.org/wiki/Culture_of_Sri_Lanka#List_of_holidays
    https://www.timeanddate.com/holidays/sri-lanka/
    https://factsanddetails.com/south-asia/Srilanka/People_Srilanka/entry-7978.html
    https://help.wendywutours.com.au/knowledge/public-holidays-and-festivals-sri-lanka

    """

    country = "LK"
    supported_categories = (BANK, PUBLIC)
    default_language = "si_LK"
    # %s (estimated).
    estimated_label = tr("%s (අනුමානිත)")
    supported_languages = ("en_US", "si_LK", "ta_LK")
    # Sri Lanka's regaining of full independence from British influence.
    start_year = 1948

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, SriLankaIslamicHolidays)
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self)
        BuddhistCalendarHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Independence Day.
        self._add_holiday_feb_4(tr("ස්වාධීනත්ව දිනය"))

        if self._year >= 1949:
            # Thai Pongal.
            self._add_holiday_jan_14(tr("தைப்பொங்கல்"))

        # New Year.
        self._add_new_years_day(tr("නව වසර"))

        # Deepavali.
        self._add_diwali(tr("දීපාවලී"))

        magh_dates = {
            2022: (FEB, 16),
            2023: (MAR, 6),
            2024: (FEB, 24),
            2025: (FEB, 12),
            2026: (MAR, 3),
        }

        if self._year in magh_dates:
            # Magh Puja.
            self._add_holiday(tr("මාඝ පූජා"), magh_dates[self._year])

        maha_shivratri_dates = {
            2021: (MAR, 11),
            2022: (MAR, 1),
            2023: (FEB, 18),
            2024: (MAR, 8),
            2025: (FEB, 26),
            2026: (FEB, 15),
            2027: (MAR, 6),
            2028: (FEB, 23),
            2029: (FEB, 11),
            2030: (MAR, 2),
        }

        if self._year in maha_shivratri_dates:
            # Maha Shivatri.
            self._add_holiday(tr("මහා ශිවාත්‍රි"), maha_shivratri_dates[self._year])

        # Day before Sinhala and Tamil New Year.
        self._add_holiday_apr_13(tr("සිංහල හා දෙමළ අලුත් අවුරුද්දට පෙර දිනය"))

        # Sinhala and Tamil New Year.
        self._add_holiday_apr_14(tr("සිංහල සහ දෙමළ නව වසර"))

        # Vesak Poya.
        self._add_vesak_may(tr("වෙසක් පොහොය"))

        # Poson Poya.
        self._add_holiday_jun_1(tr("පොසොන් පොහොය"))

        # Esala Poya.
        self._add_holiday_jul_1(tr("එසාල පොය"))

        # Duruthu Poya.
        self._add_holiday_jan_1(tr("දුරුතු පොය"))

        nikini_poya_dates = {
            2014: (AUG, 10),
            2015: (AUG, 29),
            2016: (AUG, 17),
            2017: (AUG, 7),
            2018: (AUG, 25),
            2019: (AUG, 14),
            2020: (AUG, 3),
            2021: (AUG, 22),
            2022: (AUG, 11),
            2023: (AUG, 30),
            2024: (AUG, 19),
            2025: (AUG, 8),
        }

        if self._year in nikini_poya_dates:
            # Nikini Poya.
            self._add_holiday(tr("නිකිනි පොය"), nikini_poya_dates[self._year])

        binara_poya_dates = {
            2016: (SEP, 16),
            2017: (SEP, 5),
            2018: (SEP, 24),
            2019: (SEP, 13),
            2020: (SEP, 1),
            2021: (SEP, 20),
            2022: (SEP, 10),
            2023: (SEP, 29),
            2024: (SEP, 17),
            2025: (SEP, 7),
        }

        if self._year in binara_poya_dates:
            # Binara Poya.
            self._add_holiday(tr("බිනර පොය"), binara_poya_dates[self._year])

        # Christmas.
        self._add_christmas_day(tr("ක්‍රිස්මස්"))

        #  The Prophet's Birthday.
        self._add_mawlid_day(tr("නබිගේ උපන් දිනය"))

        # Good Friday
        self._add_good_friday(tr("හොඳ සිකුරාදා"))

        # Eid al-Fitr.
        name = tr("ඊද් අල්-ෆිතර්")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)

        wap_poya_dates = {
            2014: (OCT, 8),
            2015: (OCT, 27),
            2016: (OCT, 15),
            2017: (OCT, 5),
            2018: (OCT, 24),
            2019: (OCT, 13),
            2020: (OCT, 30),
            2021: (OCT, 20),
            2022: (OCT, 9),
            2023: (OCT, 28),
            2024: (OCT, 17),
            2025: (OCT, 6),
        }
        if self._year in wap_poya_dates:
            # Wap Poya.
            self._add_holiday(tr("වප් පොය"), wap_poya_dates[self._year])

        # Eid al-Adha.
        name = tr("ඊද් අල්-අදා")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        self._add_eid_al_adha_day_three(name)

        il_poya_dates = {
            2015: (SEP, 28),
            2016: (OCT, 15),
            2017: (OCT, 5),
            2018: (SEP, 24),
            2019: (SEP, 14),
            2020: (OCT, 1),
            2021: (OCT, 20),
            2022: (OCT, 9),
            2023: (NOV, 27),
            2024: (NOV, 15),
            2025: (NOV, 3),
        }
        if self._year in il_poya_dates:
            # Il Poya.
            self._add_holiday(tr("ඉල් පොය"), il_poya_dates[self._year])

        unduwap_poya_dates = {
            2020: (DEC, 29),
            2021: (DEC, 18),
            2022: (DEC, 7),
            2023: (DEC, 26),
            2024: (DEC, 14),
            2025: (DEC, 4),
        }
        if self._year in unduwap_poya_dates:
            # Unduwap Poya.
            self._add_holiday(tr("උඳුවාප් පොය"), unduwap_poya_dates[self._year])

    def _populate_bank_holidays(self):
        # Bank Holidays
        self._add_holiday_jun_30(tr("බැංකු නිවාඩු"))

        # New Year's Eve
        self._add_new_years_eve(tr("අලුත් අවුරුදු උදාව"))

        if self._year >= 1956:
            # Labor Day
            self._add_labor_day(tr("කම්කරු දිනය"))


class LK(SriLanka):
    pass


class LKA(SriLanka):
    pass


class SriLankaIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2014: (OCT, 5),
        2015: (SEP, 23),
        2016: (SEP, 13),
        2017: (SEP, 2),
        2018: (AUG, 22),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 17),
    }

    EID_AL_FITR_DATES = {
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 4),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 1),
        2023: (APR, 22),
        2024: (APR, 10),
    }

    MAWLID_DATES = {
        2014: (JAN, 14),
        2015: ((JAN, 3), (DEC, 24)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 21),
        2019: (NOV, 10),
        2020: (OCT, 29),
        2021: (OCT, 19),
        2022: (OCT, 8),
        2023: (SEP, 27),
        2024: (SEP, 16),
    }
