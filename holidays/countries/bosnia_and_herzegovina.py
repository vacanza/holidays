#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)
#  Copyright: Kateryna Golovanova <kate@kgthreads.com>, 2022

from dateutil.relativedelta import relativedelta as rd

from holidays.constants import SUN, JAN, MAR, JUN, NOV, JULIAN_CALENDAR
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, IslamicHolidays
from holidays.holiday_groups import InternationalHolidays


class BosniaAndHerzegovina(
    HolidayBase, ChristianHolidays, IslamicHolidays, InternationalHolidays
):
    """
    Bosnia and Herzegovina holidays.
    See https://en.wikipedia.org/wiki/Public_holidays_in_Bosnia_and_Herzegovina
    for details.
    """

    country = "BA"
    subdivisions = [
        "BD",
        "FBiH",
        "RS",
    ]

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)

        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        jan_1 = self._add_new_years_day("Nova Godina")
        self._add_new_years_day_two("Drugi dan Nove Godine")

        if self.observed and jan_1.weekday() == SUN:
            self._add_new_years_day_three("Treći dan Nove Godine")

        # Labor Day.
        may_1 = self._add_labour_day("Dan rada")
        self._add_holiday("Drugi dan Dana rada", may_1 + rd(days=+1))

        if self.observed and may_1.weekday() == SUN:
            self._add_holiday("Treći dan Dana rada", may_1 + rd(days=+2))

        if self.subdiv == "FBiH":
            # Independence Day.
            self._add_holiday("Dan nezavisnosti", MAR, 1)

            self._add_good_friday("Veliki Petak (Katolički)")
            self._add_easter_sunday("Uskrs (Katolički)")
            self._add_easter_monday("Uskrsni ponedjeljak (Katolički)")

            self._add_feast_of_corpus_christi(
                "Tijelovo (Tijelo i Krv Kristova)"
            )

            # Eid al-Fitr.
            self._add_eid_al_fitr_day("Ramazanski Bajram")
            self._add_eid_al_fitr_day_two("Drugi Dan Ramazanski Bajram")

            # Eid ul-Adha.
            name = "Kurban Bajram"
            self._add_eid_al_adha_day(name)
            self._add_eid_al_adha_day_two(name)
            self._add_eid_al_adha_day_three(name)
            self._add_eid_al_adha_day_four(name)

            # Islamic New Year.
            self._add_islamic_new_year_day("Muslimanska Nova Godina")

            # All Saints Day.
            self._add_all_saints_day("Svi Sveti")

            # All Souls Day.
            self._add_all_souls_day("Dušni dan")

            # Statehood Day.
            self._add_holiday("Dan državnosti", NOV, 25)

            self._add_christmas_day("Božić (Katolički)")
            self._add_christmas_day_two("Stipandan (Stjepandan)")

        elif self.subdiv == "RS":
            self._set_calendar(JULIAN_CALENDAR)

            self._add_christmas_eve("Pravoslavno Badnje veče")
            self._add_christmas_day("Božić (Божић)")

            # Republic day.
            self._add_holiday("Dan Republike", JAN, 9)

            # Orthodox New Year.
            self._add_holiday("Pravoslavna Nova Godina", JAN, 14)

            # Orthodox Good Friday.
            self._add_good_friday("Veliki Petak (Pravoslavni)")
            self._add_easter_sunday("Vaskrs (Pravoslavni)")
            self._add_easter_monday("Uskrsni ponedjeljak (Pravoslavni)")

            # Victory Day.
            self._add_world_war_two_victory_day("Dan pobjede")

            # St. Vitus Day.
            self._add_holiday("Vidovdan", JUN, 28)

            # Dayton Agreement Day.
            self._add_holiday(
                "Dan uspostave Opšteg okvirnog sporazuma za mir u "
                "Bosni i Hercegovini",
                NOV,
                21,
            )


class BA(BosniaAndHerzegovina):
    pass


class BIH(BosniaAndHerzegovina):
    pass
