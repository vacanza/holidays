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

from holidays.calendars.gregorian import JAN, MAR, APR, MAY, JUN, AUG, NOV, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class SouthAfrica(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """South Africa holidays.

    References:
        * <https://web.archive.org/web/20250424073852/https://www.gov.za/about-sa/public-holidays>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_South_Africa>
        * <https://web.archive.org/web/20240715110800/https://www.gov.za/speeches/president-cyril-ramaphosa-progress-economic-recovery-30-oct-2023-0000>
        * <https://web.archive.org/web/20250427184315/https://www.gov.za/documents/notices/public-holidays-act-declaration-29-may-2024-public-holiday-23-feb-2024>
    """

    country = "ZA"
    observed_label = "%s (observed)"
    # Observed since 1910, with a few name changes
    start_year = 1910

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, SouthAfricaStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        kwargs.setdefault("observed_since", 1995)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        self._add_observed(self._add_new_years_day("New Year's Day"))

        self._add_good_friday("Good Friday")

        self._add_easter_monday("Family Day" if self._year >= 1980 else "Easter Monday")

        if self._year <= 1951:
            name = "Dingaan's Day"
        elif self._year <= 1979:
            name = "Day of the Covenant"
        elif self._year <= 1994:
            name = "Day of the Vow"
        else:
            name = "Day of Reconciliation"
        self._add_observed(self._add_holiday_dec_16(name))

        self._add_christmas_day("Christmas Day")

        self._add_observed(
            self._add_christmas_day_two("Day of Goodwill" if self._year >= 1980 else "Boxing Day")
        )

        if self._year >= 1995:
            self._add_observed(self._add_holiday_mar_21("Human Rights Day"))

            self._add_observed(self._add_holiday_apr_27("Freedom Day"))

            self._add_observed(self._add_labor_day("Workers' Day"))

            self._add_observed(self._add_holiday_jun_16("Youth Day"))

            self._add_observed(self._add_holiday_aug_9("National Women's Day"))

            self._add_observed(self._add_holiday_sep_24("Heritage Day"))

        # Historic public holidays no longer observed
        if 1952 <= self._year <= 1973:
            self._add_holiday_apr_6("Van Riebeeck's Day")
        elif 1980 <= self._year <= 1994:
            self._add_holiday_apr_6("Founder's Day")

        if 1987 <= self._year <= 1989:
            self._add_holiday_1st_fri_of_may("Workers' Day")

        if self._year <= 1993:
            self._add_ascension_thursday("Ascension Day")

        if self._year <= 1951:
            self._add_holiday_may_24("Empire Day")

        if self._year <= 1960:
            self._add_holiday_may_31("Union Day")
        elif self._year <= 1993:
            self._add_holiday_may_31("Republic Day")

        if 1952 <= self._year <= 1960:
            self._add_holiday_2nd_mon_of_jul("Queen's Birthday")

        if 1961 <= self._year <= 1973:
            self._add_holiday_jul_10("Family Day")

        if self._year <= 1951:
            self._add_holiday_1st_mon_of_aug("King's Birthday")

        if 1952 <= self._year <= 1979:
            self._add_holiday_1st_mon_of_sep("Settlers' Day")

        if 1952 <= self._year <= 1993:
            self._add_holiday_oct_10("Kruger Day")


class ZA(SouthAfrica):
    pass


class ZAF(SouthAfrica):
    pass


class SouthAfricaStaticHolidays:
    local_elections = "Local government elections"
    municipal_elections = "Municipal elections"
    national_and_provincial_elections = "National and provincial government elections"
    presidential_decree_holiday = "Public holiday by presidential decree"
    y2k_changeover = "Y2K changeover"
    special_public_holidays = {
        1999: (
            (JUN, 2, national_and_provincial_elections),
            (DEC, 31, y2k_changeover),
        ),
        2000: (JAN, 2, y2k_changeover),
        2004: (APR, 14, national_and_provincial_elections),
        2006: (MAR, 1, local_elections),
        2008: (MAY, 2, presidential_decree_holiday),
        2009: (APR, 22, national_and_provincial_elections),
        2011: (
            (MAY, 18, local_elections),
            (DEC, 27, presidential_decree_holiday),
        ),
        2014: (MAY, 7, national_and_provincial_elections),
        2016: (
            (AUG, 3, local_elections),
            (DEC, 27, presidential_decree_holiday),
        ),
        2019: (MAY, 8, national_and_provincial_elections),
        2021: (NOV, 1, municipal_elections),
        2022: (DEC, 27, presidential_decree_holiday),
        # Winning the 2023 Rugby World Cup
        2023: (DEC, 15, presidential_decree_holiday),
        2024: (MAY, 29, national_and_provincial_elections),
    }

    special_public_holidays_observed = {
        # https://web.archive.org/web/20120328122217/http://www.info.gov.za/speeches/1999/991028409p1002.htm
        2000: (JAN, 3, y2k_changeover),
    }
