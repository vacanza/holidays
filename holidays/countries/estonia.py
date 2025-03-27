#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Estonia(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Estonia holidays."""

    country = "EE"
    default_language = "et"
    supported_languages = ("en_US", "et", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("uusaasta"))

        # Independence Day.
        self._add_holiday_feb_24(tr("iseseisvuspäev"))

        # Good Friday.
        self._add_good_friday(tr("suur reede"))

        # Easter Sunday.
        self._add_easter_sunday(tr("ülestõusmispühade 1. püha"))

        # Spring Day.
        self._add_holiday_may_1(tr("kevadpüha"))

        # Whit Sunday.
        self._add_whit_sunday(tr("nelipühade 1. püha"))

        # Victory Day.
        self._add_holiday_jun_23(tr("võidupüha"))

        # Midsummer Day.
        self._add_saint_johns_day(tr("jaanipäev"))

        if self._year >= 1998:
            # Independence Restoration Day.
            self._add_holiday_aug_20(tr("taasiseseisvumispäev"))

        if self._year >= 2005:
            # Christmas Eve.
            self._add_christmas_eve(tr("jõululaupäev"))

        # Christmas Day.
        self._add_christmas_day(tr("esimene jõulupüha"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("teine jõulupüha"))


class EE(Estonia):
    pass


class EST(Estonia):
    pass
