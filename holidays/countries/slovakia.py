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


from holidays.constants import JAN, MAY, JUL, AUG, SEP, OCT, NOV
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Slovakia(HolidayBase, ChristianHolidays, InternationalHolidays):
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

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # Day of the Establishment of the Slovak Republic.
        self._add_holiday("Deň vzniku Slovenskej republiky", JAN, 1)

        # Epiphany Day.
        self._add_epiphany_day(
            "Zjavenie Pána (Traja králi a "
            "vianočnýsviatok pravoslávnych kresťanov)"
        )

        # Easter.
        # Good Friday.
        self._add_good_friday("Veľký piatok")

        # Easter Monday.
        self._add_easter_monday("Veľkonočný pondelok")

        # Labour Day.
        self._add_labor_day("Sviatok práce")

        # Day of Victory over Fascism.
        if year >= 1997:
            self._add_holiday("Deň víťazstva nad fašizmom", MAY, 8)

        # St. Cyril and Methodius Day.
        self._add_holiday("Sviatok svätého Cyrila a svätého Metoda", JUL, 5)

        # Slovak National Uprising Anniversary.
        self._add_holiday("Výročie Slovenského národného povstania", AUG, 29)

        if year >= 1992:
            # Day of the Constitution of the Slovak Republic.
            self._add_holiday("Deň Ústavy Slovenskej republiky", SEP, 1)

        # Day of Our Lady of the Seven Sorrows.
        self._add_holiday("Sedembolestná Panna Mária", SEP, 15)

        # All Saints Day.
        self._add_all_saints_day("Sviatok Všetkých svätých")

        if year >= 2001:
            # Day of Freedom and Democracy.
            self._add_holiday("Deň boja za slobodu a demokraciu", NOV, 17)

        # Christmas Eve.
        self._add_christmas_eve("Štedrý deň")

        # Christmas Day.
        self._add_christmas_day("Prvý sviatok vianočný")

        # Christmas Day 2. St. Stephen's Day.
        self._add_christmas_day_two("Druhý sviatok vianočný")


class SK(Slovakia):
    pass


class SVK(Slovakia):
    pass
