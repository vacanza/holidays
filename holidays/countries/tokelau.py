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
from holidays.holiday_base import HolidayBase


class Tokelau(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Tokelau Holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Tokelau>
        * <https://web.archive.org/web/20250715060109/https://www.tokelau.org.nz/About+Us/Culture.html>
        * <https://web.archive.org/web/20250715065528/https://paclii.org/tk/legis/consol_act_2016/ir2003240.pdf>
    """

    country = "TK"
    default_language = "tk"
    supported_languages = ("en_US", "tk")
    start_year = 2003

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Aho Tau Fou"))

        # Good Friday.
        self._add_good_friday(tr("Ahofalaile Lelei"))

        # Easter Monday.
        self._add_easter_monday(tr("Ahogafua o te Eheta"))

        # Tokehega Day.
        self._add_holiday_sep_3(tr("Aho o te Tokehega"))

        # Christmas Day.
        self._add_christmas_day(tr("Aho Kilihimahi"))

        # Boxing Day
        self._add_christmas_day_two(tr("Tua-aho Kilihimahi"))


class TK(Tokelau):
    pass


class TKL(Tokelau):
    pass
