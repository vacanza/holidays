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

from datetime import date
from gettext import gettext as tr

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
    SAT,
    SUN,
    _timedelta,
)
from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_TO_PREV_FRI, SUN_TO_NEXT_MON


class NewYorkStockExchange(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """New York Stock Exchange holidays.

    References:
        * [NYSE Rules](https://web.archive.org/web/20240118104341/https://www.nyse.com/publicdocs/nyse/regulation/nyse/NYSE_Rules.pdf)
        * [NYSE History - Timeline](https://web.archive.org/web/20150113014537/https://www.nyse.com/about/history/timeline_trading.html)

    Historical data:
        * [History of NYSE Holidays](https://web.archive.org/web/20221206064307/https://s3.amazonaws.com/armstrongeconomics-wp/2013/07/NYSE-Closings.pdf)
        * [NYSE Holidays & Trading Hours](https://web.archive.org/web/20211101162021/https://www.nyse.com/markets/hours-calendars)
    """

    market = "XNYS"
    default_language = "en_US"
    supported_languages = ("en_US", "gu", "hi")
    # %s (observed)
    observed_label = tr("%s (observed)")
    start_year = 1863
    supported_categories = (HALF_DAY, PUBLIC)

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, NewYorkStockExchangeStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_TO_PREV_FRI + SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _add_observed(self, dt: date, **kwargs) -> tuple[bool, date | None]:
        kwargs["rule"] = SUN_TO_NEXT_MON if dt.year <= 1952 else self._observed_rule
        return super()._add_observed(dt, **kwargs)

    def _get_weekend(self, dt: date) -> set[int]:
        # September 29, 1952: The NYSE changes its trading hours
        # to 10am to 3:30pm Monday-Friday, and closes on Saturdays.
        return {SAT, SUN} if dt >= date(1952, SEP, 29) else {SUN}

    def _populate_ranged_holidays(
        self, name: str, start: tuple[int, int], end: tuple[int, int], step: int = 1
    ):
        start_date = date(self._year, *start)
        end_date = date(self._year, *end)
        for dt in (
            _timedelta(start_date, n) for n in range(0, (end_date - start_date).days + 1, step)
        ):
            if self._is_weekend(dt) or dt in self:
                continue
            self._add_holiday(name, dt)

    def _populate_public_holidays(self):
        # According to NYSE Rules (Rule 51), when any holiday observed by the Exchange falls on
        # a Saturday, the Exchange will not be open for business on the preceding Friday ...,
        # unless unusual business conditions exist, such as the ending of a monthly or the yearly
        # accounting period.
        # Therefore, New Year's Day holiday is not moved to Dec 31, even after 1952 amendments.

        # New Year's Day.
        self._move_holiday(self._add_new_years_day(tr("New Year's Day")))

        if self._year >= 1998:
            # Martin Luther King Jr. Day.
            self._add_holiday_3rd_mon_of_jan(tr("Martin Luther King Jr. Day"))

        if 1896 <= self._year <= 1953:
            # Lincoln's Birthday.
            self._move_holiday(self._add_holiday_feb_12(tr("Lincoln's Birthday")))

        # Washington's Birthday.
        name = tr("Washington's Birthday")
        if self._year >= 1971:
            self._add_holiday_3rd_mon_of_feb(name)
        else:
            self._move_holiday(self._add_holiday_feb_22(name))

        if self._year not in {1898, 1906, 1907}:
            # Good Friday.
            self._add_good_friday(tr("Good Friday"))

        if self._year >= 1873:
            # Memorial Day.
            name = tr("Memorial Day")
            if self._year >= 1971:
                self._add_holiday_last_mon_of_may(name)
            else:
                self._move_holiday(self._add_holiday_may_30(name))

        if 1916 <= self._year <= 1953:
            # Flag Day.
            self._move_holiday(self._add_holiday_jun_14(tr("Flag Day")))

        if self._year >= 2022:
            self._move_holiday(
                # Juneteenth National Independence Day.
                self._add_holiday_jun_19(tr("Juneteenth National Independence Day"))
            )

        # Independence Day.
        self._move_holiday(self._add_holiday_jul_4(tr("Independence Day")))

        if self._year >= 1887:
            # Labor Day.
            self._add_holiday_1st_mon_of_sep(tr("Labor Day"))

        if 1909 <= self._year <= 1953:
            # Columbus Day.
            self._move_holiday(self._add_columbus_day(tr("Columbus Day")))

        if self._year <= 1968 or self._year in {1972, 1976, 1980}:
            # Election Day.
            self._add_holiday_1_day_past_1st_mon_of_nov(tr("Election Day"))

        if 1934 <= self._year <= 1953:
            # Veteran's Day.
            self._move_holiday(self._add_remembrance_day(tr("Veteran's Day")))

        thanksgiving_day_dates = {
            1865: (DEC, 7),
            1869: (NOV, 18),
            1939: (NOV, 23),
            1940: (NOV, 21),
            1941: (NOV, 20),
        }
        # Thanksgiving Day.
        name = tr("Thanksgiving Day")
        if dt := thanksgiving_day_dates.get(self._year):
            self._add_holiday(name, dt)
        elif self._year >= 1942:
            self._add_holiday_4th_thu_of_nov(name)
        else:
            self._add_holiday_last_thu_of_nov(name)

        # Christmas Day.
        self._move_holiday(self._add_christmas_day(tr("Christmas Day")))

        # Special holidays.

        if self._year == 1914:
            self._populate_ranged_holidays(
                # Pending outbreak of World War I.
                tr("Pending outbreak of World War I"),
                (JUL, 31),
                (NOV, 27),
            )
        elif self._year == 1968:
            # WED.
            self._populate_ranged_holidays(
                # Paperwork Crisis.
                tr("Paperwork Crisis"),
                (JUN, 12),
                (DEC, 24),
                7,
            )

        # Closed Saturdays.
        closed_sat_date_ranges = {
            # Start date, end date.
            1944: ((AUG, 19), (SEP, 2)),
            1945: ((JUL, 7), (SEP, 1)),
            1946: ((JUN, 1), (SEP, 28)),
            1947: ((MAY, 31), (SEP, 27)),
            1948: ((MAY, 29), (SEP, 25)),
            1949: ((MAY, 28), (SEP, 24)),
            1950: ((JUN, 3), (SEP, 30)),
            1951: ((JUN, 2), (SEP, 29)),
            1952: ((MAY, 31), (SEP, 27)),
        }
        if self._year in closed_sat_date_ranges:
            start, end = closed_sat_date_ranges[self._year]
            # Closed Saturday.
            self._populate_ranged_holidays(tr("Closed Saturday"), start, end, 7)

    def _populate_half_day_holidays(self):
        close_1pm_label = self.tr("%s (markets close at 1:00pm)")
        close_2pm_label = self.tr("%s (markets close at 2:00pm)")
        close_2_30pm_label = self.tr("%s (markets close at 2:30pm)")
        close_3pm_label = self.tr("%s (markets close at 3:00pm)")

        # Special holidays.

        name_paperwork_crisis = self.tr("Paperwork Crisis")
        if self._year == 1968:
            self._populate_ranged_holidays(
                # Back office work load.
                close_2pm_label % self.tr("Back office work load"),
                (JAN, 22),
                (MAR, 1),
            )
        elif self._year == 1969:
            # THU.
            self._populate_ranged_holidays(
                close_2pm_label % name_paperwork_crisis, (JAN, 2), (JUL, 3), 7
            )

            # MON-FRI.
            self._populate_ranged_holidays(
                close_2_30pm_label % name_paperwork_crisis, (JUL, 7), (SEP, 26)
            )

            # MON-FRI.
            self._populate_ranged_holidays(
                close_3pm_label % name_paperwork_crisis, (SEP, 29), (DEC, 31)
            )
        elif self._year == 1970:
            # MON-FRI.
            self._populate_ranged_holidays(
                close_3pm_label % name_paperwork_crisis, (JAN, 2), (MAY, 1)
            )

        # 1990-1992 early closings are covered by special holidays.
        if self._year >= 1993:
            jul_4 = (JUL, 4)
            if (
                self._is_weekday(jul_4)
                and not self._is_monday(jul_4)
                and self._year not in {1996, 2002}
            ):
                # Day before Independence Day.
                self._add_holiday_jul_3(close_1pm_label % self.tr("Day before Independence Day"))

            self._add_holiday_1_day_past_4th_thu_of_nov(
                # Day after Thanksgiving Day.
                close_1pm_label % self.tr("Day after Thanksgiving Day")
            )

            if self._is_weekday(self._christmas_day) and not self._is_monday(self._christmas_day):
                # Christmas Eve.
                self._add_christmas_eve(close_1pm_label % self.tr("Christmas Eve"))


class XNYS(NewYorkStockExchange):
    pass


class NYSE(NewYorkStockExchange):
    pass


class NewYorkStockExchangeStaticHolidays:
    """New York Stock Exchange special holidays.

    References:
        * <https://web.archive.org/web/20250421093104/https://guides.loc.gov/presidents-portraits/chronological>
        * <https://web.archive.org/web/20250208135423/https://www.presidency.ucsb.edu/documents/proclamation-3561-national-day-mourning-for-president-kennedy>
    """

    # %s (markets close at 11:00am).
    close_11am_label = tr("%s (markets close at 11:00am)")

    # %s (markets close at 12:00pm).
    close_12pm_label = tr("%s (markets close at 12:00pm)")

    # %s (markets close at 12:30pm).
    close_12_30pm_label = tr("%s (markets close at 12:30pm)")

    # %s (markets close at 1:00pm).
    close_1pm_label = tr("%s (markets close at 1:00pm)")

    # %s (markets close at 2:00pm).
    close_2pm_label = tr("%s (markets close at 2:00pm)")

    # %s (markets close at 2:30pm).
    close_2_30pm_label = tr("%s (markets close at 2:30pm)")

    # %s (markets close at 3:00pm).
    close_3pm_label = tr("%s (markets close at 3:00pm)")

    # %s (markets close at 3:30pm).
    close_3_30pm_label = tr("%s (markets close at 3:30pm)")

    # Blizzard of 1888.
    name_blizzard_of_1888 = tr("Blizzard of 1888")

    # Centennial of George Washington's Inauguration.
    name_centennial_of_gw_inauguration = tr("Centennial of George Washington's Inauguration")

    # Columbian Celebration.
    name_columbian_celebration = tr("Columbian Celebration")

    # Heatless Day.
    name_heatless_day = tr("Heatless Day")

    # Catch Up Day.
    name_catch_up_day = tr("Catch Up Day")

    # Special Bank Holiday.
    name_national_banking_holiday = tr("National Banking Holiday")

    # V-J Day. End of World War II.
    name_vj_day = tr("V-J Day. End of World War II")

    # Christmas Eve.
    name_christmas_eve = tr("Christmas Eve")

    # Closed following Attacks on the World Trade Center.
    name_closed_following_wtc_attacks = tr("Closed following Attacks on the World Trade Center")

    # Hurricane Sandy.
    name_hurricane_sandy = tr("Hurricane Sandy")

    # Liberty Day.
    name_liberty_day = tr("Liberty Day")

    # Heavy volume. To allow member firm offices to catch up on work.
    name_heavy_volume_catch_up = tr(
        "Heavy volume. To allow member firm offices to catch up on work"
    )

    # Saturday after Washington's Birthday.
    name_saturday_after_washingtons_birthday = tr("Saturday after Washington's Birthday")

    # Saturday after Good Friday.
    name_saturday_after_good_friday = tr("Saturday after Good Friday")

    # Saturday before Decoration Day.
    name_saturday_before_decoration_day = tr("Saturday before Decoration Day")

    # Saturday after Decoration Day.
    name_saturday_after_decoration_day = tr("Saturday after Decoration Day")

    # Saturday before Independence Day.
    name_saturday_before_independence_day = tr("Saturday before Independence Day")

    # Saturday after Independence Day.
    name_saturday_after_independence_day = tr("Saturday after Independence Day")

    # Day after Independence Day.
    name_day_after_independence_day = tr("Day after Independence Day")

    # Saturday before Labor Day.
    name_saturday_before_labor_day = tr("Saturday before Labor Day")

    # Saturday after Columbus Day.
    name_saturday_after_columbus_day = tr("Saturday after Columbus Day")

    # Saturday before Christmas.
    name_saturday_before_christmas_day = tr("Saturday before Christmas Day")

    # Friday after Christmas Day.
    name_friday_after_christmas = tr("Friday after Christmas Day")

    # Saturday after Christmas Day.
    name_saturday_after_christmas_day = tr("Saturday after Christmas Day")

    # Admiral Dewey Celebration.
    name_admiral_dewey_celebration = tr("Admiral Dewey Celebration")

    # Draft Registration Day.
    name_draft_registration_day = tr("Draft Registration Day")

    # To allow offices to catch up on work.
    name_to_catch_up = tr("To allow offices to catch up on work")

    # Volume activity.
    name_volume_activity = tr("Volume activity")

    # Transit strike.
    name_transit_strike = tr("Transit strike")

    # Back office work load.
    name_back_office_work_load = tr("Back office work load")

    # Snowstorm.
    name_snowstorm = tr("Snowstorm")

    # Shortened hours following market break.
    name_shortened_hours_following_market_break = tr("Shortened hours following market break")

    special_public_holidays = {
        # Funeral of former President Ulysses S. Grant.
        1885: (AUG, 8, tr("Funeral of former President Ulysses S. Grant")),
        1887: (
            (JUL, 2, name_saturday_before_independence_day),
            (DEC, 24, name_saturday_before_christmas_day),
        ),
        1888: (
            (MAR, 12, name_blizzard_of_1888),
            (MAR, 13, name_blizzard_of_1888),
            (SEP, 1, name_saturday_before_labor_day),
            # Friday after Thanksgiving Day.
            (NOV, 30, tr("Friday after Thanksgiving Day")),
        ),
        1889: (
            (APR, 29, name_centennial_of_gw_inauguration),
            (APR, 30, name_centennial_of_gw_inauguration),
            (MAY, 1, name_centennial_of_gw_inauguration),
        ),
        1890: (JUL, 5, name_saturday_after_independence_day),
        1891: (DEC, 26, name_saturday_after_christmas_day),
        1892: (
            (JUL, 2, name_saturday_before_independence_day),
            (OCT, 12, name_columbian_celebration),
            (OCT, 21, name_columbian_celebration),
            (OCT, 22, name_columbian_celebration),
        ),
        1893: (APR, 27, name_columbian_celebration),
        1896: (DEC, 26, name_saturday_after_christmas_day),
        # Grant's Birthday.
        1897: (APR, 27, tr("Grant's Birthday")),
        1898: (
            # Charter Day.
            (MAY, 4, tr("Charter Day")),
            (JUL, 2, name_saturday_before_independence_day),
            # Welcome of naval commanders.
            (AUG, 20, tr("Welcome of naval commanders")),
            (SEP, 3, name_saturday_before_labor_day),
            (DEC, 24, name_saturday_before_christmas_day),
        ),
        1899: (
            # Saturday before Lincoln's Birthday.
            (FEB, 11, tr("Saturday before Lincoln's Birthday")),
            # Monday before Decoration Day.
            (MAY, 29, tr("Monday before Decoration Day")),
            # Monday before Independence Day.
            (JUL, 3, tr("Monday before Independence Day")),
            (SEP, 29, name_admiral_dewey_celebration),
            (SEP, 30, name_admiral_dewey_celebration),
            # Funeral of Vice-President Garret A. Hobart.
            (NOV, 25, tr("Funeral of Vice-President Garret A. Hobart")),
        ),
        1900: (
            (APR, 14, name_saturday_after_good_friday),
            (SEP, 1, name_saturday_before_labor_day),
            (DEC, 24, name_saturday_before_christmas_day),
        ),
        1901: (
            # Funeral of Queen Victoria of England.
            (FEB, 2, tr("Funeral of Queen Victoria of England")),
            (FEB, 23, name_saturday_after_washingtons_birthday),
            (APR, 6, name_saturday_after_good_friday),
            # Moved to temporary quarters in Produce Exchange.
            (APR, 27, tr("Moved to temporary quarters in Produce Exchange")),
            # Enlarged temporary quarters in Produce Exchange.
            (MAY, 11, tr("Enlarged temporary quarters in Produce Exchange")),
            # Friday after Independence Day.
            (JUL, 5, tr("Friday after Independence Day")),
            (JUL, 6, name_saturday_after_independence_day),
            (AUG, 31, name_saturday_before_labor_day),
            # Death of President William McKinley.
            (SEP, 14, tr("Death of President William McKinley")),
            # Funeral of President William McKinley.
            (SEP, 19, tr("Funeral of President William McKinley")),
        ),
        1902: (
            (MAR, 29, name_saturday_after_good_friday),
            (MAY, 31, name_saturday_after_decoration_day),
            (JUL, 5, name_saturday_after_independence_day),
            # Coronation of King Edward VII of England.
            (AUG, 9, tr("Coronation of King Edward VII of England")),
            (AUG, 30, name_saturday_before_labor_day),
        ),
        1903: (
            # Saturday before Washington's Birthday.
            (FEB, 21, tr("Saturday before Washington's Birthday")),
            (APR, 11, name_saturday_after_good_friday),
            # Opening of new NYSE building.
            (APR, 22, tr("Opening of new NYSE building")),
            (SEP, 5, name_saturday_before_labor_day),
            (DEC, 26, name_saturday_after_christmas_day),
        ),
        1904: (
            (MAY, 28, name_saturday_before_decoration_day),
            (JUL, 2, name_saturday_before_independence_day),
            (SEP, 3, name_saturday_before_labor_day),
            (DEC, 24, name_saturday_before_christmas_day),
        ),
        1905: (APR, 22, name_saturday_after_good_friday),
        1907: (
            (FEB, 23, name_saturday_after_washingtons_birthday),
            (MAR, 30, name_saturday_after_good_friday),
            (AUG, 31, name_saturday_before_labor_day),
        ),
        1908: (
            (APR, 18, name_saturday_after_good_friday),
            (SEP, 5, name_saturday_before_labor_day),
            (DEC, 26, name_saturday_after_christmas_day),
        ),
        1909: (
            # Saturday after Lincoln's Birthday.
            (FEB, 13, tr("Saturday after Lincoln's Birthday")),
            (APR, 10, name_saturday_after_good_friday),
            (MAY, 29, name_saturday_before_decoration_day),
            (JUL, 3, name_saturday_before_independence_day),
            (SEP, 4, name_saturday_before_labor_day),
            # Reception Day of the Hudson-Fulton Celebration.
            (SEP, 25, tr("Reception Day of the Hudson-Fulton Celebration")),
        ),
        1910: (
            (MAR, 26, name_saturday_after_good_friday),
            (MAY, 28, name_saturday_before_decoration_day),
            (JUL, 2, name_saturday_before_independence_day),
            (SEP, 3, name_saturday_before_labor_day),
            (DEC, 24, name_saturday_before_christmas_day),
        ),
        1911: (
            (APR, 15, name_saturday_after_good_friday),
            (SEP, 2, name_saturday_before_labor_day),
            (DEC, 23, name_saturday_before_christmas_day),
        ),
        1912: (
            (AUG, 31, name_saturday_before_labor_day),
            # Funeral of Vice-President James S. Sherman.
            (NOV, 2, tr("Funeral of Vice-President James S. Sherman")),
        ),
        1913: (
            (MAR, 22, name_saturday_after_good_friday),
            (MAY, 31, name_saturday_after_decoration_day),
            (JUL, 5, name_saturday_after_independence_day),
            (AUG, 30, name_saturday_before_labor_day),
        ),
        # Saturday before New Year's Day.
        1916: (DEC, 30, tr("Saturday before New Year's Day")),
        1917: (
            (JUN, 5, name_draft_registration_day),
            # Heat.
            (AUG, 4, tr("Heat")),
            (SEP, 1, name_saturday_before_labor_day),
            (OCT, 13, name_saturday_after_columbus_day),
        ),
        1918: (
            (JAN, 28, name_heatless_day),
            (FEB, 4, name_heatless_day),
            (FEB, 11, name_heatless_day),
            (SEP, 12, name_draft_registration_day),
            # Armistice signed.
            (NOV, 11, tr("Armistice signed")),
        ),
        1919: (
            # Homecoming of 27th Division.
            (MAR, 25, tr("Homecoming of 27th Division")),
            # Parade of 77th Division.
            (MAY, 6, tr("Parade of 77th Division")),
            (MAY, 31, name_saturday_after_decoration_day),
            (JUL, 5, name_saturday_after_independence_day),
            # Heat and to allow offices to catch up on work.
            (JUL, 19, tr("Heat and to allow offices to catch up on work")),
            (AUG, 2, name_to_catch_up),
            (AUG, 16, name_to_catch_up),
            (AUG, 30, name_saturday_before_labor_day),
            # Return of General John J. Pershing.
            (SEP, 10, tr("Return of General John J. Pershing")),
        ),
        1920: (
            (APR, 3, name_saturday_after_good_friday),
            # Many firms changed office locations.
            (MAY, 1, tr("Many firms changed office locations")),
            (JUL, 3, name_saturday_before_independence_day),
            (SEP, 4, name_saturday_before_labor_day),
        ),
        1921: (
            (MAY, 28, name_saturday_before_decoration_day),
            (JUL, 2, name_saturday_before_independence_day),
            (SEP, 3, name_saturday_before_labor_day),
            # Veteran's Day.
            (NOV, 11, tr("Veteran's Day")),
        ),
        1922: (DEC, 23, name_saturday_before_christmas_day),
        1923: (
            # Death of President Warren G. Harding.
            (AUG, 3, tr("Death of President Warren G. Harding")),
            # Funeral of President Warren G. Harding.
            (AUG, 10, tr("Funeral of President Warren G. Harding")),
        ),
        1924: (MAY, 31, name_saturday_after_decoration_day),
        1925: (DEC, 26, name_saturday_after_christmas_day),
        1926: (
            (MAY, 29, name_saturday_before_decoration_day),
            (JUL, 3, name_saturday_before_independence_day),
            (SEP, 4, name_saturday_before_labor_day),
        ),
        # Parade for Colonel Charles A. Lindbergh.
        1927: (JUN, 13, tr("Parade for Colonel Charles A. Lindbergh")),
        1928: (
            (APR, 7, name_heavy_volume_catch_up),
            (APR, 21, name_heavy_volume_catch_up),
            (MAY, 5, name_heavy_volume_catch_up),
            (MAY, 12, name_heavy_volume_catch_up),
            (MAY, 19, name_heavy_volume_catch_up),
            (MAY, 26, name_heavy_volume_catch_up),
            (NOV, 24, name_heavy_volume_catch_up),
        ),
        1929: (
            (FEB, 9, name_heavy_volume_catch_up),
            (FEB, 23, name_saturday_after_washingtons_birthday),
            (MAR, 30, name_saturday_after_good_friday),
            (AUG, 31, name_saturday_before_labor_day),
            (NOV, 1, name_catch_up_day),
            (NOV, 2, name_catch_up_day),
            (NOV, 9, name_catch_up_day),
            (NOV, 16, name_catch_up_day),
            (NOV, 23, name_catch_up_day),
            (NOV, 29, name_catch_up_day),
            (NOV, 30, name_catch_up_day),
        ),
        1930: (
            (APR, 19, name_saturday_after_good_friday),
            (MAY, 31, name_saturday_after_decoration_day),
            (JUL, 5, name_saturday_after_independence_day),
            (AUG, 30, name_saturday_before_labor_day),
        ),
        1931: (
            (SEP, 5, name_saturday_before_labor_day),
            (DEC, 26, name_saturday_after_christmas_day),
        ),
        1932: (JUL, 2, name_saturday_before_independence_day),
        1933: (
            # Funeral of former President Calvin Coolidge.
            (JAN, 7, tr("Funeral of former President Calvin Coolidge")),
            # State Banking Holiday.
            (MAR, 4, tr("State Banking Holiday")),
            (MAR, 6, name_national_banking_holiday),
            (MAR, 7, name_national_banking_holiday),
            (MAR, 8, name_national_banking_holiday),
            (MAR, 9, name_national_banking_holiday),
            (MAR, 10, name_national_banking_holiday),
            (MAR, 11, name_national_banking_holiday),
            (MAR, 13, name_national_banking_holiday),
            (MAR, 14, name_national_banking_holiday),
            (JUL, 28, name_volume_activity),
            (AUG, 5, name_volume_activity),
            (AUG, 12, name_volume_activity),
            (AUG, 19, name_volume_activity),
            (AUG, 26, name_volume_activity),
            (SEP, 2, name_volume_activity),
        ),
        1936: (DEC, 26, name_saturday_after_christmas_day),
        1937: (
            (MAY, 29, name_saturday_before_decoration_day),
            (JUL, 3, name_saturday_before_independence_day),
        ),
        1945: (
            # National Day of Mourning for President Franklin D. Roosevelt.
            (APR, 14, tr("National Day of Mourning for President Franklin D. Roosevelt")),
            (AUG, 15, name_vj_day),
            (AUG, 16, name_vj_day),
            (OCT, 13, name_saturday_after_columbus_day),
            # Navy Day.
            (OCT, 27, tr("Navy Day")),
            (DEC, 24, name_christmas_eve),
        ),
        1946: (
            (FEB, 23, name_saturday_after_washingtons_birthday),
            # Railroad strike.
            (MAY, 25, tr("Railroad strike")),
        ),
        # Severe weather conditions.
        1948: (JAN, 3, tr("Severe weather conditions")),
        1949: (DEC, 24, name_christmas_eve),
        # Saturday before Christmas Eve.
        1950: (DEC, 23, tr("Saturday before Christmas Eve")),
        1954: (DEC, 24, name_christmas_eve),
        1956: (DEC, 24, name_christmas_eve),
        # Day after Christmas.
        1958: (DEC, 26, tr("Day after Christmas")),
        # Day before Decoration Day.
        1961: (MAY, 29, tr("Day before Decoration Day")),
        # Funeral of President John F. Kennedy.
        1963: (NOV, 25, tr("Funeral of President John F. Kennedy")),
        1965: (DEC, 24, name_christmas_eve),
        1968: (
            # Lincoln's Birthday.
            (FEB, 12, tr("Lincoln's Birthday")),
            # National Day of Mourning for Martin Luther King, Jr.
            (APR, 9, tr("National Day of Mourning for Martin Luther King, Jr.")),
            (JUL, 5, name_day_after_independence_day),
        ),
        1969: (
            # Heavy Snow.
            (FEB, 10, tr("Heavy Snow")),
            # Funeral of former President Dwight D. Eisenhower.
            (MAR, 31, tr("Funeral of former President Dwight D. Eisenhower")),
            # National Day of Participation for the Lunar Exploration.
            (JUL, 21, tr("National Day of Participation for the Lunar Exploration")),
        ),
        # Funeral of former President Harry S. Truman.
        1972: (DEC, 28, tr("Funeral of former President Harry S. Truman")),
        # Funeral of former President Lyndon B. Johnson.
        1973: (JAN, 25, tr("Funeral of former President Lyndon B. Johnson")),
        # Blackout in New York City.
        1977: (JUL, 14, tr("Blackout in New York City")),
        # Hurricane Gloria.
        1985: (SEP, 27, tr("Hurricane Gloria")),
        # Funeral of former President Richard M. Nixon.
        1994: (APR, 27, tr("Funeral of former President Richard M. Nixon")),
        2001: (
            (SEP, 11, name_closed_following_wtc_attacks),
            (SEP, 12, name_closed_following_wtc_attacks),
            (SEP, 13, name_closed_following_wtc_attacks),
            (SEP, 14, name_closed_following_wtc_attacks),
        ),
        # National Day of Mourning for former President Ronald Reagan.
        2004: (JUN, 11, tr("National Day of Mourning for former President Ronald Reagan")),
        # National Day of Mourning for former President Gerald R. Ford.
        2007: (JAN, 2, tr("National Day of Mourning for former President Gerald R. Ford")),
        2012: (
            (OCT, 29, name_hurricane_sandy),
            (OCT, 30, name_hurricane_sandy),
        ),
        # National Day of Mourning for former President George H. W. Bush.
        2018: (DEC, 5, tr("National Day of Mourning for former President George H. W. Bush")),
        # National Day of Mourning for former President Jimmy Carter.
        2025: (JAN, 9, tr("National Day of Mourning for former President Jimmy Carter")),
    }

    # Late opens and partial suspensions of work during the day are not implemented, such as:
    # * May 20, 1910 (Fri) - Closed from 10:00am to 12:00pm. Funeral of King Edward VII.
    # * Apr. 14, 1913 (Mon) - Closed from 10:00am to 12:00pm. Funeral of J. P. Morgan.
    # * Sept. 22, 1913 (Mon) - Closed from 10:00am to 12:00pm. Funeral of
    #   Mayor William J. Gaynor.
    # * July 11, 1918 (Thu) - Closed from 11:00am to 12:00pm. Funeral of former Mayor
    #   John Purroy Mitchell.
    # * Aug. 8, 1923 (Wed) - Closed from 11:00am to 12:30pm during funeral services for President
    #   Warren G. Harding in Washington, DC.
    # * Jan. 28, 1936 (Tue) - Closed from 10:00 to 11:00am. Funeral of King George V of England.
    # * May 18, 1942 (Mon) - Closed from 12:00pm to 1:00pm. NYSE 150th anniversary.
    # * June 19, 1945 (Tue) - Closed from 11:00am to 1:00pm. Parade for General Eisenhower.
    # * Apr. 20, 1951 (Fri) - Closed from 11:00am to 1:00pm. Parade for General MacArthur.

    special_half_day_holidays = {
        # Funeral of former President Grover Cleveland.
        1908: (JUN, 26, (close_1pm_label, tr("Funeral of former President Grover Cleveland"))),
        # Death of King Edward VII of England.
        1910: (MAY, 7, (close_11am_label, tr("Death of King Edward VII of England"))),
        1917: (
            # Parade of National Guard.
            (AUG, 29, (close_12pm_label, tr("Parade of National Guard"))),
            (OCT, 24, (close_12pm_label, name_liberty_day)),
        ),
        1918: (
            (APR, 26, (close_12pm_label, name_liberty_day)),
            # False armistice report.
            (NOV, 7, (close_2_30pm_label, tr("False armistice report"))),
        ),
        1919: (
            JAN,
            7,
            # Funeral of former President Theodore Roosevelt.
            (close_12_30pm_label, tr("Funeral of former President Theodore Roosevelt")),
        ),
        # Wall Street explosion.
        1920: (SEP, 16, (close_12pm_label, tr("Wall Street explosion"))),
        # Funeral of former President Woodrow Wilson.
        1924: (FEB, 6, (close_12_30pm_label, tr("Funeral of former President Woodrow Wilson"))),
        1925: (
            SEP,
            18,
            # Funeral of former NYSE president Seymour L. Cromwell.
            (close_2_30pm_label, tr("Funeral of former NYSE president Seymour L. Cromwell")),
        ),
        1928: (
            (MAY, 21, (close_2pm_label, name_heavy_volume_catch_up)),
            (MAY, 22, (close_2pm_label, name_heavy_volume_catch_up)),
            (MAY, 23, (close_2pm_label, name_heavy_volume_catch_up)),
            (MAY, 24, (close_2pm_label, name_heavy_volume_catch_up)),
            (MAY, 25, (close_2pm_label, name_heavy_volume_catch_up)),
        ),
        1929: (
            (NOV, 6, (close_1pm_label, name_catch_up_day)),
            (NOV, 7, (close_1pm_label, name_catch_up_day)),
            (NOV, 8, (close_1pm_label, name_catch_up_day)),
            (NOV, 11, (close_1pm_label, name_catch_up_day)),
            (NOV, 12, (close_1pm_label, name_catch_up_day)),
            (NOV, 13, (close_1pm_label, name_catch_up_day)),
            (NOV, 14, (close_1pm_label, name_catch_up_day)),
            (NOV, 15, (close_1pm_label, name_catch_up_day)),
            (NOV, 18, (close_1pm_label, name_catch_up_day)),
            (NOV, 19, (close_1pm_label, name_catch_up_day)),
            (NOV, 20, (close_1pm_label, name_catch_up_day)),
            (NOV, 21, (close_1pm_label, name_catch_up_day)),
            (NOV, 22, (close_1pm_label, name_catch_up_day)),
        ),
        1930: (
            MAR,
            11,
            # Funeral of former President William Howard Taft.
            (close_12_30pm_label, tr("Funeral of former President William Howard Taft")),
        ),
        # NRA demonstration.
        1933: (SEP, 13, (close_12pm_label, tr("NRA demonstration"))),
        1951: (DEC, 24, (close_1pm_label, name_christmas_eve)),
        1963: (
            NOV,
            22,
            # Assassination of President John F. Kennedy (markets close at 2:07pm).
            tr("Assassination of President John F. Kennedy (markets close at 2:07pm)"),
        ),
        # Funeral of former President Herbert C. Hoover.
        1964: (OCT, 23, (close_2pm_label, tr("Funeral of former President Herbert C. Hoover"))),
        1966: (
            (JAN, 6, (close_2pm_label, name_transit_strike)),
            (JAN, 7, (close_2pm_label, name_transit_strike)),
            (JAN, 10, (close_2pm_label, name_transit_strike)),
            (JAN, 11, (close_2pm_label, name_transit_strike)),
            (JAN, 12, (close_2pm_label, name_transit_strike)),
            (JAN, 13, (close_2pm_label, name_transit_strike)),
            (JAN, 14, (close_2pm_label, name_transit_strike)),
        ),
        1967: (
            (AUG, 8, (close_2pm_label, name_back_office_work_load)),
            (AUG, 9, (close_2pm_label, name_back_office_work_load)),
            (AUG, 10, (close_2pm_label, name_back_office_work_load)),
            (AUG, 11, (close_2pm_label, name_back_office_work_load)),
            (AUG, 14, (close_2pm_label, name_back_office_work_load)),
            (AUG, 15, (close_2pm_label, name_back_office_work_load)),
            (AUG, 16, (close_2pm_label, name_back_office_work_load)),
            (AUG, 17, (close_2pm_label, name_back_office_work_load)),
            (AUG, 18, (close_2pm_label, name_back_office_work_load)),
        ),
        1974: (DEC, 24, (close_2pm_label, name_christmas_eve)),
        1975: (
            (FEB, 12, (close_2_30pm_label, name_snowstorm)),
            (DEC, 24, (close_2pm_label, name_christmas_eve)),
        ),
        # Hurricane watch.
        1976: (AUG, 9, (close_3pm_label, tr("Hurricane watch"))),
        1978: (FEB, 6, (close_2pm_label, name_snowstorm)),
        1981: (
            # Assassination attempt on President Reagan (markets close at 3:17pm).
            (MAR, 30, tr("Assassination attempt on President Reagan (markets close at 3:17pm)")),
            # Con Edison power failure in lower Manhattan (markets close at 3:28pm).
            (SEP, 9, tr("Con Edison power failure in lower Manhattan (markets close at 3:28pm)")),
        ),
        1987: (
            (OCT, 23, (close_2pm_label, name_shortened_hours_following_market_break)),
            (OCT, 26, (close_2pm_label, name_shortened_hours_following_market_break)),
            (OCT, 27, (close_2pm_label, name_shortened_hours_following_market_break)),
            (OCT, 28, (close_2pm_label, name_shortened_hours_following_market_break)),
            (OCT, 29, (close_2pm_label, name_shortened_hours_following_market_break)),
            (OCT, 30, (close_2pm_label, name_shortened_hours_following_market_break)),
            (NOV, 2, (close_2_30pm_label, name_shortened_hours_following_market_break)),
            (NOV, 3, (close_2_30pm_label, name_shortened_hours_following_market_break)),
            (NOV, 4, (close_2_30pm_label, name_shortened_hours_following_market_break)),
            (NOV, 5, (close_3pm_label, name_shortened_hours_following_market_break)),
            (NOV, 6, (close_3pm_label, name_shortened_hours_following_market_break)),
            (NOV, 9, (close_3_30pm_label, name_shortened_hours_following_market_break)),
            (NOV, 10, (close_3_30pm_label, name_shortened_hours_following_market_break)),
            (NOV, 11, (close_3_30pm_label, name_shortened_hours_following_market_break)),
        ),
        1990: (DEC, 24, (close_2pm_label, name_christmas_eve)),
        1991: (DEC, 24, (close_2pm_label, name_christmas_eve)),
        1992: (
            # Day after Thanksgiving Day.
            (NOV, 27, (close_2pm_label, tr("Day after Thanksgiving Day"))),
            (DEC, 24, (close_2pm_label, name_christmas_eve)),
        ),
        1994: (FEB, 11, (close_2_30pm_label, name_snowstorm)),
        1996: (JUL, 5, (close_1pm_label, name_day_after_independence_day)),
        1997: (DEC, 26, (close_1pm_label, name_friday_after_christmas)),
        # New Year's Eve.
        1999: (DEC, 31, (close_1pm_label, tr("New Year's Eve"))),
        2002: (JUL, 5, (close_1pm_label, name_day_after_independence_day)),
        2003: (DEC, 26, (close_1pm_label, name_friday_after_christmas)),
        # Day before Independence Day.
        2013: (JUL, 3, (close_1pm_label, tr("Day before Independence Day"))),
    }
