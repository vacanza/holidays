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

from holidays.constants import JAN, MAR, JUL, AUG, NOV
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import IslamicHolidays, InternationalHolidays


class Morocco(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    Moroccan holidays
    Note that holidays falling on a sunday is "lost",
    it will not be moved to another day to make up for the collision.

    Holidays after 2020: the following four moving date holidays whose exact
    date is announced yearly are estimated (and so denoted):
    - Eid El Fetr
    - Eid El Adha
    - 1er Moharram
    - Aid al Mawlid Annabawi
    Primary sources:
    https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Maroc
    https://www.mmsp.gov.ma/fr/pratiques.aspx?id=38
    """

    country = "MA"

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self._add_new_years_day("Nouvel an - Premier janvier")

        # Independence Manifesto Day post 1944
        if year >= 1945:
            self._add_holiday(
                "Commémoration de la présentation "
                "du manifeste de l'indépendance",
                JAN,
                11,
            )

        # Labor day
        self._add_labor_day("Fête du Travail")

        # Throne day
        if year >= 2001:
            dt = (JUL, 30)
        elif year >= 1963:
            dt = (MAR, 3)
        else:
            dt = (NOV, 18)
        self._add_holiday("Fête du Trône", *dt)

        # Oued Ed-Dahab Day
        self._add_holiday("Journée de Oued Ed-Dahab", AUG, 14)

        # Revolution Day
        self._add_holiday(
            "Commémoration de la révolution du Roi et du peuple", AUG, 20
        )

        # Youth day
        if year >= 2001:
            self._add_holiday("Fête de la jeunesse", AUG, 21)
        else:
            self._add_holiday("Fête du Trône", JUL, 9)

        # Green March
        if year >= 1976:
            self._add_holiday("Marche verte", NOV, 6)

        # Independance day
        if year >= 1957:
            self._add_holiday("Fête de l'indépendance", NOV, 18)

        # Eid al-Fitr - Feast Festive
        # date of observance is announced yearly, This is an estimate since
        # having the Holiday on Weekend does change the number of days,
        # deceided to leave it since marking a Weekend as a holiday
        # wouldn't do much harm.
        name = "Eid al-Fitr"
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)

        # Eid al-Adha - Sacrifice Festive
        # date of observance is announced yearly
        name = "Eid al-Adha"
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)

        # Islamic New Year - (hijari_year, 1, 1)
        self._add_islamic_new_year_day("1er Moharram")

        # Prophet Muhammad's Birthday - (hijari_year, 3, 12)
        name = "Aid al Mawlid Annabawi"
        self._add_mawlid_day(name)
        self._add_mawlid_day_two(name)


class MA(Morocco):
    pass


class MOR(Morocco):
    pass
