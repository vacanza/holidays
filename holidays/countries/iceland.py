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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Iceland(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Iceland
    https://www.officeholidays.com/countries/iceland/index.php
    """

    country = "IS"
    default_language = "is"
    supported_languages = ("en_US", "is", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day(tr("Nýársdagur"))

        # Maundy Thursday.
        self._add_holy_thursday(tr("Skírdagur"))

        # Good Friday.
        self._add_good_friday(tr("Föstudagurinn langi"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Páskadagur"))

        # Easter Monday.
        self._add_easter_monday(tr("Annar í páskum"))

        # First Day of Summer.
        self._add_holiday_1st_thu_from_apr_19(tr("Sumardagurinn fyrsti"))

        # Labor Day.
        self._add_labor_day(tr("Verkalýðsdagurinn"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Uppstigningardagur"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Hvítasunnudagur"))

        # Whit Monday.
        self._add_whit_monday(tr("Annar í hvítasunnu"))

        # National Day.
        self._add_holiday_jun_17(tr("Þjóðhátíðardagurinn"))

        # Commerce Day.
        self._add_holiday_1st_mon_of_aug(tr("Frídagur verslunarmanna"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Aðfangadagur"))

        # Christmas Day.
        self._add_christmas_day(tr("Jóladagur"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Annar í jólum"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Gamlársdagur"))


class IS(Iceland):
    pass


class ISL(Iceland):
    pass
