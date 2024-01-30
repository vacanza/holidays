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

from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import InternationalHolidays, IslamicHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class Turkey(HolidayBase, InternationalHolidays, IslamicHolidays, StaticHolidays):
    """
    References:

    - https://en.wikipedia.org/wiki/Public_holidays_in_Turkey
    - [Law 2739] https://www5.tbmm.gov.tr/tutanaklar/KANUNLAR_KARARLAR/kanuntbmmc015/kanuntbmmc015/kanuntbmmc01502739.pdf  # noqa: E501
    - [Law 2429] https://www.mevzuat.gov.tr/MevzuatMetin/1.5.2429.pdf
    - [Hijri calendar holidays] https://vakithesaplama.diyanet.gov.tr/hicriden_miladiye.php
    """

    country = "TR"
    default_language = "tr"
    # %s (estimated).
    estimated_label = tr("%s (tahmini)")
    supported_categories = (HALF_DAY, PUBLIC)
    supported_languages = ("en_US", "tr", "uk")

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, TurkeyIslamicHolidays)
        StaticHolidays.__init__(self, TurkeyStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Law 2739 of 27 May 1935.
        if self._year <= 1935:
            return None

        # New Year's Day.
        self._add_new_years_day(tr("Yılbaşı"))

        name = (
            # National Sovereignty and Children's Day.
            tr("Ulusal Egemenlik ve Çocuk Bayramı")
            if self._year >= 1981
            # National Sovereignty Day.
            else tr("Ulusal Egemenlik Bayramı")
        )
        self._add_holiday_apr_23(name)

        if self._year >= 2009:
            # Labour and Solidarity Day.
            self._add_labor_day(tr("Emek ve Dayanışma Günü"))

        name = (
            # Commemoration of Atatürk, Youth and Sports Day.
            tr("Atatürk'ü Anma, Gençlik ve Spor Bayramı")
            if self._year >= 1981
            # Youth and Sports Day.
            else tr("Gençlik ve Spor Bayramı")
        )
        self._add_holiday_may_19(name)

        if 1963 <= self._year <= 1980:
            # Freedom and Constitution Day.
            self._add_holiday_may_27(tr("Hürriyet ve Anayasa Bayramı"))

        if self._year >= 2017:
            # Democracy and National Unity Day.
            self._add_holiday_jul_15(tr("Demokrasi ve Millî Birlik Günü"))

        # Victory Day.
        self._add_holiday_aug_30(tr("Zafer Bayramı"))

        # Republic Day.
        name = tr("Cumhuriyet Bayramı")
        self._add_holiday_oct_29(name)
        if self._year <= 1980:
            self._add_holiday_oct_30(name)

        # Eid al-Fitr.
        name = tr("Ramazan Bayramı")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)

        # Eid al-Adha.
        name = tr("Kurban Bayramı")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        self._add_eid_al_adha_day_three(name)
        self._add_eid_al_adha_day_four(name)

    def _populate_half_day_holidays(self):
        if self._year <= 1935:
            return None

        # %s (from 1pm).
        begin_time_label = self.tr("%s (saat 13.00'ten)")

        # Republic Day.
        self._add_holiday_oct_28(begin_time_label % self.tr("Cumhuriyet Bayramı"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_eve(begin_time_label % self.tr("Ramazan Bayramı"))

        # Eid al-Adha.
        self._add_arafah_day(begin_time_label % self.tr("Kurban Bayramı"))


class TR(Turkey):
    pass


class TUR(Turkey):
    pass


class TurkeyIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        1936: (MAR, 4),
        1937: (FEB, 22),
        1938: (FEB, 11),
        1939: (JAN, 31),
        1940: (JAN, 20),
        1941: ((JAN, 8), (DEC, 29)),
        1942: (DEC, 18),
        1943: (DEC, 8),
        1944: (NOV, 26),
        1945: (NOV, 15),
        1946: (NOV, 4),
        1947: (OCT, 25),
        1948: (OCT, 13),
        1949: (OCT, 3),
        1950: (SEP, 23),
        1951: (SEP, 12),
        1952: (AUG, 31),
        1953: (AUG, 20),
        1954: (AUG, 9),
        1955: (JUL, 30),
        1956: (JUL, 19),
        1957: (JUL, 8),
        1958: (JUN, 28),
        1959: (JUN, 17),
        1960: (JUN, 5),
        1961: (MAY, 25),
        1962: (MAY, 14),
        1963: (MAY, 4),
        1964: (APR, 23),
        1965: (APR, 12),
        1966: (APR, 1),
        1967: (MAR, 21),
        1968: (MAR, 10),
        1969: (FEB, 27),
        1970: (FEB, 17),
        1971: (FEB, 6),
        1972: (JAN, 27),
        1973: (JAN, 15),
        1974: ((JAN, 4), (DEC, 24)),
        1975: (DEC, 13),
        1976: (DEC, 2),
        1977: (NOV, 22),
        1978: (NOV, 11),
        1979: (OCT, 31),
        1980: (OCT, 19),
        1981: (OCT, 8),
        1982: (SEP, 27),
        1983: (SEP, 17),
        1984: (SEP, 6),
        1985: (AUG, 26),
        1986: (AUG, 16),
        1987: (AUG, 5),
        1988: (JUL, 24),
        1989: (JUL, 13),
        1990: (JUL, 3),
        1991: (JUN, 23),
        1992: (JUN, 11),
        1993: (JUN, 1),
        1994: (MAY, 21),
        1995: (MAY, 10),
        1996: (APR, 28),
        1997: (APR, 18),
        1998: (APR, 7),
        1999: (MAR, 28),
        2000: (MAR, 16),
        2001: (MAR, 5),
        2002: (FEB, 22),
        2003: (FEB, 11),
        2004: (FEB, 1),
        2005: (JAN, 20),
        2006: ((JAN, 10), (DEC, 31)),
        2007: (DEC, 20),
        2008: (DEC, 8),
        2009: (NOV, 27),
        2010: (NOV, 16),
        2011: (NOV, 6),
        2012: (OCT, 25),
        2013: (OCT, 15),
        2014: (OCT, 4),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 1),
        2018: (AUG, 21),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 16),
        2025: (JUN, 6),
        2026: (MAY, 27),
        2027: (MAY, 16),
        2028: (MAY, 5),
        2029: (APR, 24),
        2030: (APR, 13),
        2031: (APR, 2),
        2032: (MAR, 22),
    }

    EID_AL_FITR_DATES = {
        1936: (DEC, 15),
        1937: (DEC, 4),
        1938: (NOV, 23),
        1939: (NOV, 13),
        1940: (NOV, 1),
        1941: (OCT, 22),
        1942: (OCT, 12),
        1943: (OCT, 1),
        1944: (SEP, 19),
        1945: (SEP, 8),
        1946: (AUG, 29),
        1947: (AUG, 18),
        1948: (AUG, 6),
        1949: (JUL, 27),
        1950: (JUL, 16),
        1951: (JUL, 6),
        1952: (JUN, 24),
        1953: (JUN, 13),
        1954: (JUN, 2),
        1955: (MAY, 23),
        1956: (MAY, 12),
        1957: (MAY, 1),
        1958: (APR, 20),
        1959: (APR, 9),
        1960: (MAR, 29),
        1961: (MAR, 18),
        1962: (MAR, 8),
        1963: (FEB, 25),
        1964: (FEB, 15),
        1965: (FEB, 3),
        1966: (JAN, 23),
        1967: (JAN, 12),
        1968: ((JAN, 1), (DEC, 21)),
        1969: (DEC, 11),
        1970: (DEC, 1),
        1971: (NOV, 20),
        1972: (NOV, 8),
        1973: (OCT, 28),
        1974: (OCT, 17),
        1975: (OCT, 6),
        1976: (SEP, 25),
        1977: (SEP, 15),
        1978: (SEP, 4),
        1979: (AUG, 24),
        1980: (AUG, 12),
        1981: (AUG, 1),
        1982: (JUL, 22),
        1983: (JUL, 12),
        1984: (JUN, 30),
        1985: (JUN, 20),
        1986: (JUN, 9),
        1987: (MAY, 29),
        1988: (MAY, 17),
        1989: (MAY, 6),
        1990: (APR, 26),
        1991: (APR, 16),
        1992: (APR, 4),
        1993: (MAR, 24),
        1994: (MAR, 13),
        1995: (MAR, 3),
        1996: (FEB, 20),
        1997: (FEB, 9),
        1998: (JAN, 29),
        1999: (JAN, 19),
        2000: ((JAN, 8), (DEC, 27)),
        2001: (DEC, 16),
        2002: (DEC, 5),
        2003: (NOV, 25),
        2004: (NOV, 14),
        2005: (NOV, 3),
        2006: (OCT, 23),
        2007: (OCT, 12),
        2008: (SEP, 30),
        2009: (SEP, 20),
        2010: (SEP, 9),
        2011: (AUG, 30),
        2012: (AUG, 19),
        2013: (AUG, 8),
        2014: (JUL, 28),
        2015: (JUL, 17),
        2016: (JUL, 5),
        2017: (JUN, 25),
        2018: (JUN, 15),
        2019: (JUN, 4),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 21),
        2024: (APR, 10),
        2025: (MAR, 30),
        2026: (MAR, 20),
        2027: (MAR, 9),
        2028: (FEB, 26),
        2029: (FEB, 14),
        2030: (FEB, 4),
        2031: (JAN, 24),
        2032: (JAN, 14),
    }


class TurkeyStaticHolidays:
    special_public_holidays = {
        # Public holiday.
        1999: (DEC, 31, tr("Genel tati̇l"))
    }
