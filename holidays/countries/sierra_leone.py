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

from holidays.calendars.gregorian import FEB, MAR
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_WORKDAY,
)


class SierraLeone(
    ObservedHolidayBase,
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
):
    """Sierra Leone holidays.

    References:
        * https://www.officeholidays.com/countries/sierra-leone
        * https://en.wikipedia.org/wiki/Public_holidays_in_Sierra_Leone
        * https://www.timeanddate.com/holidays/sierra-leone/
    """

    country = "SL"
    default_language = "en_SL"
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    # %s (observed).
    observed_label = tr("%s (observed)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (observed, estimated)")
    supported_languages = ("en_SL", "en_US")
    # Sierra Leone gained independence on April 27, 1961
    start_year = 1961

    def __init__(self, islamic_show_estimated: bool = False, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, show_estimated=islamic_show_estimated)
        StaticHolidays.__init__(self, cls=SierraLeoneStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        dts_observed = set()

        # New Year's Day.
        dts_observed.add(self._add_new_years_day(tr("New Year's Day")))

        # Armed Forces Day.
        if self._year >= 2002:
            dts_observed.add(self._add_holiday_feb_18(tr("Armed Forces Day")))

        # International Women's Day.
        if self._year >= 2018:
            women_day = tr("International Women's Day")
            dts_observed.add(self._add_holiday_mar_8(women_day))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Independence Day.
        dts_observed.add(self._add_holiday_apr_27(tr("Independence Day")))

        # Labor Day.
        labor_day = tr("International Worker's Day")
        dts_observed.add(self._add_labor_day(labor_day))

        # Christmas Day.
        dts_observed.add(self._add_christmas_day(tr("Christmas Day")))

        # Boxing Day.
        dts_observed.add(self._add_christmas_day_two(tr("Boxing Day")))

        # Eid al-Fitr.
        dts_observed.update(self._add_eid_al_fitr_day(tr("Eid al-Fitr")))

        # Eid al-Adha.
        dts_observed.update(self._add_eid_al_adha_day(tr("Eid al-Adha")))

        # Prophet's Birthday.
        dts_observed.update(self._add_mawlid_day(tr("Prophet's Birthday")))

        if self.observed:
            self._populate_observed(dts_observed)


class SL(SierraLeone):
    pass


class SLE(SierraLeone):
    pass


class SierraLeoneStaticHolidays:
    """Sierra Leone special holidays.

    References:
    """

    special_public_holidays = {
        # Armed Forces Day first established.
        2002: (FEB, 18, tr("Armed Forces Day")),
        # International Women's Day first established.
        2018: (MAR, 8, tr("International Women's Day")),
    }
