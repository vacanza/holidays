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

from holidays.calendars.gregorian import FEB, APR, MAY, JUN, SUN, _timedelta
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
    SAT_SUN_TO_PREV_FRI,
)


class Anguilla(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Anguilla holidays.

    References:
        - [Public Holidays For 2011](https://web.archive.org/web/20110531155208/https://www.gov.ai/holiday.php)
        - [Public Holidays For 2012](https://web.archive.org/web/20120316123834/http://www.gov.ai/holiday.php)
        - [Public Holidays For 2013](https://web.archive.org/web/20131113151001/http://www.gov.ai/holiday.php)
        - [Public Holidays For 2014](https://web.archive.org/web/20141113163349/http://www.gov.ai/holiday.php)
        - [Public Holidays For 2015](https://web.archive.org/web/20151113150558/http://www.gov.ai/holiday.php)
        - [Public Holidays For 2016](https://web.archive.org/web/20161021015139/http://www.gov.ai/holiday.php)
        - [Public Holidays For 2017](https://web.archive.org/web/20170830143632/http://www.gov.ai/holiday.php)
        - [Public Holidays For 2018](https://web.archive.org/web/20181127040220/http://www.gov.ai/holiday.php)
        - [Public Holidays For 2019](https://web.archive.org/web/20191021020537/http://www.gov.ai/holiday.php)
        - [Public Holidays For 2020](https://web.archive.org/web/20210205021056/http://www.gov.ai/holiday.php)
        - [Public Holidays For 2021](https://web.archive.org/web/20210901183726/http://www.gov.ai/holiday.php)
        - [Public Holidays For 2022](https://web.archive.org/web/20221011200016/http://www.gov.ai/holiday.php)
        - [Public Holidays For 2024](https://web.archive.org/web/20241004074741/https://www.gov.ai/service/public-holidays-for-2024)
        - [Public Holidays For 2025](https://web.archive.org/web/20250425025259/https://www.gov.ai/service/public-holidays-for-2025)
        - [PUBLIC HOLIDAYS ACT R.S.A. c. P130](https://www.gov.ai/laws/P130-00-Public%20Holidays%20Act/docs/P130-00-Public%20Holidays%20Act_03.pdf)
        - [Revised Regulations of Anguilla: P130-1](https://www.gov.ai/laws/P130-01-Public%20Holidays%20Regulations/docs/P130-01-Public%20Holidays%20Regulations_05.pdf)
        - [Government of Anguilla Official Gazette](https://web.archive.org/web/20250304213202/https://gov.ai/document/2025-03-04-123357_2051160063.pdf)
        - [REVISED REGULATIONS OF ANGUILLA](https://natlex.ilo.org/dyn/natlex2/natlex2/files/download/109059/ATG109059.pdf)
    """

    country = "AI"
    default_language = "en_AI"
    supported_languages = ("en_AI", "en_US")
    # %s (observed).
    observed_label = tr("%s (observed)")
    # Declaration of independence May 30, 1967,
    # but the 2010 revision is the most recent comprehensive legal update.
    start_year = 2011
    weekend = {SUN}

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=AnguillaStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        # James Ronald Webster Day.
        self._add_observed(self._add_holiday_mar_2(tr("James Ronald Webster Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Easter Sunday"))

        # Labor Day.
        self._add_observed(self._add_labor_day(tr("Labor Day")))

        # Whit Monday.
        whit_monday = self._add_whit_monday(tr("Whit Monday"))

        name = (
            # Celebration of the Birthday of Her Majesty the Queen.
            tr("Celebration of the Birthday of Her Majesty the Queen")
            if self._year <= 2022
            # Celebration of the Birthday of His Majesty the King.
            else tr("Celebration of the Birthday of His Majesty the King")
        )
        if self._year == 2022:
            self._add_holiday_jun_3(name)
        elif self._year <= 2021:
            self._add_holiday_2nd_mon_of_jun(name)
        else:
            self._add_holiday_3rd_mon_of_jun(name)

        dt = date(self._year, MAY, 30)
        if self._is_weekend(dt):
            dt = _timedelta(dt, +2) if self._is_saturday(dt) else _timedelta(dt, +1)
        if whit_monday == dt:
            dt = _timedelta(dt, +1)
        # Anguilla Day.
        self._add_holiday(tr("Anguilla Day"), dt)

        # August Monday.
        self._add_holiday_1st_mon_of_aug(tr("August Monday"))

        # August Thursday.
        self._add_holiday_3_days_past_1st_mon_of_aug(tr("August Thursday"))

        # Constitution Day.
        self._add_holiday_4_days_past_1st_mon_of_aug(tr("Constitution Day"))

        self._add_observed(
            self._add_holiday_dec_19(
                # National Heroes and Heroines Day.
                tr("National Heroes and Heroines Day")
            ),
            rule=SAT_SUN_TO_PREV_FRI,
        )

        self._add_observed(
            # Christmas Day.
            self._add_christmas_day(tr("Christmas Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE,
        )

        self._add_observed(
            # Boxing Day.
            self._add_christmas_day_two(tr("Boxing Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE,
        )


class AI(Anguilla):
    pass


class AIA(Anguilla):
    pass


class AnguillaStaticHolidays:
    special_public_holidays = {
        # Royal Wedding of Prince William & Kate Middleton.
        2011: (APR, 29, tr("Royal Wedding of Prince William & Kate Middleton")),
        # Diamond Jubilee Celebration of Her Majesty The Queen.
        2012: (JUN, 4, tr("Diamond Jubilee Celebration of Her Majesty The Queen")),
        # Special Public Holiday.
        2025: (FEB, 28, tr("Special Public Holiday")),
    }
