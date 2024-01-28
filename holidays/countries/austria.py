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
        "1",  # Burgenland.
        "2",  # Kärnten.
        "3",  # Niederösterreich.
        "4",  # Oberösterreich.
        "5",  # Salzburg.
        "6",  # Steiermark.
        "7",  # Tirol.
        "8",  # Vorarlberg.
        "9",  # Wien.
    )
    subdivisions_aliases = {
        "B": "1",
        "K": "2",
        "N": "3",
        "O": "4",
        "S": "5",
        "St": "6",
        "T": "7",
        "V": "8",
        "W": "9",
    }

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
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

    def _populate_subdiv_1_bank_holidays(self):
        # Patron saint of Burgenland: Hl. Martin von Tours (St. Martin of Tours)
        self._add_holiday_nov_11(tr("Hl. Martin"))

    def _populate_subdiv_2_bank_holidays(self):
        # Patron saint of Carinthia: Hl. Josef (St. Joseph's day)
        self._add_saint_josephs_day(tr("Hl. Josef"))

        # Tag der Volksabstimmung (1920 Carinthian plebiscite)
        self._add_holiday_oct_10(tr("Tag der Volksabstimmung"))

    def _populate_subdiv_3_bank_holidays(self):
        # Patron saint of Lower Austria: Hl. Leopold III. (St. Leopold III)
        self._add_holiday_nov_15(tr("Hl. Leopold"))

    def _populate_subdiv_4_bank_holidays(self):
        # Patron saint of Upper Austria: Hl. Florian von Lorch (St. Florian)
        if self._year >= 2004:
            self._add_holiday_may_4(tr("Hl. Florian"))

    def _populate_subdiv_5_bank_holidays(self):
        # Patron saint of Salzburg: Hl. Rupert von Salzburg (St. Rupert of Salzburg)
        self._add_holiday_sep_24(tr("Hl. Rupert"))

    def _populate_subdiv_6_bank_holidays(self):
        # Patron saint of Styria: Hl. Josef (St. Joseph's day)
        self._add_saint_josephs_day(tr("Hl. Josef"))

    def _populate_subdiv_7_bank_holidays(self):
        # Patron saint of Tyrol: Hl. Josef (St. Joseph's day)
        self._add_saint_josephs_day(tr("Hl. Josef"))

    def _populate_subdiv_8_bank_holidays(self):
        # Patron saint of Vorarlberg: Hl. Josef (St. Joseph's day)
        self._add_saint_josephs_day(tr("Hl. Josef"))

    def _populate_subdiv_9_bank_holidays(self):
        # Patron saint of Vienna: Hl. Leopold III. (St. Leopold III)
        self._add_holiday_nov_15(tr("Hl. Leopold"))


class AT(Austria):
    pass


class AUT(Austria):
    pass
