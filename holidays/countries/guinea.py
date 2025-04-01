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

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Guinea(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Guinea Holidays.

    References:
        * <https://www.timeanddate.com/holidays/guinea/>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Guinea>
        * <https://anydayguide.com/calendar/1878>
        * <https://www.timeanddate.com/holidays/guinea/second-republic-day>
        * <https://www.timeanddate.com/holidays/guinea/all-saints-day>
    """

    country = "GN"
    # %s (estimated).
    estimated_label = tr("%s (estimé)")
    default_language = "fr"
    supported_languages = ("en_US", "fr")

    # Guinea Gained Independence from France on October 2, 1958
    start_year = 1959

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
            self, cls=GuineaIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Nouvel an"))

        if self._year <= 2021:
            # Second Republic Day.
            self._add_holiday_apr_3(tr("Jour de la Deuxième République"))

        # Easter Monday.
        self._add_easter_monday(tr("Le lundi de Pâques"))

        # Labor Day.
        self._add_labor_day(tr("Fête du Travail"))

        # Africa Day.
        self._add_africa_day(tr("Anniversaire de l'OUA"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Assomption de Marie"))

        # Independence Day.
        self._add_holiday_oct_2(tr("Fête de l'indépendance de la Guinée"))

        if self._year <= 2021:
            # All Saint's Day.
            self._add_all_saints_day(tr("La Toussaint"))

        # Christmas Day.
        self._add_christmas_day(tr("Noël"))

        # Night of Power.
        self._add_laylat_al_qadr_day(tr("Lailatoul Qadr"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Korité"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Tabaski"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("Maouloud"))


class GN(Guinea):
    pass


class GIN(Guinea):
    pass


class GuineaIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2015: (SEP, 24),
        2016: (SEP, 13),
        2017: (SEP, 2),
        2018: (AUG, 22),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 10),
        2023: (JUN, 28),
        2024: (JUN, 16),
        2025: (JUN, 7),
    }

    EID_AL_FITR_DATES = {
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 4),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 21),
        2024: (APR, 10),
        2025: (MAR, 31),
    }

    MAWLID_DATES = {
        2015: (DEC, 24),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 20),
        2019: (NOV, 10),
        2020: (OCT, 29),
        2021: (OCT, 18),
        2022: (OCT, 8),
        2023: (SEP, 27),
        2024: (SEP, 15),
        2025: (SEP, 5),
    }

    LAYLAT_AL_QADR_DATES = {
        2015: (JUL, 14),
        2016: (JUL, 3),
        2017: (JUN, 22),
        2018: (JUN, 12),
        2019: (JUN, 1),
        2020: (MAY, 20),
        2021: (MAY, 9),
        2022: (APR, 29),
        2023: (APR, 18),
        2024: (APR, 6),
        2025: (MAR, 27),
    }
