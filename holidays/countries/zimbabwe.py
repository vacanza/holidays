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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON, SUN_TO_NEXT_TUE


class Zimbabwe(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Zimbabwe holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Zimbabwe>
        * <https://en.wikipedia.org/wiki/Robert_Gabriel_Mugabe_National_Youth_Day>
        * [SI 148 of 2026](https://www.veritaszim.net/sites/veritas_d/files/SI%202026-148%20Public%20Holidays%20and%20Prohibition%20of%20Business%20%28Declaration%20of%20Public%20Holiday%29%20Notice%2C%202026.pdf)
    """

    country = "ZW"
    observed_label = "%s (observed)"
    start_year = 1988

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day("New Year's Day"))

        if self._year >= 2018:
            self._add_observed(
                # Robert Gabriel Mugabe National Youth Day.
                self._add_holiday_feb_21("Robert Gabriel Mugabe National Youth Day")
            )

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Easter Saturday.
        self._add_holy_saturday("Easter Saturday")

        if self._year >= 2024:
            # Easter Sunday.
            self._add_easter_sunday("Easter Sunday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # Independence Day.
        name = "Independence Day"
        self._add_observed(
            apr_18 := self._add_holiday_apr_18(name),
            name=name,
            rule=SUN_TO_NEXT_TUE if apr_18 == self._easter_sunday else SUN_TO_NEXT_MON,
        )

        # Workers' Day.
        self._add_observed(self._add_labor_day("Workers' Day"))

        # Africa Day.
        self._add_observed(self._add_africa_day("Africa Day"))

        # Zimbabwe Heroes' Day.
        self._add_holiday_2nd_mon_of_aug("Zimbabwe Heroes' Day")

        # Defense Forces Day.
        self._add_holiday_1_day_past_2nd_mon_of_aug("Defense Forces Day")

        if self._year >= 2026:
            # Munhumutapa Day.
            self._add_observed(self._add_holiday_sep_15("Munhumutapa Day"))

        # Unity Day.
        self._add_observed(self._add_holiday_dec_22("Unity Day"))

        # Christmas Day.
        self._add_observed(self._add_christmas_day("Christmas Day"), rule=SUN_TO_NEXT_TUE)

        # Boxing Day.
        self._add_observed(self._add_christmas_day_two("Boxing Day"))


class ZW(Zimbabwe):
    pass


class ZWE(Zimbabwe):
    pass
