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

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV
from holidays.constants import OPTIONAL, PUBLIC
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
)
from holidays.observed_holiday_base import HolidayBase


class Togo(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Togo

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Togo>
        * <https://www.timeanddate.com/holidays/togo/>
        * <https://www.goethe.de/ins/tg/fr/ueb/fer.html>
        * <https://www.republiquetogolaise.com/politique/2309-3579-23-septembre-le-togo-rend-hommage-a-ses-martyrs>
        * <https://islam.zmo.de/s/westafrica/item/25841#?xywh=-485%2C-94%2C2537%2C1868>
        * <https://en.wikipedia.org/wiki/1986_Togolese_coup_attempt>
        * <https://www.rfi.fr/fr/afrique/20140112-togo-le-13-janvier-est-plus-jour-fete>
        * <https://fr.wikipedia.org/wiki/Coup_d%27%C3%89tat_de_1967_au_Togo>
        * <https://islam.zmo.de/s/afrique_ouest/item/25800#?xywh=-1743%2C-1%2C4506%2C2362>
        * <https://www.republiquetogolaise.com/politique/2501-10232-le-togo-a-commemore-le-51eme-anniversaire-de-l-attentat-de-sarakawa>

        Ramadan start dates:
        * <https://www.republicoftogo.com/toutes-les-rubriques/societe/le-mois-du-jeune-debute-le-18-juin>
        * <https://www.republicoftogo.com/toutes-les-rubriques/societe/le-ramadan-debute-le-6-juin>
        * <https://www.tf1info.fr/societe/le-ramadan-2017-1438-commence-le-samedi-27-mai-comment-la-date-du-debut-du-jeune-est-elle-fixee-1512235.html>
        * <https://www.republicoftogo.com/toutes-les-rubriques/societe/debut-du-ramadan-demain>
        * <https://www.republiquetogolaise.com/social/0605-3100-la-communaute-musulmane-du-togo-entame-ce-lundi-le-jeune-du-mois-de-ramadan>
        * <https://www.republiquetogolaise.com/culture/2404-4278-debut-du-mois-de-ramadan>
        * <https://www.republiquetogolaise.com/culture/1304-5393-debut-du-mois-de-ramadan>
        * <https://www.republiquetogolaise.com/culture/0304-6745-debut-du-mois-de-ramadan>
        * <https://www.republiquetogolaise.com/culture/2303-7864-debut-du-mois-de-ramadan>
        * <https://www.republiquetogolaise.com/culture/1103-9017-debut-du-mois-de-ramadan>
        * <https://www.republiquetogolaise.com/culture/2802-10360-le-jeune-de-ramadan-debute-le-1er-mars>
    """

    country = "TG"
    default_language = "fr"
    supported_categories = (OPTIONAL, PUBLIC)
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    supported_languages = ("fr",)
    # Togo gained independence on April 27, 1960.
    start_year = 1960

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=TogoIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Jour de l'an"))

        if self._year >= 1967 and self._year < 2014:
            # Liberation Day.
            self._add_holiday_jan_13(tr("Fête de la libération nationale"))

        # Good Friday.
        self._add_good_friday(tr("Vendredi saint"))

        # Easter Monday.
        self._add_easter_monday(tr("Lundi de Pâques"))

        # Independence Day.
        self._add_holiday_apr_27(tr("Fête de l'indépendance"))

        # Labor Day.
        self._add_holiday_may_1(tr("Fête du travail"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Fête de l'Ascension"))

        # Whit Monday.
        self._add_whit_monday(tr("Lundi de Pentecôte"))

        # Martyrs' Day.
        self._add_holiday_jun_21(tr("Fête des Martyrs"))

        # Assumption Day.
        self._add_holiday_aug_15(tr("Assomption"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Toussaint"))

        # Christmas Day.
        self._add_christmas_day(tr("Noël"))

        # First Day of Ramadan.
        self._add_ramadan_beginning_day(tr("Ramadan"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("l'Aïd El-Fitr"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Tabaski"))

    def _populate_optional_holidays(self):
        # Prophet Mohammed's Birthday.
        self._add_mawlid_day(tr("Journée anniversaire de la naissance du prophète Mohamed à Lomé"))

        if self._year >= 1987:
            # Anniversary of the Failed Attack on Lomé.
            self._add_holiday_sep_24(tr("Anniversaire de l'attentat manqué contre Lomé"))


class TG(Togo):
    pass


class TGO(Togo):
    pass


class TogoIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2010: (NOV, 17),
        2011: (NOV, 7),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 13),
        2017: (SEP, 2),
        2018: (AUG, 22),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 16),
        2025: (JUN, 7),
    }

    EID_AL_FITR_DATES = {
        2010: (SEP, 10),
        2011: (AUG, 31),
        2012: (AUG, 19),
        2013: (AUG, 8),
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 21),
        2024: (APR, 10),
        2025: (MAR, 30),
    }

    MAWLID_DATES = {
        2020: (OCT, 29),
        2021: (OCT, 19),
        2022: (OCT, 8),
        2023: (SEP, 27),
        2024: (SEP, 16),
        2025: (SEP, 5),
    }

    RAMADAN_BEGINNING_DATES = {
        2015: (JUN, 18),
        2016: (JUN, 6),
        2017: (MAY, 27),
        2018: (MAY, 17),
        2019: (MAY, 6),
        2020: (APR, 24),
        2021: (APR, 13),
        2022: (APR, 2),
        2023: (MAR, 23),
        2024: (MAR, 11),
        2025: (MAR, 1),
    }
