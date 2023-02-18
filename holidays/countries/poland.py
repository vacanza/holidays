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

from datetime import date
from datetime import timedelta as td
from gettext import gettext as tr

from dateutil.easter import easter

from holidays.constants import JAN, FEB, MAY, JUN, JUL, AUG, NOV, DEC
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
        if year <= 1924:
            return None

        super()._populate(year)

        self[date(year, JAN, 1)] = self.tr("Nowy Rok")

        if year <= 1960 or year >= 2011:
            self[date(year, JAN, 6)] = self.tr("Święto Trzech Króli")

        if year <= 1950:
            self[date(year, FEB, 2)] = self.tr(
                "Oczyszczenie Najświętszej Marii Panny"
            )

        easter_date = easter(year)
        self[easter_date] = self.tr("Niedziela Wielkanocna")

        self[easter_date + td(days=+1)] = self.tr("Poniedziałek Wielkanocny")

        if year >= 1950:
            self[date(year, MAY, 1)] = self.tr("Święto Państwowe")

        if year <= 1950 or year >= 1990:
            self[date(year, MAY, 3)] = self.tr(
                "Święto Narodowe Trzeciego Maja"
            )

        if 1946 <= year <= 1950:
            self[date(year, MAY, 9)] = self.tr(
                "Narodowe Święto Zwycięstwa i Wolności"
            )

        if year <= 1950:
            self[easter_date + td(days=+40)] = self.tr(
                "Wniebowstąpienie Pańskie"
            )

        self[easter_date + td(days=+49)] = self.tr("Zielone Świątki")

        if year <= 1950:
            self[easter_date + td(days=+50)] = self.tr(
                "Drugi dzień Zielonych Świątek"
            )

        self[easter_date + td(days=+60)] = self.tr("Dzień Bożego Ciała")

        if year <= 1950:
            self[date(year, JUN, 29)] = self.tr(
                "Uroczystość Świętych Apostołów Piotra i Pawła"
            )

        if 1945 <= year <= 1989:
            self[date(year, JUL, 22)] = self.tr(
                "Narodowe Święto Odrodzenia Polski"
            )

        if year <= 1960 or year >= 1989:
            self[date(year, AUG, 15)] = self.tr(
                "Wniebowzięcie Najświętszej Marii Panny"
            )

        self[date(year, NOV, 1)] = self.tr("Uroczystość Wszystkich Świętych")

        if 1937 <= year <= 1944 or year >= 1989:
            self[date(year, NOV, 11)] = self.tr(
                "Narodowe Święto Niepodległości"
            )

        if year <= 1950:
            self[date(year, DEC, 8)] = self.tr(
                "Niepokalane Poczęcie Najświętszej Marii Panny"
            )

        self[date(year, DEC, 25)] = self.tr("Boże Narodzenie (pierwszy dzień)")
        self[date(year, DEC, 26)] = self.tr("Boże Narodzenie (drugi dzień)")


class PL(Poland):
    pass


class POL(Poland):
    pass
