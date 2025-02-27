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

from collections.abc import Iterable
from datetime import date
from typing import Optional

from holidays.calendars.custom import _CustomCalendar
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, OCT, NOV, AUG, SEP, DEC
from holidays.helpers import _normalize_tuple

DIWALI = "DIWALI"
THAIPUSAM = "THAIPUSAM"
HOLI = "HOLI"
GOVARDHAN_PUJA = "GOVARDHAN_PUJA"
RAKSHA_BANDHAN = "RAKSHA_BANDHAN"
JANMASHTAMI = "JANMASHTAMI"
DUSSEHRA = "DUSSEHRA"
MAHAVIR_JAYANTI = "MAHAVIR_JAYANTI"
MAHA_SHIVARATRI = "MAHA_SHIVARATRI"
RAM_NAVAMI = "RAM_NAVAMI"
SHARAD_NAVRATRI = "SHARAD_NAVRATRI"
MAHA_NAVAMI = "MAHA_NAVAMI"
GANESH_CHATURTHI = "GANESH_CHATURTHI"
GUDI_PADWA = "GUDI_PADWA"
ONAM = "ONAM"
MAKAR_SANKRANTI = "MAKAR_SANKRANTI"
CHHATH_PUJA = "CHHATH_PUJA"
GURU_NANAK_JAYANTI = "GURU_NANAK_JAYANTI"
GURU_GOBIND_SINGH_JAYANTI = "GURU_GOBINDH_SINGH_JAYANTI"
VAISAKHI = "VAISAKHI"


class _HinduLunisolar:
    # https://www.timeanddate.com/holidays/india/diwali
    diwali_dates = {
        2001: (NOV, 14),
        2002: (NOV, 4),
        2003: (OCT, 25),
        2004: (NOV, 12),
        2005: (NOV, 1),
        2006: (OCT, 21),
        2007: (NOV, 9),
        2008: (OCT, 28),
        2009: (OCT, 17),
        2010: (NOV, 5),
        2011: (OCT, 26),
        2012: (NOV, 13),
        2013: (NOV, 3),
        2014: (OCT, 23),
        2015: (NOV, 11),
        2016: (OCT, 30),
        2017: (OCT, 19),
        2018: (NOV, 7),
        2019: (OCT, 27),
        2020: (NOV, 14),
        2021: (NOV, 4),
        2022: (OCT, 24),
        2023: (NOV, 12),
        2024: (NOV, 1),
        2025: (OCT, 20),
        2026: (NOV, 8),
        2027: (OCT, 29),
        2028: (OCT, 17),
        2029: (NOV, 5),
        2030: (OCT, 26),
        2031: (NOV, 14),
        2032: (NOV, 2),
        2033: (OCT, 22),
        2034: (NOV, 10),
        2035: (OCT, 30),
    }

    thaipusam_dates = {
        1901: (MAR, 5),
        1902: (FEB, 23),
        1903: (JAN, 14),
        1904: (MAR, 2),
        1905: (FEB, 19),
        1906: (JAN, 10),
        1907: (FEB, 27),
        1908: (FEB, 17),
        1909: (JAN, 7),
        1910: (FEB, 24),
        1911: (JAN, 15),
        1912: (MAR, 4),
        1913: (FEB, 21),
        1914: (JAN, 11),
        1915: (MAR, 1),
        1916: (FEB, 18),
        1917: (JAN, 8),
        1918: (FEB, 26),
        1919: (FEB, 15),
        1920: (MAR, 5),
        1921: (FEB, 23),
        1922: (JAN, 13),
        1923: (MAR, 2),
        1924: (FEB, 19),
        1925: (JAN, 9),
        1926: (FEB, 27),
        1927: (FEB, 17),
        1928: (JAN, 8),
        1929: (FEB, 24),
        1930: (JAN, 15),
        1931: (MAR, 4),
        1932: (FEB, 21),
        1933: (JAN, 11),
        1934: (FEB, 28),
        1935: (FEB, 18),
        1936: (JAN, 9),
        1937: (FEB, 26),
        1938: (FEB, 15),
        1939: (MAR, 6),
        1940: (FEB, 23),
        1941: (JAN, 12),
        1942: (MAR, 2),
        1943: (FEB, 19),
        1944: (JAN, 10),
        1945: (FEB, 27),
        1946: (FEB, 17),
        1947: (JAN, 7),
        1948: (FEB, 25),
        1949: (FEB, 13),
        1950: (MAR, 3),
        1951: (FEB, 21),
        1952: (JAN, 12),
        1953: (FEB, 28),
        1954: (FEB, 18),
        1955: (JAN, 9),
        1956: (FEB, 26),
        1957: (FEB, 15),
        1958: (MAR, 5),
        1959: (FEB, 22),
        1960: (JAN, 13),
        1961: (MAR, 2),
        1962: (FEB, 19),
        1963: (JAN, 10),
        1964: (FEB, 28),
        1965: (FEB, 16),
        1966: (JAN, 6),
        1967: (FEB, 24),
        1968: (FEB, 13),
        1969: (MAR, 3),
        1970: (FEB, 21),
        1971: (JAN, 12),
        1972: (FEB, 29),
        1973: (FEB, 18),
        1974: (JAN, 8),
        1975: (FEB, 26),
        1976: (FEB, 15),
        1977: (MAR, 5),
        1978: (FEB, 22),
        1979: (JAN, 13),
        1980: (MAR, 2),
        1981: (FEB, 19),
        1982: (JAN, 10),
        1983: (FEB, 28),
        1984: (FEB, 17),
        1985: (MAR, 6),
        1986: (FEB, 23),
        1987: (JAN, 14),
        1988: (MAR, 3),
        1989: (FEB, 21),
        1990: (JAN, 12),
        1991: (MAR, 1),
        1992: (FEB, 18),
        1993: (JAN, 8),
        1994: (FEB, 25),
        1995: (FEB, 14),
        1996: (MAR, 4),
        1997: (FEB, 22),
        1998: (JAN, 13),
        1999: (MAR, 3),
        2000: (FEB, 20),
        2001: (JAN, 9),
        2002: (FEB, 27),
        2003: (FEB, 16),
        2004: (JAN, 7),
        2005: (FEB, 23),
        2006: (FEB, 13),
        2007: (MAR, 4),
        2008: (FEB, 22),
        2009: (JAN, 11),
        2010: (MAR, 1),
        2011: (FEB, 18),
        2012: (JAN, 8),
        2013: (FEB, 25),
        2014: (FEB, 14),
        2015: (MAR, 5),
        2016: (FEB, 23),
        2017: (JAN, 13),
        2018: (MAR, 2),
        2019: (FEB, 20),
        2020: (JAN, 10),
        2021: (FEB, 26),
        2022: (FEB, 16),
        2023: (JAN, 7),
        2024: (FEB, 24),
        2025: (JAN, 14),
        2026: (MAR, 4),
        2027: (FEB, 21),
        2028: (JAN, 11),
        2029: (FEB, 28),
        2030: (FEB, 17),
        2031: (JAN, 8),
        2032: (FEB, 26),
        2033: (FEB, 14),
        2034: (MAR, 5),
        2035: (FEB, 23),
        2036: (JAN, 13),
        2037: (MAR, 2),
        2038: (FEB, 19),
        2039: (JAN, 9),
        2040: (FEB, 27),
        2041: (FEB, 15),
        2042: (JAN, 7),
        2043: (FEB, 24),
        2044: (FEB, 14),
        2045: (MAR, 4),
        2046: (FEB, 21),
        2047: (JAN, 11),
        2048: (FEB, 28),
        2049: (FEB, 17),
        2050: (JAN, 8),
        2051: (FEB, 26),
        2052: (FEB, 15),
        2053: (MAR, 5),
        2054: (FEB, 22),
        2055: (JAN, 13),
        2056: (MAR, 1),
        2057: (FEB, 18),
        2058: (JAN, 9),
        2059: (FEB, 27),
        2060: (FEB, 17),
        2061: (JAN, 6),
        2062: (FEB, 24),
        2063: (FEB, 13),
        2064: (MAR, 3),
        2065: (FEB, 20),
        2066: (JAN, 11),
        2067: (FEB, 28),
        2068: (FEB, 18),
        2069: (JAN, 8),
        2070: (FEB, 25),
        2071: (FEB, 15),
        2072: (MAR, 5),
        2073: (FEB, 22),
        2074: (JAN, 12),
        2075: (MAR, 2),
        2076: (FEB, 19),
        2077: (JAN, 9),
        2078: (FEB, 27),
        2079: (FEB, 16),
        2080: (JAN, 7),
        2081: (FEB, 23),
        2082: (FEB, 12),
        2083: (MAR, 3),
        2084: (FEB, 21),
        2085: (JAN, 11),
        2086: (FEB, 28),
        2087: (FEB, 18),
        2088: (JAN, 9),
        2089: (FEB, 25),
        2090: (FEB, 14),
        2091: (MAR, 5),
        2092: (FEB, 22),
        2093: (JAN, 12),
        2094: (MAR, 1),
        2095: (FEB, 19),
        2096: (JAN, 10),
        2097: (FEB, 27),
        2098: (FEB, 16),
        2099: (JAN, 6),
    }

    # https://www.timeanddate.com/holidays/india/govardhan-puja
    govardhan_puja_dates = {
        2001: (NOV, 15),
        2002: (NOV, 5),
        2003: (OCT, 26),
        2004: (NOV, 13),
        2005: (NOV, 2),
        2006: (OCT, 22),
        2007: (NOV, 10),
        2008: (OCT, 29),
        2009: (OCT, 18),
        2010: (NOV, 6),
        2011: (OCT, 27),
        2012: (NOV, 14),
        2013: (NOV, 4),
        2014: (OCT, 24),
        2015: (NOV, 12),
        2016: (OCT, 31),
        2017: (OCT, 20),
        2018: (NOV, 8),
        2019: (OCT, 28),
        2020: (NOV, 15),
        2021: (NOV, 5),
        2022: (OCT, 25),
        2023: (NOV, 13),
        2024: (NOV, 2),
        2025: (OCT, 22),
        2026: (NOV, 10),
        2027: (OCT, 30),
        2028: (OCT, 18),
        2029: (NOV, 6),
        2030: (OCT, 27),
        2031: (NOV, 15),
        2032: (NOV, 3),
        2033: (OCT, 23),
        2034: (NOV, 11),
        2035: (OCT, 31),
    }

    # https://www.timeanddate.com/holidays/india/holi
    holi_dates = {
        2001: (MAR, 10),
        2002: (MAR, 29),
        2003: (MAR, 18),
        2004: (MAR, 7),
        2005: (MAR, 26),
        2006: (MAR, 15),
        2007: (MAR, 4),
        2008: (MAR, 22),
        2009: (MAR, 11),
        2010: (MAR, 1),
        2011: (MAR, 20),
        2012: (MAR, 8),
        2013: (MAR, 27),
        2014: (MAR, 17),
        2015: (MAR, 6),
        2016: (MAR, 24),
        2017: (MAR, 13),
        2018: (MAR, 2),
        2019: (MAR, 21),
        2020: (MAR, 10),
        2021: (MAR, 29),
        2022: (MAR, 18),
        2023: (MAR, 8),
        2024: (MAR, 25),
        2025: (MAR, 14),
        2026: (MAR, 4),
        2027: (MAR, 22),
        2028: (MAR, 11),
        2029: (MAR, 1),
        2030: (MAR, 20),
        2031: (MAR, 9),
        2032: (MAR, 27),
        2033: (MAR, 16),
        2034: (MAR, 5),
        2035: (MAR, 24),
    }

    # https://www.timeanddate.com/holidays/india/raksha-bandhan
    raksha_bandhan_dates = {
        2001: (AUG, 4),
        2002: (AUG, 22),
        2003: (AUG, 12),
        2004: (AUG, 29),
        2005: (AUG, 19),
        2006: (AUG, 9),
        2007: (AUG, 28),
        2008: (AUG, 16),
        2009: (AUG, 5),
        2010: (AUG, 24),
        2011: (AUG, 13),
        2012: (AUG, 2),
        2013: (AUG, 20),
        2014: (AUG, 10),
        2015: (AUG, 29),
        2016: (AUG, 18),
        2017: (AUG, 7),
        2018: (AUG, 26),
        2019: (AUG, 15),
        2020: (AUG, 3),
        2021: (AUG, 22),
        2022: (AUG, 11),
        2023: (AUG, 30),
        2024: (AUG, 19),
        2025: (AUG, 9),
        2026: (AUG, 28),
        2027: (AUG, 17),
        2028: (AUG, 5),
        2029: (AUG, 23),
        2030: (AUG, 13),
        2031: (AUG, 2),
        2032: (AUG, 20),
        2033: (AUG, 10),
        2034: (AUG, 29),
        2035: (AUG, 18),
    }

    # https://www.timeanddate.com/holidays/india/janmashtami
    janmashtami_dates = {
        2001: (AUG, 12),
        2002: (AUG, 31),
        2003: (AUG, 20),
        2004: (SEP, 7),
        2005: (AUG, 27),
        2006: (AUG, 16),
        2007: (SEP, 4),
        2008: (AUG, 24),
        2009: (AUG, 14),
        2010: (SEP, 2),
        2011: (AUG, 22),
        2012: (AUG, 10),
        2013: (AUG, 28),
        2014: (AUG, 18),
        2015: (SEP, 5),
        2016: (AUG, 25),
        2017: (AUG, 15),
        2018: (SEP, 3),
        2019: (AUG, 24),
        2020: (AUG, 12),
        2021: (AUG, 30),
        2022: (AUG, 19),
        2023: (SEP, 7),
        2024: (AUG, 26),
        2025: (AUG, 16),
        2026: (SEP, 4),
        2027: (AUG, 25),
        2028: (AUG, 13),
        2029: (SEP, 1),
        2030: (AUG, 21),
        2031: (AUG, 10),
        2032: (AUG, 28),
        2033: (AUG, 17),
        2034: (SEP, 6),
        2035: (AUG, 26),
    }

    # https://www.timeanddate.com/holidays/india/dussehra
    dussehra_dates = {
        2001: (OCT, 26),
        2002: (OCT, 15),
        2003: (OCT, 5),
        2004: (OCT, 22),
        2005: (OCT, 12),
        2006: (OCT, 2),
        2007: (OCT, 21),
        2008: (OCT, 9),
        2009: (SEP, 28),
        2010: (OCT, 17),
        2011: (OCT, 6),
        2012: (OCT, 24),
        2013: (OCT, 13),
        2014: (OCT, 3),
        2015: (OCT, 22),
        2016: (OCT, 11),
        2017: (SEP, 30),
        2018: (OCT, 19),
        2019: (OCT, 8),
        2020: (OCT, 25),
        2021: (OCT, 15),
        2022: (OCT, 5),
        2023: (OCT, 24),
        2024: (OCT, 12),
        2025: (OCT, 2),
        2026: (OCT, 20),
        2027: (OCT, 9),
        2028: (SEP, 27),
        2029: (OCT, 16),
        2030: (OCT, 6),
        2031: (OCT, 25),
        2032: (OCT, 14),
        2033: (OCT, 3),
        2034: (OCT, 22),
        2035: (OCT, 11),
    }

    # https://www.timeanddate.com/holidays/india/guru-nanak-jayanti
    guru_nanak_jayanti_dates = {
        2001: (NOV, 30),
        2002: (NOV, 19),
        2003: (NOV, 8),
        2004: (NOV, 26),
        2005: (NOV, 15),
        2006: (NOV, 5),
        2007: (NOV, 24),
        2008: (NOV, 13),
        2009: (NOV, 2),
        2010: (NOV, 21),
        2011: (NOV, 10),
        2012: (NOV, 28),
        2013: (NOV, 17),
        2014: (NOV, 6),
        2015: (NOV, 25),
        2016: (NOV, 14),
        2017: (NOV, 4),
        2018: (NOV, 23),
        2019: (NOV, 12),
        2020: (NOV, 30),
        2021: (NOV, 19),
        2022: (NOV, 8),
        2023: (NOV, 27),
        2024: (NOV, 15),
        2025: (NOV, 5),
        2027: (NOV, 14),
        2028: (NOV, 2),
        2029: (NOV, 21),
        2030: (NOV, 10),
        2031: (NOV, 28),
        2032: (NOV, 17),
        2033: (NOV, 6),
        2034: (NOV, 25),
        2035: (NOV, 15),
    }

    # https://www.timeanddate.com/holidays/india/mahavir-jayanti
    mahavir_jayanti_dates = {
        2001: (APR, 6),
        2002: (APR, 25),
        2003: (APR, 15),
        2004: (APR, 3),
        2005: (APR, 22),
        2006: (APR, 11),
        2007: (MAR, 31),
        2008: (APR, 18),
        2009: (APR, 7),
        2010: (APR, 28),
        2011: (APR, 16),
        2012: (APR, 5),
        2013: (APR, 24),
        2014: (APR, 13),
        2015: (APR, 2),
        2016: (APR, 20),
        2017: (APR, 9),
        2018: (MAR, 29),
        2019: (APR, 17),
        2020: (APR, 6),
        2021: (APR, 25),
        2022: (APR, 14),
        2023: (APR, 4),
        2024: (APR, 21),
        2025: (APR, 10),
        2026: (MAR, 31),
        2027: (APR, 18),
        2028: (APR, 7),
        2029: (APR, 26),
        2030: (APR, 16),
        2031: (APR, 5),
        2032: (APR, 23),
        2033: (APR, 12),
        2034: (APR, 1),
        2035: (APR, 20),
    }

    # https://www.timeanddate.com/holidays/india/maha-shivaratri-shivaratri
    maha_shivaratri_dates = {
        2001: (FEB, 21),
        2002: (MAR, 12),
        2003: (MAR, 1),
        2004: (FEB, 18),
        2005: (MAR, 8),
        2006: (FEB, 26),
        2007: (FEB, 16),
        2008: (MAR, 6),
        2009: (FEB, 23),
        2010: (FEB, 12),
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
        2026: (FEB, 15),
        2027: (MAR, 6),
        2028: (FEB, 23),
        2029: (FEB, 11),
        2030: (MAR, 2),
        2031: (FEB, 20),
        2032: (MAR, 10),
        2033: (FEB, 27),
        2034: (FEB, 17),
        2035: (MAR, 8),
    }

    # https://www.timeanddate.com/holidays/india/rama-navami
    ram_navami_dates = {
        2001: (APR, 2),
        2002: (APR, 21),
        2003: (APR, 11),
        2004: (MAR, 30),
        2005: (APR, 18),
        2006: (APR, 6),
        2007: (MAR, 26),
        2008: (APR, 13),
        2009: (APR, 3),
        2010: (MAR, 24),
        2011: (APR, 12),
        2012: (APR, 1),
        2013: (APR, 19),
        2014: (APR, 8),
        2015: (MAR, 28),
        2016: (APR, 15),
        2017: (APR, 4),
        2018: (MAR, 25),
        2019: (APR, 13),
        2020: (APR, 2),
        2021: (APR, 21),
        2022: (APR, 10),
        2023: (MAR, 30),
        2024: (APR, 17),
        2025: (APR, 6),
        2026: (MAR, 26),
        2027: (APR, 15),
        2028: (APR, 3),
        2029: (APR, 22),
        2030: (APR, 12),
        2031: (APR, 1),
        2032: (APR, 19),
        2033: (APR, 7),
        2034: (MAR, 28),
        2035: (APR, 16),
    }

    # https://www.timeanddate.com/holidays/india/navratri
    sharad_navratri_dates = {
        2001: (OCT, 17),
        2002: (OCT, 7),
        2003: (SEP, 26),
        2004: (OCT, 14),
        2005: (OCT, 4),
        2006: (SEP, 23),
        2007: (OCT, 12),
        2008: (SEP, 30),
        2009: (SEP, 19),
        2010: (OCT, 8),
        2011: (SEP, 28),
        2012: (OCT, 16),
        2013: (OCT, 5),
        2014: (SEP, 25),
        2015: (OCT, 13),
        2016: (OCT, 1),
        2017: (SEP, 21),
        2018: (OCT, 10),
        2019: (SEP, 29),
        2020: (OCT, 17),
        2021: (OCT, 7),
        2022: (SEP, 26),
        2023: (OCT, 15),
        2024: (OCT, 3),
        2025: (SEP, 22),
        2026: (OCT, 11),
        2027: (SEP, 30),
        2028: (SEP, 19),
        2029: (OCT, 8),
        2030: (SEP, 28),
        2031: (OCT, 17),
        2032: (OCT, 5),
        2033: (SEP, 24),
        2034: (OCT, 13),
        2035: (OCT, 2),
    }

    # https://www.timeanddate.com/holidays/india/ganesh-chaturthi
    ganesh_chaturthi_dates = {
        2001: (AUG, 22),
        2002: (SEP, 10),
        2003: (AUG, 31),
        2004: (SEP, 18),
        2005: (SEP, 7),
        2006: (AUG, 27),
        2007: (SEP, 15),
        2008: (SEP, 3),
        2009: (AUG, 23),
        2010: (SEP, 11),
        2011: (SEP, 1),
        2012: (SEP, 19),
        2013: (SEP, 9),
        2014: (AUG, 29),
        2015: (SEP, 17),
        2016: (SEP, 5),
        2017: (AUG, 25),
        2018: (SEP, 13),
        2019: (SEP, 2),
        2020: (AUG, 22),
        2021: (SEP, 10),
        2022: (AUG, 31),
        2023: (SEP, 19),
        2024: (SEP, 7),
        2025: (AUG, 27),
        2026: (SEP, 14),
        2027: (SEP, 4),
        2028: (AUG, 23),
        2029: (SEP, 11),
        2030: (SEP, 1),
        2031: (SEP, 20),
        2032: (SEP, 8),
        2033: (AUG, 28),
        2034: (SEP, 16),
        2035: (SEP, 5),
    }

    # https://www.timeanddate.com/holidays/india/maha-navami
    maha_navami_dates = {
        2001: (OCT, 25),
        2002: (OCT, 14),
        2003: (OCT, 3),
        2005: (OCT, 11),
        2006: (OCT, 1),
        2007: (OCT, 20),
        2008: (OCT, 8),
        2009: (SEP, 27),
        2010: (OCT, 16),
        2011: (OCT, 5),
        2012: (OCT, 23),
        2013: (OCT, 12),
        2014: (OCT, 2),
        2015: (OCT, 21),
        2016: (OCT, 10),
        2017: (SEP, 29),
        2018: (OCT, 18),
        2019: (OCT, 7),
        2020: (OCT, 24),
        2021: (OCT, 14),
        2022: (OCT, 4),
        2023: (OCT, 23),
        2024: (OCT, 11),
        2025: (OCT, 1),
        2026: (OCT, 19),
        2027: (OCT, 8),
        2028: (SEP, 26),
        2029: (OCT, 15),
        2030: (OCT, 5),
        2031: (OCT, 24),
        2032: (OCT, 13),
        2033: (OCT, 2),
        2034: (OCT, 21),
        2035: (OCT, 10),
    }

    # https://www.timeanddate.com/holidays/india/gudi-padwa
    gudi_padwa_dates = {
        2001: (MAR, 26),
        2002: (APR, 13),
        2003: (APR, 2),
        2004: (MAR, 21),
        2005: (APR, 9),
        2006: (MAR, 30),
        2007: (MAR, 19),
        2008: (APR, 6),
        2009: (MAR, 27),
        2010: (MAR, 16),
        2011: (APR, 4),
        2012: (MAR, 23),
        2013: (APR, 11),
        2014: (MAR, 31),
        2015: (MAR, 21),
        2016: (APR, 8),
        2017: (MAR, 28),
        2018: (MAR, 18),
        2019: (APR, 6),
        2020: (MAR, 25),
        2021: (APR, 13),
        2022: (APR, 2),
        2023: (MAR, 22),
        2024: (APR, 9),
        2025: (MAR, 30),
        2026: (MAR, 19),
        2027: (APR, 7),
        2028: (MAR, 27),
        2029: (APR, 14),
        2030: (APR, 3),
        2031: (MAR, 24),
        2032: (APR, 11),
        2033: (MAR, 31),
        2034: (MAR, 21),
        2035: (APR, 9),
    }

    # https://www.timeanddate.com/holidays/india/onam
    onam_dates = {
        2001: (AUG, 31),
        2002: (AUG, 21),
        2003: (SEP, 8),
        2004: (AUG, 28),
        2005: (SEP, 15),
        2006: (SEP, 5),
        2007: (AUG, 26),
        2008: (SEP, 12),
        2009: (SEP, 2),
        2010: (AUG, 23),
        2011: (SEP, 9),
        2012: (AUG, 29),
        2013: (AUG, 20),
        2014: (SEP, 6),
        2015: (AUG, 28),
        2016: (SEP, 13),
        2017: (SEP, 4),
        2018: (AUG, 24),
        2019: (SEP, 11),
        2020: (AUG, 31),
        2021: (AUG, 21),
        2022: (SEP, 8),
        2023: (AUG, 29),
        2024: (SEP, 15),
        2025: (SEP, 5),
        2026: (AUG, 26),
        2027: (SEP, 12),
        2028: (SEP, 1),
        2029: (AUG, 22),
        2030: (SEP, 9),
        2031: (AUG, 30),
        2032: (AUG, 20),
        2033: (SEP, 6),
        2034: (AUG, 28),
        2035: (SEP, 14),
    }

    # https://www.timeanddate.com/holidays/india/makar-sankranti
    makar_sankranti_dates = {
        2001: (JAN, 14),
        2002: (JAN, 14),
        2003: (JAN, 14),
        2004: (JAN, 15),
        2005: (JAN, 14),
        2006: (JAN, 14),
        2007: (JAN, 15),
        2008: (JAN, 15),
        2009: (JAN, 14),
        2010: (JAN, 14),
        2011: (JAN, 15),
        2012: (JAN, 15),
        2013: (JAN, 14),
        2014: (JAN, 14),
        2015: (JAN, 15),
        2016: (JAN, 15),
        2017: (JAN, 14),
        2018: (JAN, 14),
        2019: (JAN, 15),
        2020: (JAN, 15),
        2021: (JAN, 14),
        2022: (JAN, 14),
        2023: (JAN, 14),
        2024: (JAN, 14),
        2025: (JAN, 14),
        2026: (JAN, 14),
        2027: (JAN, 15),
        2028: (JAN, 15),
        2029: (JAN, 14),
        2030: (JAN, 14),
        2031: (JAN, 15),
        2032: (JAN, 15),
        2033: (JAN, 14),
        2034: (JAN, 14),
        2035: (JAN, 15),
    }

    # https://www.timeanddate.com/holidays/india/chhat-puja
    chhath_puja_dates = {
        2001: (NOV, 21),
        2002: (NOV, 10),
        2003: (OCT, 30),
        2004: (NOV, 17),
        2005: (NOV, 7),
        2006: (OCT, 28),
        2007: (NOV, 16),
        2008: (NOV, 4),
        2009: (OCT, 24),
        2010: (NOV, 11),
        2011: (NOV, 1),
        2012: (NOV, 19),
        2013: (NOV, 8),
        2014: (OCT, 29),
        2015: (NOV, 17),
        2016: (NOV, 6),
        2017: (OCT, 26),
        2018: (NOV, 13),
        2019: (NOV, 2),
        2020: (NOV, 20),
        2021: (NOV, 10),
        2022: (OCT, 30),
        2023: (NOV, 19),
        2024: (NOV, 7),
        2025: (OCT, 28),
        2026: (NOV, 15),
        2027: (NOV, 4),
        2028: (OCT, 23),
        2029: (NOV, 11),
        2030: (NOV, 1),
        2031: (NOV, 20),
        2032: (NOV, 9),
        2033: (OCT, 29),
        2034: (NOV, 17),
        2035: (NOV, 6),
    }

    # https://www.timeanddate.com/holidays/india/guru-govind-singh-jayanti
    guru_gobind_singh_jayanti_dates = {
        2001: (JAN, 2),
        2002: (JAN, 21),
        2003: (DEC, 29),
        2004: (NOV, 20),
        2005: (JAN, 5),
        2006: (JAN, 5),
        2007: (JAN, 5),
        2008: (JAN, 5),
        2009: (JAN, 5),
        2010: (JAN, 5),
        2011: (JAN, 5),
        2012: (JAN, 5),
        2013: (JAN, 18),
        2014: (JAN, 7),
        2015: (JAN, 5),
        2016: (JAN, 16),
        2017: (JAN, 5),
        2019: (JAN, 13),
        2020: (JAN, 2),
        2021: (JAN, 20),
        2022: (JAN, 9),
        2024: (JAN, 17),
        2025: (JAN, 6),
        2026: (JAN, 20),
        2027: (JAN, 15),
        2028: (JAN, 4),
        2029: (JAN, 15),
        2030: (JAN, 10),
        2032: (JAN, 18),
        2033: (JAN, 7),
        2034: (JAN, 17),
        2035: (JAN, 16),
    }

    # https://www.timeanddate.com/holidays/india/vaisakhi
    vaisakhi_dates = {
        2001: (APR, 13),
        2002: (APR, 14),
        2003: (APR, 14),
        2004: (APR, 13),
        2005: (APR, 14),
        2006: (APR, 14),
        2007: (APR, 14),
        2008: (APR, 13),
        2009: (APR, 14),
        2010: (APR, 14),
        2011: (APR, 14),
        2012: (APR, 13),
        2013: (APR, 13),
        2014: (APR, 14),
        2015: (APR, 14),
        2016: (APR, 13),
        2017: (APR, 14),
        2018: (APR, 14),
        2019: (APR, 14),
        2020: (APR, 13),
        2021: (APR, 14),
        2022: (APR, 14),
        2023: (APR, 14),
        2024: (APR, 13),
        2025: (APR, 13),
        2026: (APR, 14),
        2027: (APR, 14),
        2028: (APR, 13),
        2029: (APR, 14),
        2030: (APR, 14),
        2031: (APR, 14),
        2032: (APR, 13),
        2033: (APR, 14),
        2034: (APR, 14),
        2035: (APR, 14),
    }

    # def _get_holiday(self, holiday: str, year: int) -> tuple[Optional[date], bool]:
    #     estimated_dates = getattr(self, f"{holiday}_dates", {})
    #     exact_dates = getattr(self, f"{holiday}_dates_{_CustomCalendar.CUSTOM_ATTR_POSTFIX}", {})
    #     dt = exact_dates.get(year, estimated_dates.get(year, ()))
    #     return date(year, *dt) if dt else None, year not in exact_dates

    def _get_holiday(self, holiday: str, year: int) -> tuple[Optional[date], bool]:
        print(f"\n📍 Inside _get_holiday for {holiday}, year {year}")

        estimated_dates = getattr(self, f"{holiday.lower()}_dates", {})
        exact_dates = getattr(self, f"{holiday.lower()}_dates_{_CustomCalendar.CUSTOM_ATTR_POSTFIX}", {})

        print(f"🔍 exact_dates: {exact_dates}")
        print(f"🔍 estimated_dates: {estimated_dates}")
        print(f"🔍 Looking for year: {year}")

        dt = exact_dates.get(year, estimated_dates.get(year, ()))
        
        if dt:
            print(f"✅ Found exact date for {holiday} in {year}: {dt[0]}-{dt[1]}")
        else:
            print(f"❌ No date found for {holiday} in year {year}.")
        
        return date(year, *dt) if dt else None, year not in exact_dates

    def _get_holiday_set(self, holiday: str, year: int) -> Iterable[tuple[date, bool]]:
        estimated_dates = getattr(self, f"{holiday}_dates", {})
        exact_dates = getattr(self, f"{holiday}_dates_{_CustomCalendar.CUSTOM_ATTR_POSTFIX}", {})
        for year in (year - 1, year):
            for dt in _normalize_tuple(exact_dates.get(year, estimated_dates.get(year, ()))):
                yield date(year, *dt), year not in exact_dates

    def diwali_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(DIWALI, year)

    def thaipusam_date(self, year: int) -> tuple[Optional[date], bool]:
        if year in self.thaipusam_dates:
            month, day = self.thaipusam_dates[year]
            return date(year, month, day), False

        return self._get_holiday(THAIPUSAM, year)

    def holi_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(HOLI, year)

    def govardhan_puja_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(GOVARDHAN_PUJA, year)

    def raksha_bandhan_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(RAKSHA_BANDHAN, year)

    def janmashtami_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(JANMASHTAMI, year)

    def dussehra_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(DUSSEHRA, year)

    def mahavir_jayanti_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(MAHAVIR_JAYANTI, year)

    def maha_shivaratri_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(MAHA_SHIVARATRI, year)

    def ram_navami_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(RAM_NAVAMI, year)

    def sharad_navratri_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(SHARAD_NAVRATRI, year)

    def ganesh_chaturthi_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(GANESH_CHATURTHI, year)

    def maha_navami_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(MAHA_NAVAMI, year)

    def gudi_padwa_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(GUDI_PADWA, year)

    def onam_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(ONAM, year)

    def makar_sankranti_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(MAKAR_SANKRANTI, year)

    def chhath_puja_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(CHHATH_PUJA, year)

    def guru_nanak_jayanti_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(GURU_NANAK_JAYANTI, year)

    def guru_gobind_singh_jayanti_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(GURU_GOBIND_SINGH_JAYANTI, year)

    def vaisakhi_date(self, year: int) -> tuple[Optional[date], bool]:
        return self._get_holiday(VAISAKHI, year)


class _CustomHinduHolidays(_CustomCalendar, _HinduLunisolar):
    pass
