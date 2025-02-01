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

from holidays.calendars import _CustomHinduHolidays, _CustomIslamicHolidays
from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
    _timedelta,
)
from holidays.constants import BANK, GOVERNMENT, PUBLIC, WORKDAY
from holidays.groups import (
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
    SinhalaCalendarHolidays,
    StaticHolidays,
)
from holidays.holiday_base import HolidayBase


class SriLanka(
    HolidayBase,
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
    SinhalaCalendarHolidays,
    StaticHolidays,
):
    """
    References:
    - http://www.commonlii.org/lk/legis/num_act/ha29o1971152/  # No. 29 of 1971 (Holidays Act)
    - http://www.commonlii.org/lk/legis/num_act/ha21o1991232/  # No. 21 of 1991 (Amendment)
    - https://web.archive.org/web/20110722150724/http://www.pubad.gov.lk/Holidays/holidays%202003.htm
    - https://web.archive.org/web/20111018053717/http://www.pubad.gov.lk/Holidays/Public%20&%20Bank%20Holidays%202004.pdf
    - https://web.archive.org/web/20241120204015/https://documents.gov.lk/en/calendar.php

    Cross-Checked With:
    - https://web.archive.org/web/20111018053927/http://www.pubad.gov.lk/Holidays/Public%20&%20Bank%20Holidays%202005.pdf
    - https://web.archive.org/web/20111018061003/http://www.pubad.gov.lk/Holidays/Public%20&%20Bank%20Holidays%202006.pdf
    - https://web.archive.org/web/20110722150032/http://www.pubad.gov.lk/Holidays/Public%20&%20Bank%20Holidays%202007.pdf
    - https://web.archive.org/web/20111018071837/http://www.pubad.gov.lk/Holidays/PublicBankHolidays2008.pdf
    - https://web.archive.org/web/20120309065711/http://www.pubad.gov.lk/Holidays/Public&BankHolidays2009.pdf
    - https://web.archive.org/web/20111018071247/http://www.pubad.gov.lk/Holidays/Public&BankHolidays2010.pdf
    - https://web.archive.org/web/20110722151043/http://www.pubad.gov.lk/Holidays/Public&BankHolidays2011.pdf
    - https://web.archive.org/web/20111125074237/http://www.pubad.gov.lk/Holidays/Public&BankHolidays2012.pdf
    - https://www.cbsl.gov.lk/en/about/about-the-bank/bank-holidays-2019
    - https://www.cbsl.gov.lk/en/about/about-the-bank/bank-holidays-2020
    - https://www.cbsl.gov.lk/en/about/about-the-bank/bank-holidays-2021
    - https://www.cbsl.gov.lk/en/about/about-the-bank/bank-holidays-2022
    - https://www.cbsl.gov.lk/en/about/about-the-bank/bank-holidays-2023
    - https://www.cbsl.gov.lk/en/about/about-the-bank/bank-holidays-2024
    - https://www.cbsl.gov.lk/en/about/about-the-bank/bank-holidays-2025
    """

    country = "LK"
    supported_categories = (BANK, GOVERNMENT, PUBLIC, WORKDAY)
    default_language = "si_LK"
    # %s (estimated).
    estimated_label = tr("%s (අනුමානිත)")
    supported_languages = ("en_US", "si_LK", "ta_LK")
    # Sri Lanka's Holidays Act (No. 29 of 1971) was first proclaimed on SEP 2nd, 1971
    # but the earliest citable calendar online is from 2003.
    # As there's no source for future Poya dates, end year is capped at 2025.
    start_year = 1972
    end_year = 2025

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self, SriLankaHinduHolidays)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, SriLankaIslamicHolidays)
        SinhalaCalendarHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=SriLankaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Non-Sectarian Holidays.

        # Tamil Thai Pongal Day.
        name = tr("දෙමළ තෛපොංැලල් දිනය")
        thai_pongal_years_jan_14 = {
            2005,
            2006,
            2009,
            2010,
            2013,
            2014,
            2017,
            2018,
            2021,
            2022,
            2025,
        }
        if self._year in thai_pongal_years_jan_14:
            self._add_holiday_jan_14(name)
        else:
            self._add_holiday_jan_15(name)

        # Independence Day.
        self._add_holiday_feb_4(tr("නිදහස් සමරු දිනය"))

        # Sinhala and Tamil New Year.
        name = tr("සිංහල හා දෙමළ අලුත් අවුරුදු දිනය")
        aluth_avurudda_years_apr_13 = {
            2004,
            2008,
            2012,
            # 2016 is on APR, 14.
            2020,
            2024,
        }
        if self._year in aluth_avurudda_years_apr_13:
            dt = self._add_holiday_apr_13(name)
        else:
            dt = self._add_holiday_apr_14(name)
        # Day Before Sinhala and Tamil New Year.
        self._add_holiday(tr("සිංහල හා දෙමළ අලුත් අවුරුදු දිනට පෙර දිනය"), _timedelta(dt, -1))

        # International Workers' Day.
        self._add_labor_day(tr("ලොක කම්කරු දිනය"))

        # Hindu Holidays.

        maha_sivarathri_dates = {
            # The one used in Sri Lanka isn't an exact match with India, used with caution.
            2003: (MAR, 1),
            2004: (FEB, 18),
            2005: (MAR, 8),
            2006: (FEB, 26),
            2007: (FEB, 16),
            2008: (MAR, 6),
            2009: (FEB, 23),
            2010: (MAR, 13),
            2011: (MAR, 2),
            2012: (FEB, 20),
            2013: (MAR, 10),
            2014: (FEB, 27),
            2015: (FEB, 17),
            2016: (MAR, 7),
            2017: (FEB, 24),
            2018: (FEB, 13),
            2019: (MAR, 4),
            2020: (FEB, 21),
            2021: (MAR, 11),
            2022: (MAR, 1),
            2023: (FEB, 18),
            2024: (MAR, 8),
            2025: (FEB, 26),
        }
        maha_sivarathri_date = maha_sivarathri_dates.get(self._year)
        if maha_sivarathri_date:
            # Maha Sivarathri Day.
            self._add_holiday(tr("මහ සිවරාත්රි දිනය"), maha_sivarathri_date)

        # Deepavali was a working day in 2003.
        if self._year >= 2004:
            # Deepavali Festival Day.
            self._add_diwali(tr("දීපවාලි උත්සව දිනය"))

        # Christian Holidays.

        # Good Friday.
        self._add_good_friday(tr("මහ සිකුරාදා දිනය"))

        # Christmas Day.
        self._add_christmas_day(tr("නත්තල් උත්සව දිනය"))

        # Poya Holidays.
        # All Adhi Poya Holidays will instead be added in StaticHolidays.

        # Duruthu Full Moon Poya Day.
        self._add_duruthu_poya(tr("දුරුතු පුර පසළොස්වක පෝය දිනය"))

        # Nawam Full Moon Poya Day.
        self._add_nawam_poya(tr("නවම් පුර පසළොස්වක පෝය දිනය"))

        # Medin Full Moon Poya Day.
        self._add_medin_poya(tr("මැදින් පුර පසළොස්වක පෝය දිනය"))

        # Bak Full Moon Poya Day.
        self._add_bak_poya(tr("බක් පුර පසළොස්වක පෝය දිනය"))

        # Vesak Full Moon Poya Day.
        dt = self._add_vesak_poya(tr("වෙසක් පුර පසළොස්වක පෝය දිනය"))

        if self._year >= 2003:
            # Day Following Vesak Full Moon Poya Day.
            self._add_holiday(tr("වෙසක් පුර පසළොස්වක පෝය දිනට පසු දිනය"), _timedelta(dt, +1))

        # Poson Full Moon Poya Day.
        self._add_poson_poya(tr("පොසොන් පුර පසළොස්වක පෝය දිනය"))

        # Esala Full Moon Poya Day.
        self._add_esala_poya(tr("ඇසල පුර පසළොස්වක පෝය දිනය"))

        # Nikini Full Moon Poya Day.
        self._add_nikini_poya(tr("නිකිණි පුර පසළොස්වක පෝය දිනය"))

        # Binara Full Moon Poya Day.
        self._add_binara_poya(tr("බිනර පුර පසළොස්වක පෝය දිනය"))

        # Vap Full Moon Poya Day.
        self._add_vap_poya(tr("වප් පුර පසළොස්වක පෝය දිනය"))

        # Il Full Moon Poya Day.
        self._add_il_poya(tr("ඉල් පුර පසළොස්වක පෝය දිනය"))

        # Unduvap Full Moon Poya Day.
        self._add_unduvap_poya(tr("උඳුවප් පුර පසළොස්වක පෝය දිනය"))

        # Islamic Holidays.

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("ඊදුල් ෆීතර්"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("ඊදුල් අල්හා"))

        #  The Prophet's Birthday.
        self._add_mawlid_day(tr("නබි නායකතුමාගේ උපන් දිනය"))


class LK(SriLanka):
    pass


class LKA(SriLanka):
    pass


class SriLankaHinduHolidays(_CustomHinduHolidays):
    DIWALI_DATES = {
        2003: (OCT, 24),
        2004: (NOV, 11),
        2005: (NOV, 1),
        2006: (OCT, 21),
        2007: (NOV, 8),
        2008: (OCT, 27),
        2009: (OCT, 17),
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


class SriLankaIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2003: (FEB, 12),
        2004: (FEB, 1),
        2005: (JAN, 21),
        2006: ((JAN, 11), (DEC, 31)),
        2007: (DEC, 21),
        2008: (DEC, 9),
        2009: (NOV, 28),
        2010: (NOV, 17),
        # https://www.adaderana.lk/news.php?nid=15606
        2011: (NOV, 7),
        # https://www.adaderana.lk/news.php?nid=20136
        2012: (OCT, 27),
        2013: (OCT, 16),
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 1),
        2018: (AUG, 22),
        2019: (AUG, 12),
        2020: (AUG, 1),
        2021: (JUL, 21),
        2022: (JUL, 10),
        2023: (JUN, 29),
        2024: (JUN, 17),
        2025: (JUN, 7),
    }

    EID_AL_FITR_DATES = {
        2003: (NOV, 26),
        2004: (NOV, 14),
        2005: (NOV, 4),
        2006: (OCT, 24),
        2007: (OCT, 13),
        2008: (OCT, 1),
        2009: (SEP, 21),
        2010: (SEP, 10),
        2011: (AUG, 31),
        2012: (AUG, 19),
        2013: (AUG, 9),
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 6),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 5),
        2020: (MAY, 25),
        2021: (MAY, 14),
        2022: (MAY, 3),
        2023: (APR, 22),
        2024: (APR, 11),
        2025: (MAR, 31),
    }

    MAWLID_DATES = {
        2003: (MAY, 14),
        2004: (MAY, 2),
        2005: (APR, 22),
        2006: (APR, 11),
        2007: (APR, 1),
        2008: (MAR, 20),
        2009: (MAR, 10),
        2010: (FEB, 27),
        2011: (FEB, 16),
        2012: (FEB, 5),
        2013: (JAN, 25),
        2014: (JAN, 14),
        # Technically 2015 has both JAN 5 and DEC 24
        # but this is only observed for JAN 4.
        2015: (JAN, 4),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 20),
        2019: (NOV, 10),
        2020: (OCT, 30),
        2021: (OCT, 19),
        2022: (OCT, 9),
        2023: (SEP, 28),
        2024: (SEP, 16),
        2025: (SEP, 5),
    }


class SriLankaStaticHolidays:
    """
    References:
    - https://www.adaderana.lk/news.php?nid=13026
    - https://www.adaderana.lk/news.php?nid=17539
    - https://www.adaderana.lk/news.php?nid=22168
    - https://www.adaderana.lk/news.php?nid=34870
    - https://www.adaderana.lk/news.php?nid=55146
    - https://www.adaderana.lk/news.php?nid=61437
    - https://www.adaderana.lk/news.php?nid=64367
    - https://www.adaderana.lk/news.php?nid=81686
    - https://www.adaderana.lk/news.php?nid=82111
    - https://www.adaderana.lk/news.php?nid=82979
    - https://www.adaderana.lk/news.php?nid=83082
    - https://www.adaderana.lk/news.php?nid=84035
    - https://www.adaderana.lk/news.php?nid=98560
    - https://www.adaderana.lk/news.php?nid=102125
    - https://web.archive.org/web/20110722150724/http://www.pubad.gov.lk/Holidays/holidays%202003.htm
    - https://web.archive.org/web/20111018053717/http://www.pubad.gov.lk/Holidays/Public%20&%20Bank%20Holidays%202004.pdf
    - https://web.archive.org/web/20241120204015/https://documents.gov.lk/en/calendar.php
    """

    # Adhi Binara Full Moon Poya Day.
    adhi_binara_poya_name = tr("අධි බිනර පුර පසළොස්වක පෝය දිනය")

    # Adhi Esala Full Moon Poya Day.
    adhi_esala_poya_name = tr("අධි ඇසල පුර පසළොස්වක පෝය දිනය")

    # Adhi Poson Full Moon Poya Day.
    adhi_poson_poya_name = tr("අධි පොසොන් පුර පසළොස්වක පෝය දිනය")

    # Adhi Vap Full Moon Poya Day.
    adhi_vap_poya_name = tr("අධි වප් පුර පසළොස්වක පෝය දිනය")

    # Adhi Vesak Full Mon Poya Day.
    adhi_vesak_poya_name = tr("අධි වෙසක් පුර පසළොස්වක පෝය දිනය")

    # Half-Day Special Bank Holiday.
    half_day_special_bank_holiday_name = tr("දින භාගයක විශේෂ බැංකු නිවාඩු දිනය")

    # Public Sector Holiday.
    public_sector_holiday_name = tr("රාජ්ය අංශයේ නිවාඩු දිනය")

    # Special Bank Holiday.
    special_bank_holiday_name = tr("විශේෂ බැංකු නිවාඩු දිනය")

    # Special Public Holiday.
    special_public_holiday_name = tr("විශේෂ රජයේ නිවාඩු දිනය")

    special_bank_holidays = {
        2005: (
            (MAY, 2, special_bank_holiday_name),
            (DEC, 26, special_bank_holiday_name),
        ),
        2007: (
            (FEB, 5, special_bank_holiday_name),
            (APR, 3, special_bank_holiday_name),
        ),
        2008: (APR, 18, special_bank_holiday_name),
        2011: (
            (MAY, 2, special_bank_holiday_name),
            (DEC, 26, special_bank_holiday_name),
        ),
        2012: (
            (JAN, 16, special_bank_holiday_name),
            (FEB, 10, special_bank_holiday_name),
            (MAY, 7, special_bank_holiday_name),
        ),
        2013: (APR, 15, special_bank_holiday_name),
        2014: (APR, 15, special_bank_holiday_name),
        2015: (JAN, 5, special_bank_holiday_name),
        2016: (
            (MAY, 2, special_bank_holiday_name),
            (MAY, 23, special_bank_holiday_name),
            (DEC, 26, special_bank_holiday_name),
        ),
        2018: (
            (JAN, 15, special_bank_holiday_name),
            (FEB, 5, special_bank_holiday_name),
        ),
        2019: (
            (APR, 15, special_bank_holiday_name),
            # MAY 20 got upgraded to Special Public Holiday.
            (NOV, 11, special_bank_holiday_name),
        ),
        2020: (APR, 14, special_bank_holiday_name),
        2021: (
            (APR, 30, half_day_special_bank_holiday_name),
            (DEC, 24, half_day_special_bank_holiday_name),
        ),
        2022: (
            # MAY 2 got upgraded to Special Public Holiday.
            (OCT, 10, special_bank_holiday_name),
            (DEC, 26, special_bank_holiday_name),
        ),
        2023: (JAN, 16, special_bank_holiday_name),
        2025: (APR, 15, special_bank_holiday_name),
    }

    special_government_holidays = {
        2020: (JUN, 4, public_sector_holiday_name),
        2022: (
            (JUN, 13, public_sector_holiday_name),
            # All Friday between JUN 15, 2022 to AUG 2, 2022.
            (JUN, 17, public_sector_holiday_name),
            (JUN, 24, public_sector_holiday_name),
            (JUL, 1, public_sector_holiday_name),
            (JUL, 8, public_sector_holiday_name),
            (JUL, 15, public_sector_holiday_name),
            (JUL, 22, public_sector_holiday_name),
            (JUL, 29, public_sector_holiday_name),
        ),
    }

    special_public_holidays = {
        2004: (JUL, 31, adhi_esala_poya_name),
        2007: (MAY, 31, adhi_poson_poya_name),
        2010: (APR, 28, adhi_vesak_poya_name),
        # 2011, MAY 2 confirmed as not getting upgrade to Special Public Holiday.
        2012: (
            (MAY, 7, special_public_holiday_name),
            (AUG, 31, adhi_binara_poya_name),
        ),
        2013: (APR, 15, special_public_holiday_name),
        2015: (JUL, 1, adhi_esala_poya_name),
        2016: (APR, 15, special_public_holiday_name),
        2018: (MAY, 29, adhi_poson_poya_name),
        2019: (MAY, 20, special_public_holiday_name),
        2020: (
            (MAR, 16, special_public_holiday_name),
            (MAR, 17, special_public_holiday_name),
            (MAR, 18, special_public_holiday_name),
            (MAR, 19, special_public_holiday_name),
            (OCT, 1, adhi_vap_poya_name),
        ),
        2022: (
            (APR, 11, special_public_holiday_name),
            (APR, 12, special_public_holiday_name),
            (MAY, 2, special_public_holiday_name),
        ),
        2023: (JUL, 3, adhi_esala_poya_name),
        2024: (
            (APR, 15, special_public_holiday_name),
            (SEP, 29, special_public_holiday_name),
        ),
    }

    special_workday_holidays = {
        2003: (OCT, 24, tr("දීපවාලි උත්සව දිනය")),  # Deepavali Festival Day.
    }
