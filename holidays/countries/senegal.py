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
from holidays.calendars.gregorian import MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT
from holidays.groups import ChristianHolidays, IslamicHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Senegal(HolidayBase, ChristianHolidays, IslamicHolidays, InternationalHolidays):
    """
    Senegal holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Senegal>
    """

    country = "SN"
    default_language = "fr_SN"
    # %s (estimated).
    estimated_label = tr("%s (estimé)")
    start_year = 1961
    supported_languages = ("en_US", "fr_SN")

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=SenegalIslamicHolidays, show_estimated=islamic_show_estimated
        )
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Jour de l'an"))

        # Independence Day.
        self._add_holiday_apr_4(tr("Fête de l'Indépendance"))

        # Easter Monday.
        self._add_easter_monday(tr("Lundi de Pâques"))

        # Labor Day.
        self._add_labor_day(tr("Fête du Travail"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Ascension"))

        # Whit Monday.
        self._add_whit_monday(tr("Lundi de Pentecôte"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Assomption"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Toussaint"))

        # Christmas Day.
        self._add_christmas_day(tr("Noël"))

        # Ashura.
        self._add_ashura_day(tr("Achoura"))

        # Grand Magal of Touba.
        self._add_grand_magal_of_touba(tr("Grand Magal de Touba"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("Maouloud"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Aïd al-Fitr"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Aïd al-Adha"))


class SN(Senegal):
    pass


class SEN(Senegal):
    pass


class SenegalIslamicHolidays(_CustomIslamicHolidays):
    # https://www.timeanddate.com/holidays/senegal/tamkharit
    ASHURA_DATES = {
        2020: (AUG, 29),
        2021: (AUG, 18),
        2022: (AUG, 8),
        2023: (JUL, 28),
        2024: (JUL, 17),
    }

    # https://www.timeanddate.com/holidays/senegal/grand-magal-de-touba
    GRAND_MAGAL_OF_TOUBA_DATES = {
        2020: (OCT, 6),
        2021: (SEP, 26),
        2022: (SEP, 15),
        2023: (SEP, 4),
        2024: (AUG, 23),
    }

    # https://www.timeanddate.com/holidays/senegal/maouloud
    MAWLID_DATES = {
        2020: (OCT, 29),
        2021: (OCT, 18),
        2022: (OCT, 8),
        2023: (SEP, 27),
        2024: (SEP, 15),
    }

    # https://www.timeanddate.com/holidays/senegal/korite
    EID_AL_FITR_DATES = {
        2020: (MAY, 24),
        2021: (MAY, 12),
        2022: (MAY, 1),
        2023: (APR, 22),
        2024: (APR, 10),
        2025: (MAR, 30),
    }

    # https://www.timeanddate.com/holidays/senegal/tabaski
    EID_AL_ADHA_DATES = {
        2020: (JUL, 31),
        2021: (JUL, 21),
        2022: (JUL, 10),
        2023: (JUN, 29),
        2024: (JUN, 17),
    }
