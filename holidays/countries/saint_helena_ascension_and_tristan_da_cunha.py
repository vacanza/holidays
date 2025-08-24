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

from holidays.calendars.gregorian import JAN, MAY, JUN, SEP
from holidays.constants import BANK, GOVERNMENT, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class SaintHelenaAscensionAndTristanDaCunha(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """Saint Helena, Ascension And Tristan da Cunha holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Saint_Helena,_Ascension_and_Tristan_da_Cunha>
    """

    country = "SH"
    default_language = "en_GB"
    # %s observed.
    observed_label = tr("%s (observed)")
    # Earliest year of holidays with an accessible online record.
    start_year = 2015
    subdivisions = (
        "AC",  # Ascension.
        "HL",  # Saint Helena.
        "TA",  # Tristan da Cunha.
    )
    supported_languages = ("en_GB", "en_US")
    supported_categories = (BANK, GOVERNMENT, PUBLIC)

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=SaintHelenaAscensionAndTristanDaCunhaStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON_TUE)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Whit Monday
        self._add_whit_monday(tr("Whit Monday"))

        if self._year <= 2022:
            queens_birthday_dates = {
                2007: (JUN, 18),
                2012: (JUN, 18),
                2013: (JUN, 17),
                2017: (JUN, 19),
                2022: (JUN, 6),
            }
            # Queen's Birthday.
            name = tr("Queen's Birthday")
            if dt := queens_birthday_dates.get(self._year):
                self._add_holiday(name, dt)
            else:
                self._add_holiday_2_days_past_2nd_sat_of_jun(name)
        else:
            # King's Birthday.
            self._add_holiday_3rd_fri_of_jun(tr("King's Birthday"))

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Christmas Day")))

        # Boxing Day.
        self._add_observed(self._add_christmas_day_two(tr("Boxing Day")))

    def _populate_subdiv_ac_public_holidays(self):
        # Ascension Day.
        pass

    def _populate_subdiv_hl_public_holidays(self):
        # Saint Helena Day.
        self._add_observed(
            self._add_holiday_may_21(tr("Saint Helena Day")), rule=SAT_SUN_TO_NEXT_MON
        )


class SH(SaintHelenaAscensionAndTristanDaCunha):
    pass


class SHN(SaintHelenaAscensionAndTristanDaCunha):
    pass


class SaintHelenaAscensionAndTristanDaCunhaStaticHolidays:
    """Saint Helena, Ascension And Tristan da Cunha special holidays.

    References:
        * [Queen Elizabeth II's Funeral]()
        + [The Duke of Edinburgh Visit]()
    """

    special_public_holidays = {
        # Queen Elizabeth II's Funeral.
        2022: (SEP, 19, tr("Queen Elizabeth II's Funeral")),
        2023: (
            # The Duke of Edinburgh Visit.
            (JAN, 24, tr("The Duke of Edinburgh Visit")),
            # Coronation of His Majesty King Charles III.
            (MAY, 8, tr("Coronation of His Majesty King Charles III")),
        ),
    }
