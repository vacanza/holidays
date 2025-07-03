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

from holidays import GOVERNMENT, PUBLIC
from holidays.calendars.gregorian import SEP, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_TO_PREV_THU,
    SAT_SUN_TO_PREV_THU_FRI,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
    SAT_SUN_TO_NEXT_TUE_WED,
    SUN_TO_NEXT_WED,
)


class FalklandIslands(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """Falkland Islands holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_the_Falkland_Islands>
        * <https://web.archive.org/web/20241201174202/https://www.timeanddate.com/holidays/falkland-islands/2025>
        * [Falkland Day](https://web.archive.org/web/20250325025508/https://www.daysoftheyear.com/days/falklands-day/)
        * [Peat Cutting Day](https://en.wikipedia.org/wiki/Peat_Cutting_Monday#:~:text=Peat%20Cutting%20Day%20is%20a,Monday%20in%20October%20every%20year.)
        * [King's Birthday](https://web.archive.org/web/20230329063159/https://en.mercopress.com/2022/11/03/falklands-appoints-14-november-as-a-public-holiday-to-celebrate-birthday-of-king-charles-iii)
        * [2023-2026](https://web.archive.org/web/20250402143330/https://www.falklands.gov.fk/policy/downloads?task=download.send&id=186:falkland-islands-public-holidays-2023-2026&catid=12)
    """

    country = "FK"
    default_language = "en_GB"
    supported_languages = ("en_GB", "en_US")
    supported_categories = (GOVERNMENT, PUBLIC)
    # %s observed.
    observed_label = tr("%s (observed)")

    start_year = 1983

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=FalklandIslandsStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        if self._year <= 2022:
            # Queen's Birthday.
            self._add_observed(self._add_holiday_apr_21(tr("Queen's Birthday")))

        # Liberation Day.
        self._add_observed(self._add_holiday_jun_14(tr("Liberation Day")))

        if self._year <= 2001:
            # Falkland Day.
            self._add_observed(self._add_holiday_aug_14(tr("Falkland Day")))
        else:
            # Peat Cutting Day.
            self._add_holiday_1st_mon_of_oct(tr("Peat Cutting Day"))

        # King's Birthday.
        self._add_observed(self._add_holiday_nov_14(tr("King's Birthday")))

        dec_25 = (DEC, 25)
        christmas_day_rule = None
        christmas_day_two_rule = SAT_SUN_TO_NEXT_MON_TUE
        christmas_day_three_rule = SAT_SUN_TO_NEXT_MON_TUE
        if self._is_saturday(dec_25):
            christmas_day_rule = SAT_SUN_TO_NEXT_TUE_WED
            christmas_day_two_rule = SAT_SUN_TO_NEXT_TUE_WED
        elif self._is_sunday(dec_25):
            christmas_day_rule = SUN_TO_NEXT_WED

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Christmas Day")), rule=christmas_day_rule)

        # Boxing Day.
        self._add_observed(
            self._add_christmas_day_two(tr("Boxing Day")), rule=christmas_day_two_rule
        )

        # Christmas Holiday.
        self._add_observed(
            self._add_christmas_day_three(tr("Christmas Holiday")), rule=christmas_day_three_rule
        )

    def _populate_government_holidays(self):
        dec_30 = (DEC, 30)
        # Government Holiday.
        name = tr("Government Holiday")
        govt_holiday_one_rule = SAT_SUN_TO_PREV_THU_FRI
        govt_holiday_two_rule = SAT_SUN_TO_PREV_THU_FRI
        if self._is_friday(dec_30):
            govt_holiday_two_rule = SAT_TO_PREV_THU

        self._add_observed(self._add_holiday_dec_30(name), rule=govt_holiday_one_rule)
        self._add_observed(self._add_holiday_dec_31(name), rule=govt_holiday_two_rule)


class FK(FalklandIslands):
    pass


class FLK(FalklandIslands):
    pass


class FalklandIslandsStaticHolidays:
    """Falkland Islands special holidays.

    References:
        * <https://en.mercopress.com/2022/09/14/falklands-public-holiday-and-national-two-minute-s-silence-for-queen-elizabeth-ii>
    """

    special_public_holidays = {
        # Queen Elizabeth II's Funeral.
        2024: (SEP, 19, tr("Queen Elizabeth II's Funeral")),
    }
