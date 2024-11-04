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
    _CustomChineseHolidays,
    _CustomIslamicHolidays,
)
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.constants import GOVERNMENT, PUBLIC
from holidays.groups import (
    BuddhistCalendarHolidays,
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import ObservedHolidayBase


class Indonesia(
    ObservedHolidayBase,
    BuddhistCalendarHolidays,
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Indonesia
    - https://id.wikipedia.org/wiki/Hari_libur_di_Indonesia
    - https://www.liburnasional.com/sejarah/
    - https://id.wikipedia.org/wiki/Indonesia_dalam_tahun_1963 (1963-2024)
    - https://www.timeanddate.com/holidays/indonesia
    - https://en.wikipedia.org/wiki/Nyepi
    - https://bali.com/bali/travel-guide/culture/nyepi-balinese-new-year/
    """

    country = "ID"
    default_language = "id"
    # %s (estimated).
    estimated_label = tr("%s (perkiraan)")
    # %s (observed).
    observed_label = tr("Pegangti %s")
    # %s (observed, estimated).
    observed_estimated_label = tr("Pegangti %s (perkiraan)")
    supported_languages = ("en_US", "id", "th", "uk")
    supported_categories = (GOVERNMENT, PUBLIC)

    def __init__(self, *args, **kwargs):
        BuddhistCalendarHolidays.__init__(self, cls=IndonesiaBuddhistHolidays, show_estimated=True)
        ChineseCalendarHolidays.__init__(self, cls=IndonesiaChineseHolidays, show_estimated=True)
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, cls=IndonesiaIslamicHolidays)
        StaticHolidays.__init__(self, cls=IndonesiaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year <= 1945:
            return None

        # New Year's Day.
        self._add_new_years_day(tr("Tahun Baru Masehi"))

        # Independence Day.
        self._add_holiday_aug_17(tr("Hari Kemerdekaan Republik Indonesia"))

        # Keputusan Presiden no 24 tahun 1953. (1953-01-01; Removed)
        if self._year <= 1952:
            # Armed Forces Day.
            self._add_holiday_oct_5(tr("Hari Angkatan Perang"))

            # Heroes' Day.
            self._add_holiday_nov_10(tr("Hari Pahlawan"))

        # Keputusan Presiden no 24 tahun 1953. (1953-01-01; Added Nationally)
        if self._year >= 1953:
            # Christmas Day.
            self._add_christmas_day(tr("Hari Raya Natal"))

            # Eid al-Fitr.
            self._add_eid_al_fitr_day(tr("Hari Raya Idul Fitri"))

            # Eid al-Fitr Second Day.
            self._add_eid_al_fitr_day_two(tr("Hari kedua dari Hari Raya Idul Fitri"))

            # Eid al-Adha.
            self._add_eid_al_adha_day(tr("Hari Raya Idul Adha"))

        # Keputusan Presiden no 24 tahun 1953. (1953-01-01; Added Nationally)
        # Keputusan Presiden no 21 tahun 1963. (1963-10-15; Moved to Denominative-based)
        # Keputusan Presiden no 251 tahun 1967. (1967-12-16; Removed)
        if 1953 <= self._year <= 1963:
            # Easter Monday.
            self._add_easter_monday(tr("Hari kedua Paskah"))

            # Whit Monday.
            self._add_whit_monday(tr("Hari kedua Pentakosta"))

            # Nuzul Al Quran.
            self._add_nuzul_al_quran_day(tr("Nuzululqur'an"))

        # Keputusan Presiden no 24 tahun 1953. (1953-01-01; Added Nationally)
        # Keputusan Presiden no 21 tahun 1963. (1963-10-15; Moved to Denominative-based)
        # Keputusan Presiden no 251 tahun 1967. (1967-12-16; Added Nationally)
        if 1953 <= self._year <= 1962 or self._year >= 1968:
            # Isra' and Mi'raj.
            self._add_isra_and_miraj_day(tr("Isra Mikraj Nabi Muhammad"))

        # (Same as above, was before 1963 cut-off date)
        if 1953 <= self._year <= 1963 or self._year >= 1968:
            # Ascension Day.
            self._add_ascension_thursday(tr("Kenaikan Yesus Kristus"))

            # Islamic New Year.
            self._add_islamic_new_year_day(tr("Tahun Baru Islam"))

            # Prophet's Birthday.
            self._add_mawlid_day(tr("Maulid Nabi Muhammad"))

        # Keputusan Presiden no 21 tahun 1963. (1963-10-15; Added Denominative-based)
        # Keputusan Presiden no 251 tahun 1967. (1967-12-16; Added Nationally)
        # Keputusan Presiden no 10 tahun 1971. (1971-03-15; Removed)
        if 1968 <= self._year <= 1970:
            # Assumption Day.
            self._add_assumption_of_mary_day(tr("Mikraj Santa Maria"))

        # Keputusan Presiden no 24 tahun 1953. (1953-01-01; Added Nationally)
        # Keputusan Presiden no 21 tahun 1963. (1963-10-15; Moved to Denominative-based)
        # Keputusan Presiden no 251 tahun 1967. (1967-12-16; Removed)
        # Keputusan Presiden no 10 tahun 1971. (1971-03-15; Added Nationally)
        if 1953 <= self._year <= 1963 or self._year >= 1971:
            # Good Friday.
            self._add_good_friday(tr("Wafat Yesus Kristus"))

        # Keputusan Presiden no 3 tahun 1983. (1983-01-19; Added Nationally)
        if self._year >= 1983:
            dates_obs = {
                1983: (MAR, 15),
                1984: (MAR, 4),
                1985: (MAR, 22),
                1986: (MAR, 12),
                1987: (MAR, 31),
                1988: (MAR, 19),
                1989: (MAR, 9),
                1990: (MAR, 27),
                1991: (MAR, 17),
                1992: (MAR, 5),
                1993: (MAR, 24),
                1994: (MAR, 12),
                1995: (APR, 1),
                1996: (MAR, 21),
                1997: (APR, 9),
                1998: (MAR, 29),
                1999: (MAR, 18),
                2000: (APR, 4),
                2001: (MAR, 25),
                2002: (APR, 13),
                2003: (APR, 2),
                2004: (MAR, 22),
                2005: (MAR, 11),
                2006: (MAR, 30),
                2007: (MAR, 19),
                2008: (MAR, 7),
                2009: (MAR, 26),
                2010: (MAR, 16),
                2011: (MAR, 5),
                2012: (MAR, 23),
                2013: (MAR, 12),
                2014: (MAR, 31),
                2015: (MAR, 21),
                2016: (MAR, 9),
                2017: (MAR, 28),
                2018: (MAR, 17),
                2019: (MAR, 7),
                2020: (MAR, 25),
                2021: (MAR, 14),
                2022: (MAR, 3),
                2023: (MAR, 22),
                2024: (MAR, 11),
                2025: (MAR, 29),
                2026: (MAR, 19),
                2027: (MAR, 8),
                2028: (MAR, 26),
                2029: (MAR, 15),
                2030: (MAR, 5),
            }
            if self._year in dates_obs:
                # Day of Silence.
                self._add_holiday(tr("Hari Suci Nyepi"), dates_obs[self._year])

            # Vesak Day.
            self._add_vesak(tr("Hari Raya Waisak"))

        # Keputusan Presiden no 19 tahun 2002. (2002-04-09; Added Nationally)
        if self._year >= 2003:
            # Lunar New Year.
            self._add_chinese_new_years_day(tr("Tahun Baru Imlek"))

        # Keputusan Presiden no 24 tahun 1953. (1953-01-01; Added Nationally)
        # Keputusan Presiden no 148 tahun 1968. (1968-04-18; Removed)
        # Keputusan Presiden no 24 tahun 2013. (2013-07-29; Added Nationally)
        if 1953 <= self._year <= 1967 or self._year >= 2014:
            # International Labor Day.
            self._add_labor_day(tr("Hari Buruh Internasional"))

        # Keputusan Presiden no 24 tahun 2016. (2016-06-01; Added Nationally)
        if self._year >= 2016:
            # Pancasila Day.
            self._add_holiday_jun_1(tr("Hari Lahir Pancasila"))

        # Keputusan Presiden no 8 tahun 2024. (2024-01-29; Added Nationally)
        # This KEPPRES overwrites all pre-existing ones.
        if self._year >= 2024:
            # Easter Sunday.
            self._add_easter_sunday(tr("Kebangkitan Yesus Kristus"))


class ID(Indonesia):
    pass


class IDN(Indonesia):
    pass


class IndonesiaBuddhistHolidays(_CustomBuddhistHolidays):
    VESAK_DATES = {
        1983: (MAY, 27),
        1984: (MAY, 14),
        1985: (JUN, 3),
        1986: (MAY, 24),
        1987: (MAY, 13),
        1988: (MAY, 31),
        1989: (MAY, 21),
        1990: (MAY, 10),
        1991: (MAY, 28),
        1992: (MAY, 16),
        1993: (MAY, 6),
        1994: (MAY, 25),
        1995: (MAY, 15),
        1996: (JUN, 2),
        1997: (MAY, 22),
        1998: (MAY, 11),
        1999: (MAY, 30),
        2000: (MAY, 18),
        2001: (MAY, 7),
        2002: (MAY, 26),
        2003: (MAY, 16),
        2004: (JUN, 3),
        2005: (MAY, 24),
        2006: (MAY, 13),
        2007: (JUN, 1),
        2008: (MAY, 20),
        2009: (MAY, 9),
        2010: (MAY, 28),
        2011: (MAY, 17),
        2012: (MAY, 6),
        2013: (MAY, 25),
        2014: (MAY, 15),
        2015: (JUN, 2),
        2016: (MAY, 22),
        2017: (MAY, 11),
        2018: (MAY, 29),
        2019: (MAY, 19),
        2020: (MAY, 7),
        2021: (MAY, 26),
        2022: (MAY, 16),
        2023: (JUN, 4),
        2024: (MAY, 23),
        2025: (MAY, 12),
    }


class IndonesiaChineseHolidays(_CustomChineseHolidays):
    LUNAR_NEW_YEAR_DATES = {
        2003: (FEB, 1),
        2004: (JAN, 22),
        2005: (FEB, 9),
        2006: (JAN, 30),
        2007: (FEB, 19),
        2008: (FEB, 7),
        2009: (JAN, 26),
        2010: (FEB, 15),
        2011: (FEB, 3),
        2012: (JAN, 23),
        2013: (FEB, 11),
        2014: (JAN, 31),
        2015: (FEB, 19),
        2016: (FEB, 8),
        2017: (JAN, 28),
        2018: (FEB, 16),
        2019: (FEB, 5),
        2020: (JAN, 25),
        2021: (FEB, 12),
        2022: (FEB, 1),
        2023: (JAN, 22),
        2024: (FEB, 10),
        2025: (JAN, 29),
    }


class IndonesiaIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        1963: (MAY, 4),
        1964: (APR, 23),
        1965: (APR, 12),
        1966: (APR, 2),
        1967: (MAR, 22),
        1968: (MAR, 9),
        1969: (FEB, 27),
        1970: (FEB, 17),
        1971: (FEB, 6),
        1972: (JAN, 27),
        1973: (JAN, 15),
        1974: ((JAN, 4), (DEC, 24)),
        1975: (DEC, 13),
        1976: (DEC, 2),
        1977: (NOV, 21),
        1978: (NOV, 11),
        1979: (OCT, 31),
        1980: (OCT, 19),
        1981: (OCT, 8),
        1982: (SEP, 28),
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
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 2),
        2005: (JAN, 21),
        2006: ((JAN, 10), (DEC, 31)),
        2007: (DEC, 20),
        2008: (DEC, 8),
        2009: (NOV, 27),
        2010: (NOV, 17),
        2011: (NOV, 6),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 1),
        2018: (AUG, 22),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 10),
        2023: (JUN, 29),
        2024: (JUN, 17),
        2025: (JUN, 6),
    }

    EID_AL_FITR_DATES = {
        1963: (FEB, 25),
        1964: (FEB, 15),
        1965: (FEB, 3),
        1966: (JAN, 23),
        1967: (JAN, 12),
        1968: ((JAN, 2), (DEC, 21)),
        1969: (DEC, 11),
        1970: (NOV, 30),
        1971: (NOV, 19),
        1972: (NOV, 7),
        1973: (OCT, 27),
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
        1989: (MAY, 7),
        1990: (APR, 26),
        1991: (APR, 16),
        1992: (APR, 5),
        1993: (MAR, 25),
        1994: (MAR, 14),
        1995: (MAR, 3),
        1996: (FEB, 20),
        1997: (FEB, 9),
        1998: (JAN, 30),
        1999: (JAN, 19),
        2000: ((JAN, 8), (DEC, 27)),
        2001: (DEC, 16),
        2002: (DEC, 6),
        2003: (NOV, 25),
        2004: (NOV, 14),
        2005: (NOV, 3),
        2006: (OCT, 24),
        2007: (OCT, 13),
        2008: (OCT, 1),
        2009: (SEP, 20),
        2010: (SEP, 10),
        2011: (AUG, 30),
        2012: (AUG, 19),
        2013: (AUG, 8),
        2014: (JUL, 28),
        2015: (JUL, 17),
        2016: (JUL, 6),
        2017: (JUN, 25),
        2018: (JUN, 15),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 22),
        2024: (APR, 10),
        2025: (MAR, 31),
    }

    HIJRI_NEW_YEAR_DATES = {
        1968: (MAR, 30),
        1969: (MAR, 19),
        1970: (MAR, 10),
        1971: (FEB, 27),
        1972: (FEB, 16),
        1973: (FEB, 5),
        1974: (JAN, 25),
        1975: (JAN, 14),
        1976: ((JAN, 3), (DEC, 22)),
        1977: (DEC, 12),
        1978: (DEC, 1),
        1979: (NOV, 21),
        1980: (NOV, 9),
        1981: (OCT, 29),
        1982: (OCT, 18),
        1983: (OCT, 8),
        1984: (SEP, 26),
        1985: (SEP, 16),
        1986: (SEP, 5),
        1987: (AUG, 26),
        1988: (AUG, 14),
        1989: (AUG, 3),
        1990: (JUL, 23),
        1991: (JUL, 13),
        1992: (JUL, 2),
        1993: (JUN, 21),
        1994: (JUN, 11),
        1995: (MAY, 31),
        1996: (MAY, 19),
        1997: (MAY, 8),
        1998: (APR, 28),
        1999: (APR, 17),
        2000: (APR, 6),
        2001: (MAR, 26),
        2002: (MAR, 15),
        2003: (MAR, 3),
        2004: (FEB, 23),
        2005: (FEB, 10),
        2006: (JAN, 31),
        2007: (JAN, 20),
        2008: ((JAN, 10), (DEC, 29)),
        2009: (DEC, 18),
        2010: (DEC, 7),
        2011: (NOV, 27),
        2012: (NOV, 15),
        2013: (NOV, 5),
        2014: (OCT, 25),
        2015: (OCT, 14),
        2016: (OCT, 2),
        2017: (SEP, 21),
        2018: (SEP, 11),
        2019: (SEP, 1),
        2020: (AUG, 20),
        2021: (AUG, 11),
        2022: (JUL, 30),
        2023: (JUL, 19),
        2024: (JUL, 7),
        2025: (JUN, 27),
    }

    ISRA_AND_MIRAJ_DATES = {
        1968: (OCT, 20),
        1969: (OCT, 9),
        1970: (SEP, 29),
        1971: (SEP, 17),
        1972: (SEP, 6),
        1973: (AUG, 26),
        1974: (AUG, 16),
        1975: (AUG, 5),
        1976: (JUL, 25),
        1977: (JUL, 14),
        1978: (JUL, 3),
        1979: (JUN, 22),
        1980: (JUN, 11),
        1981: (MAY, 31),
        1982: (MAY, 21),
        1983: (MAY, 10),
        1984: (APR, 29),
        1985: (APR, 18),
        1986: (APR, 7),
        1987: (MAR, 27),
        1988: (MAR, 16),
        1989: (MAR, 5),
        1990: (FEB, 23),
        1991: (FEB, 12),
        1992: (FEB, 1),
        1993: (JAN, 20),
        1994: ((JAN, 10), (DEC, 30)),
        1995: (DEC, 20),
        1996: (DEC, 8),
        1997: (NOV, 28),
        1998: (NOV, 17),
        1999: (NOV, 6),
        2000: (OCT, 25),
        2001: (OCT, 15),
        2002: (OCT, 4),
        2003: (SEP, 22),
        2004: (SEP, 13),
        2005: (SEP, 2),
        2006: (AUG, 21),
        2007: (AUG, 11),
        2008: (JUL, 30),
        2009: (JUL, 20),
        2010: (JUL, 10),
        2011: (JUN, 29),
        2012: (JUN, 17),
        2013: (JUN, 6),
        2014: (MAY, 27),
        2015: (MAY, 16),
        2016: (MAY, 6),
        2017: (APR, 24),
        2018: (APR, 14),
        2019: (APR, 3),
        2020: (MAR, 22),
        2021: (MAR, 11),
        2022: (FEB, 28),
        2023: (FEB, 18),
        2024: (FEB, 8),
        2025: (JAN, 27),
    }

    MAWLID_DATES = {
        1968: (JUN, 8),
        1969: (MAY, 28),
        1970: (MAY, 18),
        1971: (MAY, 7),
        1972: (APR, 26),
        1973: (APR, 14),
        1974: (APR, 5),
        1975: (MAR, 25),
        1976: (MAR, 13),
        1977: (MAR, 2),
        1978: (FEB, 20),
        1979: (FEB, 9),
        1980: (JAN, 30),
        1981: (JAN, 18),
        1982: ((JAN, 8), (DEC, 28)),
        1983: (DEC, 17),
        1984: (DEC, 5),
        1985: (NOV, 25),
        1986: (NOV, 14),
        1987: (NOV, 4),
        1988: (OCT, 23),
        1989: (OCT, 12),
        1990: (OCT, 1),
        1991: (SEP, 21),
        1992: (SEP, 9),
        1993: (AUG, 30),
        1994: (AUG, 20),
        1995: (AUG, 9),
        1996: (JUL, 28),
        1997: (JUL, 17),
        1998: (JUL, 6),
        1999: (JUN, 26),
        2000: (JUN, 15),
        2001: (JUN, 4),
        2002: (MAY, 25),
        2003: (MAY, 15),
        2004: (MAY, 3),
        2005: (APR, 22),
        2006: (APR, 10),
        2007: (MAR, 31),
        2008: (MAR, 20),
        2009: (MAR, 9),
        2010: (FEB, 26),
        2011: (FEB, 15),
        2012: (FEB, 5),
        2013: (JAN, 24),
        2014: (JAN, 14),
        2015: ((JAN, 3), (DEC, 24)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 20),
        2019: (NOV, 9),
        2020: (OCT, 29),
        2021: (OCT, 20),
        2022: (OCT, 8),
        2023: (SEP, 28),
        2024: (SEP, 16),
        2025: (SEP, 5),
    }


class IndonesiaStaticHolidays:
    """
    References (Election Days):
    - https://peraturan.bpk.go.id/Details/58370/keppres-no-53-tahun-1999
    - https://peraturan.bpk.go.id/Details/55580/keppres-no-26-tahun-2004
    - https://peraturan.bpk.go.id/Details/55662/keppres-no-55-tahun-2004
    - https://peraturan.bpk.go.id/Details/55763/keppres-no-75-tahun-2004
    - https://peraturan.bpk.go.id/Details/55345/keppres-no-7-tahun-2009
    - https://peraturan.bpk.go.id/Details/55369/keppres-no-17-tahun-2009
    - https://peraturan.bpk.go.id/Details/57563/keppres-no-14-tahun-2014
    - https://peraturan.bpk.go.id/Details/57581/keppres-no-24-tahun-2014
    - https://peraturan.bpk.go.id/Details/54477/keppres-no-25-tahun-2015
    - https://peraturan.bpk.go.id/Details/57397/keppres-no-3-tahun-2017
    - https://peraturan.bpk.go.id/Details/82669/keppres-no-15-tahun-2018
    - https://peraturan.bpk.go.id/Details/104497/keppres-no-10-tahun-2019
    - https://peraturan.bpk.go.id/Details/152704/keppres-no-22-tahun-2020
    - https://peraturan.bpk.go.id/Details/277337/keppres-no-10-tahun-2024
    - https://www.buduk.desa.id/berita/read/83/surat-edaran-menteri-ketenagakerjaan-republik-indonesia-nomor-1-tahun-2024.html

    References (Joint Holidays):
    - https://data.santoslolowang.com/viewing/Agama_Nasional_Indonesia/kepbersama_2002.pdf/
    - https://nasional.tempo.co/read/5515/tahun-depan-libur-hari-raya-berubah
    - https://nasional.tempo.co/read/45224/2005-pemerintah-tetapkan-13-hari-libur-nasional
    - https://news.detik.com/berita/d-562326/30-maret-libur-hari-nyepi-31-maret-ditetapkan-cuti-bersama
    - https://news.detik.com/berita/d-836627/dari-12-hari-jatah-cuti-tahun-ini-dipaksa-cuti-bareng-11-hari
    - https://news.detik.com/berita/d-787189/inilah-jadwal-libur-dan-cuti-bersama-2008
    - https://news.detik.com/berita/d-889403/cuti-bersama-dihapus-sisa-4-hari-untuk-lebaran-natal
    - https://news.detik.com/berita/d-1263142/kamis-24-desember-cuti-bersama
    - https://news.detik.com/berita/d-1179419/daftar-libur-dan-cuti-bersama-2010
    - https://news.detik.com/berita/d-1378563/daftar-hari-libur-nasional-dan-cuti-bersama-2011
    - https://news.detik.com/berita/d-1639209/pemerintah-tetapkan-senin-16-mei-2011-cuti-bersama
    - https://news.detik.com/berita/d-1831855/cuti-bersama-tahun-2012-bertambah-1-hari-jadi-6-hari
    - https://news.detik.com/berita/d-1969257/ini-dia-jadwal-hari-libur-nasional-cuti-bersama-tahun-2013
    - https://news.detik.com/berita/d-2335984/daftar-cuti-bersama-dan-hari-libur-nasional-2014-termasuk-may-day
    - https://news.detik.com/berita/d-2576131/ini-daftar-hari-libur-dan-cuti-bersama-tahun-2015
    - https://bkpsdm.salatiga.go.id/pelaksanaan-hari-libur-nasional-dan-cuti-bersama-tahun-2015.html
    - https://news.detik.com/berita/d-2952083/ini-rincian-libur-dan-cuti-bersama-2016
    - https://news.detik.com/berita/d-3366218/libur-nasional-dan-cuti-bersama-2017-tambah-3-hari-ini-daftar-lengkapnya
    - https://setkab.go.id/tidak-kurangi-hak-cuti-tahunan-presiden-jokowi-tetapkan-23-juni-sebagai-cuti-bersama-idul-fitri/
    - https://setkab.go.id/pelayanan-publik-tetap-jalan-presiden-jokowi-tetapkan-cuti-bersama-pns-tahun-2018/
    - https://setkab.go.id/keppres-no-132019-cuti-bersama-pns-pada-idul-fitri-1440h-tanggal-3-4-dan-7-juni/
    - https://setkab.go.id/pemerintah-keluarkan-skb-3-menteri-hapus-tiga-hari-cuti-bersama-2020/
    - https://setkab.go.id/inilah-perubahan-hari-libur-nasional-dan-cuti-bersama-tahun-2021/
    - https://setkab.go.id/presiden-jokowi-terbitkan-keppres-4-tahun-2022-tentang-cuti-bersama-asn-tahun-2022/
    - https://news.detik.com/berita/d-6468002/apakah-ada-cuti-bersama-natal-2022-cek-infonya-di-sini
    - https://setkab.go.id/presiden-tandatangani-keppres-perubahan-cuti-bersama-bagi-asn/
    - https://setkab.go.id/inilah-keppres-7-2024-tentang-cuti-bersama-asn-tahun-2024/
    - https://setkab.go.id/pemerintah-tetapkan-hari-libur-nasional-dan-cuti-bersama-tahun-2025/
    """

    # General Election Day.
    general_election_day = tr("Hari Pemilihan Unum")
    # Presidential Election Day.
    presidential_election_day = tr("Hari Pemilihan Presiden")
    # Legislative Election Day.
    legislative_election_day = tr("Hari Pemilihan Legislatif")
    # Local Election Day.
    local_election_day = tr("Hari Pemilihan Kepala Daerah")

    # Eid al-Fitr Joint Holiday.
    eid_al_fitr_joint_holiday = tr("Cuti Bersama Hari Raya Idul Fitri")
    # Eid al-Adha Joint Holiday.
    eid_al_adha_joint_holiday = tr("Cuti Bersama Hari Raya Idul Adha")
    # Prophet's Birthday Joint Holiday.
    mawlid_joint_holiday = tr("Cuti Bersama Maulid Nabi Muhammad")
    # Islamic New Year Joint Holiday.
    islamic_new_year_joint_holiday = tr("Cuti Bersama Tahun Baru Islam")
    # Ascension Joint Holiday.
    ascension_joint_holiday = tr("Cuti Bersama Kenaikan Yesus Kristus")
    # Christmas Joint Holiday.
    christmas_joint_holiday = tr("Cuti Bersama Hari Raya Natal")
    # Lunar New Year Joint Holiday.
    lunar_new_year_joint_holiday = tr("Cuti Bersama Tahun Baru Imlek")
    # Day of Silence Joint Holiday.
    day_of_silence_joint_holiday = tr("Cuti Bersama Hari Suci Nyepi")
    # Vesak Joint Holiday.
    vesak_joint_holiday = tr("Cuti Bersama Hari Raya Waisak")
    # New Year's Joint Holiday.
    new_years_joint_holiday = tr("Cuti Bersama Tahun Baru Masehi")

    special_public_holidays = {
        1999: (JUN, 7, legislative_election_day),
        2004: (
            (APR, 5, legislative_election_day),
            (JUL, 5, presidential_election_day),
            (SEP, 20, presidential_election_day),
        ),
        2009: (
            (APR, 9, legislative_election_day),
            (JUL, 8, presidential_election_day),
        ),
        2014: (
            (APR, 9, legislative_election_day),
            (JUL, 9, presidential_election_day),
        ),
        2015: (DEC, 9, local_election_day),
        2017: (FEB, 15, local_election_day),
        2018: (JUN, 27, local_election_day),
        2019: (APR, 17, general_election_day),
        2020: (DEC, 9, local_election_day),
        2024: (
            (FEB, 14, general_election_day),
            (NOV, 27, local_election_day),
        ),
    }
    special_public_holidays_observed = {
        # Eid al-Fitr.
        2004: (NOV, 16, tr("Hari Raya Idul Fitri")),
    }
    special_government_holidays = {
        # Cuti Bersama (Joint Holidays/Collective Leaves).
        # This was first implemented in 2002.
        2002: (
            (DEC, 5, eid_al_fitr_joint_holiday),
            (DEC, 9, eid_al_fitr_joint_holiday),
            (DEC, 10, eid_al_fitr_joint_holiday),
            (DEC, 26, christmas_joint_holiday),
        ),
        2003: (
            (NOV, 24, eid_al_fitr_joint_holiday),
            (NOV, 27, eid_al_fitr_joint_holiday),
            (NOV, 28, eid_al_fitr_joint_holiday),
            (DEC, 26, christmas_joint_holiday),
        ),
        2004: (
            (NOV, 17, eid_al_fitr_joint_holiday),
            (NOV, 18, eid_al_fitr_joint_holiday),
            (NOV, 19, eid_al_fitr_joint_holiday),
        ),
        2005: (
            (NOV, 2, eid_al_fitr_joint_holiday),
            (NOV, 5, eid_al_fitr_joint_holiday),
            (NOV, 7, eid_al_fitr_joint_holiday),
            (NOV, 8, eid_al_fitr_joint_holiday),
        ),
        2006: (
            (MAR, 31, day_of_silence_joint_holiday),
            (MAY, 26, ascension_joint_holiday),
            # Independence Day Joint Holiday.
            (AUG, 18, tr("Cuti Bersama Hari Kemerdekaan Republik Indonesia")),
            (OCT, 23, eid_al_fitr_joint_holiday),
            (OCT, 26, eid_al_fitr_joint_holiday),
            (OCT, 27, eid_al_fitr_joint_holiday),
        ),
        2007: (
            (MAY, 18, ascension_joint_holiday),
            (OCT, 12, eid_al_fitr_joint_holiday),
            (OCT, 15, eid_al_fitr_joint_holiday),
            (OCT, 16, eid_al_fitr_joint_holiday),
            (OCT, 17, eid_al_fitr_joint_holiday),
            (OCT, 18, eid_al_fitr_joint_holiday),
            (OCT, 19, eid_al_fitr_joint_holiday),
            (DEC, 21, christmas_joint_holiday),
            (DEC, 24, christmas_joint_holiday),
            (DEC, 26, christmas_joint_holiday),
            (DEC, 31, new_years_joint_holiday),
        ),
        2008: (
            (JAN, 11, islamic_new_year_joint_holiday),
            (SEP, 29, eid_al_fitr_joint_holiday),
            (SEP, 30, eid_al_fitr_joint_holiday),
            (OCT, 3, eid_al_fitr_joint_holiday),
            (DEC, 26, christmas_joint_holiday),
        ),
        2009: (
            (JAN, 2, new_years_joint_holiday),
            (SEP, 18, eid_al_fitr_joint_holiday),
            (SEP, 23, eid_al_fitr_joint_holiday),
            (DEC, 24, christmas_joint_holiday),
        ),
        2010: (
            (SEP, 9, eid_al_fitr_joint_holiday),
            (SEP, 13, eid_al_fitr_joint_holiday),
            (DEC, 24, christmas_joint_holiday),
        ),
        2011: (
            (MAY, 16, vesak_joint_holiday),
            (AUG, 29, eid_al_fitr_joint_holiday),
            (SEP, 1, eid_al_fitr_joint_holiday),
            (SEP, 2, eid_al_fitr_joint_holiday),
            (DEC, 26, christmas_joint_holiday),
        ),
        2012: (
            (MAY, 18, ascension_joint_holiday),
            (AUG, 21, eid_al_fitr_joint_holiday),
            (AUG, 22, eid_al_fitr_joint_holiday),
            (NOV, 16, islamic_new_year_joint_holiday),
            (DEC, 24, christmas_joint_holiday),
            (DEC, 31, new_years_joint_holiday),
        ),
        2013: (
            (AUG, 5, eid_al_fitr_joint_holiday),
            (AUG, 6, eid_al_fitr_joint_holiday),
            (AUG, 7, eid_al_fitr_joint_holiday),
            (OCT, 14, eid_al_adha_joint_holiday),
            (DEC, 26, christmas_joint_holiday),
        ),
        2014: (
            (JUL, 30, eid_al_fitr_joint_holiday),
            (JUL, 31, eid_al_fitr_joint_holiday),
            (AUG, 1, eid_al_fitr_joint_holiday),
            (DEC, 26, christmas_joint_holiday),
        ),
        2015: (
            (JUL, 16, eid_al_fitr_joint_holiday),
            (JUL, 20, eid_al_fitr_joint_holiday),
            (JUL, 21, eid_al_fitr_joint_holiday),
        ),
        2016: (
            (JUL, 4, eid_al_fitr_joint_holiday),
            (JUL, 5, eid_al_fitr_joint_holiday),
            (JUL, 8, eid_al_fitr_joint_holiday),
            (DEC, 26, christmas_joint_holiday),
        ),
        2017: (
            (JAN, 2, new_years_joint_holiday),
            (JUN, 23, eid_al_fitr_joint_holiday),
            (JUN, 27, eid_al_fitr_joint_holiday),
            (JUN, 28, eid_al_fitr_joint_holiday),
            (JUN, 29, eid_al_fitr_joint_holiday),
            (JUN, 30, eid_al_fitr_joint_holiday),
            (DEC, 26, christmas_joint_holiday),
        ),
        2018: (
            (JUN, 11, eid_al_fitr_joint_holiday),
            (JUN, 12, eid_al_fitr_joint_holiday),
            (JUN, 13, eid_al_fitr_joint_holiday),
            (JUN, 14, eid_al_fitr_joint_holiday),
            (JUN, 18, eid_al_fitr_joint_holiday),
            (JUN, 19, eid_al_fitr_joint_holiday),
            (JUN, 20, eid_al_fitr_joint_holiday),
            (DEC, 24, christmas_joint_holiday),
        ),
        2019: (
            (JUN, 3, eid_al_fitr_joint_holiday),
            (JUN, 4, eid_al_fitr_joint_holiday),
            (JUN, 7, eid_al_fitr_joint_holiday),
            (DEC, 24, christmas_joint_holiday),
        ),
        2020: (
            (AUG, 21, islamic_new_year_joint_holiday),
            (OCT, 28, mawlid_joint_holiday),
            (OCT, 30, mawlid_joint_holiday),
            (DEC, 24, christmas_joint_holiday),
        ),
        2021: (MAY, 12, eid_al_fitr_joint_holiday),
        2022: (
            (APR, 29, eid_al_fitr_joint_holiday),
            (MAY, 4, eid_al_fitr_joint_holiday),
            (MAY, 5, eid_al_fitr_joint_holiday),
            (MAY, 6, eid_al_fitr_joint_holiday),
        ),
        2023: (
            (JAN, 23, lunar_new_year_joint_holiday),
            (MAR, 23, day_of_silence_joint_holiday),
            (APR, 19, eid_al_fitr_joint_holiday),
            (APR, 20, eid_al_fitr_joint_holiday),
            (APR, 21, eid_al_fitr_joint_holiday),
            (APR, 24, eid_al_fitr_joint_holiday),
            (APR, 25, eid_al_fitr_joint_holiday),
            (JUN, 2, vesak_joint_holiday),
            (JUN, 28, eid_al_adha_joint_holiday),
            (JUN, 30, eid_al_adha_joint_holiday),
            (DEC, 26, christmas_joint_holiday),
        ),
        2024: (
            (FEB, 9, lunar_new_year_joint_holiday),
            (MAR, 12, day_of_silence_joint_holiday),
            (APR, 8, eid_al_fitr_joint_holiday),
            (APR, 9, eid_al_fitr_joint_holiday),
            (APR, 12, eid_al_fitr_joint_holiday),
            (APR, 15, eid_al_fitr_joint_holiday),
            (MAY, 10, ascension_joint_holiday),
            (MAY, 24, vesak_joint_holiday),
            (JUN, 18, eid_al_adha_joint_holiday),
            (DEC, 26, christmas_joint_holiday),
        ),
        2025: (
            (JAN, 28, lunar_new_year_joint_holiday),
            (MAR, 28, day_of_silence_joint_holiday),
            (APR, 2, eid_al_fitr_joint_holiday),
            (APR, 3, eid_al_fitr_joint_holiday),
            (APR, 4, eid_al_fitr_joint_holiday),
            (APR, 7, eid_al_fitr_joint_holiday),
            (MAY, 13, vesak_joint_holiday),
            (MAY, 30, ascension_joint_holiday),
            (JUN, 9, eid_al_adha_joint_holiday),
            (DEC, 26, christmas_joint_holiday),
        ),
    }
    special_government_holidays_observed = {
        2020: (DEC, 31, eid_al_fitr_joint_holiday),
    }
