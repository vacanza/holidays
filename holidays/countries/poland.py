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

from holidays.calendars.gregorian import JUN, AUG, NOV, DEC, FRI, _get_nth_weekday_from, _timedelta
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
        * School holidays:
            * [Dz.U. 2023 poz. 1211, consolidated text of the 2017 regulation](https://web.archive.org/web/20260109101730/https://api.sejm.gov.pl/eli/acts/DU/2023/1211/text.pdf)
            * [Dz.U. 2020 poz. 2111, § 11gd](https://web.archive.org/web/20260118090726/https://api.sejm.gov.pl/eli/acts/DU/2020/2111/text.pdf)
            * [Kalendarz roku szkolnego 2017/2018](https://web.archive.org/web/20250531154227/https://www.gov.pl/attachment/793fe87a-fa9e-426c-bcc0-27a8529f51c3)
            * [Kalendarz roku szkolnego 2018/2019](https://web.archive.org/web/20190407125813/https://www.gov.pl/web/edukacja/kalendarz-roku-szkolnego-20182019)
            * [Kalendarz roku szkolnego 2019/2020](https://web.archive.org/web/20260316182418/https://www.gov.pl/attachment/44e42d57-5ee7-4f7f-ac5d-2406b6a49bcc)
            * [Kalendarz roku szkolnego 2020/2021](https://web.archive.org/web/20260424042518/https://www.gov.pl/web/edukacja/kalendarz-roku-szkolnego-2020-21)
            * [Kalendarz roku szkolnego 2021/2022](https://web.archive.org/web/20260202143701/https://www.gov.pl/web/edukacja/kalendarz-roku-szkolnego-20212022)
            * [Kalendarz roku szkolnego 2022/2023](https://web.archive.org/web/20260217122839/https://www.gov.pl/web/edukacja/kalendarz-roku-szkolnego-20222023)
            * [Kalendarz roku szkolnego 2023/2024](https://web.archive.org/web/20250526112433/https://www.gov.pl/attachment/2fdb3ebb-2ce0-46d7-8190-4c6b2bf53762)
            * [Kalendarz roku szkolnego 2024/2025](https://web.archive.org/web/20250913005131/https://www.gov.pl/attachment/a208f13d-7752-45fa-a423-79658ad01ae1)
            * [Kalendarz roku szkolnego 2025/2026](https://web.archive.org/web/20260211011152/https://www.gov.pl/attachment/7112b88a-0237-4f83-b133-0d72c4ac83dc)
            * [Kalendarz roku szkolnego 2026/2027](https://web.archive.org/web/20261023091817/https://www.gov.pl/attachment/07b00367-6dbc-48bf-a69e-eaf1da41e3b2)
            * [Terminy ferii zimowych w roku szkolnym 2027/2028](https://web.archive.org/web/20261111124316/https://www.gov.pl/web/edukacja/terminy-ferii-zimowych-w-roku-szkolnym-20272028)

    !!! note "School holidays"
        Public holidays are nationwide; the subdivisions exist for `SCHOOL` holidays, which
        are supported from 2018 (the first full calendar year under the 2017 regulation).
        The Christmas, spring, and summer breaks are fixed by regulation across the country,
        while the minister assigns each voivodeship its own two-week winter break per year.
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

    # ISO week each voivodeship's two-week winter break opens in, ordered by `subdivisions`.
    winter_break_weeks = {
        2018: (3, 7, 5, 7, 5, 7, 3, 3, 5, 4, 5, 5, 7, 4, 7, 3),
        2019: (5, 3, 7, 3, 7, 3, 5, 5, 7, 4, 7, 7, 3, 4, 3, 5),
        2020: (7, 5, 3, 5, 3, 5, 7, 7, 3, 4, 3, 3, 5, 4, 5, 7),
        2021: (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        2022: (5, 3, 7, 3, 7, 3, 5, 5, 7, 4, 7, 7, 3, 4, 3, 5),
        2023: (7, 5, 3, 5, 3, 5, 7, 7, 3, 4, 3, 3, 5, 4, 5, 7),
        2024: (3, 7, 5, 7, 5, 7, 3, 3, 5, 4, 5, 5, 7, 4, 7, 3),
        2025: (6, 4, 8, 4, 8, 4, 6, 6, 8, 5, 8, 8, 4, 5, 4, 6),
        2026: (6, 6, 8, 8, 6, 6, 4, 6, 8, 4, 4, 8, 4, 4, 8, 6),
        2027: (3, 7, 5, 7, 3, 7, 5, 3, 3, 3, 5, 3, 5, 7, 7, 7),
        2028: (7, 3, 7, 3, 5, 7, 5, 7, 5, 3, 3, 7, 3, 5, 3, 3),
    }

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
        # 2018 is the first calendar year covered in full by the 2017 regulation.
        if self.subdiv is None or self._year < 2018:
            return None

        # Two weeks from the Monday of the week assigned to the voivodeship. Announced only
        # about two years ahead, so later years have no winter break until the table grows.
        if winter_break_weeks := self.winter_break_weeks.get(self._year):
            self._add_multiday_holiday(
                date.fromisocalendar(
                    self._year,
                    winter_break_weeks[self.subdivisions.index(self._normalized_subdiv)],
                    1,
                ),
                14,
                # Winter Break.
                name=tr("Ferie zimowe"),
            )

        # Thursday before Easter → the Tuesday after it.
        self._add_multiday_holiday(
            _timedelta(self._easter_sunday, -3),
            6,
            # Spring Break.
            name=tr("Wiosenna przerwa świąteczna"),
        )

        # § 2 ust. 1 & 1a: classes end on the 1st Friday after Jun 20, moved back to the
        # Wednesday when the Thursday in between is a public holiday (Corpus Christi, since 2019).
        classes_end = _get_nth_weekday_from(1, FRI, date(self._year, JUN, 21))
        if self._year >= 2019 and _timedelta(classes_end, -1) == _timedelta(
            self._easter_sunday, +60
        ):
            classes_end = _timedelta(classes_end, -2)
        summer_break_start = _timedelta(classes_end, +1)

        # § 2 ust. 1 & § 3 ust. 1 pkt 4: ends on Aug 31, or the 1st Sunday of September when
        # Sep 1 falls on a Friday, Saturday, or Sunday (so classes start on the following Monday).
        aug_31 = date(self._year, AUG, 31)
        summer_break_end = (
            _timedelta(aug_31, 6 - aug_31.weekday())
            if self._is_thursday(aug_31) or self._is_friday(aug_31) or self._is_saturday(aug_31)
            else aug_31
        )
        self._add_multiday_holiday(
            summer_break_start,
            (summer_break_end - summer_break_start).days + 1,
            # Summer Break.
            name=tr("Ferie letnie"),
        )

        # Dec 23 (Dec 22 if that is a Monday) → Dec 31.
        christmas_break_start = date(self._year, DEC, 22)
        if not self._is_monday(christmas_break_start):
            christmas_break_start = _timedelta(christmas_break_start, +1)
        self._add_multiday_holiday(
            christmas_break_start,
            (date(self._year, DEC, 31) - christmas_break_start).days + 1,
            # Christmas Break.
            name=tr("Zimowa przerwa świąteczna"),
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
