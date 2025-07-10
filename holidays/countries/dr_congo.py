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
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_PREV_SAT


class DRCongo(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Democratic Republic of the Congo holidays.

    References:
        * [Public holidays in the Democratic Republic of the Congo](https://en.wikipedia.org/wiki/Public_holidays_in_the_Democratic_Republic_of_the_Congo)
        * [ORDONNANCE 79-154](https://web.archive.org/web/20220329181351/http://www.leganet.cd/Legislation/DroitSocial/O.79.154.23.06.1979.htm)
        * [Ordonnance n° 14/010](https://web.archive.org/web/20230419184344/http://leganet.cd/Legislation/Divers/Ordonnance.14.10.14.mai.2014.htm)
        * [Ordonnance n° 23-042](https://web.archive.org/web/20250113230411/http://www.droitcongolais.info/files/143.03.23_Ordonnance-du-30-mars-2023_jours-feries.pdf)
        * [LEGANET.CD](https://web.archive.org/web/20250104233847/https://www.leganet.cd/Legislation/Droit%20administratif/Urbanismevoiries/Div/L.009.05.08.2002.htm)
    """

    country = "CD"
    default_language = "fr"
    # %s (observed).
    observed_label = tr("%s (observé)")
    supported_languages = ("en_US", "fr")
    # ORDONNANCE 79-154.
    start_year = 1980

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SUN_TO_PREV_SAT)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Nouvel an"))

        # Established on May 10th, 2014 via Ordonnance n° 14/010.
        if self._year >= 2015:
            # Martyrs of Independence.
            self._add_holiday_jan_4(tr("Martyrs de l'indépendance"))

            # National Hero Laurent Désiré Kabila Day.
            self._add_holiday_jan_16(tr("Journée du héros national Laurent Désiré Kabila"))

            # National Hero Patrice Emery Lumumba Day.
            self._add_holiday_jan_17(tr("Journée du héros national Patrice Emery Lumumba"))

        # Established on March 30th, 2023 via Ordonnance n° 23-042.
        if self._year >= 2023:
            self._add_holiday_apr_6(
                # Day of the Struggle of Simon Kimbangu and African Consciousness.
                tr("Journée du combat de Simon Kimbangu et de la conscience africaine")
            )

        # Labor Day.
        self._add_labor_day(tr("Fête du travail"))

        if self._year >= 1998:
            self._add_holiday_may_17(
                # Armed Forces Day.
                tr("Journée des Forces armées")
                if self._year >= 2019
                # Liberation Day.
                else tr("Jour de la Libération")
            )

        # Independence Day.
        self._add_holiday_jun_30(tr("Journée de l’indépendance"))

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
