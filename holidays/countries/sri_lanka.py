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

from holidays.calendars import (
    _CustomBuddhistHolidays,
    _CustomIslamicHolidays,
    _CustomHinduHolidays,
)
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.constants import BANK, PUBLIC
from holidays.groups import (
    InternationalHolidays,
    IslamicHolidays,
    ChristianHolidays,
    HinduCalendarHolidays,
    BuddhistCalendarHolidays,
    StaticHolidays,
)
from holidays.holiday_base import HolidayBase


class SriLanka(
    HolidayBase,
    InternationalHolidays,
    IslamicHolidays,
    ChristianHolidays,
    HinduCalendarHolidays,
    BuddhistCalendarHolidays,
    StaticHolidays,
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
        StaticHolidays.__init__(self, cls=SriLankaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Independence Day.
        self._add_holiday_feb_4(tr("ස්වාධීනත්ව දිනය"))

        if self._year >= 1949:
            # Thai Pongal.
            self._add_holiday_jan_14(tr("தைப்பொங்கல்"))

        # Deepavali.
        self._add_diwali(tr("දීපාවලී"))

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

        # Eid al-Adha.
        name = tr("ඊද් අල්-අදා")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        self._add_eid_al_adha_day_three(name)

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


class SriLankaBuddhistHolidays(_CustomBuddhistHolidays):
    VESAK_DATES = {
        2001: (MAY, 7),
        2002: (MAY, 26),
        2003: (MAY, 15),
        2004: (JUN, 2),
        2005: (MAY, 22),
        2006: (MAY, 12),
        2007: (MAY, 31),
        2008: (MAY, 19),
        2009: (MAY, 9),
        2010: (MAY, 28),
        2011: (MAY, 17),
        2012: (MAY, 5),
        2013: (MAY, 24),
        2014: (MAY, 13),
        2015: (JUN, 1),
        2016: (MAY, 21),
        2017: (MAY, 10),
        2018: (MAY, 29),
        2019: (MAY, 19),
        2020: (MAY, 7),
        2021: (MAY, 26),
        2022: (MAY, 15),
        2023: (JUN, 2),
        2024: (MAY, 22),
        2025: (MAY, 12),
    }


class SriLankaHinduHolidays(_CustomHinduHolidays):
    # Deepavali
    DIWALI_DATES = {
        2001: (NOV, 14),
        2002: (NOV, 3),
        2003: (OCT, 23),
        2004: (NOV, 11),
        2005: (NOV, 1),
        2006: (OCT, 21),
        2007: (NOV, 8),
        2008: (OCT, 27),
        2009: (NOV, 15),
        2010: (NOV, 5),
        2011: (OCT, 26),
        2012: (NOV, 13),
        2013: (NOV, 2),
        2014: (OCT, 22),
        2015: (NOV, 10),
        2016: (OCT, 29),
        2017: (OCT, 18),
        2018: (NOV, 6),
        2019: (OCT, 27),
        2020: (NOV, 14),
        2021: (NOV, 4),
        2022: (OCT, 24),
        2023: (NOV, 12),
        2024: (OCT, 31),
        2025: (OCT, 20),
    }


class SriLankaStaticHolidays:
    """
    This class contains the static holiday dates for Sri Lanka.
    """

    # Magh Puja.
    magh_puja_name = tr("මාඝ පූජා")
    # Maha Shivatri.
    maha_shivratri_name = tr("මහා ශිවාත්‍රි")
    # Nikini Poya.
    nikini_poya_name = tr("නිකිනි පොය")
    # Binara Poya.
    binara_poya_name = tr("බිනර පොය")
    # Wap Poya.
    wap_poya_name = tr("වප් පොය")
    # Il Poya.
    il_poya_name = tr("ඉල් පොය")
    # Unduwap Poya.
    unduwap_poya_name = tr("උඳුවාප් පොය")

    special_public_holidays = {
        2014: (
            (AUG, 10, nikini_poya_name),
            (OCT, 8, wap_poya_name),
        ),
        2015: (
            (AUG, 29, nikini_poya_name),
            (SEP, 28, il_poya_name),
            (OCT, 27, wap_poya_name),
        ),
        2016: (
            (AUG, 17, nikini_poya_name),
            (SEP, 16, binara_poya_name),
            (OCT, 15, wap_poya_name),
        ),
        2017: (
            (AUG, 7, nikini_poya_name),
            (SEP, 5, binara_poya_name),
            (OCT, 5, il_poya_name),
        ),
        2018: (
            (AUG, 25, nikini_poya_name),
            (SEP, 24, binara_poya_name),
            (OCT, 24, wap_poya_name),
        ),
        2019: (
            (AUG, 14, nikini_poya_name),
            (SEP, 13, binara_poya_name),
            (OCT, 13, wap_poya_name),
            (SEP, 14, il_poya_name),
        ),
        2020: (
            (AUG, 3, nikini_poya_name),
            (SEP, 1, binara_poya_name),
            (OCT, 30, wap_poya_name),
            (OCT, 1, il_poya_name),
            (DEC, 29, unduwap_poya_name),
        ),
        2021: (
            (MAR, 11, maha_shivratri_name),
            (AUG, 22, nikini_poya_name),
            (SEP, 20, binara_poya_name),
            (OCT, 20, wap_poya_name),
            (OCT, 20, il_poya_name),
            (DEC, 18, unduwap_poya_name),
        ),
        2022: (
            (FEB, 16, magh_puja_name),
            (MAR, 1, maha_shivratri_name),
            (AUG, 11, nikini_poya_name),
            (SEP, 10, binara_poya_name),
            (OCT, 9, wap_poya_name),
            (DEC, 7, unduwap_poya_name),
        ),
        2023: (
            (MAR, 6, magh_puja_name),
            (FEB, 18, maha_shivratri_name),
            (AUG, 30, nikini_poya_name),
            (SEP, 29, binara_poya_name),
            (OCT, 28, wap_poya_name),
            (NOV, 27, il_poya_name),
            (DEC, 26, unduwap_poya_name),
        ),
        2024: (
            (FEB, 24, magh_puja_name),
            (MAR, 8, maha_shivratri_name),
            (AUG, 19, nikini_poya_name),
            (SEP, 17, binara_poya_name),
            (OCT, 17, wap_poya_name),
            (NOV, 15, il_poya_name),
            (DEC, 14, unduwap_poya_name),
        ),
        2025: (
            (FEB, 12, magh_puja_name),
            (FEB, 26, maha_shivratri_name),
            (AUG, 8, nikini_poya_name),
            (SEP, 7, binara_poya_name),
            (OCT, 6, wap_poya_name),
            (NOV, 3, il_poya_name),
            (DEC, 4, unduwap_poya_name),
        ),
        2026: (
            (MAR, 3, magh_puja_name),
            (FEB, 15, maha_shivratri_name),
            (OCT, 15, il_poya_name),
            (DEC, 29, unduwap_poya_name),
        ),
        2027: (MAR, 6, maha_shivratri_name),
        2028: (FEB, 23, maha_shivratri_name),
        2029: (FEB, 11, maha_shivratri_name),
        2030: (MAR, 2, maha_shivratri_name),
    }
