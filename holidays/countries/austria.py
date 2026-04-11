#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.constants import BANK, PROTESTANT, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Austria(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Austria holidays.

    !!! note "Note"
        Although sources for RGBl. Nr. 21, RGBl. Nr. 125, StGBl. Nr. 282, BGBl. Nr. 421,
        BGBl. Nr. 548, and RGBl. I S. 790 are readily available, they either do not specify
        any public holiday observances or are limited to very specific professions.

    References:
        * <https://de.wikipedia.org/wiki/Feiertage_in_Österreich>
        * [BGBl. Nr. 31/1933](http://archive.today/2026.04.08-130337/https://alex.onb.ac.at/cgi-content/alex?apm=0&aid=bgb&datum=19330004&seite=00000103&size=45)
        * [StGBl. Nr. 116/1945](https://web.archive.org/web/20260408120714/https://www.ris.bka.gv.at/Dokumente/BgblPdf/1945_116_0/1945_116_0.pdf)
        * [BGBl. Nr. 173/1949](https://web.archive.org/web/20260408143732/https://ris.bka.gv.at/Dokumente/BgblPdf/1949_173_0/1949_173_0.pdf)
        * [BGBl. Nr. 227/1955 and BGBl. Nr. 228/1955](https://web.archive.org/web/20260408143052/https://ris.bka.gv.at/Dokumente/BgblPdf/1955_227_0/1955_227_0.pdf)
        * [BGBl. Nr. 153/1957](https://web.archive.org/web/20250521041322/https://www.ris.bka.gv.at/Dokumente/BgblPdf/1957_153_0/1957_153_0.pdf)
        * [BGBl. Nr. 264/1967](https://web.archive.org/web/20241220074402/https://ris.bka.gv.at/Dokumente/BgblPdf/1967_264_0/1967_264_0.pdf)
        * [BGBl. Nr. 144/1983](https://web.archive.org/web/20260408111100/https://www.ris.bka.gv.at/Dokumente/BgblPdf/1983_144_0/1983_144_0.pdf)
        * [BGBl. I Nr. 191/1999](https://web.archive.org/web/20260330075009/https://www.ris.bka.gv.at/Dokumente/BgblPdf/1999_191_1/1999_191_1.pdf)
        * [BGBl. I Nr. 113/2006](https://web.archive.org/web/20260408114618/https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2006_I_113/BGBLA_2006_I_113.pdf)
        * [BGBl. I Nr. 22/2019](https://web.archive.org/web/20260408111719/https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2019_I_22/BGBLA_2019_I_22.pdf)
        * <https://web.archive.org/web/20260408155524/https://www.nachrichten.at/archivierte-artikel/serien/wir-oberoesterreicher/Vom-Maertyrer-zum-Patron;art11547,68941>
    """

    country = "AT"
    default_language = "de"
    # BGBl. Nr. 31/1933 became in effect on June 1st, 1933.
    start_year = 1934
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
        "Burgenland": "1",
        "Bgld": "1",
        "B": "1",
        "Kärnten": "2",
        "Ktn": "2",
        "K": "2",
        "Niederösterreich": "3",
        "NÖ": "3",
        "N": "3",
        "Oberösterreich": "4",
        "OÖ": "4",
        "O": "4",
        "Salzburg": "5",
        "Sbg": "5",
        "S": "5",
        "Steiermark": "6",
        "Stmk": "6",
        "St": "6",
        "Tirol": "7",
        "T": "7",
        "Vorarlberg": "8",
        "Vbg": "8",
        "V": "8",
        "Wien": "9",
        "W": "9",
    }
    supported_categories = (BANK, PROTESTANT, PUBLIC)
    supported_languages = ("de", "en_US", "th", "uk")

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Neujahr"))

        # Removed via StGBl. Nr. 116/1945.
        # Re-added via BGBl. Nr. 173/1949.
        if self._year <= 1945 or self._year >= 1950:
            # Epiphany.
            self._add_epiphany_day(tr("Heilige Drei Könige"))

        # Easter Monday.
        self._add_easter_monday(tr("Ostermontag"))

        # Added via via StGBl. Nr. 116/1945.
        if self._year >= 1946:
            # Labor Day.
            self._add_labor_day(tr("Staatsfeiertag"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Christi Himmelfahrt"))

        # Whit Monday.
        self._add_whit_monday(tr("Pfingstmontag"))

        # Added via BGBl. Nr. 31/1933.
        # Removed via StGBl. Nr. 116/1945.
        if self._year <= 1945:
            # Saint Peter and Saint Paul's Day.
            self._add_saints_peter_and_paul_day(tr("Peter und Paul"))

        # Corpus Christi.
        self._add_corpus_christi_day(tr("Fronleichnam"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        # Added via BGBl. Nr. 264/1967.
        if self._year >= 1967:
            # National Day.
            self._add_holiday_oct_26(tr("Nationalfeiertag"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Allerheiligen"))

        # Removed via StGBl. Nr. 116/1945.
        # Re-added via BGBl. Nr. 227/1955.
        if self._year <= 1944 or self._year >= 1955:
            # Immaculate Conception.
            self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

        # Christmas Day.
        self._add_christmas_day(tr("Christtag"))

        # Saint Stephen's Day.
        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_bank_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Karfreitag"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Heiliger Abend"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Silvester"))

    def _populate_protestant_holidays(self):
        # Added via BGBl. Nr. 228/1955.
        # Removed via BGBl. I Nr. 22/2019.
        if 1956 <= self._year <= 2018:
            # Good Friday.
            self._add_good_friday(tr("Karfreitag"))

    def _populate_subdiv_1_bank_holidays(self):
        # Saint Martin's Day.
        self._add_saint_martins_day(tr("Hl. Martin"))

    def _populate_subdiv_2_bank_holidays(self):
        # Saint Joseph's Day.
        self._add_saint_josephs_day(tr("Hl. Josef"))

        # 1920 Carinthian plebiscite.
        self._add_holiday_oct_10(tr("Tag der Volksabstimmung"))

    def _populate_subdiv_3_bank_holidays(self):
        # Saint Leopold's Day.
        self._add_holiday_nov_15(tr("Hl. Leopold"))

    def _populate_subdiv_4_bank_holidays(self):
        # Appointed as Saint of Upper Austrian via Provincial Government decision
        # on March 17th, 2004.
        if self._year >= 2004:
            # Saint Florian's Day.
            self._add_holiday_may_4(tr("Hl. Florian"))

    def _populate_subdiv_5_bank_holidays(self):
        # Saint Rupert's Day.
        self._add_holiday_sep_24(tr("Hl. Rupert"))

    def _populate_subdiv_6_bank_holidays(self):
        # Saint Joseph's Day.
        self._add_saint_josephs_day(tr("Hl. Josef"))

    def _populate_subdiv_7_bank_holidays(self):
        # Saint Joseph's Day.
        self._add_saint_josephs_day(tr("Hl. Josef"))

    def _populate_subdiv_8_bank_holidays(self):
        # Saint Joseph's Day.
        self._add_saint_josephs_day(tr("Hl. Josef"))

    def _populate_subdiv_9_bank_holidays(self):
        # Saint Leopold's Day.
        self._add_holiday_nov_15(tr("Hl. Leopold"))


class AT(Austria):
    pass


class AUT(Austria):
    pass
