#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.calendars.gregorian import FEB, APR, AUG, SEP
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON, SUN_TO_NEXT_TUE


class Kenya(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Kenya
    http://kenyaembassyberlin.de/Public-Holidays-in-Kenya.48.0.html
    https://www.officeholidays.com/holidays/kenya/moi-day
    """

    country = "KE"
    observed_label = "%s (Observed)"
    special_holidays = {
        2020: (FEB, 11, "President Moi Celebration of Life Day"),
        2022: (
            (APR, 29, "State Funeral for Former President Mwai Kibaki"),
            (AUG, 9, "Election Day"),
            (SEP, 10, "Day of Mourning for Queen Elizabeth II"),
            (SEP, 11, "Day of Mourning for Queen Elizabeth II"),
            (SEP, 12, "Day of Mourning for Queen Elizabeth II"),
            (SEP, 13, "Inauguration Day"),
        ),
    }

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(observed_rule=SUN_TO_NEXT_MON, *args, **kwargs)

    def _populate(self, year):
        if year <= 1962:
            return None

        super()._populate(year)

        # New Year's Day
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Good Friday
        self._add_good_friday("Good Friday")

        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Labour Day
        self._add_observed(self._add_labor_day("Labour Day"))

        if year >= 2010:
            # Mandaraka Day
            self._add_observed(self._add_holiday_jun_1("Madaraka Day"))

        if 2002 <= year <= 2009 or year >= 2018:
            self._add_observed(
                # Utamaduni/Moi Day
                self._add_holiday_oct_10("Utamaduni Day" if year >= 2021 else "Moi Day")
            )

        self._add_observed(
            # Mashuja/Kenyatta Day
            self._add_holiday_oct_20("Mashujaa Day" if year >= 2010 else "Kenyatta Day")
        )

        # Jamhuri Day
        self._add_observed(self._add_holiday_dec_12("Jamhuri Day"))

        # Christmas Day
        self._add_observed(self._add_christmas_day("Christmas Day"), rule=SUN_TO_NEXT_TUE)

        # Boxing Day
        self._add_observed(self._add_christmas_day_two("Boxing Day"))


class KE(Kenya):
    pass


class KEN(Kenya):
    pass
