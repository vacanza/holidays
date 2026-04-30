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

from datetime import date, timedelta

from holidays.calendars import _CustomHinduHolidays
from holidays.calendars.gregorian import JAN, JUL, AUG, SEP, OCT, NOV
from holidays.groups import HinduCalendarHolidays, TibetanCalendarHolidays
from holidays.holiday_base import HolidayBase


class Bhutan(HolidayBase, HinduCalendarHolidays, TibetanCalendarHolidays):
    """Bhutan holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Bhutan>
        * [The Bhutanese calendar](https://web.archive.org/web/20250707105447/http://www.kalacakra.org/calendar/bhutlist.htm)
        * [2007-2011](https://web.archive.org/web/20070730055559/http://www.rcsc.gov.bt/tmpFolder/CalendarOfEvent/holiday.htm)
        * [2010-2011](https://web.archive.org/web/20100127021618/http://www.mohca.gov.bt/?mode=READMORE&news_id=157)
        * [2014](https://web.archive.org/web/20141222122050/http://www.mohca.gov.bt/Publications/calander_2014-15.pdf)
        * [2015](https://web.archive.org/web/20151004161522/http://www.mohca.gov.bt/Publications/calander_2015-16.pdf)
        * [2016](https://web.archive.org/web/20170606131500/http://www.mohca.gov.bt/download/calander_2016-17.pdf)
        * [2017](https://web.archive.org/web/20180107115733/http://www.mohca.gov.bt/wp-content/uploads/2017/11/calander_2017-18.pdf)
        * [2018](https://web.archive.org/web/20180906031327/http://www.mohca.gov.bt/wp-content/uploads/2017/11/scan0126.pdf)
        * [2019](https://web.archive.org/web/20191221201614/http://www.mohca.gov.bt/downloads/scan0004.pdf)
        * [2020](https://web.archive.org/web/20200720030220/http://www.mohca.gov.bt/wp-content/uploads/2019/12/2020-Holiday-List0001.pdf)
        * [2021](https://web.archive.org/web/20230511011459/http://www.mohca.gov.bt/downloads/Holidays2021.pdf)
        * [2022](https://web.archive.org/web/20220619061040/https://www.mohca.gov.bt/wp-content/uploads/2021/11/HolidayList.pdf)
        * [2023](https://web.archive.org/web/20221210152039/https://www.mohca.gov.bt/wp-content/uploads/2022/11/Holidays-2023.pdf)
        * [2024](https://web.archive.org/web/20250407140158/https://www.moha.gov.bt/wp-content/uploads/2023/11/National-Holiday-List-for-2024-2-.pdf)
        * [2025](https://web.archive.org/web/20250703030226/https://www.moha.gov.bt/wp-content/uploads/2024/11/Calendar_2025.pdf>
    """

    country = "BT"
    # %s (estimated).
    estimated_label = "%s (estimated)"
    # Jigme Khesar Namgyel Wangchuck ascended to the throne on December 9th, 2006.
    start_year = 2007

    WINTER_SOLSTICE_DATES = {
        2007: (JAN, 2),
        2008: (JAN, 2),
        2009: (JAN, 2),
        2010: (JAN, 2),
        2011: (JAN, 2),
        2012: (JAN, 2),
        2013: (JAN, 2),
        2014: (JAN, 2),
        2015: (JAN, 2),
        2016: (JAN, 2),
        2017: (JAN, 2),
        2018: (JAN, 2),
        2019: (JAN, 3),
        2020: (JAN, 2),
        2021: (JAN, 2),
        2022: (JAN, 1),
        2023: (JAN, 2),
        2024: (JAN, 2),
        2025: (JAN, 2),
        2026: (JAN, 2),
        2027: (JAN, 2),
        2028: (JAN, 2),
        2029: (JAN, 2),
        2030: (JAN, 2),
        2031: (JAN, 2),
        2032: (JAN, 2),
        2033: (JAN, 2),
        2034: (JAN, 2),
        2035: (JAN, 2),
        2036: (JAN, 2),
        2037: (JAN, 2),
        2038: (JAN, 2),
        2039: (JAN, 2),
        2040: (JAN, 2),
        2041: (JAN, 2),
        2042: (JAN, 2),
        2043: (JAN, 2),
        2044: (JAN, 2),
        2045: (JAN, 2),
        2046: (JAN, 2),
        2047: (JAN, 2),
        2048: (JAN, 2),
        2049: (JAN, 2),
        2050: (JAN, 2),
        2051: (JAN, 2),
        2052: (JAN, 2),
        2053: (JAN, 2),
        2054: (JAN, 2),
        2055: (JAN, 2),
        2056: (JAN, 2),
        2057: (JAN, 2),
        2058: (JAN, 2),
        2059: (JAN, 2),
        2060: (JAN, 2),
        2061: (JAN, 2),
        2062: (JAN, 2),
        2063: (JAN, 2),
        2064: (JAN, 2),
        2065: (JAN, 2),
        2066: (JAN, 2),
        2067: (JAN, 2),
        2068: (JAN, 2),
        2069: (JAN, 2),
        2070: (JAN, 2),
        2071: (JAN, 2),
        2072: (JAN, 2),
        2073: (JAN, 2),
        2074: (JAN, 2),
        2075: (JAN, 2),
        2076: (JAN, 2),
        2077: (JAN, 2),
        2078: (JAN, 2),
        2079: (JAN, 2),
        2080: (JAN, 2),
        2081: (JAN, 2),
        2082: (JAN, 2),
        2083: (JAN, 2),
        2084: (JAN, 2),
        2085: (JAN, 2),
        2086: (JAN, 2),
        2087: (JAN, 2),
        2088: (JAN, 2),
        2089: (JAN, 2),
        2090: (JAN, 2),
        2091: (JAN, 2),
        2092: (JAN, 2),
        2093: (JAN, 2),
        2094: (JAN, 2),
        2095: (JAN, 2),
        2096: (JAN, 2),
        2097: (JAN, 2),
        2098: (JAN, 2),
        2099: (JAN, 2),
        2100: (JAN, 2),
    }

    BLESSED_RAINY_DAY_DATES = {
        2007: (SEP, 23),
        2008: (SEP, 22),
        2009: (SEP, 23),
        2010: (SEP, 23),
        2011: (SEP, 23),
        2012: (SEP, 22),
        2013: (SEP, 23),
        2014: (SEP, 23),
        2015: (SEP, 22),
        2016: (SEP, 23),
        2017: (SEP, 23),
        2018: (SEP, 23),
        2019: (SEP, 24),
        2020: (SEP, 23),
        2021: (SEP, 23),
        2022: (SEP, 23),
        2023: (SEP, 24),
        2024: (SEP, 23),
        2025: (SEP, 23),
        2026: (SEP, 23),
        2027: (SEP, 23),
        2028: (SEP, 22),
        2029: (SEP, 22),
        2030: (SEP, 23),
        2031: (SEP, 23),
        2032: (SEP, 23),
        2033: (SEP, 23),
        2034: (SEP, 23),
        2035: (SEP, 23),
        2036: (SEP, 23),
        2037: (SEP, 23),
        2038: (SEP, 23),
        2039: (SEP, 23),
        2040: (SEP, 23),
        2041: (SEP, 23),
        2042: (SEP, 23),
        2043: (SEP, 23),
        2044: (SEP, 23),
        2045: (SEP, 23),
        2046: (SEP, 23),
        2047: (SEP, 23),
        2048: (SEP, 23),
        2049: (SEP, 23),
        2050: (SEP, 23),
        2051: (SEP, 23),
        2052: (SEP, 23),
        2053: (SEP, 23),
        2054: (SEP, 23),
        2055: (SEP, 23),
        2056: (SEP, 23),
        2057: (SEP, 23),
        2058: (SEP, 23),
        2059: (SEP, 23),
        2060: (SEP, 23),
        2061: (SEP, 23),
        2062: (SEP, 23),
        2063: (SEP, 23),
        2064: (SEP, 23),
        2065: (SEP, 23),
        2066: (SEP, 23),
        2067: (SEP, 23),
        2068: (SEP, 23),
        2069: (SEP, 23),
        2070: (SEP, 23),
        2071: (SEP, 23),
        2072: (SEP, 23),
        2073: (SEP, 23),
        2074: (SEP, 23),
        2075: (SEP, 23),
        2076: (SEP, 23),
        2077: (SEP, 23),
        2078: (SEP, 23),
        2079: (SEP, 23),
        2080: (SEP, 23),
        2081: (SEP, 23),
        2082: (SEP, 23),
        2083: (SEP, 23),
        2084: (SEP, 23),
        2085: (SEP, 23),
        2086: (SEP, 23),
        2087: (SEP, 23),
        2088: (SEP, 23),
        2089: (SEP, 23),
        2090: (SEP, 23),
        2091: (SEP, 23),
        2092: (SEP, 23),
        2093: (SEP, 23),
        2094: (SEP, 23),
        2095: (SEP, 23),
        2096: (SEP, 23),
        2097: (SEP, 23),
        2098: (SEP, 23),
        2099: (SEP, 23),
        2100: (SEP, 23),
    }
    subdivisions = (
        "11",  # Paro.
        "12",  # Chhukha.
        "13",  # Haa.
        "14",  # Samtse.
        "15",  # Thimphu.
        "21",  # Tsirang.
        "22",  # Dagana.
        "23",  # Punakha.
        "24",  # Wangdue Phodrang.
        "31",  # Sarpang.
        "32",  # Trongsa.
        "33",  # Bumthang.
        "34",  # Zhemgang.
        "41",  # Trashigang.
        "42",  # Monggar.
        "43",  # Pema Gatshel.
        "44",  # Lhuentse.
        "45",  # Samdrup Jongkhar.
        "GA",  # Gasa.
        "TY",  # Trashi Yangtse.
    )

    subdivisions_aliases = {
        "Paro": "11",
        "Chhukha": "12",
        "Haa": "13",
        "Samtse": "14",
        "Thimphu": "15",
        "Tsirang": "21",
        "Dagana": "22",
        "Punakha": "23",
        "Wangdue Phodrang": "24",
        "Sarpang": "31",
        "Trongsa": "32",
        "Bumthang": "33",
        "Zhemgang": "34",
        "Trashigang": "41",
        "Monggar": "42",
        "Pema Gatshel": "43",
        "Lhuentse": "44",
        "Samdrup Jongkhar": "45",
        "Gasa": "GA",
        "Trashi Yangtse": "TY",
    }

    def __init__(self, *args, hindu_show_estimated: bool = True, **kwargs):
        """
        Args:
            hindu_show_estimated:
                Whether to add "estimated" label to Hindu holidays name
                if holiday date is estimated.
        """
        HinduCalendarHolidays.__init__(
            self, cls=BhutanHinduHolidays, show_estimated=hindu_show_estimated
        )
        TibetanCalendarHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        name = "Birth Anniversary of His Majesty the King"
        # Birth Anniversary of His Majesty the King.
        self._add_holiday_feb_21(name)
        self._add_holiday_feb_22(name)
        self._add_holiday_feb_23(name)

        # Birth Anniversary of the 3rd Druk Gyalpo.
        self._add_holiday_may_2("Birth Anniversary of the 3rd Druk Gyalpo")

        # Coronation of His Majesty the King.
        self._add_holiday_nov_1("Coronation of His Majesty the King")

        # Birth Anniversary of the 4th Druk Gyalpo - Constitution Day.
        self._add_holiday_nov_11("Birth Anniversary of the 4th Druk Gyalpo - Constitution Day")

        # National Day.
        self._add_holiday_dec_17("National Day")

        # Winter Solstice.
        dt = self.WINTER_SOLSTICE_DATES.get(self._year)
        if dt:
            self._add_holiday("Winter Solstice", *dt)

        # Traditional Day of Offering.
        self._add_day_of_offering("Traditional Day of Offering")

        # Losar.
        name = "Losar"
        self._add_losar(name)
        self._add_losar_day_two(name)

        # Death Anniversary of Zhabdrung.
        self._add_death_of_zhabdrung("Death Anniversary of Zhabdrung")

        # Lord Buddha's Parinirvana.
        self._add_buddha_parinirvana("Lord Buddha's Parinirvana")

        # Birth Anniversary of Guru Rinpoche.
        self._add_birth_of_guru_rinpoche("Birth Anniversary of Guru Rinpoche")

        # First Sermon of Lord Buddha.
        dt = BhutanTibetanHolidays.BUDDHA_FIRST_SERMON_DATES.get(self._year)
        if dt:
            self._add_holiday("First Sermon of Lord Buddha", *dt)

        # Blessed Rainy Day.
        dt = self.BLESSED_RAINY_DAY_DATES.get(self._year)
        if dt:
            self._add_holiday("Blessed Rainy Day", *dt)

        # Dassain.
        self._add_dussehra("Dassain")

        # Descending Day of Lord Buddha.
        dt = BhutanTibetanHolidays.DESCENDING_DAY_OF_LORD_BUDDHA_DATES.get(self._year)
        if dt:
            self._add_holiday("Descending Day of Lord Buddha", *dt)

    def _populate_subdiv_15_public_holidays(self):
        # Thimphu Drubchoe.
        dt = BhutanTibetanHolidays.THIMPHU_DRUBCHEN_DATES.get(self._year)
        if dt:
            self._add_holiday("Thimphu Drubchoe", *dt)

        # Thimphu Tshechu.
        dt = BhutanTibetanHolidays.THIMPHU_TSHECHU_DATES.get(self._year)
        if dt:
            dt_obj = date(self._year, *dt)
            self._add_holiday("Thimphu Tshechu", dt_obj)
            self._add_holiday("Thimphu Tshechu", dt_obj + timedelta(days=1))
            self._add_holiday("Thimphu Tshechu", dt_obj + timedelta(days=2))


class BT(Bhutan):
    pass


class BTN(Bhutan):
    pass


class BhutanHinduHolidays(_CustomHinduHolidays):
    DUSSEHRA_DATES = {
        2007: (OCT, 21),
        2008: (OCT, 9),
        2009: (SEP, 28),
        2010: (OCT, 17),
        2011: (OCT, 6),
        2014: (OCT, 3),
        2015: (OCT, 22),
        2016: (OCT, 11),
        2017: (SEP, 30),
        2018: (OCT, 19),
        2019: (OCT, 8),
        2020: (OCT, 26),
        2021: (OCT, 15),
        2022: (OCT, 5),
        2023: (OCT, 24),
        2024: (OCT, 12),
        2025: (OCT, 2),
    }


class BhutanTibetanHolidays:
    BUDDHA_FIRST_SERMON_DATES = {
        2007: (JUL, 18),
        2008: (AUG, 5),
        2009: (JUL, 25),
        2010: (JUL, 15),
        2011: (AUG, 3),
        2012: (JUL, 23),
        2013: (JUL, 12),
        2014: (JUL, 31),
        2015: (JUL, 20),
        2016: (JUL, 8),
        2017: (JUL, 27),
        2018: (JUL, 16),
        2019: (AUG, 4),
        2020: (JUL, 24),
        2021: (JUL, 14),
        2022: (AUG, 1),
        2023: (JUL, 21),
        2024: (JUL, 10),
        2025: (JUL, 28),
        2026: (JUL, 18),
        2027: (AUG, 6),
        2028: (JUL, 25),
        2029: (JUL, 15),
        2030: (AUG, 3),
        2031: (JUL, 23),
        2032: (JUL, 11),
        2033: (JUL, 30),
        2034: (JUL, 19),
        2035: (JUL, 9),
        2036: (JUL, 27),
        2037: (JUL, 16),
        2038: (AUG, 4),
        2039: (JUL, 25),
        2040: (JUL, 13),
        2041: (AUG, 1),
        2042: (JUL, 21),
        2043: (JUL, 10),
        2044: (JUL, 28),
        2045: (JUL, 18),
        2046: (AUG, 6),
        2047: (JUL, 26),
        2048: (JUL, 15),
        2049: (AUG, 3),
        2050: (JUL, 23),
        2051: (JUL, 12),
        2052: (JUL, 29),
        2053: (JUL, 19),
        2054: (JUL, 9),
        2055: (JUL, 28),
        2056: (JUL, 16),
        2057: (AUG, 4),
        2058: (JUL, 24),
        2059: (JUL, 13),
        2060: (JUL, 31),
        2061: (JUL, 20),
        2062: (JUL, 10),
        2063: (JUL, 29),
        2064: (JUL, 18),
        2065: (AUG, 6),
        2066: (JUL, 26),
        2067: (JUL, 15),
        2068: (AUG, 2),
        2069: (JUL, 22),
        2070: (JUL, 11),
        2071: (JUL, 30),
        2072: (JUL, 19),
        2073: (AUG, 7),
        2074: (JUL, 28),
        2075: (JUL, 17),
        2076: (AUG, 4),
        2077: (JUL, 24),
        2078: (JUL, 13),
        2079: (AUG, 1),
        2080: (JUL, 20),
        2081: (JUL, 10),
        2082: (JUL, 29),
        2083: (JUL, 18),
        2084: (AUG, 5),
        2085: (JUL, 25),
        2086: (JUL, 15),
        2087: (AUG, 2),
        2088: (JUL, 22),
        2089: (JUL, 11),
        2090: (JUL, 30),
        2091: (JUL, 20),
        2092: (AUG, 7),
        2093: (JUL, 27),
        2094: (JUL, 16),
        2095: (AUG, 4),
        2096: (JUL, 23),
        2097: (JUL, 13),
        2098: (JUL, 31),
        2099: (JUL, 21),
        2100: (JUL, 11),
    }

    DESCENDING_DAY_OF_LORD_BUDDHA_DATES = {
        2007: (NOV, 1),
        2008: (NOV, 19),
        2009: (NOV, 9),
        2010: (OCT, 29),
        2011: (NOV, 17),
        2012: (NOV, 6),
        2013: (OCT, 26),
        2014: (NOV, 14),
        2015: (NOV, 3),
        2016: (NOV, 20),
        2017: (NOV, 10),
        2018: (OCT, 31),
        2019: (NOV, 19),
        2020: (NOV, 7),
        2021: (OCT, 27),
        2022: (NOV, 15),
        2023: (NOV, 4),
        2024: (NOV, 22),
        2025: (NOV, 11),
        2026: (NOV, 1),
        2027: (NOV, 20),
        2028: (NOV, 9),
        2029: (OCT, 29),
        2030: (NOV, 17),
        2031: (NOV, 6),
        2032: (OCT, 25),
        2033: (NOV, 13),
        2034: (NOV, 2),
        2035: (NOV, 21),
        2036: (NOV, 10),
        2037: (OCT, 31),
        2038: (NOV, 19),
        2039: (NOV, 8),
        2040: (OCT, 27),
        2041: (NOV, 15),
        2042: (NOV, 4),
        2043: (NOV, 23),
        2044: (NOV, 11),
        2045: (NOV, 1),
        2046: (NOV, 20),
        2047: (NOV, 9),
        2048: (OCT, 29),
        2049: (NOV, 16),
        2050: (NOV, 5),
        2051: (NOV, 24),
        2052: (NOV, 13),
        2053: (NOV, 2),
        2054: (NOV, 21),
        2055: (NOV, 11),
        2056: (OCT, 30),
        2057: (NOV, 18),
        2058: (NOV, 7),
        2059: (OCT, 27),
        2060: (NOV, 14),
        2061: (NOV, 4),
        2062: (NOV, 23),
        2063: (NOV, 12),
        2064: (NOV, 1),
        2065: (NOV, 20),
        2066: (NOV, 9),
        2067: (OCT, 29),
        2068: (NOV, 16),
        2069: (NOV, 5),
        2070: (NOV, 24),
        2071: (NOV, 14),
        2072: (NOV, 2),
        2073: (NOV, 21),
        2074: (NOV, 11),
        2075: (OCT, 31),
        2076: (NOV, 17),
        2077: (NOV, 7),
        2078: (OCT, 27),
        2079: (NOV, 15),
        2080: (NOV, 4),
        2081: (NOV, 23),
        2082: (NOV, 12),
        2083: (NOV, 1),
        2084: (NOV, 19),
        2085: (NOV, 8),
        2086: (OCT, 28),
        2087: (NOV, 16),
        2088: (NOV, 5),
        2089: (NOV, 24),
        2090: (NOV, 14),
        2091: (NOV, 3),
        2092: (NOV, 21),
        2093: (NOV, 10),
        2094: (OCT, 30),
        2095: (NOV, 18),
        2096: (NOV, 6),
        2097: (OCT, 27),
        2098: (NOV, 15),
        2099: (NOV, 5),
        2100: (NOV, 24),
    }

    THIMPHU_DRUBCHEN_DATES = {
        2007: (SEP, 17),
        2008: (OCT, 5),
        2009: (SEP, 24),
        2010: (SEP, 13),
        2011: (OCT, 2),
        2012: (SEP, 21),
        2013: (SEP, 11),
        2014: (SEP, 30),
        2015: (SEP, 19),
        2016: (OCT, 7),
        2017: (SEP, 26),
        2018: (SEP, 15),
        2019: (OCT, 4),
        2020: (SEP, 23),
        2021: (SEP, 12),
        2022: (OCT, 1),
        2023: (SEP, 21),
        2024: (SEP, 10),
        2025: (SEP, 29),
        2026: (SEP, 18),
        2027: (OCT, 6),
        2028: (SEP, 24),
        2029: (SEP, 13),
        2030: (OCT, 2),
        2031: (SEP, 21),
        2032: (SEP, 10),
        2033: (SEP, 29),
        2034: (SEP, 18),
        2035: (OCT, 7),
        2036: (SEP, 25),
        2037: (SEP, 15),
        2038: (OCT, 4),
        2039: (SEP, 23),
        2040: (SEP, 12),
        2041: (OCT, 1),
        2042: (SEP, 20),
        2043: (SEP, 9),
        2044: (SEP, 28),
        2045: (SEP, 17),
        2046: (OCT, 5),
        2047: (SEP, 25),
        2048: (SEP, 13),
        2049: (OCT, 2),
        2050: (SEP, 22),
        2051: (SEP, 11),
        2052: (SEP, 29),
        2053: (SEP, 18),
        2054: (OCT, 7),
        2055: (SEP, 26),
        2056: (SEP, 15),
        2057: (OCT, 4),
        2058: (SEP, 23),
        2059: (SEP, 13),
        2060: (OCT, 1),
        2061: (SEP, 20),
        2062: (OCT, 8),
        2063: (SEP, 27),
        2064: (SEP, 16),
        2065: (OCT, 5),
        2066: (SEP, 25),
        2067: (SEP, 14),
        2068: (OCT, 2),
        2069: (SEP, 21),
        2070: (SEP, 10),
        2071: (SEP, 29),
        2072: (SEP, 17),
        2073: (OCT, 6),
        2074: (SEP, 26),
        2075: (SEP, 16),
        2076: (OCT, 4),
        2077: (SEP, 23),
        2078: (SEP, 12),
        2079: (OCT, 1),
        2080: (SEP, 19),
        2081: (OCT, 8),
        2082: (SEP, 27),
        2083: (SEP, 17),
        2084: (OCT, 5),
        2085: (SEP, 25),
        2086: (SEP, 14),
        2087: (OCT, 3),
        2088: (SEP, 21),
        2089: (SEP, 10),
        2090: (SEP, 29),
        2091: (SEP, 18),
        2092: (OCT, 6),
        2093: (SEP, 26),
        2094: (SEP, 16),
        2095: (OCT, 4),
        2096: (SEP, 22),
        2097: (SEP, 11),
        2098: (SEP, 30),
        2099: (SEP, 20),
        2100: (OCT, 9),
    }

    THIMPHU_TSHECHU_DATES = {
        2007: (SEP, 22),
        2008: (OCT, 9),
        2009: (SEP, 28),
        2010: (SEP, 17),
        2011: (OCT, 6),
        2012: (SEP, 25),
        2013: (SEP, 14),
        2014: (OCT, 3),
        2015: (SEP, 23),
        2016: (OCT, 11),
        2017: (SEP, 30),
        2018: (SEP, 19),
        2019: (OCT, 8),
        2020: (SEP, 26),
        2021: (SEP, 15),
        2022: (OCT, 4),
        2023: (SEP, 24),
        2024: (SEP, 13),
        2025: (OCT, 2),
        2026: (SEP, 21),
        2027: (OCT, 10),
        2028: (SEP, 28),
        2029: (SEP, 17),
        2030: (OCT, 6),
        2031: (SEP, 26),
        2032: (SEP, 14),
        2033: (OCT, 3),
        2034: (SEP, 23),
        2035: (OCT, 11),
        2036: (SEP, 30),
        2037: (SEP, 19),
        2038: (OCT, 7),
        2039: (SEP, 27),
        2040: (SEP, 16),
        2041: (OCT, 5),
        2042: (SEP, 24),
        2043: (SEP, 14),
        2044: (OCT, 1),
        2045: (SEP, 20),
        2046: (OCT, 9),
        2047: (SEP, 28),
        2048: (SEP, 17),
        2049: (OCT, 6),
        2050: (SEP, 26),
        2051: (SEP, 15),
        2052: (OCT, 3),
        2053: (SEP, 22),
        2054: (OCT, 11),
        2055: (SEP, 30),
        2056: (SEP, 18),
        2057: (OCT, 7),
        2058: (SEP, 27),
        2059: (SEP, 17),
        2060: (OCT, 5),
        2061: (SEP, 24),
        2062: (OCT, 13),
        2063: (OCT, 2),
        2064: (SEP, 20),
        2065: (OCT, 9),
        2066: (SEP, 28),
        2067: (SEP, 18),
        2068: (OCT, 6),
        2069: (SEP, 25),
        2070: (SEP, 15),
        2071: (OCT, 3),
        2072: (SEP, 21),
        2073: (OCT, 10),
        2074: (SEP, 30),
        2075: (SEP, 19),
        2076: (OCT, 7),
        2077: (SEP, 26),
        2078: (SEP, 16),
        2079: (OCT, 4),
        2080: (SEP, 22),
        2081: (OCT, 11),
        2082: (SEP, 30),
        2083: (SEP, 20),
        2084: (OCT, 8),
        2085: (SEP, 27),
        2086: (SEP, 17),
        2087: (OCT, 5),
        2088: (SEP, 24),
        2089: (SEP, 14),
        2090: (OCT, 2),
        2091: (SEP, 21),
        2092: (OCT, 10),
        2093: (SEP, 29),
        2094: (SEP, 19),
        2095: (OCT, 7),
        2096: (SEP, 25),
        2097: (SEP, 15),
        2098: (OCT, 3),
        2099: (SEP, 22),
        2100: (OCT, 11),
    }
