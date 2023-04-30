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

from holidays.constants import JAN, MAY, JUL, AUG, SEP, OCT, NOV
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Slovakia(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Slovakia
    https://sk.wikipedia.org/wiki/Zoznam_sviatkov_na_Slovensku
    https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/1993/241/
    """

    country = "SK"
    default_language = "sk"
    special_holidays = {
        2018: (
            (
                OCT,
                30,
                # 100th anniversary of the adoption of the Declaration
                # of the Slovak Nation.
                tr("100. výročie prijatia Deklarácie slovenského národa"),
            ),
        )
    }

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        # Independent Slovak Republic established on Jan 01, 1993
        if year <= 1992:
            return None
        super()._populate(year)

        # Day of the Establishment of the Slovak Republic.
        self._add_holiday(tr("Deň vzniku Slovenskej republiky"), JAN, 1)

        # Epiphany.
        self._add_epiphany_day(
            tr(
                "Zjavenie Pána (Traja králi a "
                "vianočnýsviatok pravoslávnych kresťanov)"
            )
        )

        # Good Friday.
        self._add_good_friday(tr("Veľký piatok"))

        # Easter Monday.
        self._add_easter_monday(tr("Veľkonočný pondelok"))

        # Labor Day.
        self._add_labor_day(tr("Sviatok práce"))

        # Day of Victory over Fascism.
        if year >= 1997:
            # Day of Victory over Fascism.
            self._add_holiday(tr("Deň víťazstva nad fašizmom"), MAY, 8)

        self._add_holiday(
            # St. Cyril and Methodius Day.
            tr("Sviatok svätého Cyrila a svätého Metoda"),
            JUL,
            5,
        )

        self._add_holiday(
            # Slovak National Uprising Anniversary.
            tr("Výročie Slovenského národného povstania"),
            AUG,
            29,
        )

        # Constitution Day.
        self._add_holiday(tr("Deň Ústavy Slovenskej republiky"), SEP, 1)

        # Day of Our Lady of the Seven Sorrows.
        self._add_holiday(tr("Sedembolestná Panna Mária"), SEP, 15)

        if year >= 2021:
            self._add_holiday(
                # Day of the Establishment of the Independent Czech-Slovak
                # State.
                tr("Deň vzniku samostatného česko-slovenského štátu"),
                OCT,
                28,
            )

        # All Saints' Day.
        self._add_all_saints_day(tr("Sviatok Všetkých svätých"))

        if year >= 2001:
            # Struggle for Freedom and Democracy Day.
            self._add_holiday(tr("Deň boja za slobodu a demokraciu"), NOV, 17)

        # Christmas Eve.
        self._add_christmas_eve(tr("Štedrý deň"))

        # Christmas Day.
        self._add_christmas_day(tr("Prvý sviatok vianočný"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Druhý sviatok vianočný"))


class SK(Slovakia):
    pass


class SVK(Slovakia):
    pass
