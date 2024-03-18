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

from gettext import gettext as tr

from holidays.calendars.gregorian import JAN, MAR, MAY, SEP, OCT, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class Seychelles(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://www.psb.gov.sc/public-holidays
    https://www.cbs.sc/PublicHolidays.html

    [Act 19 of 1976, 1994 Amendment]
        Oldest Seychelles Holidays Law available online in full.
        https://seylii.org/akn/sc/act/1976/19/eng@2012-06-30
    [Act 11 of 2014]
        Holidays names changed.
        https://seylii.org/akn/sc/act/2014/11/eng@2014-08-04
    [Act 3 of 2017]
        Added Easter Monday, repealing Liberation Day.
        https://seylii.org/akn/sc/act/2017/3/eng@2017-04-12

    Where any public holiday, except Sunday, falls on a Sunday the next following day,
    not being itself a public holiday, shall be a public holiday.
    """

    country = "SC"
    default_language = "en_SC"
    # %s (observed).
    observed_label = tr("%s (observed)")
    supported_languages = ("en_SC", "en_US")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, SeychellesStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Earliest source is the 1994 amendment of Seychelles Public Holidays Act.
        if self._year <= 1993:
            return None

        # New Year's Day.
        self._add_new_years_day(tr("New Year's Day"))

        # New Year Holiday.
        self._add_observed(self._add_new_years_day_two(tr("New Year Holiday")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Saturday.
        self._add_holy_saturday(tr("Easter Saturday"))

        if self._year >= 2017:
            # Easter Monday.
            self._add_easter_monday(tr("Easter Monday"))

        # Labour Day.
        self._add_observed(self._add_labor_day(tr("Labour Day")))

        # The Fete Dieu.
        self._add_corpus_christi_day(tr("The Fete Dieu"))

        if self._year <= 2016:
            # Liberation Day.
            self._add_observed(self._add_holiday_jun_5(tr("Liberation Day")))

        self._add_observed(
            self._add_holiday_jun_18(
                # National Day.
                tr("National Day")
                if self._year <= 2014
                # Constitution Day.
                else tr("Constitution Day")
            )
        )

        self._add_observed(
            self._add_holiday_jun_29(
                # Independence Day.
                tr("Independence Day")
                if self._year <= 2014
                # Independence (National) Day.
                else tr("Independence (National) Day")
            )
        )

        # Assumption Day.
        self._add_observed(self._add_assumption_of_mary_day(tr("Assumption Day")))

        # All Saints Day.
        self._add_observed(self._add_all_saints_day(tr("All Saints Day")))

        self._add_observed(
            # The Feast of the Immaculate Conception.
            self._add_immaculate_conception_day(tr("The Feast of the Immaculate Conception"))
        )

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Christmas Day")))


class SC(Seychelles):
    pass


class SYC(Seychelles):
    pass


class SeychellesStaticHolidays:
    """
    Sources:
     - https://seylii.org/akn/sc/act/si/2015/58/eng@2015-12-01
     - https://seylii.org/akn/sc/act/si/2015/59/eng@2015-12-11
     - https://seylii.org/akn/sc/act/si/2016/58/eng@2016-09-06
     - https://seylii.org/akn/sc/act/si/2019/10/eng@2019-03-05
     - https://seylii.org/akn/sc/act/si/2019/61/eng@2019-10-18
     - https://seylii.org/akn/sc/act/si/2020/134/eng@2020-09-17
     - https://seylii.org/akn/sc/act/si/2020/154/eng@2020-10-26
     - https://www.statehouse.gov.sc/news/1765/public-holiday-october-1
     - https://www.egov.sc/PressRoom/DisplayPressRelease.aspx?PRLID=196
     - https://www.nation.sc/archive/216478/saturday-may-12-2007-public-holiday

    All Election Dates usually proceed from the Outer Islands first, then the Inner Islands, and
    the main capital, Mahé, on the last day. The current implementation only uses the last day,
    as officially decreed in 2007, 2011, 2015, and 2020.
    """

    # Bridge Public Holiday.
    bridge_public_holiday = tr("Bridge Public Holiday")

    # Presidential Election Day.
    presidential_election_day = tr("Presidential Election Day")

    # Parliamentary Election Day.
    parliamentary_election_day = tr("Parliamentary Election Day")

    # General Election Day.
    general_election_day = tr("General Election Day")

    special_public_holidays = {
        2007: (MAY, 12, presidential_election_day),
        2011: (
            (MAY, 21, presidential_election_day),
            (OCT, 1, parliamentary_election_day),
        ),
        2015: (
            (DEC, 5, presidential_election_day),
            (DEC, 18, presidential_election_day),
        ),
        2016: (SEP, 10, parliamentary_election_day),
        # Funeral of the Former President France Albert René.
        2019: (MAR, 7, tr("Funeral of the Former President France Albert René")),
        2020: (
            (JAN, 3, bridge_public_holiday),
            (OCT, 24, general_election_day),
            (OCT, 26, bridge_public_holiday),
        ),
    }
