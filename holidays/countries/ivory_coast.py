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

from holidays.groups import ChristianHolidays, IslamicHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class IvoryCoast(ObservedHolidayBase, ChristianHolidays, IslamicHolidays, InternationalHolidays):
    """Ivory Coast holidays.

    References:
        * <https://natlex.ilo.org/dyn/natlex2/r/natlex/fe/details?p3_isn=44374>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Ivory_Coast>
        * <https://www.timeanddate.com/holidays/ivory-coast/>
        * <https://holidayapi.com/countries/ci/>
    """

    country = "CI"
    estimated_label = "%s (estimated)"
    observed_label = "%s (observed)"
    observed_estimated_label = "%s (observed, estimated)"
    # Ivory Coast gained independence in 1960.
    start_year = 1960
    default_language = "fr"
    supported_languages = ("en_US", "fr")

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        IslamicHolidays.__init__(self, show_estimated=islamic_show_estimated)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Secular Holidays
        # New Year's Day.
        self._add_new_years_day(tr("1ᵉʳ janvier"))
        # Labor Day.
        self._add_observed(self._add_labor_day(tr("Fête du travail")))
        # Independence Day
        self._add_observed(self._add_holiday_aug_7(tr("Fête Nationale")))
        if self._year >= 1996:
            # National Peace Day - November 15.
            # Introduced in 1996. See details: https://en.wikipedia.org/wiki/C%C3%B4te_d%27Ivoire#History
            self._add_holiday_nov_15(tr("Journée Nationale de la Paix"))

        # Christian Holidays
        # Easter Monday.
        self._add_easter_monday(tr("Lundi de Pâques"))
        # Ascension Day.
        self._add_ascension_thursday(tr("Jour de l’Ascension"))
        # Pentecost Monday (Whit Monday).
        self._add_whit_monday(tr("Lundi de Pentecôte"))
        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Fête de l’Assomption"))
        # All Saints' Day.
        self._add_all_saints_day(tr("Fête de la Toussaint"))
        # Christmas Day.
        self._add_christmas_day(tr("Fête de Noël"))

        # Islamic Holidays
        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Fête de fin du Ramadan (Aid-EI-Fitr)"))
        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Fête de la Tabaski (Aîd-El-Kébir)"))
        # Day after Prophet's Birthday.
        self._add_mawlid_day(tr("L’Anniversaire de la Naissance du Prophète Mahomet (Maouloud)"))
        # Night of Destiny (Laylat al-Qadr)
        self._add_laylat_al_qadr_day(tr("Nuit du Destin (Lailatou-Kadr)"))


# Aliases.
class CI(IvoryCoast):
    pass


class CIV(IvoryCoast):
    pass
