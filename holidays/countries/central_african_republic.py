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
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import ChristianHolidays, IslamicHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase


class CentralAfricanRepublic(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays
):
    """Central African Republic holidays.

    References:
        * [Public holidays in the Central African Republic](https://en.wikipedia.org/wiki/Public_holidays_in_the_Central_African_Republic)
        * [Holidays Today in Central African Republic](https://www.timeanddate.com/holidays/central-african-republic/)
        * [Central African Republic](https://holidayapi.com/countries/cf/2023)
        * [Public Holidays and Bank Holidays for Central African Republic](https://web.archive.org/web/20071220234339/http://www.qppstudio.net/publicholidays2007/central_african_republic.htm)
        * [PUBLIC HOLIDAYS](https://web.archive.org/web/20171215122602/http://www.ais-asecna.org/pdf/gen/gen-2-1/04gen2-1-01.pdf)
    """

    country = "CF"
    default_language = "fr"
    supported_languages = ("en_US", "fr")
    # %s (estimated).
    estimated_label = tr("%s (estimé)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (observé, estimé)")
    # December 1, 1958: Autonomy within the French Community, celebrated as Republic Day.
    start_year = 1959

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
            self, cls=CentralAfricanRepublicIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Jour de l'an"))

        # Barthélemy Boganda Day.
        self._add_holiday_mar_29(tr("Journée Barthélemy Boganda"))

        # Easter Monday.
        self._add_easter_monday(tr("Lundi de Pâques"))

        # Labor Day.
        self._add_labor_day(tr("Fête du Travail"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Ascension Day"))

        # Whit Monday.
        self._add_whit_monday(tr("Pentecôte"))

        if self._year >= 2007:
            # General Prayer Day.
            self._add_holiday_jun_30(tr("Journée de prière générale"))

        if self._year >= 1960:
            # Independence Day.
            self._add_holiday_aug_13(tr("Jour de l'indépendance"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Assomption"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Toussaint"))

        # National Day.
        self._add_holiday_dec_1(tr("Fête nationale"))

        # Christmas Day.
        self._add_christmas_day(tr("Jour de Noël"))

        if self._year >= 2007:
            # Eid al-Fitr.
            self._add_eid_al_fitr_day(tr("Aïd al-Fitr"))

            # Eid al-Adha.
            self._add_eid_al_adha_day(tr("Aïd al-Adha"))


class CF(CentralAfricanRepublic):
    pass


class CAF(CentralAfricanRepublic):
    pass


class CentralAfricanRepublicIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2001: (MAR, 6),
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 2),
        2005: (JAN, 21),
        2006: ((JAN, 10), (DEC, 31)),
        2007: (DEC, 20),
        2008: (DEC, 9),
        2009: (NOV, 28),
        2010: (NOV, 17),
        2011: (NOV, 7),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 13),
        2017: (SEP, 2),
        2018: (AUG, 21),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 16),
        2025: (JUN, 7),
    }

    EID_AL_FITR_DATES = {
        2001: (DEC, 17),
        2002: (DEC, 6),
        2003: (NOV, 26),
        2004: (NOV, 14),
        2005: (NOV, 4),
        2006: (OCT, 24),
        2007: (OCT, 13),
        2008: (OCT, 2),
        2009: (SEP, 21),
        2010: (SEP, 10),
        2011: (AUG, 31),
        2012: (AUG, 19),
        2013: (AUG, 8),
        2014: (JUL, 28),
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
        2025: (MAR, 30),
    }
