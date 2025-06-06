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

from datetime import date
from gettext import gettext as tr

from holidays.constants import PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY


class Nauru(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Nauru holidays.

    References:
        * <https://www.worldatlas.com/articles/what-languages-are-spoken-in-nauru.html>
        * <https://publicholidays.asia/nauru/>
        * <https://commonwealthchamber.com/day-of-the-tribes-nauru/>
        * <https://anydayguide.com/calendar/2514>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Nauru>
        * <https://www.timeanddate.com/holidays/nauru/>
    """

    country = "NR"
    default_language = "en_AU"
    supported_categories = (PUBLIC,)
    # %s (observed).
    observed_label = tr("%s (observed)")
    supported_languages = ("en_AU",)
    # Nauru gained independence on January 31, 1968
    start_year = 1969

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_observed(self, dts: set[date], multiple: bool = False) -> None:
        for dt in sorted(dts):
            self._add_observed(dt, rule=SAT_SUN_TO_NEXT_WORKDAY)

    def _populate_public_holidays(self):
        dts_observed = set()

        # New Year's Day.
        dts_observed.add(self._add_new_years_day(tr("New Year's Day")))

        # Independence Day.
        dts_observed.add(self._add_holiday_jan_31(tr("Independence Day")))

        # International Women's Day.
        dts_observed.add(self._add_womens_day(tr("International Women's Day")))

        # Good Friday.
        dts_observed.add(self._add_good_friday(tr("Good Friday")))

        # Easter Monday.
        dts_observed.add(self._add_easter_monday(tr("Easter Monday")))

        # Easter Tuesday.
        dts_observed.add(self._add_easter_tuesday(tr("Easter Tuesday")))

        # Constitution Day.
        dts_observed.add(self._add_holiday_may_17(tr("Constitution Day")))

        # RONPhos Handover Day.
        dts_observed.add(self._add_holiday_jul_1(tr("RONPhos Handover Day")))

        # Ibumin Earoeni Day.
        dts_observed.add(self._add_holiday_aug_19(tr("Ibumin Earoeni Day")))

        # Sir Hammer DeRoburt Day.
        dts_observed.add(self._add_holiday_sep_25(tr("Sir Hammer DeRoburt Day")))

        # Angam Day.
        dts_observed.add(self._add_holiday_oct_26(tr("Angam Day")))

        # Christmas Day.
        dts_observed.add(self._add_christmas_day(tr("Christmas Day")))

        # Boxing Day.
        dts_observed.add(self._add_christmas_day_two(tr("Boxing Day")))

        if self.observed:
            self._populate_observed(dts_observed)


class NR(Nauru):
    pass


class NRU(Nauru):
    pass
