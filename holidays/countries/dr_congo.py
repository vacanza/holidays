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

from gettext import gettext as tr

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class DRCongo(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Democratic Republic of the Congo holidays.

    References:
        * Public holidays in the Democratic Republic of the Congo <https://en.wikipedia.org/wiki/Public_holidays_in_the_Democratic_Republic_of_the_Congo>
        * ORDONNANCE 79-154 <https://web.archive.org/web/20220329181351/http://www.leganet.cd/Legislation/DroitSocial/O.79.154.23.06.1979.htm>
        * Ordonnance n° 14/010 <https://web.archive.org/web/20230419184344/http://leganet.cd/Legislation/Divers/Ordonnance.14.10.14.mai.2014.htm>
        * Ordonnance n° 23-042 <https://web.archive.org/web/20250113230411/http://www.droitcongolais.info/files/143.03.23_Ordonnance-du-30-mars-2023_jours-feries.pdf>
    """

    country = "CD"
    default_language = "fr"
    supported_languages = ("en_US", "fr")
    # Democratic Republic of the Congo marks independence from Belgium in June 1960.
    start_year = 1961

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Jour de l'An"))

        # Martyrs of Independence.
        self._add_holiday_jan_4(tr("Martyrs de l’indépendance"))

        if self._year >= 2002:
            # National Hero Laurent Désiré KABILA Day.
            self._add_holiday_jan_16(tr("Journée du Héro National Laurent Désiré KABILA"))

        if self._year >= 1962:
            # National Hero Patrice Emery LUMUMBA Day.
            self._add_holiday_jan_17(tr("Journée du Héro National Patrice Emery LUMUMBA"))

        if self._year >= 2023:
            self._add_holiday_apr_6(
                # Day of the Struggle of Simon Kimbangu and African Consciousness.
                tr("Journée du combat de Simon Kimbangu et de la conscience africaine")
            )

        # Labor Day.
        self._add_labor_day(tr("Fête du Travail"))

        if self._year >= 1998:
            self._add_holiday_may_17(
                # Revolution and Armed Forces Day.
                tr("Journée de la Révolution et des Forces Armées")
                if self._year >= 2019
                # Liberation Day.
                else tr("Jour de la Libération")
            )

        # Independence Day.
        self._add_holiday_jun_30(tr("Jour de l'indépendance"))

        # Parents' Day.
        self._add_holiday_aug_1(tr("Fête des parents"))

        if self._year >= 2024:
            # Congolese Genocide Memorial Day.
            self._add_holiday_aug_2(tr("Journée commémorative du génocide Congolais"))

        # Christmas Day.
        self._add_christmas_day(tr("Noël"))


class CD(DRCongo):
    pass


class COD(DRCongo):
    pass
