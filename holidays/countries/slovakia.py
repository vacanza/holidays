#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars.gregorian import OCT
from holidays.constants import PUBLIC, WORKDAY
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class Slovakia(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Slovakia
    https://sk.wikipedia.org/wiki/Zoznam_sviatkov_na_Slovensku
    https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/1993/241/
    """

    country = "SK"
    default_language = "sk"
    supported_categories = (PUBLIC, WORKDAY)
    supported_languages = ("en_US", "sk", "uk")
    # Independent Slovak Republic established on Jan 01, 1993
    start_year = 1993

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=SlovakiaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Day of the Establishment of the Slovak Republic.
        self._add_holiday_jan_1(tr("Deň vzniku Slovenskej republiky"))

        self._add_epiphany_day(
            # Epiphany.
            tr("Zjavenie Pána (Traja králi a vianočný sviatok pravoslávnych kresťanov)")
        )

        # Good Friday.
        self._add_good_friday(tr("Veľký piatok"))

        # Easter Monday.
        self._add_easter_monday(tr("Veľkonočný pondelok"))

        # Labor Day.
        self._add_labor_day(tr("Sviatok práce"))

        if self._year >= 1997:
            # Day of Victory over Fascism.
            self._add_world_war_two_victory_day(tr("Deň víťazstva nad fašizmom"))

        # Saints Cyril and Methodius Day.
        self._add_holiday_jul_5(tr("Sviatok svätého Cyrila a svätého Metoda"))

        # Slovak National Uprising Anniversary.
        self._add_holiday_aug_29(tr("Výročie Slovenského národného povstania"))

        # Constitution Day.
        self._add_holiday_sep_1(tr("Deň Ústavy Slovenskej republiky"))

        # Day of Our Lady of the Seven Sorrows.
        self._add_holiday_sep_15(tr("Sedembolestná Panna Mária"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Sviatok Všetkých svätých"))

        if self._year >= 2001:
            # Struggle for Freedom and Democracy Day.
            self._add_holiday_nov_17(tr("Deň boja za slobodu a demokraciu"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Štedrý deň"))

        # Christmas Day.
        self._add_christmas_day(tr("Prvý sviatok vianočný"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Druhý sviatok vianočný"))

    def _populate_workday_holidays(self):
        # According to Law 241/1993, this state holiday is not a non-working day.
        if self._year >= 2021:
            # Day of the Establishment of the Independent Czech-Slovak State.
            self._add_holiday_oct_28(tr("Deň vzniku samostatného česko-slovenského štátu"))


class SK(Slovakia):
    pass


class SVK(Slovakia):
    pass


class SlovakiaStaticHolidays:
    special_public_holidays = {
        # 100th anniversary of the adoption of the Declaration
        # of the Slovak Nation.
        2018: (OCT, 30, tr("100. výročie prijatia Deklarácie slovenského národa"))
    }
