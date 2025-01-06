#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date

from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
    _timedelta,
)
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_TO_PREV_FRI, SUN_TO_NEXT_MON


class NewYorkStockExchange(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """
    Official regulations:
    - https://www.nyse.com/publicdocs/nyse/regulation/nyse/NYSE_Rules.pdf
    - https://www.nyse.com/markets/hours-calendars
    Historical data:
    - s3.amazonaws.com/armstrongeconomics-wp/2013/07/NYSE-Closings.pdf
    - https://web.archive.org/web/20211101162021/https://www.nyse.com/markets/hours-calendars
    """

    market = "XNYS"
    observed_label = "%s (observed)"
    start_year = 1863

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, NewYorkStockExchangeStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_TO_PREV_FRI + SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        name = "New Year's Day"
        self._move_holiday(self._add_new_years_day(name))

        # MLK, 3rd Monday of January.
        if self._year >= 1998:
            self._add_holiday_3rd_mon_of_jan("Martin Luther King Jr. Day")

        # LINCOLN BIRTHDAY: observed 1896 - 1953 and 1968, Feb 12 (observed)
        if 1896 <= self._year <= 1953 or self._year == 1968:
            self._move_holiday(self._add_holiday_feb_12("Lincoln's Birthday"))

        # WASHINGTON'S BIRTHDAY: Feb 22 (obs) until 1971, then 3rd Mon of Feb
        name = "Washington's Birthday"
        if self._year <= 1970:
            self._move_holiday(self._add_holiday_feb_22(name))
        else:
            self._add_holiday_3rd_mon_of_feb(name)

        # GOOD FRIDAY - closed every year except 1898, 1906, and 1907
        if self._year not in {1898, 1906, 1907}:
            self._add_good_friday("Good Friday")

        # MEM DAY (May 30) - closed every year since 1873
        # last Mon in May since 1971
        if self._year >= 1873:
            name = "Memorial Day"
            if self._year <= 1970:
                self._move_holiday(self._add_holiday_may_30(name))
            else:
                self._add_holiday_last_mon_of_may(name)

        # FLAG DAY: June 14th 1916 - 1953
        if 1916 <= self._year <= 1953:
            self._move_holiday(self._add_holiday_jun_14("Flag Day"))

        # JUNETEENTH: since 2022
        if self._year >= 2022:
            self._move_holiday(self._add_holiday_jun_19("Juneteenth National Independence Day"))

        # INDEPENDENCE DAY (July 4) - history suggests closed every year
        self._move_holiday(self._add_holiday_jul_4("Independence Day"))

        # LABOR DAY - first mon in Sept, since 1887
        if self._year >= 1887:
            self._add_holiday_1st_mon_of_sep("Labor Day")

        # COLUMBUS DAY/INDIGENOUS PPL DAY: Oct 12 - closed 1909-1953
        if 1909 <= self._year <= 1953:
            self._move_holiday(self._add_columbus_day("Columbus Day"))

        # ELECTION DAY: Tuesday after first Monday in November (2 U.S. Code §7)
        # closed until 1969, then closed pres years 1972-80
        if self._year <= 1968 or self._year in {1972, 1976, 1980}:
            self._add_holiday_1_day_past_1st_mon_of_nov("Election Day")

        # VETERAN'S DAY: Nov 11 - closed 1918, 1921, 1934-1953
        if self._year in {1918, 1921} or 1934 <= self._year <= 1953:
            self._move_holiday(self._add_remembrance_day("Veteran's Day"))

        # THXGIVING DAY: 4th Thurs in Nov - closed every year
        self._add_holiday_4th_thu_of_nov("Thanksgiving Day")

        # XMAS DAY: Dec 25th - every year
        self._move_holiday(self._add_christmas_day("Christmas Day"))

        # Special holidays.
        if self._year == 1914:
            # Beginning of WWI.
            begin = date(self._year, JUL, 31)
            end = date(self._year, NOV, 27)
            for dt in (_timedelta(begin, n) for n in range((end - begin).days + 1)):
                if self._is_weekend(dt) or dt in self:
                    continue
                self._add_holiday("World War I", dt)
        elif self._year == 1968:
            begin = date(self._year, JUN, 12)
            end = date(self._year, DEC, 24)
            # Wednesday special holiday.
            for dt in (_timedelta(begin, n) for n in range(0, (end - begin).days + 1, 7)):
                self._add_holiday("Paper Crisis", dt)


class XNYS(NewYorkStockExchange):
    pass


class NYSE(NewYorkStockExchange):
    pass


class NewYorkStockExchangeStaticHolidays:
    """
    References:
    - https://guides.loc.gov/presidents-portraits/chronological
    - https://www.presidency.ucsb.edu/documents/proclamation-3561-national-day-mourning-for-president-kennedy
    """

    # Blizzard of 1888.
    name_blizard_1888 = "Blizzard of 1888"

    # Centennial of George Washington's Inauguration.
    name_george_washington_centennial = "Centennial of George Washington's Inauguration"

    # Columbian Celebration.
    name_columbian_celebration = "Columbian Celebration"

    # Heatless Day.
    name_heatless_day = "Heatless Day"

    # Catch Up Day.
    name_catch_up_day = "Catch Up Day"

    # Special Bank Holiday.
    name_special_bank_holiday = "Special Bank Holiday"

    # V-J Day (WWII).
    name_vj_day_wwii = "V-J Day (WWII)"

    # Christmas Eve.
    name_christmas_eve = "Christmas Eve"

    # Closed for Sept 11, 2001 Attacks.
    name_sept11_attacks = "Closed for Sept 11, 2001 Attacks"

    # Hurricane Sandy.
    name_hurricane_sandy = "Hurricane Sandy"

    special_public_holidays = {
        1888: (
            (MAR, 12, name_blizard_1888),
            (MAR, 13, name_blizard_1888),
            (NOV, 30, "Thanksgiving Friday 1888"),
        ),
        1889: (
            (APR, 29, name_george_washington_centennial),
            (APR, 30, name_george_washington_centennial),
            (MAY, 1, name_george_washington_centennial),
        ),
        1892: (
            (OCT, 12, name_columbian_celebration),
            (OCT, 21, name_columbian_celebration),
        ),
        1893: (APR, 27, name_columbian_celebration),
        1897: (APR, 27, "Grant's Birthday"),
        1898: (MAY, 4, "Charter Day"),
        1899: (
            (MAY, 29, "Monday before Decoration Day"),
            (JUL, 3, "Monday before Independence Day"),
            (SEP, 29, "Admiral Dewey Celebration"),
        ),
        1900: (DEC, 24, name_christmas_eve),
        1901: (
            (JUL, 5, "Friday after Independence Day"),
            (SEP, 19, "National Day of Mourning for President WIlliam McKinley"),
        ),
        1903: (APR, 22, "Opening of new NYSE building"),
        1917: (JUN, 5, "Draft Registration Day"),
        1918: (
            (JAN, 28, name_heatless_day),
            (FEB, 4, name_heatless_day),
            (FEB, 11, name_heatless_day),
            (SEP, 12, "Draft Registration Day"),
            (NOV, 11, "Armistice Day"),
        ),
        1919: (
            (MAR, 25, "Homecoming Day for 27th Division"),
            (MAY, 6, "Parade Day for 77th Division"),
            (SEP, 10, "Return of General Pershing"),
        ),
        1923: (
            (AUG, 3, "Death of President Warren G. Harding"),
            (AUG, 10, "National Day of Mourning for President Warren G. Harding"),
        ),
        1927: (JUN, 13, "Parade for Colonel Charles Lindbergh"),
        1929: (
            (NOV, 1, name_catch_up_day),
            (NOV, 29, name_catch_up_day),
        ),
        1933: (
            (MAR, 6, name_special_bank_holiday),
            (MAR, 7, name_special_bank_holiday),
            (MAR, 8, name_special_bank_holiday),
            (MAR, 9, name_special_bank_holiday),
            (MAR, 10, name_special_bank_holiday),
            (MAR, 13, name_special_bank_holiday),
            (MAR, 14, name_special_bank_holiday),
        ),
        1945: (
            (AUG, 15, name_vj_day_wwii),
            (AUG, 16, name_vj_day_wwii),
            (DEC, 24, name_christmas_eve),
        ),
        1954: (DEC, 24, name_christmas_eve),
        1956: (DEC, 24, name_christmas_eve),
        1958: (DEC, 26, "Day after Christmas"),
        1961: (MAY, 29, "Day before Decoration Day"),
        1963: (NOV, 25, "National Day of Mourning for President John F. Kennedy"),
        1965: (DEC, 24, name_christmas_eve),
        1968: (
            (APR, 9, "National Day of Mourning for Martin Luther King Jr."),
            (JUL, 5, "Day after Independence Day"),
        ),
        1969: (
            (FEB, 10, "Heavy Snow"),
            (MAR, 31, "National Day of Mourning for former President Dwight D. Eisenhower"),
            (JUL, 21, "National Participation in Lunar Exploration"),
        ),
        1972: (DEC, 28, "National Day of Mourning for former President Harry S. Truman"),
        1973: (JAN, 25, "National Day of Mourning for former President Lyndon B. Johnson"),
        1977: (JUL, 14, "Blackout in New York City"),
        1985: (SEP, 27, "Hurricane Gloria"),
        1994: (APR, 27, "National Day of Mourning for former President Richard M. Nixon"),
        2001: (
            (SEP, 11, name_sept11_attacks),
            (SEP, 12, name_sept11_attacks),
            (SEP, 13, name_sept11_attacks),
            (SEP, 14, name_sept11_attacks),
        ),
        2004: (JUN, 11, "National Day of Mourning for former President Ronald Reagan"),
        2007: (JAN, 2, "National Day of Mourning for former President Gerald R. Ford"),
        2012: (
            (OCT, 29, name_hurricane_sandy),
            (OCT, 30, name_hurricane_sandy),
        ),
        2018: (DEC, 5, "National Day of Mourning for former President George H. W. Bush"),
        2025: (JAN, 9, "National Day of Mourning for former President Jimmy Carter"),
    }
