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
from holidays.calendars.gregorian import JAN, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.constants import BANK, PUBLIC
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.holiday_base import HolidayBase


class Tanzania(
    HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """
    References:
    - https://old.tanzlii.org/tz/legislation/act/1962/48/  # 1962
    - https://old.tanzlii.org/tz/legislation/act/1964/52/  # 1964
    - https://old.tanzlii.org/tz/legislation/act/1966/39/  # 1966
    - 1993: https://www.parliament.go.tz/polis/uploads/bills/acts/1566639469-The%20Written%20Laws%20(Miscellaneous%20Amendments)%20Act,%201993.pdf
    - 1994: https://www.parliament.go.tz/polis/uploads/bills/acts/1566638051-The%20Written%20Laws%20(Miscellaneous%20Amendments)%20(No.%202)%20Act,%201994.pdf
    - 2002: http://parliament.go.tz/polis/uploads/bills/acts/1454076376-ActNo-25-2002.pdf
    - https://en.wikipedia.org/wiki/Public_holidays_in_Tanzania
    - http://mytanzaniatimes.blogspot.com/2014/08/holiday-nane-nane-farmers-day-in.html
    - https://www.theeastafrican.co.ke/tea/business/tanzania-declares-public-holiday-on-census-day-3918836
    - https://www.dw.com/en/samia-suluhu-hassan-who-is-tanzanias-new-president/a-56932264

    Checked With:
    - 2023: https://www.bot.go.tz/webdocs/Other/2023%20public%20holidays.pdf
    - 2022: https://www.bot.go.tz/webdocs/Other/PUBLIC%20HOLIDAYS%202022.pdf
    - 2021: https://www.bot.go.tz/webdocs/Other/PUBLIC%20HOLIDAYS%202021.pdf
    - 2020: https://www.bot.go.tz/webdocs/Other/PUBLIC%20HOLIDAYS%202020.pdf
    - 2018: https://issamichuzi.blogspot.com/2017/11/sikukuu-za-kitaifa-zenye-mapumziko-kwa.html
    - from 2013 onwards: https://www.timeanddate.com/holidays/tanzania/

    Limitations:

    - Only works from 1994 onwards due to the lack of sources for certain legislation:
        Government Notices No. 79 of 1977
        Government Notices No. 300 of 1985
        Government Notices No. 296 of 1994

    - Exact Islamic holidays dates are only available for 2013-2023; the rest are estimates.
    """

    country = "TZ"
    supported_categories = (BANK, PUBLIC)
    default_language = "sw"
    # %s (estimated).
    estimated_label = tr("%s (makisio)")
    supported_languages = ("en_US", "sw")
    # Written Law (Miscellaneous Amendments) (No. 2) Act, 1994.
    start_year = 1994

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, cls=TanzaniaIslamicHolidays)
        StaticHolidays.__init__(self, TanzaniaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_bank_holidays(self):
        # Sikukuu ya Pasaka.
        # Status: In-Use.
        # Only observed by financial institutions.

        # Easter Sunday.
        self._add_easter_sunday(tr("Sikukuu ya Pasaka"))

    def _populate_public_holidays(self):
        # In-lieus ("Badala ya %s") are observed on Monday should it fall on the weekends.
        # Abrogated in Public Holidays Ordinance  No. 28 of 1966.
        # Reinstituted in Written Law (Miscellaneous Amendments) (No. 2) Act, 1994.
        # Claimed to be abrogated again on an unspecified date.

        # Fixed Date Holidays.

        # Mwaka Mpya.
        # Status: In-Use.
        # Abrogated in Public Holidays Ordinance No. 28 of 1966.
        # Reinstituted prior to the Written Law (Miscellaneous Amendments) (No. 1) Act, 1993.

        # New Year's Day.
        self._add_new_years_day(tr("Mwaka Mpya"))

        # Mapinduzi ya Zanzibar.
        # Status: In-Use.
        # Commemorates the fall of the Sultanate of Zanzibar on Jan 12, 1964.

        # Zanzibar Revolution Day.
        self._add_holiday_jan_12(tr("Mapinduzi ya Zanzibar"))

        # Siku ya kumbukumbu ya Rais wa Kwanza wa Serikali ya Mapinduzi Zanzibar
        # Sheikh Abeid Amani Karume.
        # Status: In-Use.
        # Commemorates the death of Abeid Amani Karume on Apr 7, 1972.
        # Assumed to start via Government Notices 79 of 1977.

        self._add_holiday_apr_7(
            # The Sheikh Abeid Amani Karume Day.
            tr(
                "Siku ya kumbukumbu ya Rais wa Kwanza wa Serikali ya Mapinduzi Zanzibar "
                "Sheikh Abeid Amani Karume"
            )
        )

        # Muungano wa Tanganyika na Zanzibar.
        # Status: In-Use.
        # Commemorates the creation of the United Republic of Tanzania on Apr 26, 1964.

        # Union Celebrations.
        self._add_holiday_apr_26(tr("Muungano wa Tanganyika na Zanzibar"))

        # Sikukuu ya Wafanyakazi.
        # Status: In-Use.

        # Worker's Day.
        self._add_labor_day(tr("Sikukuu ya Wafanyakazi"))

        # Sabasaba.
        # Status: In-Use.
        # Celebrates the formation of Tanganyika African National Union party on Jul 7, 1954.
        # First started in the Public Holidays Ordinance No. 57 of 1964.
        # Abrogated in 1993 (need official source on this)
        # Reinstituted via Government Notices 296 of 1994.

        # International Trade Fair.
        self._add_holiday_jul_7(tr("Sabasaba"))

        # Siku ya Wakulima.
        # Status: In-Use.
        # Also known as Nane Nane.
        # Started via Government Notices 296 of 1994 to replace Sabasaba.

        # Peasants Day.
        self._add_holiday_aug_8(tr("Siku ya Wakulima"))

        # Kumbukumbu ya Mwalimu Nyerere.
        # Status: In-Use.
        # Commemorates the death of Julius Kambarage Nyerere on Oct 14, 1999.
        # Adopted in Written Law (Miscellaneous Amendments) (No. 3) Act, 2002.

        if self._year >= 2003:
            # The Mwalimu Nyerere Day.
            self._add_holiday_oct_14(tr("Kumbukumbu ya Mwalimu Nyerere"))

        # Uhuru na Jamhuri.
        # Status: In-Use.
        # Commemorates the Independence of Tanganyika from the United Kingdom on Dec 9, 1961.

        # Independence and Republic Day.
        self._add_holiday_dec_9(tr("Uhuru na Jamhuri"))

        # Kuzaliwa Kristo.
        # Status: In-Use.

        # Christmas Day.
        self._add_christmas_day(tr("Kuzaliwa Kristo"))

        # Siku ya Kupeana Zawadi.
        # Status: In-Use.
        # Abrogated in Public Holidays Ordinance No. 28 of 1966.
        # Reinstituted in Written Law (Miscellaneous Amendments) (No. 1) Act, 1993.

        # Boxing Day.
        self._add_christmas_day_two(tr("Siku ya Kupeana Zawadi"))

        # Christian Calendar Holidays.

        # Ijumaa Kuu.
        # Status: In-Use.

        # Good Friday.
        self._add_good_friday(tr("Ijumaa Kuu"))

        # Jumatatu ya Pasaka.
        # Status: In-Use.

        # Easter Monday.
        self._add_easter_monday(tr("Jumatatu ya Pasaka"))

        # Islamic Calendar Holidays.

        # Eid El-Fitry.
        # Status: In-Use.
        # Used to be celebrated for 2 days in the 1964 and 1966 amendments.

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Eid El-Fitry"))

        # Eid El-Hajj.
        # Status: In-Use.
        # Used to be celebrated for 2 days in the 1964 amendments.

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Eid El-Hajj"))

        # Maulidi.
        # Status: In-Use.

        # Prophet's Birthday.
        self._add_mawlid_day(tr("Maulidi"))

        # Defunct Holidays.

        # 5th Day of February ??? (Name Unavailable)
        # Status: Defunct.
        # Abrogated in Written Law (Miscellaneous Amendments) (No. 1) Act, 1993.


class TZ(Tanzania):
    pass


class TZA(Tanzania):
    pass


class TanzaniaIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2013: (OCT, 15),
        2014: (OCT, 5),
        2015: (SEP, 23),
        2016: (SEP, 16),
        2017: (SEP, 2),
        2018: (AUG, 22),
        2019: (AUG, 13),
        2020: (JUL, 31),
        2021: (JUL, 21),
        2022: (JUL, 10),
        2023: (JUN, 29),
    }

    EID_AL_FITR_DATES = {
        2013: (AUG, 8),
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 14),
        2022: (MAY, 3),
        2023: (APR, 22),
        2024: (APR, 10),
    }

    MAWLID_DATES = {
        2013: (JAN, 24),
        2014: (JAN, 14),
        2015: ((JAN, 3), (DEC, 24)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 21),
        2019: (NOV, 10),
        2020: (OCT, 29),
        2021: (OCT, 19),
        2022: (OCT, 9),
        2023: (SEP, 28),
    }


class TanzaniaStaticHolidays:
    # Special Holidays.

    # John Pombe Magufuli Inauguration Day.
    john_magufuli_inauguration = tr("Sikukuu ya Kuapishwa kwa John Pombe Magufuli")

    # Tanzania General Election Day.
    tz_election_day = tr("Sikukuu ya Uchaguzi Mkuu wa Tanzania")

    # National Population and Housing Census Day.
    phc_census_day = tr("Siku ya Sensa ya Kitaifa ya Watu na Makazi")

    # John Pombe Magufuli's Funeral.
    john_magufuli_funeral = tr("Mazishi cha John Pombe Magufuli")

    special_public_holidays = {
        2002: (AUG, 25, phc_census_day),
        2015: (NOV, 5, john_magufuli_inauguration),
        2020: (OCT, 28, tz_election_day),
        2021: (
            (MAR, 22, john_magufuli_funeral),
            (MAR, 25, john_magufuli_funeral),
        ),
        2022: (AUG, 23, phc_census_day),
    }
