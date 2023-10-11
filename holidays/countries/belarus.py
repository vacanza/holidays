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

from holidays.calendars.gregorian import GREGORIAN_CALENDAR, JAN, MAR, APR, MAY, JUN, JUL, NOV, DEC
from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class Belarus(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    Belarus holidays.

    References:
     - http://president.gov.by/en/holidays_en/
     - http://www.belarus.by/en/about-belarus/national-holidays
     - http://laws.newsby.org/documents/ukazp/pos05/ukaz05806.htm
     - http://president.gov.by/uploads/documents/2019/464uk.pdf
     - https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B0%D0%B7%D0%B4%D0%BD%D0%B8%D0%BA%D0%B8_%D0%91%D0%B5%D0%BB%D0%BE%D1%80%D1%83%D1%81%D1%81%D0%B8%D0%B8  # noqa: E501
    """

    country = "BY"
    default_language = "be"
    supported_languages = ("be", "en_US")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, BelarusStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        # The current set of holidays actual from 1998.
        if year <= 1997:
            return None

        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day(tr("Новы год"))

        if year >= 2020:
            self._add_new_years_day_two(tr("Новы год"))

        # Orthodox Christmas Day.
        self._add_christmas_day(tr("Нараджэнне Хрыстова (праваслаўнае Раство)"))

        # Women's Day.
        self._add_womens_day(tr("Дзень жанчын"))

        # Radunitsa (Day of Rejoicing).
        self._add_rejoicing_day(tr("Радаўніца"))

        # Labour Day.
        self._add_labor_day(tr("Свята працы"))

        # Victory Day.
        self._add_world_war_two_victory_day(tr("Дзень Перамогі"))

        # Independence Day.
        self._add_holiday_jul_3(tr("Дзень Незалежнасці Рэспублікі Беларусь (Дзень Рэспублікі)"))

        # October Revolution Day.
        self._add_holiday_nov_7(tr("Дзень Кастрычніцкай рэвалюцыі"))

        # Catholic Christmas Day.
        self._add_christmas_day(tr("Нараджэнне Хрыстова (каталіцкае Раство)"), GREGORIAN_CALENDAR)


class BY(Belarus):
    pass


class BLR(Belarus):
    pass


class BelarusStaticHolidays:
    # Date format (see strftime() Format Codes)
    substituted_date_format = tr("%d.%m.%Y")
    # Day off (substituted from %s).
    substituted_label = tr("Выходны (перанесены з %s)")
    substituted_holidays = {
        1998: (
            (JAN, 10, JAN, 2),
            (APR, 25, APR, 27),
        ),
        1999: (
            (JAN, 16, JAN, 8),
            (APR, 17, APR, 19),
        ),
        2000: (
            (MAY, 13, MAY, 8),
            (NOV, 11, NOV, 6),
        ),
        2001: (
            (JAN, 20, JAN, 2),
            (MAR, 3, MAR, 9),
            (APR, 21, APR, 23),
            (APR, 28, APR, 30),
            (JUL, 7, JUL, 2),
            (DEC, 22, DEC, 24),
            (DEC, 29, DEC, 31),
        ),
        2002: (
            (JAN, 5, JAN, 2),
            (MAY, 18, MAY, 10),
            (NOV, 16, NOV, 8),
        ),
        2003: (
            (JAN, 4, JAN, 6),
            (MAY, 3, MAY, 5),
        ),
        2004: (
            (JAN, 10, JAN, 2),
            (JAN, 17, JAN, 5),
            (JAN, 31, JAN, 6),
            (APR, 17, APR, 19),
        ),
        2005: (MAR, 12, MAR, 7),
        2006: (
            (JAN, 21, JAN, 2),
            (MAY, 6, MAY, 8),
            (NOV, 4, NOV, 6),
        ),
        2007: (
            (2006, DEC, 30, JAN, 2),
            (MAR, 17, MAR, 9),
            (APR, 14, APR, 16),
            (MAY, 5, APR, 30),
            (JUL, 7, JUL, 2),
            (DEC, 22, DEC, 24),
            (DEC, 29, DEC, 31),
        ),
        2008: (
            (JAN, 12, JAN, 2),
            (MAY, 3, MAY, 5),
            (JUN, 28, JUL, 4),
            (DEC, 20, DEC, 26),
        ),
        2009: (
            (JAN, 10, JAN, 2),
            (APR, 25, APR, 27),
        ),
        2010: (
            (JAN, 23, JAN, 8),
            (APR, 17, APR, 12),
            (MAY, 15, MAY, 10),
        ),
        2011: (
            (MAR, 12, MAR, 7),
            (MAY, 14, MAY, 2),
        ),
        2012: (
            (MAR, 11, MAR, 9),
            (APR, 28, APR, 23),
            (JUN, 30, JUL, 2),
            (DEC, 22, DEC, 24),
            (DEC, 29, DEC, 31),
        ),
        2013: (
            (JAN, 5, JAN, 2),
            (MAY, 18, MAY, 10),
        ),
        2014: (
            (JAN, 4, JAN, 2),
            (JAN, 11, JAN, 6),
            (MAY, 3, APR, 30),
            (JUL, 12, JUL, 4),
            (DEC, 20, DEC, 26),
        ),
        2015: (
            (JAN, 10, JAN, 2),
            (APR, 25, APR, 20),
        ),
        2016: (
            (JAN, 16, JAN, 8),
            (MAR, 5, MAR, 7),
        ),
        2017: (
            (JAN, 21, JAN, 2),
            (APR, 29, APR, 24),
            (MAY, 6, MAY, 8),
            (NOV, 4, NOV, 6),
        ),
        2018: (
            (JAN, 20, JAN, 2),
            (MAR, 3, MAR, 9),
            (APR, 14, APR, 16),
            (APR, 28, APR, 30),
            (JUL, 7, JUL, 2),
            (DEC, 22, DEC, 24),
            (DEC, 29, DEC, 31),
        ),
        2019: (
            (MAY, 4, MAY, 6),
            (MAY, 11, MAY, 8),
            (NOV, 16, NOV, 8),
        ),
        2020: (
            (JAN, 4, JAN, 6),
            (APR, 4, APR, 27),
        ),
        2021: (
            (JAN, 16, JAN, 8),
            (MAY, 15, MAY, 10),
        ),
        2022: (
            (MAR, 12, MAR, 7),
            (MAY, 14, MAY, 2),
        ),
        2023: (
            (APR, 29, APR, 24),
            (MAY, 13, MAY, 8),
            (NOV, 11, NOV, 6),
        ),
    }
