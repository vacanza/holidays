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

from datetime import timedelta as td
from gettext import gettext as tr

from dateutil.easter import EASTER_ORTHODOX, easter

from holidays.constants import JAN, MAR, MAY, SEP, NOV, DEC
from holidays.holiday_base import HolidayBase


class Bulgaria(HolidayBase):
    """
    Official holidays in Bulgaria in their current form. This class does not
    any return holidays before 1990, as holidays in the People's Republic of
    Bulgaria and earlier were different.

    Most holidays are fixed and if the date falls on a Saturday or a Sunday,
    the following Monday is a non-working day. The exceptions are (1) the
    Easter holidays, which are always a consecutive Friday, Saturday, and
    Sunday; and (2) the National Awakening Day which, while an official holiday
    and a non-attendance day for schools, is still a working day.

    Sources (Bulgarian):
    - http://lex.bg/laws/ldoc/1594373121
    - https://www.parliament.bg/bg/24
    - https://kik-info.com/spravochnik/calendar/2021/

    Sources (English):
    - https://en.wikipedia.org/wiki/Public_holidays_in_Bulgaria
    """

    country = "BG"
    default_language = "bg"

    def _populate(self, year):
        if year < 1990:
            return None

        super()._populate(year)

        # New Year's Day.
        self._add_holiday(tr("Нова година"), JAN, 1)

        # Liberation Day.
        self._add_holiday(
            tr("Ден на Освобождението на България от османско иго"), MAR, 3
        )

        # International Workers' Day.
        self._add_holiday(
            tr("Ден на труда и на международната работническа солидарност"),
            MAY,
            1,
        )

        # Saint George's Day.
        self._add_holiday(
            tr("Гергьовден, Ден на храбростта и Българската армия"), MAY, 6
        )

        # Bulgarian Education and Culture and Slavonic Literature Day.
        self._add_holiday(
            tr(
                "Ден на светите братя Кирил и Методий, на българската азбука, "
                "просвета и култура и на славянската книжовност"
            ),
            MAY,
            24,
        )

        # Unification Day.
        self._add_holiday(tr("Ден на Съединението"), SEP, 6)

        # Independence Day.
        self._add_holiday(tr("Ден на Независимостта на България"), SEP, 22)

        # National Awakening Day.
        self._add_holiday(tr("Ден на народните будители"), NOV, 1)

        # Christmas Eve.
        self._add_holiday(tr("Бъдни вечер"), DEC, 24)
        # Christmas Day 1.
        self._add_holiday(tr("Рождество Христово"), DEC, 25)
        # Christmas Day 2.
        self._add_holiday(tr("Рождество Христово"), DEC, 26)

        # Easter.
        easter_date = easter(year, method=EASTER_ORTHODOX)
        # Good Friday.
        self._add_holiday(tr("Велики петък"), easter_date + td(days=-2))
        # Easter Saturday.
        self._add_holiday(tr("Велика събота"), easter_date + td(days=-1))
        # Easter Sunday.
        self._add_holiday(tr("Великден"), easter_date)
        # Easter Monday.
        self._add_holiday(tr("Великден"), easter_date + td(days=+1))


class BG(Bulgaria):
    pass


class BLG(Bulgaria):
    pass
