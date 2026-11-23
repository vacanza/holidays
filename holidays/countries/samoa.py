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

from holidays.calendars.gregorian import AUG
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON, SUN_TO_NEXT_TUE


class Samoa(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Samoa holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Samoa>
        * [Public Holidays Act 2008](https://web.archive.org/web/20261123115142/https://mcil.gov.ws/sites/default/files/documents/2008-01/Public-Holidays-Act-2008.pdf)
        * <https://web.archive.org/web/20240914112255/https://www.mcil.gov.ws/?attachment_id=6336>
    """

    country = "WS"
    observed_label = "%s (observed)"
    # Public Holidays Act 2008 came into force on January 1, 2008.
    start_year = 2008

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, SamoaStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day("New Year's Day"), rule=SUN_TO_NEXT_TUE)
        self._add_observed(self._add_new_years_day_two("The Day After New Year's Day"))

        # Good Friday.
        self._add_good_friday("Good Friday")
        self._add_holy_saturday("Day After Good Friday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # Mother's Day.
        self._add_holiday_1_day_past_2nd_sun_of_may("Mother's Day")

        # Independence Day.
        self._add_observed(self._add_holiday_jun_1("Independence Day"))

        # Father's Day.
        self._add_holiday_1_day_past_2nd_sun_of_aug("Father's Day")

        # White Monday (Lotu a Tamaiti).
        self._add_holiday_1_day_past_2nd_sun_of_oct("White Sunday (Lotu a Tamaiti)")

        # Christmas Day.
        self._add_observed(self._add_christmas_day("Christmas Day"), rule=SUN_TO_NEXT_TUE)

        # Boxing Day.
        self._add_observed(self._add_christmas_day_two("Boxing Day"))


class WS(Samoa):
    pass


class WSM(Samoa):
    pass


class SamoaStaticHolidays:
    """Samoa special holidays.

    References:
        * [General Election 2025](https://web.archive.org/web/20260811202425/https://www.mcil.gov.ws/sites/default/files/documents/2025-08/Public-Notice-General-Election-2025-Eng.pdf)
        * [Public holidays calendar 2025-2027](https://web.archive.org/web/20261024100428/https://mcil.gov.ws/public-holidays-calendar)
    """

    # General Election Holiday.
    general_election_holiday = "General Election Holiday"

    special_public_holidays = {
        2025: (
            (AUG, 28, general_election_holiday),
            (AUG, 29, general_election_holiday),
        ),
    }
