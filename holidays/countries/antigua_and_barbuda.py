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
from holidays import JAN, MAR
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
    SAT_SUN_TO_NEXT_MON,
    MON_TO_NEXT_TUE,
)


class AntiguaAndBarbuda(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """Antigua and Barbuda holidays.

    References:
        * [The Public Holidays Act, 1954](https://laws.gov.ag/wp-content/uploads/2018/08/cap-354.pdf)
        * [The Public Holidays (Amendment) Act, 2005](https://laws.gov.ag/wp-content/uploads/2018/08/a2005-8.pdf)
        * [The Public Holidays (Amendment) Act, 2014](https://laws.gov.ag/wp-content/uploads/2019/03/Public-Holidays-Amendment-Act.pdf)
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Antigua_and_Barbuda>
    """

    country = "AG"
    observed_label = "%s (observed)"
    start_year = 1955

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, AntiguaAndBarbudaStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # Labour Day.
        self._add_holiday_1st_mon_of_may("Labour Day")

        # Whit Monday.
        self._add_whit_monday("Whit Monday")

        if self._year < 2005:
            # Caribbean Community (Caricom) Day.
            self._add_holiday_1st_mon_of_jul("Caribbean Community (Caricom) Day")

        # Carnival Monday.
        self._add_holiday_1st_mon_of_aug("Carnival Monday")
        if self._year > 2005:
            self._add_observed(
                # Carnival Tuesday.
                self._add_holiday_1st_mon_of_aug("Carnival Tuesday"),
                rule=MON_TO_NEXT_TUE,
                show_observed_label=False,
            )

        # Independence Day.
        independence_day_name = "Independence Day"
        if self._year >= 2005:
            self._add_observed(
                self._add_holiday_nov_1(independence_day_name), rule=SAT_SUN_TO_NEXT_MON
            )
        else:
            self._add_holiday_nov_1(independence_day_name)

        if self._year >= 2014:
            # Sir Vere Cornwall Bird (SNR) Day.
            self._add_holiday_dec_9("Sir Vere Cornwall Bird (SNR) Day")
        elif self._year >= 2005:
            # National Heroes Day.
            self._add_holiday_dec_9("National Heroes Day")

        # Christmas Day.
        self._add_observed(self._add_christmas_day("Christmas Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)

        # Boxing Day.
        self._add_observed(self._add_christmas_day_two("Boxing Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)


class AG(AntiguaAndBarbuda):
    pass


class ATG(AntiguaAndBarbuda):
    pass


class AntiguaAndBarbudaStaticHolidays:
    """Antigua and Barbuda special holidays.

    References:
        * According to the Public Holidays (Amendment) Act, 2014, the day after the general
          election is a holiday.
            * [2018 Antiguan general election](https://en.wikipedia.org/wiki/2018_Antiguan_general_election)
            * [2023 Antiguan general election](https://en.wikipedia.org/wiki/2023_Antiguan_general_election)
            * [The Public Holidays (Amendment) Act, 2014](https://laws.gov.ag/wp-content/uploads/2019/03/Public-Holidays-Amendment-Act.pdf)
    """

    # Day after the General Election.
    day_after_the_general_election = "Day after the General Election"
    special_public_holidays = {
        2018: ((MAR, 22, day_after_the_general_election),),
        2023: ((JAN, 19, day_after_the_general_election),),
    }
