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
        * [SI 148 of 2026](https://web.archive.org/web/20261111132603/https://www.veritaszim.net/sites/veritas_d/files/SI%202026-148%20Public%20Holidays%20and%20Prohibition%20of%20Business%20(Declaration%20of%20Public%20Holiday)%20Notice,%202026.pdf)
        * [General Notice 86 of 2009](https://web.archive.org/web/20260316124751/https://www.law.co.zw/download/1103/)
        * [General Notice 244 of 2016](https://web.archive.org/web/20261111132554/https://www.veritaszim.net/sites/veritas_d/files/GN%202016-244%20Public%20Holidays%202017.pdf)
        * [General Notice 861 of 2019](https://web.archive.org/web/20240812194407/https://www.veritaszim.net/sites/veritas_d/files/GN%202019-861%20Public%20Holidays%20in%202020.pdf)
        * [General Notice 2554 of 2020](https://web.archive.org/web/20240630032450/https://veritaszim.net/sites/veritas_d/files/GN%202020-2552%20Public%20Holidays%20in%202021.pdf)
        * [General Notice 851 of 2021](https://web.archive.org/web/20240803030943/https://www.veritaszim.net/sites/veritas_d/files/GN%202021-851%20PUBLIC%20HOLIDAYS%20AND%20PROHIBITION%20OF%20BUSINESS%20ACT%20FOR%202022.pdf)
        * [General Notice 495 of 2022](https://web.archive.org/web/20240717135511/https://veritaszim.net/sites/veritas_d/files/GN%202022-495%20Public%20Holidays%20and%20Prohibition%20of%20Business%20Act_0.pdf)
        * [General Notice 1036 of 2023](https://web.archive.org/web/20250804235726/https://www.veritaszim.net/sites/veritas_d/files/GN%202023-1036%20Public%20Holidays%20and%20Prohibition%20of%20Business%20Act%2C%20Public%20Holidays%20in%202024.pdf)
        * [General Notice 954 of 2024](https://web.archive.org/web/20241113043414/https://www.veritaszim.net/sites/veritas_d/files/GN%202024-0954%20Public%20Holidays%20in%202025_0.pdf)
        * [General Notice 1361 of 2025](https://web.archive.org/web/20261111132507/https://www.veritaszim.net/sites/veritas_d/files/GN%202025-1361%20Public%20Holidays%20in%202026.pdf)
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

        self._add_observed(
            # Independence Day.
            apr_18 := self._add_holiday_apr_18("Independence Day"),
            rule=SUN_TO_NEXT_TUE if apr_18 == self._easter_sunday else SUN_TO_NEXT_MON,
        )

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Easter Saturday.
        self._add_holy_saturday("Easter Saturday")

        # General Notice 86 of 2009.
        if self._year >= 2010:
            # Easter Sunday.
            self._add_easter_sunday("Easter Sunday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # Workers' Day.
        self._add_observed(self._add_labor_day("Workers' Day"))

        # Africa Day.
        self._add_observed(self._add_africa_day("Africa Day"))

        # Zimbabwe Heroes' Day.
        self._add_holiday_2nd_mon_of_aug("Zimbabwe Heroes' Day")

        # Defense Forces Day.
        self._add_holiday_1_day_past_2nd_mon_of_aug("Defense Forces Day")

        # SI 148 of 2026.
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
