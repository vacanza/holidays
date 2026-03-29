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
from holidays.calendars.gregorian import FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.holiday_base import HolidayBase


class Gabon(
    HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """Gabon holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Gabon>
        * [Decree 600/PR-MTPS of Jul 10, 1976](https://web.archive.org/web/20260307151111/https://journal-officiel.ga/14135-600-pr-mtps/)
        * [Decree 715/PR/MTEFPRH of Apr 2, 1992](https://web.archive.org/web/20260307150611/https://journal-officiel.ga/8555-715-pr-mtefprh/)
        * <https://web.archive.org/web/20200805200923/https://www.travail.gouv.ga/402-evenements/489-liste-des-jours-feries/>

    !!! note "Unavailable sources"
        * Decree 451/PR-MT.PS of Mar 14, 1970
        * Decree 147/PR of Dec 5, 1974
        * Decree 911/PR/MTE of Aug 25, 1980
        * Decree 00727/PR/MTEFP of Jun 29, 1998
        * Decree 000484/PR/MTE of May 26, 2004
    """

    country = "GA"
    default_language = "fr"
    # %s (estimated).
    estimated_label = tr("%s (estimé)")
    # Decree 600/PR-MTPS of Jul 10, 1976.
    start_year = 1977
    supported_languages = ("en_US", "fr")

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=GabonIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, cls=GabonStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Jour de l'an"))

        if self._year <= 1992:
            # Renovation Day.
            self._add_holiday_mar_12(tr("Journée de la rénovation"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Pâques"))

        # Easter Monday.
        self._add_easter_monday(tr("Lundi de Pâques"))

        if self._year >= 2015:
            # Women's Rights Day.
            self._add_holiday_apr_17(tr("Journée des droits de la femme"))

        # Labor Day.
        self._add_labor_day(tr("Fête du Travail"))

        if self._year <= 1991:
            # Youth Day.
            self._add_holiday_2nd_sun_of_may(tr("Fête de la Jeunesse"))

        if self._year >= 2018:
            # Ascension Day.
            self._add_ascension_thursday(tr("Ascension"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Pentecôte"))

        # Whit Monday.
        self._add_whit_monday(tr("Lundi de Pentecôte"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Assomption de Marie"))

        # Independence Day.
        self._add_holiday_aug_16(tr("Jour de l'indépendance"))

        # Independence Day Holiday.
        name = tr("Fête de l'indépendance")
        self._add_holiday_aug_17(name)

        if self._year <= 1991:
            self._add_holiday_aug_18(name)

        if self._year >= 2024:
            # Liberation Day.
            self._add_holiday_aug_30(tr("Journée de la Libération"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Toussaint"))

        # Christmas Day.
        self._add_christmas_day(tr("Noël"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Fin du Ramadan"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Fête du sacrifice"))


class GA(Gabon):
    pass


class GAB(Gabon):
    pass


class GabonIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2001, 2025)
    EID_AL_ADHA_DATES = {
        2001: (MAR, 6),
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 2),
        2008: (DEC, 9),
        2009: (NOV, 28),
        2010: (NOV, 17),
        2011: (NOV, 7),
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 13),
        2017: (SEP, 2),
        2018: (AUG, 22),
    }

    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2001, 2025)
    EID_AL_FITR_DATES = {
        2001: (DEC, 17),
        2002: (DEC, 6),
        2003: (NOV, 26),
        2005: (NOV, 4),
        2006: (OCT, 24),
        2008: (OCT, 2),
        2009: (SEP, 21),
        2011: (AUG, 31),
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
    }


class GabonStaticHolidays:
    """Gabon special holidays.

    References:
        * <https://web.archive.org/web/20241116171700/https://info241.com/referendum-constitutionnel-du-16-novembre-trois-jours-feries,9646>
        * <https://web.archive.org/web/20250409074948/https://info241.com/presidentielle-2025-les-11-et-12-avril-declares-feries-pour,10205>
        * <https://web.archive.org/web/20250501091256/https://info241.com/gabon-le-2-mai-declare-ferie-et-recuperable-pour-l-investiture,2385>
        * <https://web.archive.org/web/20260307182549/https://info241.com/gabon-le-samedi-27-septembre-declare-jour-ferie-pour-les,2558>
    """

    # Public holiday.
    public_holiday = tr("Jour férié")

    special_public_holidays = {
        2024: (
            (NOV, 14, public_holiday),
            (NOV, 15, public_holiday),
            (NOV, 16, public_holiday),
        ),
        2025: (
            (APR, 11, public_holiday),
            (APR, 12, public_holiday),
            (MAY, 2, public_holiday),
            (SEP, 27, public_holiday),
        ),
    }
