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

from datetime import timedelta as td
from gettext import gettext as tr

from holidays.constants import MAR, APR, MAY, JUN, JUL, SEP, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class France(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Official French holidays.

    Some provinces have specific holidays, only those are included in the
    PROVINCES, because these provinces have different administrative status,
    which makes it difficult to enumerate.

    For religious holidays usually happening on Sundays (Easter, Pentecost),
    only the following Monday is considered a holiday.

    Primary sources:
        https://fr.wikipedia.org/wiki/Fêtes_et_jours_fériés_en_France
        https://www.service-public.fr/particuliers/vosdroits/F2405
    """

    country = "FR"
    default_language = "fr"
    subdivisions = [
        "Alsace-Moselle",
        "Guadeloupe",
        "Guyane",
        "La Réunion",
        "Martinique",
        "Mayotte",
        "Métropole",
        "Nouvelle-Calédonie",
        "Polynésie Française",
        "Saint-Barthélémy",
        "Saint-Martin",
        "Wallis-et-Futuna",
    ]

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # Civil holidays

        if year >= 1811:
            # New Year's Day.
            self._add_new_years_day(tr("Jour de l'an"))

        if year >= 1919:
            self._add_labor_day(
                # Labor Day.
                tr("Fête du Travail")
                if year >= 1948
                # Labor and Social Concord Day.
                else tr("Fête du Travail et de la Concorde sociale")
            )

        if 1953 <= year <= 1959 or year >= 1982:
            # Victory Day.
            self._add_holiday(tr("Fête de la Victoire"), MAY, 8)

        if year >= 1880:
            # National Day.
            self._add_holiday(tr("Fête nationale"), JUL, 14)

        if year >= 1918:
            # Armistice Day.
            self._add_holiday(tr("Armistice"), NOV, 11)

        # Religious holidays

        if self.subdiv in {
            "Alsace-Moselle",
            "Guadeloupe",
            "Martinique",
            "Polynésie Française",
        }:
            # Good Friday.
            self._add_good_friday(tr("Vendredi saint"))

        if self.subdiv == "Guadeloupe":
            self._add_holiday(
                # Mi-Careme.
                tr("Mi-Carême"),
                self._easter_sunday + td(days=-24),
            )

        if year >= 1886:
            # Easter Monday.
            self._add_easter_monday(tr("Lundi de Pâques"))

            if year not in {2005, 2006, 2007}:
                # Whit Monday.
                self._add_whit_monday(tr("Lundi de Pentecôte"))

        if year >= 1802:
            # Ascension Day.
            self._add_ascension_thursday(tr("Ascension"))
            # Assumption Day.
            self._add_assumption_of_mary_day(tr("Assomption"))
            # All Saints' Day.
            self._add_all_saints_day(tr("Toussaint"))
            # Christmas Day.
            self._add_christmas_day(tr("Noël"))

        # Non-metropolitan holidays

        if self.subdiv in {"Guadeloupe", "Martinique"}:
            # Feast of Victor Schoelcher.
            self._add_holiday(tr("Fête de Victor Schoelcher"), JUL, 21)

        # Abolition of slavery.
        abolition_name = tr("Abolition de l'esclavage")

        if self.subdiv == "Alsace-Moselle":
            # Saint Stephen's Day.
            self._add_christmas_day_two(tr("Saint Étienne"))

        elif self.subdiv == "Guadeloupe":
            self._add_holiday(abolition_name, MAY, 27)

        elif self.subdiv == "Guyane":
            self._add_holiday(abolition_name, JUN, 10)

        elif self.subdiv == "La Réunion" and year >= 1981:
            self._add_holiday(abolition_name, DEC, 20)

        elif self.subdiv == "Martinique":
            self._add_holiday(abolition_name, MAY, 22)

        elif self.subdiv == "Mayotte":
            self._add_holiday(abolition_name, APR, 27)

        elif self.subdiv == "Nouvelle-Calédonie":
            # Citizenship Day.
            self._add_holiday(tr("Fête de la Citoyenneté"), SEP, 24)

        elif self.subdiv == "Polynésie Française":
            # Missionary Day.
            self._add_holiday(tr("Arrivée de l'Évangile"), MAR, 5)
            # Internal Autonomy Day.
            self._add_holiday(tr("Fête de l'autonomie"), JUN, 29)

        elif self.subdiv == "Saint-Barthélémy":
            self._add_holiday(abolition_name, OCT, 9)

        elif self.subdiv == "Saint-Martin" and year >= 2018:
            self._add_holiday(abolition_name, MAY, 28)

        elif self.subdiv == "Wallis-et-Futuna":
            # Feast of Saint Peter Chanel.
            self._add_holiday(tr("Saint Pierre Chanel"), APR, 28)
            # Festival of the territory
            self._add_holiday(tr("Fête du Territoire"), JUL, 29)


# *Warning* FR is also used by dateutil (Friday), so be careful with its use
class FR(France):
    pass


class FRA(France):
    pass
