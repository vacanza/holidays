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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class Nauru(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Nauru holidays.

    References:
        * <https://www.worldatlas.com/articles/what-languages-are-spoken-in-nauru.html>
        * <https://publicholidays.asia/nauru/>
        * <https://commonwealthchamber.com/day-of-the-tribes-nauru/>
        * <https://anydayguide.com/calendar/2514>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Nauru>
        * <https://www.timeanddate.com/holidays/nauru/>
        * [Public Service Act 2016](https://ronlaw.gov.nr/pdfviewer/docs%252Facts%252F2016%252FPublic%2520Service%2520Act%25202016_serv4.pdf)
        * [Nauru's Online Legal Database](https://ronlaw.gov.nr/)

    Gazettes:
        * [15th Jan 2024](https://ronlaw.gov.nr/pdfviewer/docs%252Fgazettes%252F2024%252F01%252FNauru%2520Government%2520Gazette%252C%2520No.%252014%2520%2815%2520January%25202024%29.pdf)
        * [International Womens Day was started on 2019](https://ronlaw.gov.nr/pdfviewer/docs%2Fgazettes%2F2018%2F11%2FGazette%20No.%20175%20%2828%20November%202018%29.pdf)
        * [RONPHOS Handover Day was started on 2018](https://ronlaw.gov.nr/pdfviewer/docs%2Fgazettes%2F2018%2F06%2FGazette%20No.%20102%20%2829%20June%202018%29.pdf)
        * [Ibumin Earoeni Day was started on 2019](https://ronlaw.gov.nr/pdfviewer/docs%2Fgazettes%2F2019%2F08%2FGazette%20No.%20139%20%2812%20August%202019%29.pdf)
        * [Sir Hammer DeRoburt Day was started on 2021](https://ronlaw.gov.nr/pdfviewer/docs%2Fgazettes%2F2021%2F09%2FGazette%20No.%20144%20%2821%20September%202021%29.pdf)
    """

    country = "NR"
    default_language = "en_NR"
    # %s (observed).
    observed_label = tr("%s (observed)")
    supported_languages = ("en_AU",)
    # Nauru gained independence on January 31, 1968
    start_year = 1969

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        self._add_observed(
            # Independence Day.
            self._add_holiday_jan_31(tr("Independence Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE,
        )

        self._add_observed(
            # Day following Independence Day.
            self._add_holiday_feb_1(tr("Day following Independence Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE,
        )

        if self._year >= 2019:
            # International Women's Day.
            self._add_observed(self._add_womens_day(tr("International Women's Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Easter Tuesday.
        self._add_easter_tuesday(tr("Easter Tuesday"))

        # Constitution Day.
        self._add_observed(self._add_holiday_may_17(tr("Constitution Day")))

        if self._year >= 2018:
            # RONPHOS Handover.
            self._add_observed(self._add_holiday_jul_1(tr("RONPHOS Handover")))

        if self._year >= 2019:
            # Ibumin Earoeni Day.
            self._add_observed(self._add_holiday_aug_19(tr("Ibumin Earoeni Day")))

        if self._year >= 2021:
            # Sir Hammer DeRoburt Day.
            self._add_observed(self._add_holiday_sep_25(tr("Sir Hammer DeRoburt Day")))

        # Angam Day.
        self._add_observed(self._add_holiday_oct_26(tr("Angam Day")))

        self._add_observed(
            # Christmas Day.
            self._add_christmas_day(tr("Christmas Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE,
        )

        self._add_observed(
            # Day following Christmas.
            self._add_christmas_day_two(tr("Day following Christmas")),
            rule=SAT_SUN_TO_NEXT_MON_TUE,
        )


class NR(Nauru):
    pass


class NRU(Nauru):
    pass
