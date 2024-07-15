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
    - https://en.wikipedia.org/wiki/Public_holidays_in_Greenland
    - https://www.norden.org/en/info-norden/public-holidays-greenland
    - https://www.timeanddate.com/holidays/greenland/
"""

from gettext import gettext as tr

from holidays.constants import OPTIONAL, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class GlHolidays(HolidayBase, ChristianHolidays, InternationalHolidays):
    """A class to represent holidays for Greenland."""

    country = "GL"
    name = "Greenland"
    default_language = "kl"
    supported_categories = (OPTIONAL, PUBLIC)
    supported_languages = ("da", "en_US", "kl")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Ukioq nutaaq"))

        # Maundy Thursday.
        self._add_holy_thursday(tr("Sisamanngornermi illernartumi"))

        # Good Friday.
        self._add_good_friday(tr("Tallimanngorneq ajortorsiorneq"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Poorskimi"))

        # Easter Monday.
        self._add_easter_monday(tr("Poorskimi ullut aappaat"))

        # Great Day of Prayers.
        self._add_holiday_26_days_past_easter(tr("Ulloq qinuffiusoq"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Ulloq Kristusip qilaliarnera"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Piinsip ullua"))

        # Whit Monday.
        self._add_whit_monday(tr("Piinsip ulluisa aappaanni"))

        # Christmas Day.
        self._add_christmas_day(tr("Juulli"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Juullip aappaa"))

    def _populate_optional_holidays(self):
        # Epiphany.
        self._add_epiphany_day(tr("Mitaarneq"))

        # International Workers' Day.
        self._add_labor_day(tr("Sulisartut ulluat"))

        # National Day.
        self._add_holiday_jun_21(tr("Ullortuneq"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Juulliaqqami"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Ukiortaami"))
