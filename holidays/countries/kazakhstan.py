#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY


class Kazakhstan(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    References:
        - https://www.officeholidays.com/countries/kazakhstan/2020
        - https://egov.kz/cms/en/articles/holidays-calend
        - https://en.wikipedia.org/wiki/Public_holidays_in_Kazakhstan
        - https://adilet.zan.kz/rus/docs/Z010000267\_/history  # noqa W605
    """

    country = "KZ"
    observed_label = "%s (Observed)"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        kwargs.setdefault("observed_since", 2002)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        # Kazakhstan declared its sovereignty on 25 October 1990
        if year <= 1990:
            return None

        super()._populate(year)
        dts_observed = set()

        # New Year's holiday (2 days)
        name = "New Year"
        dts_observed.add(self._add_new_years_day(name))
        dts_observed.add(self._add_new_years_day_two(name))

        # Orthodox Christmas (nonworking day, without extending)
        if year >= 2006:
            self._add_christmas_day("Orthodox Christmas")

        # International Women's Day
        dts_observed.add(self._add_womens_day("International Women's Day"))

        # Nauryz holiday
        if year >= 2002:
            name = "Nauryz holiday"
            dts_observed.add(self._add_holiday_mar_22(name))
            if year >= 2010:
                dts_observed.add(self._add_holiday_mar_21(name))
                dts_observed.add(self._add_holiday_mar_23(name))

        # Kazakhstan People Solidarity Holiday
        dts_observed.add(self._add_labor_day("Kazakhstan People Solidarity Holiday"))

        # Defender of the Fatherland Day
        if year >= 2013:
            dts_observed.add(self._add_holiday_may_7("Defender of the Fatherland Day"))

        # Victory Day
        dts_observed.add(self._add_world_war_two_victory_day("Victory Day"))

        # Capital Day
        if year >= 2009:
            dts_observed.add(self._add_holiday_jul_6("Capital Day"))

        # Constitution Day of the Republic of Kazakhstan
        if year >= 1996:
            dts_observed.add(
                self._add_holiday_aug_30("Constitution Day of the Republic of Kazakhstan")
            )

        # Republic Day
        if 1994 <= year <= 2008 or year >= 2022:
            dts_observed.add(self._add_holiday_oct_25("Republic Day"))

        # First President Day
        if 2012 <= year <= 2021:
            dts_observed.add(self._add_holiday_dec_1("First President Day"))

        # Kazakhstan Independence Day
        name = "Kazakhstan Independence Day"
        dts_observed.add(self._add_holiday_dec_16(name))
        if 2002 <= year <= 2021:
            dts_observed.add(self._add_holiday_dec_17(name))

        if self.observed:
            self._populate_observed(dts_observed)

        # Kurban Ait (nonworking day, without extending)
        if year >= 2006:
            self._add_eid_al_adha_day("Kurban Ait")


class KZ(Kazakhstan):
    pass


class KAZ(Kazakhstan):
    pass
