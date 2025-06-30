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

from holidays.constants import OPTIONAL, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_PREV_SAT, SUN_TO_NEXT_MON


class Netherlands(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Netherlands holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_the_Netherlands>
        * <https://nl.wikipedia.org/wiki/Feestdagen_in_Nederland>
        * <https://web.archive.org/web/20250427131819/https://www.iamsterdam.com/en/plan-your-trip/practical-info/public-holidays>
    """

    country = "NL"
    default_language = "nl"
    supported_categories = (OPTIONAL, PUBLIC)
    supported_languages = ("en_US", "fy", "nl", "uk")
    start_year = 1801

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Nieuwjaarsdag"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Eerste paasdag"))

        # Easter Monday.
        self._add_easter_monday(tr("Tweede paasdag"))

        if self._year >= 1891:
            name = (
                # King's Day.
                tr("Koningsdag")
                if self._year >= 2014
                # Queen's Day.
                else tr("Koninginnedag")
            )
            if self._year >= 2014:
                dt = self._add_holiday_apr_27(name)
            elif self._year >= 1949:
                dt = self._add_holiday_apr_30(name)
            else:
                dt = self._add_holiday_aug_31(name)
            self._move_holiday(dt, rule=SUN_TO_PREV_SAT if self._year >= 1980 else SUN_TO_NEXT_MON)

        if self._year >= 1950 and self._year % 5 == 0:
            # Liberation Day.
            self._add_holiday_may_5(tr("Bevrijdingsdag"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Hemelvaartsdag"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Eerste Pinksterdag"))

        # Whit Monday.
        self._add_whit_monday(tr("Tweede Pinksterdag"))

        # Christmas Day.
        self._add_christmas_day(tr("Eerste Kerstdag"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Tweede Kerstdag"))

    def _populate_optional_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Goede Vrijdag"))

        if self._year >= 1990:
            # Liberation Day.
            self._add_holiday_may_5(tr("Bevrijdingsdag"))


class NL(Netherlands):
    pass


class NLD(Netherlands):
    pass
