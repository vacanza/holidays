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

from holidays.calendars.austria_school import (
    AUSTRIA_EARLY_SUMMER_BREAK_SUBDIVS,
    AUSTRIA_SCHOOL_HOLIDAYS_START_YEAR,
    AUSTRIA_SEMESTER_BREAK_WEEK_OVERRIDES,
    AUSTRIA_SEMESTER_BREAK_WEEKS,
    AUTUMN_BREAK,
    CHRISTMAS_BREAK,
    EASTER_BREAK,
    SEMESTER_BREAK,
    SUMMER_BREAK,
    WHIT_BREAK,
)
from holidays.calendars.gregorian import (
    JAN,
    FEB,
    JUN,
    JUL,
    SEP,
    OCT,
    DEC,
    MON,
    SAT,
    _timedelta,
    _get_nth_weekday_from,
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

    !!! note "School holidays"
        Austrian school holidays are set by federal law rather than published per year, so
        they are computed from § 2 Schulzeitgesetz 1985. They are subdivision-specific
        because the Semesterferien and the Hauptferien are staggered across the
        Bundesländer. See `holidays.calendars.austria_school` for the details.
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

    @staticmethod
    def _get_school_holiday_names() -> dict[int, str]:
        return {
            # Autumn Break.
            AUTUMN_BREAK: tr("Herbstferien"),
            # Christmas Break.
            CHRISTMAS_BREAK: tr("Weihnachtsferien"),
            # Semester Break.
            SEMESTER_BREAK: tr("Semesterferien"),
            # Easter Break.
            EASTER_BREAK: tr("Osterferien"),
            # Whit Break.
            WHIT_BREAK: tr("Pfingstferien"),
            # Summer Break.
            SUMMER_BREAK: tr("Hauptferien"),
        }

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
        if self.subdiv is None or self._year < AUSTRIA_SCHOOL_HOLIDAYS_START_YEAR:
            return None

        subdiv = self._normalized_subdiv
        school_holiday_names = self._get_school_holiday_names()
        christmas_break_name = school_holiday_names[CHRISTMAS_BREAK]

        # Jan 1 → Jan 6: the tail of the break that started in the previous year.
        self._add_multiday_holiday(date(self._year, JAN, 1), 6, name=christmas_break_name)

        # Monday through Saturday of the Bundesland's February week.
        semester_break_week = AUSTRIA_SEMESTER_BREAK_WEEK_OVERRIDES.get(self._year, {}).get(
            subdiv, AUSTRIA_SEMESTER_BREAK_WEEKS[subdiv]
        )
        self._add_multiday_holiday(
            _get_nth_weekday_of_month(semester_break_week, MON, FEB, self._year),
            6,
            name=school_holiday_names[SEMESTER_BREAK],
        )

        # Saturday before Palm Sunday → Easter Monday.
        easter_sunday = self._easter_sunday
        self._add_multiday_holiday(
            _timedelta(easter_sunday, -8), 10, name=school_holiday_names[EASTER_BREAK]
        )

        # Saturday before Pentecost → Pentecost Monday.
        self._add_multiday_holiday(
            _timedelta(easter_sunday, +48), 3, name=school_holiday_names[WHIT_BREAK]
        )

        # The 1st Saturday on or after Jun 28 (Jul 5 for the Bundesländer whose school year
        # starts a week later) → the day before the next school year starts, so 65 days.
        is_early = subdiv in AUSTRIA_EARLY_SUMMER_BREAK_SUBDIVS
        summer_break_start = _get_nth_weekday_from(
            1, SAT, date(self._year, JUN, 28) if is_early else date(self._year, JUL, 5)
        )
        self._add_multiday_holiday(
            summer_break_start,
            (
                _get_nth_weekday_of_month(1 if is_early else 2, MON, SEP, self._year)
                - summer_break_start
            ).days,
            name=school_holiday_names[SUMMER_BREAK],
        )

        # Oct 27 → Oct 31.
        self._add_multiday_holiday(
            date(self._year, OCT, 27), 5, name=school_holiday_names[AUTUMN_BREAK]
        )

        # Dec 24 (Dec 23 if that is a Monday) → Dec 31, with Jan 1 → Jan 6 added above as
        # part of the next year.
        christmas_break_start = date(self._year, DEC, 23)
        if not self._is_monday(christmas_break_start):
            christmas_break_start = _timedelta(christmas_break_start, +1)
        self._add_multiday_holiday(
            christmas_break_start,
            (date(self._year, DEC, 31) - christmas_break_start).days + 1,
            name=christmas_break_name,
        )

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
