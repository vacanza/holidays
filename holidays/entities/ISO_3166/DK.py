#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

"""
References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Denmark
    - https://www.norden.org/en/info-norden/public-holidays-denmark
    - https://www.ft.dk/samling/20222/lovforslag/l13/index.htm
"""

from gettext import gettext as tr

from holidays.constants import OPTIONAL, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class DkHolidays(HolidayBase, ChristianHolidays, InternationalHolidays):
    """A class to represent holidays for Denmark."""

    country = "DK"
    name = "Denmark"
    default_language = "da"
    supported_categories = (OPTIONAL, PUBLIC)
    supported_languages = ("da", "en_US", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Nytårsdag"))

        # Maundy Thursday.
        self._add_holy_thursday(tr("Skærtorsdag"))

        # Good Friday.
        self._add_good_friday(tr("Langfredag"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Påskedag"))

        # Easter Monday.
        self._add_easter_monday(tr("Anden påskedag"))

        if self._year <= 2023:
            # Great Day of Prayers.
            self._add_holiday_26_days_past_easter(tr("Store bededag"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Kristi himmelfartsdag"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Pinsedag"))

        # Whit Monday.
        self._add_whit_monday(tr("Anden pinsedag"))

        # Christmas Day.
        self._add_christmas_day(tr("Juledag"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Anden juledag"))

    def _populate_optional_holidays(self):
        # International Workers' Day.
        self._add_labor_day(tr("Arbejdernes kampdag"))

        # Constitution Day.
        self._add_holiday_jun_5(tr("Grundlovsdag"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Juleaftensdag"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Nytårsaften"))
