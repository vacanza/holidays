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

from dateutil.easter import easter

from holidays.constants import JAN, MAY, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class Slovakia(HolidayBase):
    """
    https://sk.wikipedia.org/wiki/Sviatok
    https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/1993/241/20181011.html
    """

    country = "SK"
    special_holidays = {
        2018: (
            (OCT, 30, "100. výročie prijatia Deklarácie slovenského národa"),
        )
    }

    def _populate(self, year):
        super()._populate(year)

        self[date(year, JAN, 1)] = "Deň vzniku Slovenskej republiky"
        self[date(year, JAN, 6)] = (
            "Zjavenie Pána (Traja králi a"
            " vianočnýsviatok pravoslávnych"
            " kresťanov)"
        )

        easter_date = easter(year)
        self[easter_date + td(days=-2)] = "Veľký piatok"
        self[easter_date + td(days=+1)] = "Veľkonočný pondelok"

        self[date(year, MAY, 1)] = "Sviatok práce"

        if year >= 1997:
            self[date(year, MAY, 8)] = "Deň víťazstva nad fašizmom"

        self[date(year, JUL, 5)] = "Sviatok svätého Cyrila a svätého Metoda"

        self[date(year, AUG, 29)] = (
            "Výročie Slovenského národného" " povstania"
        )

        self[date(year, SEP, 1)] = "Deň Ústavy Slovenskej republiky"

        self[date(year, SEP, 15)] = "Sedembolestná Panna Mária"

        self[date(year, NOV, 1)] = "Sviatok Všetkých svätých"

        if year >= 2001:
            self[date(year, NOV, 17)] = "Deň boja za slobodu a demokraciu"

        self[date(year, DEC, 24)] = "Štedrý deň"

        self[date(year, DEC, 25)] = "Prvý sviatok vianočný"

        self[date(year, DEC, 26)] = "Druhý sviatok vianočný"


class SK(Slovakia):
    pass


class SVK(Slovakia):
    pass
