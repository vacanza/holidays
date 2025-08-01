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
    """

    country = "BT"
    # Jigme Khesar Namgyel Wangchuck ascended to the throne on December 9th, 2006.
    start_year = 2007
    subdivisions = (
        "15",  # Thimphu.
    )
    subdivisions_aliases = {
        "Thimphu": "15",
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
