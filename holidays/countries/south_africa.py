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

from holidays.calendars.gregorian import JAN, MAR, APR, MAY, JUN, AUG, NOV, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class SouthAfrica(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    http://www.gov.za/about-sa/public-holidays
    https://en.wikipedia.org/wiki/Public_holidays_in_South_Africa
    """

    country = "ZA"
    observed_label = "%s (Observed)"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, SouthAfricaStaticHolidays)
        super().__init__(observed_rule=SUN_TO_NEXT_MON, observed_since=1995, *args, **kwargs)

    def _populate(self, year):
        # Observed since 1910, with a few name changes
        if year <= 1909:
            return None

        super()._populate(year)

        self._add_observed(self._add_new_years_day("New Year's Day"))

        self._add_good_friday("Good Friday")

        self._add_easter_monday("Family Day" if year >= 1980 else "Easter Monday")

        if year <= 1951:
            name = "Dingaan's Day"
        elif year <= 1979:
            name = "Day of the Covenant"
        elif year <= 1994:
            name = "Day of the Vow"
        else:
            name = "Day of Reconciliation"
        self._add_observed(self._add_holiday_dec_16(name))

        self._add_christmas_day("Christmas Day")

        self._add_observed(
            self._add_christmas_day_two("Day of Goodwill" if year >= 1980 else "Boxing Day")
        )

        if year >= 1995:
            self._add_observed(self._add_holiday_mar_21("Human Rights Day"))

            self._add_observed(self._add_holiday_apr_27("Freedom Day"))

            self._add_observed(self._add_labor_day("Workers' Day"))

            self._add_observed(self._add_holiday_jun_16("Youth Day"))

            self._add_observed(self._add_holiday_aug_9("National Women's Day"))

            self._add_observed(self._add_holiday_sep_24("Heritage Day"))

        # Special holiday http://tiny.cc/za_y2k
        if self.observed and year == 2000:
            self._add_holiday_jan_3("Y2K changeover (Observed)")

        # Historic public holidays no longer observed
        if 1952 <= year <= 1973:
            self._add_holiday_apr_6("Van Riebeeck's Day")
        elif 1980 <= year <= 1994:
            self._add_holiday_apr_6("Founder's Day")

        if 1987 <= year <= 1989:
            self._add_holiday_1st_fri_of_may("Workers' Day")

        if year <= 1993:
            self._add_ascension_thursday("Ascension Day")

        if year <= 1951:
            self._add_holiday_may_24("Empire Day")

        if year <= 1960:
            self._add_holiday_may_31("Union Day")
        elif year <= 1993:
            self._add_holiday_may_31("Republic Day")

        if 1952 <= year <= 1960:
            self._add_holiday_2nd_mon_of_jul("Queen's Birthday")

        if 1961 <= year <= 1973:
            self._add_holiday_jul_10("Family Day")

        if year <= 1951:
            self._add_holiday_1st_mon_of_aug("King's Birthday")

        if 1952 <= year <= 1979:
            self._add_holiday_1st_mon_of_sep("Settlers' Day")

        if 1952 <= year <= 1993:
            self._add_holiday_oct_10("Kruger Day")


class ZA(SouthAfrica):
    pass


class ZAF(SouthAfrica):
    pass


class SouthAfricaStaticHolidays:
    special_holidays = {
        1999: (
            (JUN, 2, "National and provincial government elections"),
            (DEC, 31, "Y2K changeover"),
        ),
        2000: (JAN, 2, "Y2K changeover"),
        2004: (APR, 14, "National and provincial government elections"),
        2006: (MAR, 1, "Local government elections"),
        2008: (MAY, 2, "Public holiday by presidential decree"),
        2009: (APR, 22, "National and provincial government elections"),
        2011: (
            (MAY, 18, "Local government elections"),
            (DEC, 27, "Public holiday by presidential decree"),
        ),
        2014: (MAY, 7, "National and provincial government elections"),
        2016: (
            (AUG, 3, "Local government elections"),
            (DEC, 27, "Public holiday by presidential decree"),
        ),
        2019: (MAY, 8, "National and provincial government elections"),
        2021: (NOV, 1, "Municipal elections"),
        2022: (DEC, 27, "Public holiday by presidential decree"),
    }
