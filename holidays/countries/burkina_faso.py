#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class BurkinaFaso(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Burkina_Faso
    """

    country = "BF"
    observed_label = "%s (observed)"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, cls=BurkinaFasoIslamicHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # On 5 August 1960, Burkina Faso (Republic of Upper Volta at that time)
        # gained independence from France.
        if self._year <= 1960:
            return None

        # New Year's Day.
        self._add_observed(self._add_new_years_day("New Year's Day"))

        if self._year >= 1967:
            # Revolution Day.
            self._add_observed(self._add_holiday_jan_3("Revolution Day"))

        # International Women's Day.
        self._add_observed(self._add_womens_day("International Women's Day"))

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # Labour Day.
        self._add_observed(self._add_labor_day("Labour Day"))

        # Ascension Day.
        self._add_ascension_thursday("Ascension Day")

        # Independence Day.
        self._add_observed(self._add_holiday_aug_5("Independence Day"))

        # Assumption Day.
        self._add_observed(self._add_assumption_of_mary_day("Assumption Day"))

        if self._year >= 2016:
            # Martyrs' Day.
            self._add_observed(self._add_holiday_oct_31("Martyrs' Day"))

        # All Saints' Day.
        self._add_observed(self._add_all_saints_day("All Saints' Day"))

        self._add_observed(
            # Proclamation of Independence Day.
            self._add_holiday_dec_11("Proclamation of Independence Day")
        )

        # Christmas Day.
        self._add_observed(self._add_christmas_day("Christmas Day"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day("Eid al-Fitr")

        # Eid al-Adha.
        self._add_eid_al_adha_day("Eid al-Adha")

        # Mawlid.
        self._add_mawlid_day("Mawlid")


class BF(BurkinaFaso):
    pass


class BFA(BurkinaFaso):
    pass


class BurkinaFasoIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
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
    }

    EID_AL_FITR_DATES = {
        2014: (JUL, 29),
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
    }

    MAWLID_DATES = {
        2014: (JAN, 14),
        2015: ((JAN, 3), (DEC, 24)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 21),
        2019: (NOV, 10),
        2020: (OCT, 29),
        2021: (OCT, 19),
        2022: (OCT, 9),
    }
