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

from gettext import gettext as tr

from holidays.calendars.gregorian import JAN, JUN, JUL, SEP, OCT, DEC
from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_TO_PREV_FRI, SUN_TO_NEXT_MON


class ChicagoMercantileExchange(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """Chicago Mercantile Exchange (CME) holidays.

    Prior to 2015, minor holidays halted at 10:30 AM CT.
    From 2015 onward, CME standardized these to 12:00 PM CT.
        * [Martin Luther King Holiday Schedule 2009](https://web.archive.org/web/20090126144353/http://cmegroup.com/tools-information/holiday-calendar/files/2009-martin-luther-king.pdf)
        * [Martin Luther King Holiday Schedule 2015](https://web.archive.org/web/20150905223758/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-martin-luther-king-holiday-schedule.pdf)

    References:
        * [2009](https://web.archive.org/web/20090122062834/http://www.cmegroup.com/tools-information/holiday-calendar/)
        * [2010](https://web.archive.org/web/20100315131807/http://www.cmegroup.com/tools-information/holiday-calendar/)
        * [2011](https://web.archive.org/web/20110728164055/http://www.cmegroup.com/tools-information/holiday-calendar/)
        * [2012](https://web.archive.org/web/20120912192947/http://www.cmegroup.com/tools-information/holiday-calendar/)
        * [2013](https://web.archive.org/web/20130927113936/http://www.cmegroup.com/tools-information/holiday-calendar/)
        * [2014](https://web.archive.org/web/20141130223720/http://www.cmegroup.com/tools-information/holiday-calendar/)
        * [2015](https://web.archive.org/web/20151026083555/http://www.cmegroup.com/tools-information/holiday-calendar/)
        * [2016](https://web.archive.org/web/20151215022239/http://www.cmegroup.com/tools-information/holiday-calendar/)
        * [2017](https://web.archive.org/web/20170104172130/http://www.cmegroup.com/tools-information/holiday-calendar.html)
        * [2018](https://web.archive.org/web/20180815103620/https://www.cmegroup.com/tools-information/holiday-calendar.html)
        * [2019](https://web.archive.org/web/20190122145657/http://www.cmegroup.com/tools-information/holiday-calendar.html)
        * [2020](https://web.archive.org/web/20201230225003/http://www.cmegroup.com/tools-information/holiday-calendar.html)
        * [2021](https://web.archive.org/web/20211203222922/http://www.cmegroup.com/tools-information/holiday-calendar.html)
        * [2022](https://web.archive.org/web/20221123183200/https://www.cmegroup.com/tools-information/holiday-calendar.html)
        * [2023](https://web.archive.org/web/20231203104831/https://www.cmegroup.com/tools-information/holiday-calendar.html)
        * [2024](https://web.archive.org/web/20240703233842/https://www.cmegroup.com/trading-hours.html)
        * [2025](https://web.archive.org/web/20250327221007/https://www.cmegroup.com/trading-hours.html)
        * [2026](https://web.archive.org/web/20260522122235/https://www.cmegroup.com/trading-hours.html)
    """

    market = "XCME"
    default_language = "en_US"
    supported_languages = ("en_US", "gu", "hi")
    start_year = 2000
    supported_categories = (HALF_DAY, PUBLIC)

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, ChicagoMercantileExchangeStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_TO_PREV_FRI + SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._move_holiday(self._add_new_years_day(tr("New Year's Day")), rule=SUN_TO_NEXT_MON)

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Independence Day.
        self._move_holiday(self._add_holiday_jul_4(tr("Independence Day")), rule=SUN_TO_NEXT_MON)

        # Thanksgiving Day.
        self._add_holiday_4th_thu_of_nov(tr("Thanksgiving Day"))

        # Christmas Day.
        self._move_holiday(self._add_christmas_day(tr("Christmas Day")))

    def _populate_half_day_holidays(self):
        # %s (markets pause at 10:30am CT)
        pause_1030am_label = tr("%s (markets pause at 10:30am CT)")
        # %s (markets pause at 12:00pm CT)
        pause_1200pm_label = tr("%s (markets pause at 12:00pm CT)")
        minor_pause_label = pause_1200pm_label if self._year >= 2015 else pause_1030am_label

        self._add_holiday_3rd_mon_of_jan(
            # Dr. Martin Luther King, Jr. Day.
            self._format_holiday_name(minor_pause_label, tr("Dr. Martin Luther King, Jr. Day"))
        )

        self._add_holiday_3rd_mon_of_feb(
            # President's Day.
            self._format_holiday_name(minor_pause_label, tr("President's Day"))
        )

        self._add_holiday_last_mon_of_may(
            # Memorial Day.
            self._format_holiday_name(minor_pause_label, tr("Memorial Day"))
        )

        if self._year >= 2022:
            self._move_holiday(
                self._add_holiday_jun_19(
                    # Juneteenth Day.
                    self._format_holiday_name(pause_1200pm_label, tr("Juneteenth Day"))
                )
            )

        jul_4 = (JUL, 4)
        if self._is_saturday(jul_4):
            self._add_holiday_jul_3(
                # Independence Day.
                self._format_holiday_name(minor_pause_label, tr("Independence Day"))
            )
        elif self._is_weekday(jul_4) and not self._is_monday(jul_4):
            self._add_holiday_jul_3(
                # Day before Independence Day.
                self._format_holiday_name(minor_pause_label, tr("Day before Independence Day"))
            )

        self._add_holiday_1st_mon_of_sep(
            # Labor Day.
            self._format_holiday_name(minor_pause_label, tr("Labor Day"))
        )

        self._add_holiday_1_day_past_4th_thu_of_nov(
            # Day after Thanksgiving Day.
            self._format_holiday_name(pause_1200pm_label, tr("Day after Thanksgiving Day"))
        )

        if self._is_weekday(self._christmas_day) and not self._is_monday(self._christmas_day):
            self._add_christmas_eve(
                # Christmas Eve.
                self._format_holiday_name(pause_1200pm_label, tr("Christmas Eve"))
            )


class XCME(ChicagoMercantileExchange):
    pass


class CME(ChicagoMercantileExchange):
    pass


class ChicagoMercantileExchangeStaticHolidays:
    """Chicago Mercantile Exchange (CME) special holidays.

    References:
        * [Attacks on the World Trade Center](https://web.archive.org/web/20260610102432/https://www.chicagotribune.com/2001/09/11/markets-halt-after-world-trade-center-hit/)
        * [National Day of Mourning for President Ronald Reagan](https://web.archive.org/web/20260610093402/https://investor.cmegroup.com/news-releases/news-release-details/chicago-mercantile-exchange-close-friday-june-11-honor-national)
        * [National Day of Mourning for President Gerald R. Ford](https://web.archive.org/web/20260610093503/https://investor.cmegroup.com/news-releases/news-release-details/cme-announces-market-hours-operation-honor-national-day-mourning)
        * [Hurricane Sandy](https://web.archive.org/web/20260610093358/https://www.cmegroup.com/tools-information/lookups/advisories/clearing/files/Chadv12-464.pdf)
        * [National Day of Mourning for former President George H. W. Bush](https://web.archive.org/web/20250824115358/https://www.prnewswire.com/news-releases/cme-group-us-equity-interest-rate-markets-to-close-for-national-day-of-mourning-300758702.html)
        * [National Day of Mourning to Honor Former President Jimmy Carter](https://web.archive.org/web/20250715124404/https://www.cmegroup.com/media-room/press-releases/2025/12/30/cme_group_announcestradinghoursforusnationaldayofmourningtohonor.html)
    """

    # Closed following Attacks on the World Trade Center.
    name_closed_following_wtc_attacks = tr("Closed following Attacks on the World Trade Center")

    # Hurricane Sandy.
    name_hurricane_sandy = tr("Hurricane Sandy")

    special_public_holidays = {
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
