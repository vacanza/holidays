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
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class Kiribati(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Kiribati holidays.

    References:
        * [Public Holidays Ordinance](https://web.archive.org/web/20250130150749/https://www.paclii.org/ki/legis/consol_act/pho216/)
        * [Public Holidays (Amendment) Act 2002](https://web.archive.org/web/20250130161614/https://www.paclii.org/ki/legis/num_act/pha2002243/)
        * [Public Holidays Act Consolidated](https://web.archive.org/web/20250404213705/https://www.paclii.org/ki/legis/consol_act/pho216.pdf)
        * [National Public Holiday Order 2026](https://www.president.gov.ki/images/Gazettes/2025/PH_2026_181225.pdf)
        * [Revised National Public Holiday Order 2025](https://www.president.gov.ki/images/Gazettes/2025/PH_2025_revised_181225.pdf)

    """

    country = "KI"
    observed_label = "%s (observed)"
    start_year = 1980

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year == 2025:
            # Official 2025 public holidays.
            self._add_holiday("New Year's Day", 1, 1)
            self._add_holiday("In Honour of International Women's Day", 3, 7)
            self._add_holiday("National Health Day", 4, 7)
            self._add_good_friday("Good Friday")
            self._add_easter_monday("Easter Monday")
            self._add_holiday("Special Day in Honour of Pope Francis", 4, 25)
            self._add_holiday("In Honour of International Labour Day", 5, 2)
            self._add_holiday("In Honour of National Police Day", 6, 23)
            self._add_holiday("Gospel Day", 7, 11)
            self._add_holiday("National Day", 7, 12)
            self._add_holiday("In Honour of National Day", 7, 14)
            self._add_holiday("National Culture and Senior Citizens Day", 7, 15)
            self._add_holiday("Kiribati Special Day", 7, 16)
            self._add_holiday("In honor of National Youth & Children's Day", 8, 1)
            self._add_holiday("In Honour of World Teachers Day", 10, 6)
            self._add_holiday("In Honour of Human Rights Day", 12, 12)
            self._add_holiday("Christmas Day", 12, 25)
            self._add_holiday("Boxing Day (Gift Day)", 12, 26)
            self._add_holiday("Kiribati Holiday", 12, 29)
            self._add_holiday("Kiribati Holiday", 12, 30)
            self._add_holiday("Kiribati Holiday", 12, 31)
            return

        if self._year == 2026:
            # Official 2026 public holidays.
            self._add_holiday("New Year's Day", 1, 1)
            self._add_holiday("Kiribati Holiday", 1, 2)
            self._add_holiday("In Honour of International Women's Day", 3, 9)
            self._add_good_friday("Good Friday")
            self._add_easter_monday("Easter Monday")
            self._add_holiday("National Health Day", 4, 7)
            self._add_holiday("International Labour Day", 5, 1)
            self._add_holiday("In Honour of National Police Day", 6, 22)
            self._add_holiday("Gospel Day", 7, 10)
            self._add_holiday("In Honour of National Day", 7, 13)
            self._add_holiday("Kiribati Culture and Senior Citizens Day", 7, 14)
            self._add_holiday("Kiribati Special Day", 7, 15)
            self._add_holiday("National Youth & Children's Day", 8, 3)
            self._add_holiday("World Teachers Day", 10, 5)
            self._add_holiday("In Honour of Human Rights Day", 12, 11)
            self._add_holiday("Christmas Day", 12, 25)
            self._add_holiday("In Honour of Boxing Day (Gift Day)", 12, 28)
            self._add_holiday("Kiribati Holiday", 12, 29)
            self._add_holiday("Kiribati Holiday", 12, 30)
            self._add_holiday("Kiribati Holiday", 12, 31)
            return

        # New Year's Day.
        self._add_observed(self._add_new_years_day("New Year's Day"))

        if self._year >= 2003:
            # International Women's Day.
            self._add_observed(self._add_womens_day("International Women's Day"))

        # Good Friday.
        self._add_good_friday("Good Friday")

        if self._year <= 2002:
            # Holy Saturday.
            self._add_holy_saturday("Holy Saturday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        if self._year >= 2003:
            # National Health Day.
            self._add_observed(self._add_holiday_apr_19("National Health Day"))

        if 1993 <= self._year <= 2002:
            # Public Holiday.
            self._add_observed(self._add_holiday_may_9("Public Holiday"))

        if self._year >= 2002:
            # Gospel Day.
            self._add_holiday_jul_11("Gospel Day")

        if self._year >= 1993:
            # National Day - Independence Anniversary.
            self._add_observed(self._add_holiday_jul_12("National Day - Independence Anniversary"))

        if self._year >= 2002:
            # National Day (in honor of Unimwane).
            self._add_holiday_jul_15("National Day (in honor of Unimwane)")
            # National Day (in honor of Unaine).
            self._add_observed(self._add_holiday_jul_16("National Day (in honor of Unaine)"))

        if self._year <= 2002:
            # Public Holiday.
            self._add_holiday_1st_mon_of_aug("Public Holiday")
        else:
            # Youth Day.
            self._add_observed(self._add_holiday_aug_5("Youth Day"))

        if self._year <= 1992:
            # Public Holiday.
            self._add_observed(self._add_holiday_nov_10("Public Holiday"))

        if self._year >= 1993:
            # Human Rights and Peace Day.
            name = "Human Rights and Peace Day"
            self._add_observed(
                self._add_holiday_dec_9(name)
                if self._year >= 2003
                else self._add_holiday_dec_10(name)
            )

        # Christmas Day.
        self._add_observed(self._add_christmas_day("Christmas Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)

        # Boxing Day.
        self._add_observed(self._add_christmas_day_two("Boxing Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)


class KI(Kiribati):
    pass


class KIR(Kiribati):
    pass
