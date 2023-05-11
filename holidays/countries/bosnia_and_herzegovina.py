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
#  Copyright: Kateryna Golovanova <kate@kgthreads.com>, 2022

from datetime import timedelta as td

from holidays.calendars import GREGORIAN_CALENDAR, JULIAN_CALENDAR
from holidays.constants import JAN, MAR, NOV
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, IslamicHolidays
from holidays.holiday_groups import InternationalHolidays


class BosniaAndHerzegovina(
    HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays
):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Bosnia_and_Herzegovina
    https://www.paragraf.ba/neradni-dani-fbih.html
    https://www.paragraf.ba/neradni-dani-republike-srpske.html
    https://www.paragraf.ba/neradni-dani-brcko.html
    """

    country = "BA"
    subdivisions = (
        "BD",
        "FBiH",
        "RS",
    )

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # Orthodox Christmas
        self._add_christmas_day("Božić (Божић)")

        # Orthodox Good Friday
        self._add_good_friday("Veliki Petak (Pravoslavni)")

        # Labor Day
        may_1 = self._add_labor_day("Dan rada")
        self._add_holiday("Drugi dan Dana rada", may_1 + td(days=+1))

        if self.observed and self._is_sunday(may_1):
            self._add_holiday("Treći dan Dana rada", may_1 + td(days=+2))

        # Catholic Easter Monday
        self._add_easter_monday(
            "Uskrsni ponedjeljak (Katolički)", GREGORIAN_CALENDAR
        )

        # Catholic Christmas
        self._add_christmas_day("Božić (Katolički)", GREGORIAN_CALENDAR)

        # Eid al-Fitr
        self._add_eid_al_fitr_day("Ramazanski Bajram")

        # Eid ul-Adha
        self._add_eid_al_adha_day("Kurban Bajram")

    def _add_subdiv_holidays(self):
        # New Year's Day
        jan_1 = self._add_new_years_day("Nova Godina")
        self._add_new_years_day_two("Drugi dan Nove Godine")
        if (
            self.subdiv in {"FBiH", "BD"}
            and self.observed
            and self._is_sunday(jan_1)
        ):
            self._add_new_years_day_three("Treći dan Nove Godine")

        super()._add_subdiv_holidays()

    def _add_subdiv_bd_holidays(self):
        # Day of establishment of Brčko District
        self._add_holiday("Dan uspostavljanja Brčko distrikta", MAR, 8)

    def _add_subdiv_fbih_holidays(self):
        # Orthodox Christmas Eve
        self._add_christmas_eve("Pravoslavno Badnje veče")

        # Independence Day
        self._add_holiday("Dan nezavisnosti", MAR, 1)

        # Orthodox Easter
        self._add_easter_sunday("Vaskrs (Pravoslavni)")

        # Orthodox Easter Monday
        self._add_easter_monday("Uskrsni ponedjeljak (Pravoslavni)")

        # Victory Day
        self._add_world_war_two_victory_day("Dan pobjede nad fašizmom")

        # Statehood Day
        self._add_holiday("Dan državnosti", NOV, 25)

        # Catholic Good Friday
        self._add_good_friday("Veliki Petak (Katolički)", GREGORIAN_CALENDAR)

        # Catholic Easter
        self._add_easter_sunday("Uskrs (Katolički)", GREGORIAN_CALENDAR)

        # Catholic Christmas Eve
        self._add_christmas_eve("Badnji dan (Katolički)", GREGORIAN_CALENDAR)

        # Eid al-Fitr, day 2
        self._add_eid_al_fitr_day_two("Drugi Dan Ramazanski Bajram")

        # Eid ul-Adha, day 2
        self._add_eid_al_adha_day_two("Drugi Dan Kurban Bajram")

    def _add_subdiv_rs_holidays(self):
        # Orthodox Christmas Eve
        self._add_christmas_eve("Pravoslavno Badnje veče")

        # Orthodox New Year
        self._add_holiday("Pravoslavna Nova Godina", JAN, 14)

        # Orthodox Easter
        self._add_easter_sunday("Vaskrs (Pravoslavni)")

        # Orthodox Easter Monday
        self._add_easter_monday("Uskrsni ponedjeljak (Pravoslavni)")

        # Victory Day
        self._add_world_war_two_victory_day("Dan pobjede nad fašizmom")

        # Dayton Agreement Day
        self._add_holiday(
            (
                "Dan uspostave Opšteg okvirnog sporazuma za mir u "
                "Bosni i Hercegovini"
            ),
            NOV,
            21,
        )

        # Catholic Good Friday
        self._add_good_friday("Veliki Petak (Katolički)", GREGORIAN_CALENDAR)

        # Catholic Easter
        self._add_easter_sunday("Uskrs (Katolički)", GREGORIAN_CALENDAR)

        # Catholic Christmas Eve
        self._add_christmas_eve("Badnji dan (Katolički)", GREGORIAN_CALENDAR)

        # Eid al-Fitr, day 2
        self._add_eid_al_fitr_day_two("Drugi Dan Ramazanski Bajram")

        # Eid ul-Adha, day 2
        self._add_eid_al_adha_day_two("Drugi Dan Kurban Bajram")


class BA(BosniaAndHerzegovina):
    pass


class BIH(BosniaAndHerzegovina):
    pass
