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

from holidays.calendars.gregorian import FEB, APR, JUN, MAY, _timedelta
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_PREV_FRI,
    SAT_TO_NEXT_MON,
    SUN_TO_NEXT_MON,
    SUN_TO_NEXT_TUE,
)


class Anguilla(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Anguilla holidays.

    References:
        - [Public Holidays For 2011](https://web.archive.org/web/20110531155208/https://gov.ai/holiday.php)
        - [Public Holidays For 2012](https://web.archive.org/web/20120316123834/http://www.gov.ai/holiday.php)
        - [Public Holidays For 2019](https://web.archive.org/web/20190129001329/http://www.gov.ai:80/holiday.php)
        - [PUBLIC HOLIDAYS ACT R.S.A. c. P130](https://www.gov.ai/laws/P130-00-Public%20Holidays%20Act/docs/P130-00-Public%20Holidays%20Act_03.pdf)
        - [Revised Regulations of Anguilla: P130-1](https://www.gov.ai/laws/P130-01-Public%20Holidays%20Regulations/docs/P130-01-Public%20Holidays%20Regulations_05.pdf)
        - [Government of Anguilla Official Gazette](https://gov.ai/document/2025-03-04-123357_2051160063.pdf)
        - [REVISED REGULATIONS OF ANGUILLA](https://natlex.ilo.org/dyn/natlex2/natlex2/files/download/109059/ATG109059.pdf)
    """

    country = "AI"
    default_language = "en_US"
    supported_languages = ("en_US",)
    # %s (observed).
    observed_label = tr("%s (observed)")
    # Declaration of independence May 30, 1967,
    # but the 2010 revision is the most recent comprehensive legal update.
    start_year = 2010

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=AnguillaStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")), rule=SAT_SUN_TO_NEXT_MON)

        # James Ronald Webster Day.
        self._add_observed(
            self._add_holiday_mar_2(tr("James Ronald Webster Day")),
            rule=SAT_SUN_TO_NEXT_MON,
        )

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Easter Sunday"))

        # Labour Day.
        self._add_observed(self._add_labor_day(tr("Labour Day")), rule=SAT_SUN_TO_NEXT_MON)

        # Whit Monday.
        whit_monday = self._add_whit_monday(tr("Whit Monday"))

        # Celebration of the Birthday of Her Majesty the Queen.
        self._add_holiday_2nd_mon_of_jun(
            tr("Celebration of the Birthday of Her Majesty the Queen")
        )

        dt = date(self._year, MAY, 30)
        if self._is_weekend(dt):
            dt = _timedelta(dt, +2) if self._is_saturday(dt) else _timedelta(dt, +1)
        if whit_monday == dt:
            dt = _timedelta(dt, +1)
        # Anguilla Day.
        self._add_holiday(tr("Anguilla Day"), dt)

        # Sovereignty Day.
        self._add_holiday_mar_2(tr("Sovereignty Day"))

        # August Monday.
        self._add_observed(
            self._add_holiday_1st_mon_of_aug(tr("August Monday")), rule=SAT_SUN_TO_PREV_FRI
        )

        # August Thursday.
        self._add_observed(
            self._add_holiday_3_days_past_1st_mon_of_aug(tr("August Thursday")),
            rule=SAT_SUN_TO_PREV_FRI,
        )

        # Constitution Day.
        self._add_observed(
            self._add_holiday_4_days_past_1st_mon_of_aug(tr("Constitution Day")),
            rule=SAT_SUN_TO_PREV_FRI,
        )

        self._add_observed(
            self._add_holiday_dec_19(
                # National Heroes and Heroines Day.
                tr("National Heroes and Heroines Day")
                if self._year >= 2011
                # Separation Day.
                else tr("Separation Day")
            ),
            rule=SAT_SUN_TO_PREV_FRI,
        )

        # Christmas Day.
        self._add_christmas_day(tr("Christmas Day"))

        christmas_date = self._christmas_day
        boxing_date = _timedelta(christmas_date, +1)

        if self._is_sunday(christmas_date):
            # Boxing Day.
            self._add_observed(self._add_christmas_day_two(tr("Boxing Day")), rule=SUN_TO_NEXT_MON)
            # Boxing Day.
            self._add_observed(self._add_christmas_day_two(tr("Boxing Day")), rule=SUN_TO_NEXT_TUE)
        elif self._is_saturday(christmas_date):
            # Boxing Day.
            self._add_observed(self._add_christmas_day_two(tr("Boxing Day")), rule=SAT_TO_NEXT_MON)
        elif self._is_saturday(boxing_date):
            # Boxing Day.
            self._add_observed(self._add_christmas_day_two(tr("Boxing Day")), rule=SAT_TO_NEXT_MON)
        else:
            # Boxing Day.
            self._add_christmas_day_two(tr("Boxing Day"))


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
        # Special Public Holiday Day.
        2025: (FEB, 28, tr("Special Public Holiday Day")),
    }
