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

from datetime import date

from holidays.calendars.gregorian import (
    JAN,
    FEB,
    SEP,
    OCT,
    DEC,
    MON,
    _timedelta,
    _get_nth_weekday_of_month,
)
from holidays.constants import BANK, PROTESTANT, PUBLIC, SCHOOL
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.helpers import tr
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
        * School holidays:
            * [Schulzeitgesetz 1985, § 2](https://web.archive.org/web/20261022132837/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10009575)
            * [BGBl. I Nr. 49/2019, Ausschussbericht](https://web.archive.org/web/20250708135051/https://www.parlament.gv.at/dokument/XXVI/I/613/fname_751628.pdf)
            * [Schulferien 2021/2022](https://web.archive.org/web/20260313141155/https://www.bmb.gv.at/Themen/schule/schulpraxis/termine/ferientermine_21_22.html)
            * [Schulferien 2022/2023](https://web.archive.org/web/20260614032957/https://www.bmb.gv.at/Themen/schule/schulpraxis/termine/ferientermine_22_23.html)
            * [Schulferien 2023/2024](https://web.archive.org/web/20260607023018/https://www.bmb.gv.at/Themen/schule/schulpraxis/termine/ferientermine_23_24.html)
            * [Schulferien 2024/2025](https://web.archive.org/web/20260607020451/https://www.bmb.gv.at/Themen/schule/schulpraxis/termine/ferientermine_24_25.html)
            * [Schulferien 2025/2026](https://web.archive.org/web/20260710225417/https://www.bmb.gv.at/Themen/schule/schulpraxis/termine/ferientermine_25_26.html)
            * [Schulferien 2026/2027](https://web.archive.org/web/20260618083703/https://www.bmb.gv.at/Themen/schule/schulpraxis/termine/ferientermine_26_27.html)

    !!! note "School holidays"
        Austrian school holidays are set by federal law rather than published per year, so
        they are computed from § 2 Schulzeitgesetz 1985 starting in 2021 (the first calendar
        year that falls entirely under § 2 Abs. 4 as in effect since September 1st, 2020).
        They are subdivision-specific because the Semesterferien and the Hauptferien are
        staggered across the Bundesländer. Only the centrally set breaks are covered;
        school-specific autonomous days (`schulautonome Tage`) and opt-outs are not included.
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
    supported_categories = (BANK, PROTESTANT, PUBLIC, SCHOOL)
    supported_languages = ("de", "en_US", "th", "uk")

    # § 2 Abs. 2 Z 1 lit. b: the February week each Bundesland's Semesterferien starts in.
    semester_break_weeks = {
        "1": 2,  # Burgenland.
        "2": 2,  # Kärnten.
        "3": 1,  # Niederösterreich.
        "4": 3,  # Oberösterreich.
        "5": 2,  # Salzburg.
        "6": 3,  # Steiermark.
        "7": 2,  # Tirol.
        "8": 2,  # Vorarlberg.
        "9": 1,  # Wien.
    }

    # § 2 Abs. 2a moves, keyed by the calendar year the Semesterferien fall in.
    semester_break_week_overrides = {
        # BGBl. II Nr. 25/2021, § 8: Oberösterreich and Steiermark.
        2021: {"4": 2, "6": 2},
        # BGBl. II Nr. 487/2022: Vorarlberg.
        2024: {"8": 1},
        # BGBl. II Nr. 297/2025, Nr. 322/2025 and Nr. 343/2025: Vorarlberg, Tirol and Salzburg.
        2027: {"5": 3, "7": 3, "8": 3},
    }

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _add_multiday_holiday(
        self, start_date: date, duration_days: int, *, name: str | None = None
    ) -> set[date]:
        """Add a multi-day holiday starting from `start_date` (inclusive)."""
        return super()._add_multiday_holiday(
            _timedelta(start_date, -1), duration_days=duration_days, name=name
        )

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

        # Pentecost Monday.
        self._add_pentecost_monday(tr("Pfingstmontag"))

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

    def _populate_school_holidays(self):
        # 2021 is the first calendar year covered entirely by § 2 Abs. 4
        # as in effect since September 1st, 2020.
        if self.subdiv is None or self._year < 2021:
            return None

        subdiv = self._normalized_subdiv

        # Christmas Break.
        christmas_break_name = tr("Weihnachtsferien")

        # Jan 1 → Jan 6: the tail of the break that started in the previous year.
        self._add_multiday_holiday(date(self._year, JAN, 1), 6, name=christmas_break_name)

        # Dec 24 (Dec 23 if that is a Monday) → Dec 31.
        christmas_break_start = date(self._year, DEC, 24)
        if self._is_tuesday(christmas_break_start):
            christmas_break_start = _timedelta(christmas_break_start, -1)
        self._add_multiday_holiday(
            christmas_break_start,
            (date(self._year, DEC, 31) - christmas_break_start).days + 1,
            name=christmas_break_name,
        )

        # Monday through Saturday of the Bundesland's February week.
        semester_break_week = self.semester_break_week_overrides.get(self._year, {}).get(
            subdiv, self.semester_break_weeks[subdiv]
        )
        self._add_multiday_holiday(
            _get_nth_weekday_of_month(semester_break_week, MON, FEB, self._year),
            6,
            # Semester Break.
            name=tr("Semesterferien"),
        )

        # Saturday before Palm Sunday → Easter Monday.

        # Easter Break.
        self._add_multiday_holiday(_timedelta(self._easter_sunday, -8), 10, name=tr("Osterferien"))

        # Saturday before Pentecost → Pentecost Monday.
        self._add_multiday_holiday(
            _timedelta(self._easter_sunday, +48),
            3,
            # Whit Break.
            name=tr("Pfingstferien"),
        )

        # The 1st Saturday on or after Jul 5 → the day before the next school year starts,
        # so 65 days.
        # § 2 Abs. 1: the Bundesländer whose school year starts on the 1st Monday of September, so
        # that their Hauptferien both start and end a week before the other six (§ 2 Abs. 2 Z 2).
        classes_start = _get_nth_weekday_of_month(
            1 if subdiv in {"1", "3", "9"} else 2, MON, SEP, self._year
        )
        # Summer Break.
        self._add_multiday_holiday(_timedelta(classes_start, -65), 65, name=tr("Hauptferien"))

        # Oct 27 → Oct 31.

        # Autumn Break.
        self._add_multiday_holiday(date(self._year, OCT, 27), 5, name=tr("Herbstferien"))

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
