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

from holidays.groups import TibetanCalendarHolidays
from holidays.holiday_base import HolidayBase


class Bhutan(HolidayBase, TibetanCalendarHolidays):
    """Bhutan holidays.

    References:
        * [ROYAL GOVERNMENT OF BHUTAN](https://web.archive.org/web/20250407140158/https://www.moha.gov.bt/wp-content/uploads/2023/11/National-Holiday-List-for-2024-2-.pdf)
        * [PHPA-II HOLIDAY LIST 2025](https://phpa2.gov.bt/holiday-list/)
        * [Public Holidays for the year 2007](https://web.archive.org/web/20070730055559/http://www.rcsc.gov.bt/tmpFolder/CalendarOfEvent/holiday.htm)
        * [The Bhutanese calendar](http://www.kalacakra.org/calendar/bhutlist.htm)
        * [ROYAL GOVERNMENT OF BHUTAN 2014-15](https://web.archive.org/web/20141222122050/http://www.mohca.gov.bt/Publications/calander_2014-15.pdf)
        * [ROYAL GOVERNMENT OF BHUTAN 2015-16](https://web.archive.org/web/20151004161522/http://www.mohca.gov.bt/Publications/calander_2015-16.pdf)
        * [ROYAL GOVERNMENT OF BHUTAN 2016-17](https://web.archive.org/web/20170606131500/http://www.mohca.gov.bt/download/calander_2016-17.pdf)
        * [ROYAL GOVERNMENT OF BHUTAN 2017-18](https://web.archive.org/web/20180107115733/http://www.mohca.gov.bt/wp-content/uploads/2017/11/calander_2017-18.pdf)
        * [ROYAL GOVERNMENT OF BHUTAN 2017-2018](https://web.archive.org/web/20180906031327/http://www.mohca.gov.bt/wp-content/uploads/2017/11/scan0126.pdf)
        * [ROYAL GOVERNMENT OF BHUTAN 2019-2020](https://web.archive.org/web/20191221201614/http://www.mohca.gov.bt/downloads/scan0004.pdf)
        * [ROYAL GOVERNMENT OF BHUTAN 2020-2021](https://web.archive.org/web/20200720030220/http://www.mohca.gov.bt/wp-content/uploads/2019/12/2020-Holiday-List0001.pdf)
        * [ROYAL GOVERNMENT OF BHUTAN 2021-2022](https://web.archive.org/web/20230511011459/http://www.mohca.gov.bt/downloads/Holidays2021.pdf)
        * [ROYAL GOVERNMENT OF BHUTAN 2022-2023](https://web.archive.org/web/20220619061040/https://www.mohca.gov.bt/wp-content/uploads/2021/11/HolidayList.pdf)
        * [ROYAL GOVERNMENT OF BHUTAN 2023](https://web.archive.org/web/20221210152039/https://www.mohca.gov.bt/wp-content/uploads/2022/11/Holidays-2023.pdf)
        * [Ministry of Home and Cultural Affairs ](https://web.archive.org/web/20100127021618/http://www.mohca.gov.bt/?mode=READMORE&news_id=157)
    """

    country = "BT"
    # Jigme Khesar Namgyel Wangchuck ascended to the throne on December 9th, 2006.
    start_year = 2007
    subdivisions = (
        "33",  # Bumthang
        "12",  # Chhukha
        "22",  # Dagana
        "GA",  # Gasa
        "13",  # Haa
        "44",  # Lhuentse
        "42",  # Monggar
        "11",  # Paro
        "43",  # Pemagatshel
        "23",  # Punakha
        "45",  # Samdrup Jongkhar
        "14",  # Samtse
        "31",  # Sarpang
        "15",  # Thimphu
        "41",  # Trashigang
        "TY",  # Trashiyangtse
        "32",  # Trongsa
        "21",  # Tsirang
        "24",  # Wangdue Phodrang
        "34",  # Zhemgang
    )

    subdivisions_aliases = {
        "Bumthang": "33",
        "Chhukha": "12",
        "Dagana": "22",
        "Gasa": "GA",
        "Haa": "13",
        "Lhuentse": "44",
        "Monggar": "42",
        "Paro": "11",
        "Pemagatshel": "43",
        "Punakha": "23",
        "Samdrup Jongkhar": "45",
        "Samtse": "14",
        "Sarpang": "31",
        "Thimphu": "15",
        "Trashigang": "41",
        "Trashiyangtse": "TY",
        "Trongsa": "32",
        "Tsirang": "21",
        "Wangdue Phodrang": "24",
        "Zhemgang": "34",
    }

    def __init__(self, *args, **kwargs):
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

        # National Day.
        self._add_holiday_dec_17("National Day")

        # Coronation of His Majesty the King.
        self._add_holiday_nov_1("Coronation of His Majesty the King")

        # Birth Anniversary of the 4th Druk Gyalpo - Constitution Day.
        self._add_holiday_nov_11("Birth Anniversary of the 4th Druk Gyalpo - Constitution Day")

        # Winter Solstice.
        self._add_tibetan_winter_solstice("Winter Solstice")

        # Traditional Day of Offering.
        self._add_day_of_offering("Traditional Day of Offering")

        # Losar.
        name = "Losar"
        self._add_losar(name)
        self._add_losar_day_two(name)

        # Death Anniversary of Zhabdrung (Zhabdrung Kuchoe).
        self._add_death_of_zhabdrung("Death Anniversary of Zhabdrung (Zhabdrung Kuchoe)")

        # Lord Buddha's Parinirvana.
        self._add_buddha_parinirvana("Lord Buddha's Parinirvana")

        # Birth Anniversary of Guru Rinpoche.
        self._add_birth_of_guru_rinpoche("Birth Anniversary of Guru Rinpoche")

        # First Sermon of Lord Buddha.
        self._add_buddha_first_sermon("First Sermon of Lord Buddha")

        # Blessed Rainy Day.
        self._add_blessed_rainy_day("Blessed Rainy Day")

        # Dassain.
        self._add_dashain("Dassain")

        # Descending Day of Lord Buddha.
        self._add_descending_day_of_lord_buddha("Descending Day of Lord Buddha")

    def _populate_subdiv_15_public_holidays(self):
        # Thimphu Drubchoe.
        self._add_thimpu_drubchen_day("Thimphu Drubchoe")

        # Thimphu Tshechu.
        name = "Thimphu Tshechu"
        self._add_thimphu_tsechu_day(name)
        self._add_thimphu_tsechu_day_two(name)
        self._add_thimphu_tsechu_day_three(name)


class BT(Bhutan):
    pass


class BTN(Bhutan):
    pass
