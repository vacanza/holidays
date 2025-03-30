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

from holidays.calendars.gregorian import FEB
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class IvoryCoast(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """Ivory Coast holidays.

    References:
        * <https://natlex.ilo.org/dyn/natlex2/r/natlex/fe/details?p3_isn=44374>
        * <https://www.droit-afrique.com/uploads/RCI-Decret-1996-205-jours-feries.pdf>
        * <https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_en_C%C3%B4te_d%27Ivoire>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Ivory_Coast>
        * <https://www.timeanddate.com/holidays/ivory-coast/>
        * <https://holidayapi.com/countries/ci/>
        * National Peace Day (introduced in 1996):
            * <https://en.wikipedia.org/wiki/C%C3%B4te_d%27Ivoire#History>

    Note:
        In Islamic calendar, days begin at sunset. The naming convention "day after" refers
        to the daylight hours following the night of the celebration, which is technically
        the same Gregorian calendar day.
    """

    country = "CI"
    # %s (estimated).
    estimated_label = tr("%s (estimé)")
    # Day after the %s.
    observed_label = tr("Lendemain de la %s")
    # Day after the %s (estimated).
    observed_estimated_label = tr("Lendemain de la %s (estimé)")
    # Ivory Coast gained independence in 1960.
    start_year = 1961
    default_language = "fr"
    supported_languages = ("en_CI", "en_US", "fr")

    def __init__(self, islamic_show_estimated: bool = False, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        # the observed dates for the Ivory Coast's islamic holidays have been verified against
        # local references (COSIM) and align with the default Umm al-Qura calculations.
        IslamicHolidays.__init__(self, show_estimated=islamic_show_estimated)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, IvoryCoastStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Secular Holidays.

        # New Year's Day.
        self._add_new_years_day(tr("1er janvier"))

        # Labor Day.
        self._add_observed(self._add_labor_day(tr("Fête du travail")))

        # Independence Day.
        self._add_observed(self._add_holiday_aug_7(tr("Fête Nationale")))

        if self._year >= 1996:
            # National Peace Day.
            self._add_holiday_nov_15(tr("Journée Nationale de la Paix"))

        if 1996 <= self._year <= 2000:
            self._add_holiday_dec_7(
                # Anniversary of death of President Felix Houphouet-Boigny.
                tr("Anniversaire du décès du Président Felix Houphouet-Boigny")
            )

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
        self._add_eid_al_fitr_day(tr("Fête de fin du Ramadan"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Fête de la Tabaski"))

        # Day after Prophet's Birthday.
        self._add_mawlid_day(tr("Lendemain de l’Anniversaire de la Naissance du Prophète Mahomet"))

        # Day after Night of Power.
        self._add_laylat_al_qadr_day(tr("Lendemain de la Nuit du Destin"))


class CI(IvoryCoast):
    pass


class CIV(IvoryCoast):
    pass


class IvoryCoastStaticHolidays:
    """Ivory Coast special holidays.

    References:
        * [2024 AFCON](https://apanews.net/public-holiday-as-cote-divoire-wins-afcon-trophy/)
    """

    special_public_holidays = {
        # 2024 African Cup of Nations Victory.
        2024: (FEB, 12, tr("Victoire à la Coupe d’Afrique des Nations 2024")),
    }
