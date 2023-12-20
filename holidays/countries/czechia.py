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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Czechia(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_the_Czech_Republic
    """

    country = "CZ"
    default_language = "cs"
    supported_languages = ("cs", "en_US", "sk", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        self._add_holiday_jan_1(
            # Independent Czech State Restoration Day.
            tr("Den obnovy samostatného českého státu")
            if self._year >= 2000
            # New Year's Day.
            else tr("Nový rok"),
        )

        if self._year <= 1951 or self._year >= 2016:
            # Good Friday.
            self._add_good_friday(tr("Velký pátek"))

        # Easter Monday.
        self._add_easter_monday(tr("Velikonoční pondělí"))

        if self._year >= 1951:
            # Labor Day.
            self._add_labor_day(tr("Svátek práce"))

        if self._year >= 1992:
            # Victory Day.
            self._add_holiday_may_8(tr("Den vítězství"))
        elif self._year >= 1947:
            # Day of Victory over Fascism.
            self._add_world_war_two_victory_day(tr("Den vítězství nad hitlerovským fašismem"))

        if self._year >= 1951:
            # Saints Cyril and Methodius Day.
            self._add_holiday_jul_5(tr("Den slovanských věrozvěstů Cyrila a Metoděje"))

            # Jan Hus Day.
            self._add_holiday_jul_6(tr("Den upálení mistra Jana Husa"))

        if self._year >= 2000:
            # Statehood Day.
            self._add_holiday_sep_28(tr("Den české státnosti"))

        if self._year >= 1951:
            # Independent Czechoslovak State Day.
            self._add_holiday_oct_28(tr("Den vzniku samostatného československého státu"))

        if self._year >= 1990:
            # Struggle for Freedom and Democracy Day.
            self._add_holiday_nov_17(tr("Den boje za svobodu a demokracii"))

            # Christmas Eve.
            self._add_christmas_eve(tr("Štědrý den"))

        if self._year >= 1951:
            # Christmas Day.
            self._add_christmas_day(tr("1. svátek vánoční"))

            # Second Day of Christmas.
            self._add_christmas_day_two(tr("2. svátek vánoční"))


class CZ(Czechia):
    pass


class CZE(Czechia):
    pass
