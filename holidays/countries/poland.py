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
    JUN,
    AUG,
    NOV,
    DEC,
    FRI,
    _timedelta,
    _get_nth_weekday_from,
)
from holidays.calendars.poland_school import (
    CHRISTMAS_BREAK,
    EASTER_BREAK,
    POLAND_SCHOOL_HOLIDAY_SUBDIVS,
    POLAND_SCHOOL_HOLIDAYS_START_YEAR,
    POLAND_WINTER_BREAK_WEEKS,
    SUMMER_BREAK,
    WINTER_BREAK,
)
from holidays.constants import PUBLIC, SCHOOL
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.helpers import tr
from holidays.holiday_base import HolidayBase


class Poland(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Poland holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Poland>
        * <https://pl.wikipedia.org/wiki/Dni_wolne_od_pracy_w_Polsce>
        * <https://web.archive.org/web/20250402103635/https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20240001965>

    !!! note "School holidays"
        Public holidays are nationwide; the subdivisions exist for `SCHOOL` holidays, since
        the minister assigns each voivodeship its own two-week winter break. The other three
        breaks are the same across the country. See `holidays.calendars.poland_school`.
    """

    country = "PL"
    default_language = "pl"
    subdivisions = (
        # Voivodeships.
        "02",  # Dolnośląskie.
        "04",  # Kujawsko-pomorskie.
        "06",  # Lubelskie.
        "08",  # Lubuskie.
        "10",  # Łódzkie.
        "12",  # Małopolskie.
        "14",  # Mazowieckie.
        "16",  # Opolskie.
        "18",  # Podkarpackie.
        "20",  # Podlaskie.
        "22",  # Pomorskie.
        "24",  # Śląskie.
        "26",  # Świętokrzyskie.
        "28",  # Warmińsko-mazurskie.
        "30",  # Wielkopolskie.
        "32",  # Zachodniopomorskie.
    )
    subdivisions_aliases = {
        "Dolnośląskie": "02",
        "Kujawsko-pomorskie": "04",
        "Lubelskie": "06",
        "Lubuskie": "08",
        "Łódzkie": "10",
        "Małopolskie": "12",
        "Mazowieckie": "14",
        "Opolskie": "16",
        "Podkarpackie": "18",
        "Podlaskie": "20",
        "Pomorskie": "22",
        "Śląskie": "24",
        "Świętokrzyskie": "26",
        "Warmińsko-mazurskie": "28",
        "Wielkopolskie": "30",
        "Zachodniopomorskie": "32",
    }
    supported_categories = (PUBLIC, SCHOOL)
    supported_languages = ("de", "en_US", "pl", "uk")
    start_year = 1925

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(
            self, (PolandStaticHolidays, *kwargs.pop("static_holidays_classes", ()))
        )
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
            # Christmas Break.
            CHRISTMAS_BREAK: tr("Zimowa przerwa świąteczna"),
            # Winter Break.
            WINTER_BREAK: tr("Ferie zimowe"),
            # Easter Break.
            EASTER_BREAK: tr("Wiosenna przerwa świąteczna"),
            # Summer Break.
            SUMMER_BREAK: tr("Ferie letnie"),
        }

    @property
    def _classes_end_date(self) -> date:
        """Last day of classes, per § 2 ust. 1."""
        # The 1st Friday after Jun 20, moved back to the Wednesday when the Thursday in
        # between is a public holiday. Corpus Christi is the only one that can fall there,
        # and the clause was added on June 13th, 2019.
        classes_end = _get_nth_weekday_from(1, FRI, date(self._year, JUN, 21))
        return (
            _timedelta(classes_end, -2)
            if self._year >= 2019
            and _timedelta(classes_end, -1) == _timedelta(self._easter_sunday, +60)
            else classes_end
        )

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Nowy Rok"))

        if self._year <= 1960 or self._year >= 2011:
            # Epiphany.
            self._add_epiphany_day(tr("Święto Trzech Króli"))

        if self._year <= 1950:
            # Candlemas.
            self._add_candlemas(tr("Oczyszczenie Najświętszej Marii Panny"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Niedziela Wielkanocna"))

        # Easter Monday.
        self._add_easter_monday(tr("Poniedziałek Wielkanocny"))

        if self._year >= 1950:
            # National Day.
            self._add_holiday_may_1(tr("Święto Państwowe"))

        if self._year <= 1950 or self._year >= 1990:
            # National Day of the Third of May.
            self._add_holiday_may_3(tr("Święto Narodowe Trzeciego Maja"))

        if 1946 <= self._year <= 1950:
            # National Victory and Freedom Day.
            self._add_holiday_may_9(tr("Narodowe Święto Zwycięstwa i Wolności"))

        if self._year <= 1950:
            # Ascension Day.
            self._add_ascension_thursday(tr("Wniebowstąpienie Pańskie"))

        # Pentecost.
        self._add_pentecost(tr("Zielone Świątki"))

        if self._year <= 1950:
            # Pentecost Monday.
            self._add_pentecost_monday(tr("Drugi dzień Zielonych Świątek"))

        # Corpus Christi.
        self._add_corpus_christi_day(tr("Dzień Bożego Ciała"))

        if self._year <= 1950:
            self._add_saints_peter_and_paul_day(
                # Saints Peter and Paul Day.
                tr("Uroczystość Świętych Apostołów Piotra i Pawła")
            )

        if 1945 <= self._year <= 1989:
            # National Day of Rebirth of Poland.
            self._add_holiday_jul_22(tr("Narodowe Święto Odrodzenia Polski"))

        if self._year <= 1960 or self._year >= 1989:
            # Assumption Day.
            self._add_assumption_of_mary_day(tr("Wniebowzięcie Najświętszej Marii Panny"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Uroczystość Wszystkich Świętych"))

        if 1937 <= self._year <= 1944 or self._year >= 1989:
            # National Independence Day.
            self._add_holiday_nov_11(tr("Narodowe Święto Niepodległości"))

        if self._year <= 1950:
            self._add_immaculate_conception_day(
                # Immaculate Conception of the Blessed Virgin Mary.
                tr("Niepokalane Poczęcie Najświętszej Marii Panny")
            )

        if self._year >= 2025:
            # Christmas Eve.
            self._add_christmas_eve(tr("Wigilia Bożego Narodzenia"))

        # Christmas Day.
        self._add_christmas_day(tr("Boże Narodzenie (pierwszy dzień)"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Boże Narodzenie (drugi dzień)"))

    def _populate_school_holidays(self):
        if self.subdiv is None or self._year < POLAND_SCHOOL_HOLIDAYS_START_YEAR:
            return None

        school_holiday_names = self._get_school_holiday_names()

        # Two weeks from the Monday of the week assigned to the voivodeship. Announced only
        # about two years ahead, so later years have no winter break until the table grows.
        if winter_break_weeks := POLAND_WINTER_BREAK_WEEKS.get(self._year - 1):
            self._add_multiday_holiday(
                date.fromisocalendar(
                    self._year,
                    winter_break_weeks[
                        POLAND_SCHOOL_HOLIDAY_SUBDIVS.index(self._normalized_subdiv)
                    ],
                    1,
                ),
                14,
                name=school_holiday_names[WINTER_BREAK],
            )

        # Thursday before Easter → the Tuesday after it.
        self._add_multiday_holiday(
            _timedelta(self._easter_sunday, -3), 6, name=school_holiday_names[EASTER_BREAK]
        )

        # Day after classes end → Aug 31.
        summer_break_start = _timedelta(self._classes_end_date, +1)
        self._add_multiday_holiday(
            summer_break_start,
            (date(self._year, AUG, 31) - summer_break_start).days + 1,
            name=school_holiday_names[SUMMER_BREAK],
        )

        # Dec 23 (Dec 22 if that is a Monday) → Dec 31.
        christmas_break_start = date(self._year, DEC, 22)
        if not self._is_monday(christmas_break_start):
            christmas_break_start = _timedelta(christmas_break_start, +1)
        self._add_multiday_holiday(
            christmas_break_start,
            (date(self._year, DEC, 31) - christmas_break_start).days + 1,
            name=school_holiday_names[CHRISTMAS_BREAK],
        )


class PL(Poland):
    pass


class POL(Poland):
    pass


class PolandStaticHolidays:
    special_public_holidays = {
        # National Independence Day - 100th anniversary.
        2018: (NOV, 12, tr("Narodowe Święto Niepodległości - 100-lecie")),
    }
