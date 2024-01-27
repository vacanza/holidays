#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: vacanza team (https://github.com/orgs/vacanza/teams) (c) 2023-2024
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from typing import Optional, Tuple

from holidays.calendars.custom import _CustomCalendar
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, SEP, OCT, NOV

BUDDHA_BIRTHDAY = "BUDDHA_BIRTHDAY"
DOUBLE_NINTH = "DOUBLE_NINTH"
DRAGON_BOAT = "DRAGON_BOAT"
HUNG_KINGS = "HUNG_KINGS"
LUNAR_NEW_YEAR = "LUNAR_NEW_YEAR"
MID_AUTUMN = "MID_AUTUMN"


class _ChineseLunisolar:
    BUDDHA_BIRTHDAY_DATES = {
        1901: (MAY, 25),
        1902: (MAY, 15),
        1903: (MAY, 4),
        1904: (MAY, 22),
        1905: (MAY, 11),
        1906: (MAY, 1),
        1907: (MAY, 19),
        1908: (MAY, 7),
        1909: (MAY, 26),
        1910: (MAY, 16),
        1911: (MAY, 6),
        1912: (MAY, 24),
        1913: (MAY, 13),
        1914: (MAY, 2),
        1915: (MAY, 21),
        1916: (MAY, 9),
        1917: (MAY, 28),
        1918: (MAY, 17),
        1919: (MAY, 7),
        1920: (MAY, 25),
        1921: (MAY, 15),
        1922: (MAY, 4),
        1923: (MAY, 23),
        1924: (MAY, 11),
        1925: (APR, 30),
        1926: (MAY, 19),
        1927: (MAY, 8),
        1928: (MAY, 26),
        1929: (MAY, 16),
        1930: (MAY, 6),
        1931: (MAY, 24),
        1932: (MAY, 13),
        1933: (MAY, 2),
        1934: (MAY, 20),
        1935: (MAY, 10),
        1936: (MAY, 28),
        1937: (MAY, 17),
        1938: (MAY, 7),
        1939: (MAY, 26),
        1940: (MAY, 14),
        1941: (MAY, 3),
        1942: (MAY, 22),
        1943: (MAY, 11),
        1944: (APR, 30),
        1945: (MAY, 19),
        1946: (MAY, 8),
        1947: (MAY, 27),
        1948: (MAY, 16),
        1949: (MAY, 5),
        1950: (MAY, 24),
        1951: (MAY, 13),
        1952: (MAY, 1),
        1953: (MAY, 20),
        1954: (MAY, 10),
        1955: (MAY, 29),
        1956: (MAY, 17),
        1957: (MAY, 7),
        1958: (MAY, 26),
        1959: (MAY, 15),
        1960: (MAY, 3),
        1961: (MAY, 22),
        1962: (MAY, 11),
        1963: (MAY, 1),
        1964: (MAY, 19),
        1965: (MAY, 8),
        1966: (MAY, 27),
        1967: (MAY, 16),
        1968: (MAY, 4),
        1969: (MAY, 23),
        1970: (MAY, 12),
        1971: (MAY, 2),
        1972: (MAY, 20),
        1973: (MAY, 10),
        1974: (APR, 29),
        1975: (MAY, 18),
        1976: (MAY, 6),
        1977: (MAY, 25),
        1978: (MAY, 14),
        1979: (MAY, 3),
        1980: (MAY, 21),
        1981: (MAY, 11),
        1982: (MAY, 1),
        1983: (MAY, 20),
        1984: (MAY, 8),
        1985: (MAY, 27),
        1986: (MAY, 16),
        1987: (MAY, 5),
        1988: (MAY, 23),
        1989: (MAY, 12),
        1990: (MAY, 2),
        1991: (MAY, 21),
        1992: (MAY, 10),
        1993: (MAY, 28),
        1994: (MAY, 18),
        1995: (MAY, 7),
        1996: (MAY, 24),
        1997: (MAY, 14),
        1998: (MAY, 3),
        1999: (MAY, 22),
        2000: (MAY, 11),
        2001: (APR, 30),
        2002: (MAY, 19),
        2003: (MAY, 8),
        2004: (MAY, 26),
        2005: (MAY, 15),
        2006: (MAY, 5),
        2007: (MAY, 24),
        2008: (MAY, 12),
        2009: (MAY, 2),
        2010: (MAY, 21),
        2011: (MAY, 10),
        2012: (APR, 28),
        2013: (MAY, 17),
        2014: (MAY, 6),
        2015: (MAY, 25),
        2016: (MAY, 14),
        2017: (MAY, 3),
        2018: (MAY, 22),
        2019: (MAY, 12),
        2020: (APR, 30),
        2021: (MAY, 19),
        2022: (MAY, 8),
        2023: (MAY, 26),
        2024: (MAY, 15),
        2025: (MAY, 4),
        2026: (MAY, 24),
        2027: (MAY, 13),
        2028: (MAY, 2),
        2029: (MAY, 20),
        2030: (MAY, 9),
        2031: (MAY, 28),
        2032: (MAY, 16),
        2033: (MAY, 6),
        2034: (MAY, 25),
        2035: (MAY, 15),
        2036: (MAY, 3),
        2037: (MAY, 22),
        2038: (MAY, 11),
        2039: (APR, 30),
        2040: (MAY, 18),
        2041: (MAY, 7),
        2042: (MAY, 26),
        2043: (MAY, 16),
        2044: (MAY, 5),
        2045: (MAY, 24),
        2046: (MAY, 13),
        2047: (MAY, 2),
        2048: (MAY, 20),
        2049: (MAY, 9),
        2050: (MAY, 28),
        2051: (MAY, 17),
        2052: (MAY, 6),
        2053: (MAY, 25),
        2054: (MAY, 15),
        2055: (MAY, 4),
        2056: (MAY, 22),
        2057: (MAY, 11),
        2058: (APR, 30),
        2059: (MAY, 19),
        2060: (MAY, 7),
        2061: (MAY, 26),
        2062: (MAY, 16),
        2063: (MAY, 5),
        2064: (MAY, 23),
        2065: (MAY, 12),
        2066: (MAY, 1),
        2067: (MAY, 20),
        2068: (MAY, 9),
        2069: (APR, 28),
        2070: (MAY, 17),
        2071: (MAY, 7),
        2072: (MAY, 25),
        2073: (MAY, 14),
        2074: (MAY, 3),
        2075: (MAY, 22),
        2076: (MAY, 10),
        2077: (APR, 30),
        2078: (MAY, 19),
        2079: (MAY, 8),
        2080: (MAY, 26),
        2081: (MAY, 16),
        2082: (MAY, 5),
        2083: (MAY, 24),
        2084: (MAY, 12),
        2085: (MAY, 1),
        2086: (MAY, 20),
        2087: (MAY, 10),
        2088: (APR, 28),
        2089: (MAY, 17),
        2090: (MAY, 7),
        2091: (MAY, 25),
        2092: (MAY, 13),
        2093: (MAY, 3),
        2094: (MAY, 21),
        2095: (MAY, 11),
        2096: (APR, 30),
        2097: (MAY, 19),
        2098: (MAY, 8),
        2099: (MAY, 27),
    }

    DOUBLE_NINTH_DATES = {
        1901: (OCT, 20),
        1902: (OCT, 10),
        1903: (OCT, 28),
        1904: (OCT, 17),
        1905: (OCT, 7),
        1906: (OCT, 26),
        1907: (OCT, 15),
        1908: (OCT, 3),
        1909: (OCT, 22),
        1910: (OCT, 11),
        1911: (OCT, 30),
        1912: (OCT, 18),
        1913: (OCT, 8),
        1914: (OCT, 27),
        1915: (OCT, 17),
        1916: (OCT, 5),
        1917: (OCT, 24),
        1918: (OCT, 13),
        1919: (NOV, 1),
        1920: (OCT, 20),
        1921: (OCT, 9),
        1922: (OCT, 28),
        1923: (OCT, 18),
        1924: (OCT, 7),
        1925: (OCT, 26),
        1926: (OCT, 15),
        1927: (OCT, 4),
        1928: (OCT, 21),
        1929: (OCT, 11),
        1930: (OCT, 30),
        1931: (OCT, 19),
        1932: (OCT, 8),
        1933: (OCT, 27),
        1934: (OCT, 16),
        1935: (OCT, 6),
        1936: (OCT, 23),
        1937: (OCT, 12),
        1938: (OCT, 31),
        1939: (OCT, 21),
        1940: (OCT, 9),
        1941: (OCT, 28),
        1942: (OCT, 18),
        1943: (OCT, 7),
        1944: (OCT, 25),
        1945: (OCT, 14),
        1946: (OCT, 3),
        1947: (OCT, 22),
        1948: (OCT, 11),
        1949: (OCT, 30),
        1950: (OCT, 19),
        1951: (OCT, 9),
        1952: (OCT, 27),
        1953: (OCT, 16),
        1954: (OCT, 5),
        1955: (OCT, 24),
        1956: (OCT, 12),
        1957: (OCT, 31),
        1958: (OCT, 21),
        1959: (OCT, 10),
        1960: (OCT, 28),
        1961: (OCT, 18),
        1962: (OCT, 7),
        1963: (OCT, 25),
        1964: (OCT, 14),
        1965: (OCT, 3),
        1966: (OCT, 22),
        1967: (OCT, 12),
        1968: (OCT, 30),
        1969: (OCT, 19),
        1970: (OCT, 8),
        1971: (OCT, 27),
        1972: (OCT, 15),
        1973: (OCT, 4),
        1974: (OCT, 23),
        1975: (OCT, 13),
        1976: (OCT, 31),
        1977: (OCT, 21),
        1978: (OCT, 10),
        1979: (OCT, 29),
        1980: (OCT, 17),
        1981: (OCT, 6),
        1982: (OCT, 25),
        1983: (OCT, 14),
        1984: (OCT, 3),
        1985: (OCT, 22),
        1986: (OCT, 12),
        1987: (OCT, 31),
        1988: (OCT, 19),
        1989: (OCT, 8),
        1990: (OCT, 26),
        1991: (OCT, 16),
        1992: (OCT, 4),
        1993: (OCT, 23),
        1994: (OCT, 13),
        1995: (NOV, 1),
        1996: (OCT, 20),
        1997: (OCT, 10),
        1998: (OCT, 28),
        1999: (OCT, 17),
        2000: (OCT, 6),
        2001: (OCT, 25),
        2002: (OCT, 14),
        2003: (OCT, 4),
        2004: (OCT, 22),
        2005: (OCT, 11),
        2006: (OCT, 30),
        2007: (OCT, 19),
        2008: (OCT, 7),
        2009: (OCT, 26),
        2010: (OCT, 16),
        2011: (OCT, 5),
        2012: (OCT, 23),
        2013: (OCT, 13),
        2014: (OCT, 2),
        2015: (OCT, 21),
        2016: (OCT, 9),
        2017: (OCT, 28),
        2018: (OCT, 17),
        2019: (OCT, 7),
        2020: (OCT, 25),
        2021: (OCT, 14),
        2022: (OCT, 4),
        2023: (OCT, 23),
        2024: (OCT, 11),
        2025: (OCT, 29),
        2026: (OCT, 18),
        2027: (OCT, 8),
        2028: (OCT, 26),
        2029: (OCT, 16),
        2030: (OCT, 5),
        2031: (OCT, 24),
        2032: (OCT, 12),
        2033: (OCT, 1),
        2034: (OCT, 20),
        2035: (OCT, 9),
        2036: (OCT, 27),
        2037: (OCT, 17),
        2038: (OCT, 7),
        2039: (OCT, 26),
        2040: (OCT, 14),
        2041: (OCT, 3),
        2042: (OCT, 22),
        2043: (OCT, 11),
        2044: (OCT, 29),
        2045: (OCT, 18),
        2046: (OCT, 8),
        2047: (OCT, 27),
        2048: (OCT, 16),
        2049: (OCT, 5),
        2050: (OCT, 24),
        2051: (OCT, 13),
        2052: (OCT, 30),
        2053: (OCT, 20),
        2054: (OCT, 9),
        2055: (OCT, 28),
        2056: (OCT, 17),
        2057: (OCT, 7),
        2058: (OCT, 25),
        2059: (OCT, 14),
        2060: (OCT, 2),
        2061: (OCT, 21),
        2062: (OCT, 11),
        2063: (OCT, 30),
        2064: (OCT, 18),
        2065: (OCT, 8),
        2066: (OCT, 27),
        2067: (OCT, 16),
        2068: (OCT, 4),
        2069: (OCT, 23),
        2070: (OCT, 12),
        2071: (OCT, 31),
        2072: (OCT, 20),
        2073: (OCT, 9),
        2074: (OCT, 28),
        2075: (OCT, 18),
        2076: (OCT, 6),
        2077: (OCT, 25),
        2078: (OCT, 14),
        2079: (OCT, 3),
        2080: (OCT, 21),
        2081: (OCT, 11),
        2082: (OCT, 30),
        2083: (OCT, 19),
        2084: (OCT, 8),
        2085: (OCT, 27),
        2086: (OCT, 16),
        2087: (OCT, 5),
        2088: (OCT, 22),
        2089: (OCT, 12),
        2090: (OCT, 31),
        2091: (OCT, 21),
        2092: (OCT, 9),
        2093: (OCT, 28),
        2094: (OCT, 17),
        2095: (OCT, 6),
        2096: (OCT, 24),
        2097: (OCT, 13),
        2098: (OCT, 3),
        2099: (OCT, 22),
    }

    DRAGON_BOAT_DATES = {
        1901: (JUN, 20),
        1902: (JUN, 10),
        1903: (MAY, 31),
        1904: (JUN, 18),
        1905: (JUN, 7),
        1906: (JUN, 26),
        1907: (JUN, 15),
        1908: (JUN, 3),
        1909: (JUN, 22),
        1910: (JUN, 11),
        1911: (JUN, 1),
        1912: (JUN, 19),
        1913: (JUN, 9),
        1914: (MAY, 29),
        1915: (JUN, 17),
        1916: (JUN, 5),
        1917: (JUN, 23),
        1918: (JUN, 13),
        1919: (JUN, 2),
        1920: (JUN, 20),
        1921: (JUN, 10),
        1922: (MAY, 31),
        1923: (JUN, 18),
        1924: (JUN, 6),
        1925: (JUN, 25),
        1926: (JUN, 14),
        1927: (JUN, 4),
        1928: (JUN, 22),
        1929: (JUN, 11),
        1930: (JUN, 1),
        1931: (JUN, 20),
        1932: (JUN, 8),
        1933: (MAY, 28),
        1934: (JUN, 16),
        1935: (JUN, 5),
        1936: (JUN, 23),
        1937: (JUN, 13),
        1938: (JUN, 2),
        1939: (JUN, 21),
        1940: (JUN, 10),
        1941: (MAY, 30),
        1942: (JUN, 18),
        1943: (JUN, 7),
        1944: (JUN, 25),
        1945: (JUN, 14),
        1946: (JUN, 4),
        1947: (JUN, 23),
        1948: (JUN, 11),
        1949: (JUN, 1),
        1950: (JUN, 19),
        1951: (JUN, 9),
        1952: (MAY, 28),
        1953: (JUN, 15),
        1954: (JUN, 5),
        1955: (JUN, 24),
        1956: (JUN, 13),
        1957: (JUN, 2),
        1958: (JUN, 21),
        1959: (JUN, 10),
        1960: (MAY, 29),
        1961: (JUN, 17),
        1962: (JUN, 6),
        1963: (JUN, 25),
        1964: (JUN, 14),
        1965: (JUN, 4),
        1966: (JUN, 23),
        1967: (JUN, 12),
        1968: (MAY, 31),
        1969: (JUN, 19),
        1970: (JUN, 8),
        1971: (MAY, 28),
        1972: (JUN, 15),
        1973: (JUN, 5),
        1974: (JUN, 24),
        1975: (JUN, 14),
        1976: (JUN, 2),
        1977: (JUN, 21),
        1978: (JUN, 10),
        1979: (MAY, 30),
        1980: (JUN, 17),
        1981: (JUN, 6),
        1982: (JUN, 25),
        1983: (JUN, 15),
        1984: (JUN, 4),
        1985: (JUN, 22),
        1986: (JUN, 11),
        1987: (MAY, 31),
        1988: (JUN, 18),
        1989: (JUN, 8),
        1990: (MAY, 28),
        1991: (JUN, 16),
        1992: (JUN, 5),
        1993: (JUN, 24),
        1994: (JUN, 13),
        1995: (JUN, 2),
        1996: (JUN, 20),
        1997: (JUN, 9),
        1998: (MAY, 30),
        1999: (JUN, 18),
        2000: (JUN, 6),
        2001: (JUN, 25),
        2002: (JUN, 15),
        2003: (JUN, 4),
        2004: (JUN, 22),
        2005: (JUN, 11),
        2006: (MAY, 31),
        2007: (JUN, 19),
        2008: (JUN, 8),
        2009: (MAY, 28),
        2010: (JUN, 16),
        2011: (JUN, 6),
        2012: (JUN, 23),
        2013: (JUN, 12),
        2014: (JUN, 2),
        2015: (JUN, 20),
        2016: (JUN, 9),
        2017: (MAY, 30),
        2018: (JUN, 18),
        2019: (JUN, 7),
        2020: (JUN, 25),
        2021: (JUN, 14),
        2022: (JUN, 3),
        2023: (JUN, 22),
        2024: (JUN, 10),
        2025: (MAY, 31),
        2026: (JUN, 19),
        2027: (JUN, 9),
        2028: (MAY, 28),
        2029: (JUN, 16),
        2030: (JUN, 5),
        2031: (JUN, 24),
        2032: (JUN, 12),
        2033: (JUN, 1),
        2034: (JUN, 20),
        2035: (JUN, 10),
        2036: (MAY, 30),
        2037: (JUN, 18),
        2038: (JUN, 7),
        2039: (MAY, 27),
        2040: (JUN, 14),
        2041: (JUN, 3),
        2042: (JUN, 22),
        2043: (JUN, 11),
        2044: (MAY, 31),
        2045: (JUN, 19),
        2046: (JUN, 8),
        2047: (MAY, 29),
        2048: (JUN, 15),
        2049: (JUN, 4),
        2050: (JUN, 23),
        2051: (JUN, 13),
        2052: (JUN, 1),
        2053: (JUN, 20),
        2054: (JUN, 10),
        2055: (MAY, 30),
        2056: (JUN, 17),
        2057: (JUN, 6),
        2058: (JUN, 25),
        2059: (JUN, 14),
        2060: (JUN, 3),
        2061: (JUN, 22),
        2062: (JUN, 11),
        2063: (JUN, 1),
        2064: (JUN, 19),
        2065: (JUN, 8),
        2066: (MAY, 28),
        2067: (JUN, 16),
        2068: (JUN, 4),
        2069: (JUN, 23),
        2070: (JUN, 13),
        2071: (JUN, 2),
        2072: (JUN, 20),
        2073: (JUN, 10),
        2074: (MAY, 30),
        2075: (JUN, 17),
        2076: (JUN, 6),
        2077: (JUN, 24),
        2078: (JUN, 14),
        2079: (JUN, 4),
        2080: (JUN, 22),
        2081: (JUN, 11),
        2082: (JUN, 1),
        2083: (JUN, 19),
        2084: (JUN, 7),
        2085: (MAY, 27),
        2086: (JUN, 15),
        2087: (JUN, 5),
        2088: (JUN, 23),
        2089: (JUN, 13),
        2090: (JUN, 2),
        2091: (JUN, 21),
        2092: (JUN, 9),
        2093: (MAY, 29),
        2094: (JUN, 17),
        2095: (JUN, 6),
        2096: (JUN, 24),
        2097: (JUN, 14),
        2098: (JUN, 4),
        2099: (JUN, 23),
    }

    HUNG_KINGS_DATES = {
        1901: (APR, 28),
        1902: (APR, 17),
        1903: (APR, 7),
        1904: (APR, 25),
        1905: (APR, 14),
        1906: (APR, 3),
        1907: (APR, 22),
        1908: (APR, 10),
        1909: (APR, 29),
        1910: (APR, 19),
        1911: (APR, 8),
        1912: (APR, 26),
        1913: (APR, 16),
        1914: (APR, 5),
        1915: (APR, 23),
        1916: (APR, 12),
        1917: (APR, 30),
        1918: (APR, 20),
        1919: (APR, 10),
        1920: (APR, 28),
        1921: (APR, 17),
        1922: (APR, 6),
        1923: (APR, 25),
        1924: (APR, 13),
        1925: (APR, 2),
        1926: (APR, 21),
        1927: (APR, 11),
        1928: (APR, 29),
        1929: (APR, 19),
        1930: (APR, 8),
        1931: (APR, 27),
        1932: (APR, 15),
        1933: (APR, 4),
        1934: (APR, 23),
        1935: (APR, 12),
        1936: (APR, 1),
        1937: (APR, 20),
        1938: (APR, 10),
        1939: (APR, 29),
        1940: (APR, 17),
        1941: (APR, 6),
        1942: (APR, 24),
        1943: (APR, 14),
        1944: (APR, 2),
        1945: (APR, 21),
        1946: (APR, 11),
        1947: (APR, 30),
        1948: (APR, 18),
        1949: (APR, 7),
        1950: (APR, 26),
        1951: (APR, 15),
        1952: (APR, 4),
        1953: (APR, 23),
        1954: (APR, 12),
        1955: (APR, 2),
        1956: (APR, 20),
        1957: (APR, 9),
        1958: (APR, 28),
        1959: (APR, 17),
        1960: (APR, 5),
        1961: (APR, 24),
        1962: (APR, 14),
        1963: (APR, 3),
        1964: (APR, 21),
        1965: (APR, 11),
        1966: (MAR, 31),
        1967: (APR, 19),
        1968: (APR, 7),
        1969: (APR, 26),
        1970: (APR, 15),
        1971: (APR, 5),
        1972: (APR, 23),
        1973: (APR, 12),
        1974: (APR, 2),
        1975: (APR, 21),
        1976: (APR, 9),
        1977: (APR, 27),
        1978: (APR, 16),
        1979: (APR, 6),
        1980: (APR, 24),
        1981: (APR, 14),
        1982: (APR, 3),
        1983: (APR, 22),
        1984: (APR, 10),
        1985: (APR, 29),
        1986: (APR, 18),
        1987: (APR, 7),
        1988: (APR, 25),
        1989: (APR, 15),
        1990: (APR, 5),
        1991: (APR, 24),
        1992: (APR, 12),
        1993: (APR, 1),
        1994: (APR, 20),
        1995: (APR, 9),
        1996: (APR, 27),
        1997: (APR, 16),
        1998: (APR, 6),
        1999: (APR, 25),
        2000: (APR, 14),
        2001: (APR, 3),
        2002: (APR, 22),
        2003: (APR, 11),
        2004: (APR, 28),
        2005: (APR, 18),
        2006: (APR, 7),
        2007: (APR, 26),
        2008: (APR, 15),
        2009: (APR, 5),
        2010: (APR, 23),
        2011: (APR, 12),
        2012: (MAR, 31),
        2013: (APR, 19),
        2014: (APR, 9),
        2015: (APR, 28),
        2016: (APR, 16),
        2017: (APR, 6),
        2018: (APR, 25),
        2019: (APR, 14),
        2020: (APR, 2),
        2021: (APR, 21),
        2022: (APR, 10),
        2023: (APR, 29),
        2024: (APR, 18),
        2025: (APR, 7),
        2026: (APR, 26),
        2027: (APR, 16),
        2028: (APR, 4),
        2029: (APR, 23),
        2030: (APR, 12),
        2031: (APR, 1),
        2032: (APR, 19),
        2033: (APR, 9),
        2034: (APR, 28),
        2035: (APR, 17),
        2036: (APR, 6),
        2037: (APR, 25),
        2038: (APR, 14),
        2039: (APR, 3),
        2040: (APR, 20),
        2041: (APR, 10),
        2042: (APR, 29),
        2043: (APR, 19),
        2044: (APR, 7),
        2045: (APR, 26),
        2046: (APR, 15),
        2047: (APR, 4),
        2048: (APR, 22),
        2049: (APR, 11),
        2050: (APR, 1),
        2051: (APR, 20),
        2052: (APR, 9),
        2053: (APR, 28),
        2054: (APR, 17),
        2055: (APR, 6),
        2056: (APR, 24),
        2057: (APR, 13),
        2058: (APR, 2),
        2059: (APR, 21),
        2060: (APR, 10),
        2061: (MAR, 31),
        2062: (APR, 19),
        2063: (APR, 8),
        2064: (APR, 26),
        2065: (APR, 15),
        2066: (APR, 4),
        2067: (APR, 23),
        2068: (APR, 11),
        2069: (APR, 1),
        2070: (APR, 20),
        2071: (APR, 9),
        2072: (APR, 27),
        2073: (APR, 16),
        2074: (APR, 5),
        2075: (APR, 24),
        2076: (APR, 13),
        2077: (APR, 2),
        2078: (APR, 21),
        2079: (APR, 11),
        2080: (MAR, 30),
        2081: (APR, 18),
        2082: (APR, 7),
        2083: (APR, 26),
        2084: (APR, 14),
        2085: (APR, 4),
        2086: (APR, 23),
        2087: (APR, 12),
        2088: (APR, 1),
        2089: (APR, 20),
        2090: (APR, 9),
        2091: (APR, 28),
        2092: (APR, 16),
        2093: (APR, 5),
        2094: (APR, 24),
        2095: (APR, 14),
        2096: (APR, 2),
        2097: (APR, 21),
        2098: (APR, 11),
        2099: (APR, 29),
    }

    LUNAR_NEW_YEAR_DATES = {
        1901: (FEB, 19),
        1902: (FEB, 8),
        1903: (JAN, 29),
        1904: (FEB, 16),
        1905: (FEB, 4),
        1906: (JAN, 25),
        1907: (FEB, 13),
        1908: (FEB, 2),
        1909: (JAN, 22),
        1910: (FEB, 10),
        1911: (JAN, 30),
        1912: (FEB, 18),
        1913: (FEB, 6),
        1914: (JAN, 26),
        1915: (FEB, 14),
        1916: (FEB, 3),
        1917: (JAN, 23),
        1918: (FEB, 11),
        1919: (FEB, 1),
        1920: (FEB, 20),
        1921: (FEB, 8),
        1922: (JAN, 28),
        1923: (FEB, 16),
        1924: (FEB, 5),
        1925: (JAN, 24),
        1926: (FEB, 13),
        1927: (FEB, 2),
        1928: (JAN, 23),
        1929: (FEB, 10),
        1930: (JAN, 30),
        1931: (FEB, 17),
        1932: (FEB, 6),
        1933: (JAN, 26),
        1934: (FEB, 14),
        1935: (FEB, 4),
        1936: (JAN, 24),
        1937: (FEB, 11),
        1938: (JAN, 31),
        1939: (FEB, 19),
        1940: (FEB, 8),
        1941: (JAN, 27),
        1942: (FEB, 15),
        1943: (FEB, 5),
        1944: (JAN, 25),
        1945: (FEB, 13),
        1946: (FEB, 2),
        1947: (JAN, 22),
        1948: (FEB, 10),
        1949: (JAN, 29),
        1950: (FEB, 17),
        1951: (FEB, 6),
        1952: (JAN, 27),
        1953: (FEB, 14),
        1954: (FEB, 3),
        1955: (JAN, 24),
        1956: (FEB, 12),
        1957: (JAN, 31),
        1958: (FEB, 18),
        1959: (FEB, 8),
        1960: (JAN, 28),
        1961: (FEB, 15),
        1962: (FEB, 5),
        1963: (JAN, 25),
        1964: (FEB, 13),
        1965: (FEB, 2),
        1966: (JAN, 21),
        1967: (FEB, 9),
        1968: (JAN, 30),
        1969: (FEB, 17),
        1970: (FEB, 6),
        1971: (JAN, 27),
        1972: (FEB, 15),
        1973: (FEB, 3),
        1974: (JAN, 23),
        1975: (FEB, 11),
        1976: (JAN, 31),
        1977: (FEB, 18),
        1978: (FEB, 7),
        1979: (JAN, 28),
        1980: (FEB, 16),
        1981: (FEB, 5),
        1982: (JAN, 25),
        1983: (FEB, 13),
        1984: (FEB, 2),
        1985: (FEB, 20),
        1986: (FEB, 9),
        1987: (JAN, 29),
        1988: (FEB, 17),
        1989: (FEB, 6),
        1990: (JAN, 27),
        1991: (FEB, 15),
        1992: (FEB, 4),
        1993: (JAN, 23),
        1994: (FEB, 10),
        1995: (JAN, 31),
        1996: (FEB, 19),
        1997: (FEB, 7),
        1998: (JAN, 28),
        1999: (FEB, 16),
        2000: (FEB, 5),
        2001: (JAN, 24),
        2002: (FEB, 12),
        2003: (FEB, 1),
        2004: (JAN, 22),
        2005: (FEB, 9),
        2006: (JAN, 29),
        2007: (FEB, 18),
        2008: (FEB, 7),
        2009: (JAN, 26),
        2010: (FEB, 14),
        2011: (FEB, 3),
        2012: (JAN, 23),
        2013: (FEB, 10),
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
        2026: (FEB, 17),
        2027: (FEB, 6),
        2028: (JAN, 26),
        2029: (FEB, 13),
        2030: (FEB, 3),
        2031: (JAN, 23),
        2032: (FEB, 11),
        2033: (JAN, 31),
        2034: (FEB, 19),
        2035: (FEB, 8),
        2036: (JAN, 28),
        2037: (FEB, 15),
        2038: (FEB, 4),
        2039: (JAN, 24),
        2040: (FEB, 12),
        2041: (FEB, 1),
        2042: (JAN, 22),
        2043: (FEB, 10),
        2044: (JAN, 30),
        2045: (FEB, 17),
        2046: (FEB, 6),
        2047: (JAN, 26),
        2048: (FEB, 14),
        2049: (FEB, 2),
        2050: (JAN, 23),
        2051: (FEB, 11),
        2052: (FEB, 1),
        2053: (FEB, 19),
        2054: (FEB, 8),
        2055: (JAN, 28),
        2056: (FEB, 15),
        2057: (FEB, 4),
        2058: (JAN, 24),
        2059: (FEB, 12),
        2060: (FEB, 2),
        2061: (JAN, 21),
        2062: (FEB, 9),
        2063: (JAN, 29),
        2064: (FEB, 17),
        2065: (FEB, 5),
        2066: (JAN, 26),
        2067: (FEB, 14),
        2068: (FEB, 3),
        2069: (JAN, 23),
        2070: (FEB, 11),
        2071: (JAN, 31),
        2072: (FEB, 19),
        2073: (FEB, 7),
        2074: (JAN, 27),
        2075: (FEB, 15),
        2076: (FEB, 5),
        2077: (JAN, 24),
        2078: (FEB, 12),
        2079: (FEB, 2),
        2080: (JAN, 22),
        2081: (FEB, 9),
        2082: (JAN, 29),
        2083: (FEB, 17),
        2084: (FEB, 6),
        2085: (JAN, 26),
        2086: (FEB, 14),
        2087: (FEB, 3),
        2088: (JAN, 24),
        2089: (FEB, 10),
        2090: (JAN, 30),
        2091: (FEB, 18),
        2092: (FEB, 7),
        2093: (JAN, 27),
        2094: (FEB, 15),
        2095: (FEB, 5),
        2096: (JAN, 25),
        2097: (FEB, 12),
        2098: (FEB, 1),
        2099: (JAN, 21),
    }

    MID_AUTUMN_DATES = {
        1901: (SEP, 27),
        1902: (SEP, 16),
        1903: (OCT, 5),
        1904: (SEP, 24),
        1905: (SEP, 13),
        1906: (OCT, 2),
        1907: (SEP, 22),
        1908: (SEP, 10),
        1909: (SEP, 28),
        1910: (SEP, 18),
        1911: (OCT, 6),
        1912: (SEP, 25),
        1913: (SEP, 15),
        1914: (OCT, 4),
        1915: (SEP, 23),
        1916: (SEP, 12),
        1917: (SEP, 30),
        1918: (SEP, 19),
        1919: (OCT, 8),
        1920: (SEP, 26),
        1921: (SEP, 16),
        1922: (OCT, 5),
        1923: (SEP, 25),
        1924: (SEP, 13),
        1925: (OCT, 2),
        1926: (SEP, 21),
        1927: (SEP, 10),
        1928: (SEP, 28),
        1929: (SEP, 17),
        1930: (OCT, 6),
        1931: (SEP, 26),
        1932: (SEP, 15),
        1933: (OCT, 4),
        1934: (SEP, 23),
        1935: (SEP, 12),
        1936: (SEP, 30),
        1937: (SEP, 19),
        1938: (OCT, 8),
        1939: (SEP, 27),
        1940: (SEP, 16),
        1941: (OCT, 5),
        1942: (SEP, 24),
        1943: (SEP, 14),
        1944: (OCT, 1),
        1945: (SEP, 20),
        1946: (SEP, 10),
        1947: (SEP, 29),
        1948: (SEP, 17),
        1949: (OCT, 6),
        1950: (SEP, 26),
        1951: (SEP, 15),
        1952: (OCT, 3),
        1953: (SEP, 22),
        1954: (SEP, 11),
        1955: (SEP, 30),
        1956: (SEP, 19),
        1957: (SEP, 8),
        1958: (SEP, 27),
        1959: (SEP, 17),
        1960: (OCT, 5),
        1961: (SEP, 24),
        1962: (SEP, 13),
        1963: (OCT, 2),
        1964: (SEP, 20),
        1965: (SEP, 10),
        1966: (SEP, 29),
        1967: (SEP, 18),
        1968: (OCT, 6),
        1969: (SEP, 26),
        1970: (SEP, 15),
        1971: (OCT, 3),
        1972: (SEP, 22),
        1973: (SEP, 11),
        1974: (SEP, 30),
        1975: (SEP, 20),
        1976: (SEP, 8),
        1977: (SEP, 27),
        1978: (SEP, 17),
        1979: (OCT, 5),
        1980: (SEP, 23),
        1981: (SEP, 12),
        1982: (OCT, 1),
        1983: (SEP, 21),
        1984: (SEP, 10),
        1985: (SEP, 29),
        1986: (SEP, 18),
        1987: (OCT, 7),
        1988: (SEP, 25),
        1989: (SEP, 14),
        1990: (OCT, 3),
        1991: (SEP, 22),
        1992: (SEP, 11),
        1993: (SEP, 30),
        1994: (SEP, 20),
        1995: (SEP, 9),
        1996: (SEP, 27),
        1997: (SEP, 16),
        1998: (OCT, 5),
        1999: (SEP, 24),
        2000: (SEP, 12),
        2001: (OCT, 1),
        2002: (SEP, 21),
        2003: (SEP, 11),
        2004: (SEP, 28),
        2005: (SEP, 18),
        2006: (OCT, 6),
        2007: (SEP, 25),
        2008: (SEP, 14),
        2009: (OCT, 3),
        2010: (SEP, 22),
        2011: (SEP, 12),
        2012: (SEP, 30),
        2013: (SEP, 19),
        2014: (SEP, 8),
        2015: (SEP, 27),
        2016: (SEP, 15),
        2017: (OCT, 4),
        2018: (SEP, 24),
        2019: (SEP, 13),
        2020: (OCT, 1),
        2021: (SEP, 21),
        2022: (SEP, 10),
        2023: (SEP, 29),
        2024: (SEP, 17),
        2025: (OCT, 6),
        2026: (SEP, 25),
        2027: (SEP, 15),
        2028: (OCT, 3),
        2029: (SEP, 22),
        2030: (SEP, 12),
        2031: (OCT, 1),
        2032: (SEP, 19),
        2033: (SEP, 8),
        2034: (SEP, 27),
        2035: (SEP, 16),
        2036: (OCT, 4),
        2037: (SEP, 24),
        2038: (SEP, 13),
        2039: (OCT, 2),
        2040: (SEP, 20),
        2041: (SEP, 10),
        2042: (SEP, 28),
        2043: (SEP, 17),
        2044: (OCT, 5),
        2045: (SEP, 25),
        2046: (SEP, 15),
        2047: (OCT, 4),
        2048: (SEP, 22),
        2049: (SEP, 11),
        2050: (SEP, 30),
        2051: (SEP, 19),
        2052: (SEP, 7),
        2053: (SEP, 26),
        2054: (SEP, 16),
        2055: (OCT, 5),
        2056: (SEP, 24),
        2057: (SEP, 13),
        2058: (OCT, 2),
        2059: (SEP, 21),
        2060: (SEP, 9),
        2061: (SEP, 28),
        2062: (SEP, 17),
        2063: (OCT, 6),
        2064: (SEP, 25),
        2065: (SEP, 15),
        2066: (OCT, 3),
        2067: (SEP, 23),
        2068: (SEP, 11),
        2069: (SEP, 29),
        2070: (SEP, 19),
        2071: (SEP, 8),
        2072: (SEP, 26),
        2073: (SEP, 16),
        2074: (OCT, 5),
        2075: (SEP, 24),
        2076: (SEP, 12),
        2077: (OCT, 1),
        2078: (SEP, 20),
        2079: (SEP, 10),
        2080: (SEP, 28),
        2081: (SEP, 17),
        2082: (OCT, 6),
        2083: (SEP, 26),
        2084: (SEP, 14),
        2085: (OCT, 3),
        2086: (SEP, 22),
        2087: (SEP, 11),
        2088: (SEP, 29),
        2089: (SEP, 19),
        2090: (SEP, 8),
        2091: (SEP, 27),
        2092: (SEP, 16),
        2093: (OCT, 5),
        2094: (SEP, 24),
        2095: (SEP, 13),
        2096: (SEP, 30),
        2097: (SEP, 20),
        2098: (SEP, 9),
        2099: (SEP, 29),
    }

    def _get_holiday(self, holiday: str, year: int) -> Tuple[Optional[date], bool]:
        estimated_dates = getattr(self, f"{holiday}_DATES", {})
        exact_dates = getattr(self, f"{holiday}_DATES_{_CustomCalendar.CUSTOM_ATTR_POSTFIX}", {})
        dt = exact_dates.get(year, estimated_dates.get(year, ()))
        return date(year, *dt) if dt else None, year not in exact_dates

    def buddha_birthday_date(self, year: int) -> Tuple[Optional[date], bool]:
        return self._get_holiday(BUDDHA_BIRTHDAY, year)

    def double_ninth_date(self, year: int) -> Tuple[Optional[date], bool]:
        return self._get_holiday(DOUBLE_NINTH, year)

    def dragon_boat_date(self, year: int) -> Tuple[Optional[date], bool]:
        return self._get_holiday(DRAGON_BOAT, year)

    def hung_kings_date(self, year: int) -> Tuple[Optional[date], bool]:
        return self._get_holiday(HUNG_KINGS, year)

    def lunar_new_year_date(self, year: int) -> Tuple[Optional[date], bool]:
        return self._get_holiday(LUNAR_NEW_YEAR, year)

    def mid_autumn_date(self, year: int) -> Tuple[Optional[date], bool]:
        return self._get_holiday(MID_AUTUMN, year)


class _CustomChineseHolidays(_CustomCalendar, _ChineseLunisolar):
    pass
