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

from holidays.groups import ChristianHolidays, IslamicHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class Burundi(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Burundi holidays.

    References:
        * <https://web.archive.org/web/20240915030631/https://www.officeholidays.com/countries/burundi>

    Note that holidays falling on a sunday maybe observed on the following Monday.
    This depends on formal announcements by the government, which only happens close
    to the date of the holiday.
    """

    country = "BI"
    observed_label = "%s (observed)"
    start_year = 1962

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, show_estimated=islamic_show_estimated)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Unity Day
        if self._year >= 1992:
            self._add_observed(self._add_holiday_feb_5("Unity Day"))

        # President Ntaryamira Day
        if self._year >= 1995:
            self._add_observed(self._add_holiday_apr_6("President Ntaryamira Day"))

        # Labour Day
        self._add_observed(self._add_labor_day("Labour Day"))

        # Ascension Day
        self._add_ascension_thursday("Ascension Day")

        # President Nkurunziza Day
        if self._year >= 2022:
            self._add_observed(self._add_holiday_jun_8("President Nkurunziza Day"))

        # Independence Day
        self._add_observed(self._add_holiday_jul_1("Independence Day"))

        # Assumption Day
        self._add_observed(self._add_assumption_of_mary_day("Assumption Day"))

        # Prince Louis Rwagasore Day
        self._add_observed(self._add_holiday_oct_13("Prince Louis Rwagasore Day"))

        # President Ndadaye's Day
        if self._year >= 1994:
            self._add_observed(self._add_holiday_oct_21("President Ndadaye's Day"))

        # All Saints' Day
        self._add_observed(self._add_all_saints_day("All Saints' Day"))

        # Christmas Day
        self._add_observed(self._add_christmas_day("Christmas Day"))

        # Eid ul Fitr
        for dt in self._add_eid_al_fitr_day("Eid ul Fitr"):
            self._add_observed(dt)

        # Eid al Adha
        for dt in self._add_eid_al_adha_day("Eid al Adha"):
            self._add_observed(dt)


class BI(Burundi):
    pass


class BDI(Burundi):
    pass
