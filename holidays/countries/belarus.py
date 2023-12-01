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
    special_holidays = {
        1998: (
            (JAN, 2, JAN, 10),
            (APR, 27, APR, 25),
        ),
        1999: (
            (JAN, 8, JAN, 16),
            (APR, 19, APR, 17),
        ),
        2000: (
            (MAY, 8, MAY, 13),
            (NOV, 6, NOV, 11),
        ),
        2001: (
            (JAN, 2, JAN, 20),
            (MAR, 9, MAR, 3),
            (APR, 23, APR, 21),
            (APR, 30, APR, 28),
            (JUL, 2, JUL, 7),
            (DEC, 24, DEC, 22),
            (DEC, 31, DEC, 29),
        ),
        2002: (
            (JAN, 2, JAN, 5),
            (MAY, 10, MAY, 18),
            (NOV, 8, NOV, 16),
        ),
        2003: (
            (JAN, 6, JAN, 4),
            (MAY, 5, MAY, 3),
        ),
        2004: (
            (JAN, 2, JAN, 10),
            (JAN, 5, JAN, 17),
            (JAN, 6, JAN, 31),
            (APR, 19, APR, 17),
        ),
        2005: (MAR, 7, MAR, 12),
        2006: (
            (JAN, 2, JAN, 21),
            (MAY, 8, MAY, 6),
            (NOV, 6, NOV, 4),
        ),
        2007: (
            (JAN, 2, DEC, 30, 2006),
            (MAR, 9, MAR, 17),
            (APR, 16, APR, 14),
            (APR, 30, MAY, 5),
            (JUL, 2, JUL, 7),
            (DEC, 24, DEC, 22),
            (DEC, 31, DEC, 29),
        ),
        2008: (
            (JAN, 2, JAN, 12),
            (MAY, 5, MAY, 3),
            (JUL, 4, JUN, 28),
            (DEC, 26, DEC, 20),
        ),
        2009: (
            (JAN, 2, JAN, 10),
            (APR, 27, APR, 25),
        ),
        2010: (
            (JAN, 8, JAN, 23),
            (APR, 12, APR, 17),
            (MAY, 10, MAY, 15),
        ),
        2011: (
            (MAR, 7, MAR, 12),
            (MAY, 2, MAY, 14),
        ),
        2012: (
            (MAR, 9, MAR, 11),
            (APR, 23, APR, 28),
            (JUL, 2, JUN, 30),
            (DEC, 24, DEC, 22),
            (DEC, 31, DEC, 29),
        ),
        2013: (
            (JAN, 2, JAN, 5),
            (MAY, 10, MAY, 18),
        ),
        2014: (
            (JAN, 2, JAN, 4),
            (JAN, 6, JAN, 11),
            (APR, 30, MAY, 3),
            (JUL, 4, JUL, 12),
            (DEC, 26, DEC, 20),
        ),
        2015: (
            (JAN, 2, JAN, 10),
            (APR, 20, APR, 25),
        ),
        2016: (
            (JAN, 8, JAN, 16),
            (MAR, 7, MAR, 5),
        ),
        2017: (
            (JAN, 2, JAN, 21),
            (APR, 24, APR, 29),
            (MAY, 8, MAY, 6),
            (NOV, 6, NOV, 4),
        ),
        2018: (
            (JAN, 2, JAN, 20),
            (MAR, 9, MAR, 3),
            (APR, 16, APR, 14),
            (APR, 30, APR, 28),
            (JUL, 2, JUL, 7),
            (DEC, 24, DEC, 22),
            (DEC, 31, DEC, 29),
        ),
        2019: (
            (MAY, 6, MAY, 4),
            (MAY, 8, MAY, 11),
            (NOV, 8, NOV, 16),
        ),
        2020: (
            (JAN, 6, JAN, 4),
            (APR, 27, APR, 4),
        ),
        2021: (
            (JAN, 8, JAN, 16),
            (MAY, 10, MAY, 15),
        ),
        2022: (
            (MAR, 7, MAR, 12),
            (MAY, 2, MAY, 14),
        ),
        2023: (
            (APR, 24, APR, 29),
            (MAY, 8, MAY, 13),
            (NOV, 6, NOV, 11),
        ),
    }
