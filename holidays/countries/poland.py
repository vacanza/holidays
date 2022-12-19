#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Arkadii Yakovets <ark@cho.red>, (c) 2022
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from gettext import gettext as tr

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAY, AUG, NOV, DEC
from holidays.holiday_base import HolidayBase


class Poland(HolidayBase):
    """
    https://pl.wikipedia.org/wiki/Dni_wolne_od_pracy_w_Polsce
    """

    country = "PL"
    default_language = "pl"
    special_holidays = {
        2018: ((NOV, 12, tr("Narodowe Święto Niepodległości - 100-lecie")),)
    }

    def _populate(self, year):
        super()._populate(year)

        self[date(year, JAN, 1)] = self.tr("Nowy Rok")
        if year >= 2011:
            self[date(year, JAN, 6)] = self.tr("Święto Trzech Króli")

        easter_date = easter(year)
        self[easter_date] = self.tr("Niedziela Wielkanocna")
        self[easter_date + rd(days=+1)] = self.tr("Poniedziałek Wielkanocny")

        if year >= 1950:
            self[date(year, MAY, 1)] = self.tr("Święto Państwowe")
        if year >= 1919:
            self[date(year, MAY, 3)] = self.tr(
                "Święto Narodowe Trzeciego Maja"
            )

        self[easter_date + rd(days=+49)] = self.tr("Zielone Świątki")
        self[easter_date + rd(days=+60)] = self.tr("Dzień Bożego Ciała")

        self[date(year, AUG, 15)] = self.tr(
            "Wniebowzięcie Najświętszej Marii Panny"
        )

        self[date(year, NOV, 1)] = self.tr("Uroczystość Wszystkich Świętych")
        if (1937 <= year <= 1945) or year >= 1989:
            self[date(year, NOV, 11)] = self.tr(
                "Narodowe Święto Niepodległości"
            )

        self[date(year, DEC, 25)] = self.tr("Boże Narodzenie (pierwszy dzień)")
        self[date(year, DEC, 26)] = self.tr("Boże Narodzenie (drugi dzień)")


class PL(Poland):
    pass


class POL(Poland):
    pass
