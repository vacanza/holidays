#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.countries.france import France
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase


class FrenchSouthernTerritories(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """French Southern Territories holidays.

    References:
        * <https://holidayapi.com/countries/tf/2022>
    """

    country = "TF"
    parent_entity = France
    default_language = "fr"
    supported_languages = ("en_US", "fr")
    # Start dates copied from France class as I didn't find any specific reference for ATF.
    start_year = 1801

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Civil holidays.
        if self._year >= 1811:
            # New Year's Day.
            self._add_new_years_day(tr("Jour de l'an"))

        if self._year >= 1919:
            self._add_labor_day(
                # Labor Day.
                tr("Fête du Travail")
                if self._year >= 1948
                # Labor and Social Concord Day.
                else tr("Fête du Travail et de la Concorde sociale")
            )

        if 1953 <= self._year <= 1959 or self._year >= 1982:
            # Victory Day.
            self._add_world_war_two_victory_day(tr("Fête de la Victoire"))

        if self._year >= 1880:
            # National Day.
            self._add_holiday_jul_14(tr("Fête nationale"))

        if self._year >= 1918:
            # Armistice Day.
            self._add_holiday_nov_11(tr("Armistice"))

        # Religious holidays.

        if self._year >= 1886:
            # Easter Monday.
            self._add_easter_monday(tr("Lundi de Pâques"))

            if self._year not in {2005, 2006, 2007}:
                # Whit Monday.
                self._add_whit_monday(tr("Lundi de Pentecôte"))

        if self._year >= 1802:
            # Ascension Day.
            self._add_ascension_thursday(tr("Ascension"))
            # Assumption Day.
            self._add_assumption_of_mary_day(tr("Assomption"))
            # All Saints' Day.
            self._add_all_saints_day(tr("Toussaint"))
            # Christmas Day.
            self._add_christmas_day(tr("Noël"))


class TF(FrenchSouthernTerritories):
    pass


class ATF(FrenchSouthernTerritories):
    pass
