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

from holidays.calendars.gregorian import JAN, APR, JUN, JUL, SEP, OCT, NOV, DEC
from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.helpers import tr
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_TO_PREV_FRI,
    SUN_TO_NEXT_MON,
)


class SecuritiesIndustryAndFinancialMarketsAssociation(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """Securities Industry and Financial Markets Association (SIFMA) holidays.

    SIFMA recommends full and early closes for trading of U.S. dollar-denominated fixed income
    securities (the U.S. bond market). Before November 2006 the recommendations were issued
    by The Bond Market Association.

    References:
        * [SIFMA Holiday Recommendations 1996-2019](https://web.archive.org/web/20260116172921/https://www.sifma.org/wp-content/uploads/2017/08/Misc-US-Historical-Holiday-Market-Recommendations-SIFMA.pdf)
        * [U.S. Holiday Archive](https://web.archive.org/web/20261013030156/https://www.sifma.org/resources/guides-playbooks/us-holiday-archive)
        * [Holiday Schedule](https://web.archive.org/web/20261012114604/https://www.sifma.org/resources/general/holiday-schedule)
        * [Good Friday 2015](https://web.archive.org/web/20261018073918/https://www.sifma.org/news/press-releases/sifma-recommends-early-market-close-on-april-3-for-trading-of-us-dollar-denominated-fixed-income-securities-in-the-us-in-observance-of-the-good-friday-holiday)
        * [Market closure 2001](https://web.archive.org/web/20260529072848/https://home.treasury.gov/news/press-releases/po627)
        * [National Day of Mourning 2004](https://web.archive.org/web/20230607061001/https://www.isda.org/2004/06/11/u-s-exchange-and-market-closings-on-june-11-2004-for-mourning-president-ronald-reagan/)
        * [National Day of Mourning 2007](https://web.archive.org/web/20260516183523/https://www.sec.gov/news/press/2006/2006-222.htm)
        * [National Day of Mourning 2025](https://web.archive.org/web/20260217172921/https://www.sifma.org/news/press-releases/sifma-recommends-early-market-close-on-january-9-2025-for-the-national-day-of-mourning-in-honor-of-former-president-carter)
    """

    market = "XSIF"
    default_language = "en_US"
    # %s (observed).
    observed_label = tr("%s (observed)")
    supported_categories = (HALF_DAY, PUBLIC)
    supported_languages = ("en_US",)
    start_year = 1996
    # Years with an early close instead of a full close on Good Friday, usually because the
    # BLS employment report is released that day.
    good_friday_early_close_years = {1999, 2007, 2010, 2012, 2015, 2021, 2023, 2026}

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(
            self, SecuritiesIndustryAndFinancialMarketsAssociationStaticHolidays
        )
        kwargs.setdefault("observed_rule", SAT_TO_PREV_FRI + SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _add_day_before(self, name: str, dt: date) -> None:
        """Add an early close on the last business day before the observed `dt`."""
        observed_dt = self._get_observed_date(dt, self._observed_rule) or dt
        self._add_holiday(name, self._get_next_workday(observed_dt, -1))

    def _populate_public_holidays(self):
        # New Year's Day.
        self._move_holiday(self._add_new_years_day(tr("New Year's Day")), rule=SUN_TO_NEXT_MON)

        # Martin Luther King Jr. Day.
        self._add_holiday_3rd_mon_of_jan(tr("Martin Luther King Jr. Day"))

        # Washington's Birthday.
        self._add_holiday_3rd_mon_of_feb(tr("Washington's Birthday"))

        if self._year not in self.good_friday_early_close_years:
            # Good Friday.
            self._add_good_friday(tr("Good Friday"))

        # Memorial Day.
        self._add_holiday_last_mon_of_may(tr("Memorial Day"))

        if self._year >= 2022:
            self._move_holiday(
                # Juneteenth National Independence Day.
                self._add_holiday_jun_19(tr("Juneteenth National Independence Day"))
            )

        # Independence Day.
        self._move_holiday(self._add_holiday_jul_4(tr("Independence Day")))

        # Labor Day.
        self._add_holiday_1st_mon_of_sep(tr("Labor Day"))

        # Columbus Day.
        self._add_holiday_2nd_mon_of_oct(tr("Columbus Day"))

        # Veterans Day.
        self._move_holiday(self._add_remembrance_day(tr("Veterans Day")), rule=SUN_TO_NEXT_MON)

        # Thanksgiving Day.
        self._add_holiday_4th_thu_of_nov(tr("Thanksgiving Day"))

        # Christmas Day.
        self._move_holiday(self._add_christmas_day(tr("Christmas Day")))

    def _populate_half_day_holidays(self):
        # %s (markets close at 2:00pm).
        close_2pm_label = tr("%s (markets close at 2:00pm)")

        if self._year <= 2009:
            self._add_holiday_3_days_prior_3rd_mon_of_jan(
                self._format_holiday_name(
                    close_2pm_label,
                    # Day before Martin Luther King Jr. Day.
                    tr("Day before Martin Luther King Jr. Day"),
                )
            )

            self._add_holiday_3_days_prior_3rd_mon_of_feb(
                # Day before Washington's Birthday.
                self._format_holiday_name(close_2pm_label, tr("Day before Washington's Birthday"))
            )

        if self._year >= 1997 and (
            self._year == 1999 or self._year not in self.good_friday_early_close_years
        ):
            self._add_holy_thursday(
                # Day before Good Friday.
                self._format_holiday_name(close_2pm_label, tr("Day before Good Friday"))
            )

        self._add_holiday_3_days_prior_last_mon_of_may(
            # Day before Memorial Day.
            self._format_holiday_name(close_2pm_label, tr("Day before Memorial Day"))
        )

        if self._year <= 2008 or self._year >= 2014:
            self._add_day_before(
                # Day before Independence Day.
                self._format_holiday_name(close_2pm_label, tr("Day before Independence Day")),
                date(self._year, JUL, 4),
            )

        if self._year <= 2008:
            self._add_holiday_3_days_prior_1st_mon_of_sep(
                # Day before Labor Day.
                self._format_holiday_name(close_2pm_label, tr("Day before Labor Day"))
            )

            self._add_holiday_3_days_prior_2nd_mon_of_oct(
                # Day before Columbus Day.
                self._format_holiday_name(close_2pm_label, tr("Day before Columbus Day"))
            )

            if self._year in {1996, 2001, 2002, 2003, 2005, 2007, 2008}:
                self._add_day_before(
                    # Day before Veterans Day.
                    self._format_holiday_name(close_2pm_label, tr("Day before Veterans Day")),
                    date(self._year, NOV, 11),
                )

            self._add_holiday_1_day_prior_4th_thu_of_nov(
                # Day before Thanksgiving Day.
                self._format_holiday_name(close_2pm_label, tr("Day before Thanksgiving Day"))
            )

        self._add_holiday_1_day_past_4th_thu_of_nov(
            # Day after Thanksgiving Day.
            self._format_holiday_name(close_2pm_label, tr("Day after Thanksgiving Day"))
        )

        self._add_day_before(
            # Day before Christmas Day.
            self._format_holiday_name(close_2pm_label, tr("Day before Christmas Day")),
            date(self._year, DEC, 25),
        )

        if self._year not in {1999, 2010}:
            dec_31 = date(self._year, DEC, 31)
            self._add_holiday(
                # Day before New Year's Day.
                self._format_holiday_name(close_2pm_label, tr("Day before New Year's Day")),
                self._get_next_workday(dec_31, -1) if self._is_weekend(dec_31) else dec_31,
            )


class XSIF(SecuritiesIndustryAndFinancialMarketsAssociation):
    pass


class USGS(SecuritiesIndustryAndFinancialMarketsAssociation):
    pass


class SecuritiesIndustryAndFinancialMarketsAssociationStaticHolidays:
    """Securities Industry and Financial Markets Association (SIFMA) special holidays."""

    # %s (markets close at 11:00am).
    close_11am_label = tr("%s (markets close at 11:00am)")

    # %s (markets close at 12:00pm).
    close_12pm_label = tr("%s (markets close at 12:00pm)")

    # %s (markets close at 1:00pm).
    close_1pm_label = tr("%s (markets close at 1:00pm)")

    # %s (markets close at 2:00pm).
    close_2pm_label = tr("%s (markets close at 2:00pm)")

    # Good Friday.
    name_good_friday = tr("Good Friday")

    # Hurricane Sandy.
    name_hurricane_sandy = tr("Hurricane Sandy")

    special_public_holidays = {
        # Closed following Attacks on the World Trade Center.
        2001: (SEP, 12, tr("Closed following Attacks on the World Trade Center")),
        # National Day of Mourning for former President Ronald Reagan.
        2004: (JUN, 11, tr("National Day of Mourning for former President Ronald Reagan")),
        2012: (OCT, 30, name_hurricane_sandy),
        # National Day of Mourning for former President George H. W. Bush.
        2018: (DEC, 5, tr("National Day of Mourning for former President George H. W. Bush")),
    }

    special_half_day_holidays = {
        # Day after Independence Day.
        1996: (JUL, 5, (close_2pm_label, tr("Day after Independence Day"))),
        # Day after Christmas Day.
        1997: (DEC, 26, (close_2pm_label, tr("Day after Christmas Day"))),
        1999: (
            (APR, 2, (close_12pm_label, name_good_friday)),
            # Day before New Year's Day.
            (DEC, 31, (close_1pm_label, tr("Day before New Year's Day"))),
        ),
        # Day after New Year's Day.
        2004: (JAN, 2, (close_2pm_label, tr("Day after New Year's Day"))),
        2007: (
            (
                JAN,
                2,
                (
                    close_2pm_label,
                    # National Day of Mourning for former President Gerald R. Ford.
                    tr("National Day of Mourning for former President Gerald R. Ford"),
                ),
            ),
            (APR, 6, (close_11am_label, name_good_friday)),
        ),
        2010: (APR, 2, (close_12pm_label, name_good_friday)),
        2012: (
            (APR, 6, (close_12pm_label, name_good_friday)),
            (OCT, 29, (close_12pm_label, name_hurricane_sandy)),
        ),
        2015: (APR, 3, (close_12pm_label, name_good_friday)),
        2021: (APR, 2, (close_12pm_label, name_good_friday)),
        2023: (APR, 7, (close_12pm_label, name_good_friday)),
        2025: (
            JAN,
            9,
            # National Day of Mourning for former President Jimmy Carter.
            (close_2pm_label, tr("National Day of Mourning for former President Jimmy Carter")),
        ),
        2026: (APR, 3, (close_12pm_label, name_good_friday)),
    }
