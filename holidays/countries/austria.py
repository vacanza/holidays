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

from holidays.constants import BANK, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Austria(HolidayBase, ChristianHolidays, InternationalHolidays):
    country = "AT"
    default_language = "de"
    supported_categories = (BANK, PUBLIC)
    supported_languages = ("de", "en_US", "uk")
    subdivisions = (
        "1",    # Burgenland
        "2",    # Kärnten
        "3",    # Niederösterreich
        "4",    # Oberösterreich
        "5",    # Salzburg
        "6",    # Steiermark
        "7",    # Tirol
        "8",    # Vorarlberg
        "9"     # Wien
    )
    subdivisions_aliases = {
        "B": "1", "Bgl": "1", "Burgenland": "1",
        "K": "2", "Ktn": "2", "Kärnten": "2", "Carinthia": "2",
        "N": "3", "NÖ": "3", "Niederösterreich": "3", "Lower Austria": "3",
        "O": "4", "OÖ": "4", "Oberösterreich": "4", "Upper Austria": "4",
        "S": "5", "Sbg": "5", "Salzburg": "5",
        "St": "6", "Stmk": "6", "Steiermark": "6", "Styria": "6",
        "T": "7", "Tirol": "7", "Tyrol": "7",
        "V": "8", "Vbg": "8", "Vorarlberg": "8",
        "W": "9", "Wien": "9", "Vienna": "9"
    }

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)

        # Set the default subdivision.
        if not kwargs.get("subdiv", kwargs.get("state")):
            kwargs["subdiv"] = "9"

        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Neujahr"))

        # Epiphany.
        self._add_epiphany_day(tr("Heilige Drei Könige"))

        # Easter Monday.
        self._add_easter_monday(tr("Ostermontag"))

        # Labor Day.
        self._add_labor_day(tr("Staatsfeiertag"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Christi Himmelfahrt"))

        # Whit Monday.
        self._add_whit_monday(tr("Pfingstmontag"))

        # Corpus Christi.
        self._add_corpus_christi_day(tr("Fronleichnam"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        if 1919 <= self._year <= 1934:
            # National Day.
            self._add_holiday_nov_12(tr("Nationalfeiertag"))
        if self._year >= 1967:
            self._add_holiday_oct_26(tr("Nationalfeiertag"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Allerheiligen"))

        # Immaculate Conception.
        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

        # Christmas Day.
        self._add_christmas_day(tr("Christtag"))

        # St. Stephen's Day.
        self._add_christmas_day_two(tr("Stefanitag"))

    def _populate_bank_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Karfreitag"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Heiliger Abend"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Silvester"))


class AT(Austria):
    pass


class AUT(Austria):
    pass
