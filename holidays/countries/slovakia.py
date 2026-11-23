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
    JUN,
    SEP,
    OCT,
    NOV,
    DEC,
    MON,
    FRI,
    _get_nth_weekday_from,
    _get_nth_weekday_of_month,
    _timedelta,
)
from holidays.constants import PUBLIC, SCHOOL, WORKDAY
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.helpers import tr
from holidays.holiday_base import HolidayBase


class Slovakia(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Slovakia holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Slovakia>
        * <https://sk.wikipedia.org/wiki/Zoznam_sviatkov_na_Slovensku>
        * <https://web.archive.org/web/20250413192257/https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/1993/241/>
        * [Law 326/2020](https://web.archive.org/web/20250713005858/https://static.slov-lex.sk/static/SK/ZZ/2020/326/20210101.html)
        * [Law 530/2023](https://web.archive.org/web/20250424165411/https://static.slov-lex.sk/static/SK/ZZ/2023/530/20240101.html)
        * [Law 261/2025](https://web.archive.org/web/20251014224441/https://static.slov-lex.sk/static/SK/ZZ/2025/261/20251101.html)
        * School holidays:
            * [Decree 231/2009 Z. z.](https://web.archive.org/web/20261122140651/https://static.slov-lex.sk/static/SK/ZZ/2009/231/20250401.html)
            * [Ministerial Decision 2020/17949:1-A1810](https://web.archive.org/web/20210124070207/https://www.minedu.sk/data/att/17786.pdf)
            * [Ministerial Decision 2020/18259:4-A1810](https://web.archive.org/web/20210124070556/https://www.minedu.sk/data/att/18150.pdf)
            * [Decree 163/2022 Z. z.](https://web.archive.org/web/20261122140659/https://static.slov-lex.sk/static/SK/ZZ/2022/163/20220530.html)
            * [Decree 72/2024 Z. z.](https://web.archive.org/web/20261122140702/https://static.slov-lex.sk/static/SK/ZZ/2024/72/20240501.html)
            * [Decree 56/2025 Z. z.](https://web.archive.org/web/20261122140710/https://static.slov-lex.sk/static/SK/ZZ/2025/56/20250401.html)
            * [Termíny prázdnin (MŠVVaM SR)](https://web.archive.org/web/20260712091851/https://www.minedu.sk/terminy-prazdnin/)
            * [Termíny prázdnin 2023/2024-2025/2026](https://web.archive.org/web/20261122140716/https://www.minedu.sk/data/att/79d/30348.9978ac.pdf)
            * [Termíny prázdnin 2024/2025-2026/2027](https://web.archive.org/web/20260325072009/https://www.minedu.sk/data/att/698/31010.60eac0.pdf)
            * [Termíny prázdnin 2026/2027-2027/2028](https://web.archive.org/web/20261122140723/https://www.minedu.sk/data/att/c3e/35639.e4736d.pdf)

    !!! note "School holidays"
        Slovak school holidays are regulated by Decree 231/2009 Z. z. (§ 2 and § 3) and
        published by the Ministry of Education from 2014 (the first full calendar year covered
        by the ministry's archived schedules). Public holidays are nationwide; subdivisions
        are the eight regions (*kraje*) used for `SCHOOL` holidays, as the one-week Spring Break
        (*Jarné prázdniny*) rotates across three regional groups (Central: `BC`, `TC`, `ZI`;
        East: `KI`, `PV`; West: `BL`, `NI`, `TA`). Per § 150(2) of Act 245/2008 Z. z., school
        holidays do not apply to kindergartens (*materské školy*), and school-specific days off
        granted by principals (*riaditeľské voľno*) are not included.
    """

    country = "SK"
    default_language = "sk"
    subdivisions = (
        "BC",  # Banskobystrický kraj.
        "BL",  # Bratislavský kraj.
        "KI",  # Košický kraj.
        "NI",  # Nitriansky kraj.
        "PV",  # Prešovský kraj.
        "TA",  # Trnavský kraj.
        "TC",  # Trenčiansky kraj.
        "ZI",  # Žilinský kraj.
    )
    subdivisions_aliases = {
        "Banskobystrický kraj": "BC",
        "BB": "BC",
        "Bratislavský kraj": "BL",
        "BA": "BL",
        "Košický kraj": "KI",
        "KE": "KI",
        "Nitriansky kraj": "NI",
        "NR": "NI",
        "Prešovský kraj": "PV",
        "PO": "PV",
        "Trnavský kraj": "TA",
        "TT": "TA",
        "Trenčiansky kraj": "TC",
        "TN": "TC",
        "Žilinský kraj": "ZI",
        "ZA": "ZI",
    }
    supported_categories = (PUBLIC, SCHOOL, WORKDAY)
    supported_languages = ("en_US", "sk", "uk")
    # Independent Slovak Republic established on Jan 01, 1993.
    start_year = 1993

    # Regional groups for the 3-week rotation of Jarné prázdniny (0: Central, 1: East, 2: West).
    spring_break_subdiv_groups = {
        "BC": 0,
        "BL": 2,
        "KI": 1,
        "NI": 2,
        "PV": 1,
        "TA": 2,
        "TC": 0,
        "ZI": 0,
    }

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=SlovakiaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _add_multiday_holiday(
        self, start_date: date, duration_days: int, *, name: str | None = None
    ) -> set[date]:
        """Add a multi-day holiday starting from `start_date` (inclusive)."""
        return super()._add_multiday_holiday(
            _timedelta(start_date, -1), duration_days=duration_days, name=name
        )

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

        if self._year >= 1997 and self._year != 2026:
            # Day of Victory over Fascism.
            self._add_world_war_two_victory_day(tr("Deň víťazstva nad fašizmom"))

        # Saints Cyril and Methodius Day.
        self._add_holiday_jul_5(tr("Sviatok svätého Cyrila a svätého Metoda"))

        # Slovak National Uprising Anniversary.
        self._add_holiday_aug_29(tr("Výročie Slovenského národného povstania"))

        if self._year <= 2023:
            # Constitution Day.
            self._add_holiday_sep_1(tr("Deň Ústavy Slovenskej republiky"))

        if self._year != 2026:
            # Day of Our Lady of the Seven Sorrows.
            self._add_holiday_sep_15(tr("Sedembolestná Panna Mária"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Sviatok Všetkých svätých"))

        if 2001 <= self._year <= 2024:
            # Struggle for Freedom and Democracy Day.
            self._add_holiday_nov_17(tr("Deň boja za slobodu a demokraciu"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Štedrý deň"))

        # Christmas Day.
        self._add_christmas_day(tr("Prvý sviatok vianočný"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Druhý sviatok vianočný"))

    def _populate_workday_holidays(self):
        # According to Law 241/1993, these state holidays are not non-working days.

        # Law 261/2025.
        if self._year == 2026:
            # Day of Victory over Fascism.
            self._add_world_war_two_victory_day(tr("Deň víťazstva nad fašizmom"))

            # Day of Our Lady of the Seven Sorrows.
            self._add_holiday_sep_15(tr("Sedembolestná Panna Mária"))

        # Law 530/2023.
        if self._year >= 2024:
            # Constitution Day.
            self._add_holiday_sep_1(tr("Deň Ústavy Slovenskej republiky"))

        # Law 326/2020.
        if self._year >= 2021:
            # Day of the Establishment of the Independent Czech-Slovak State.
            self._add_holiday_oct_28(tr("Deň vzniku samostatného česko-slovenského štátu"))

        # Law 261/2025.
        if self._year >= 2025:
            # Struggle for Freedom and Democracy Day.
            self._add_holiday_nov_17(tr("Deň boja za slobodu a demokraciu"))

    def _populate_school_holidays(self):
        # 2014 is the first full calendar year covered by the archived MŠVVaM SR schedules.
        if self.subdiv is None or self._year <= 2013:
            return None

        # Christmas Break.
        christmas_break_name = tr("Vianočné prázdniny")

        # § 3(3): Jan 1 → Jan 7 (the tail of the break that started in the previous year).
        self._add_multiday_holiday(date(self._year, JAN, 1), 7, name=christmas_break_name)

        # § 3(3): Dec 23 (Dec 22 when Dec 23 is a Tuesday) → Dec 31.
        christmas_break_start = date(self._year, DEC, 23)
        if self._is_tuesday(christmas_break_start):
            christmas_break_start = _timedelta(christmas_break_start, -1)
        self._add_multiday_holiday(
            christmas_break_start,
            (date(self._year, DEC, 31) - christmas_break_start).days + 1,
            name=christmas_break_name,
        )

        # § 3(4): Half-Year Break on the closest Friday or Monday after Jan 31.
        # Cancelled in 2021 by Ministerial Decision 2020/18259:4-A1810 of Dec 11, 2020.
        # Abolished for 2022/2023-2024/2025 via Decree 163/2022 Z. z.
        # Reinstated from 2025/2026 via Decree 56/2025 Z. z.
        if self._year not in {2021, 2023, 2024, 2025}:
            feb_1 = date(self._year, FEB, 1)
            self._add_holiday(
                # Half-Year Break.
                tr("Polročné prázdniny"),
                _get_nth_weekday_from(
                    1, MON if self._is_monday(feb_1) or self._is_weekend(feb_1) else FRI, feb_1
                ),
            )

        # § 3(5): One-week Spring Break (Mon-Fri) starting from the 3rd Monday of February,
        # rotating across the three regional groups in a 3-year cycle from 2015 onwards.
        group = self.spring_break_subdiv_groups[self._normalized_subdiv]
        week_offset = (0, 2, 1)[group] if self._year == 2014 else (group + 2015 - self._year) % 3
        self._add_multiday_holiday(
            _timedelta(_get_nth_weekday_of_month(3, MON, FEB, self._year), 7 * week_offset),
            5,
            # Spring Break.
            name=tr("Jarné prázdniny"),
        )

        # § 3(6): Thursday before Easter → Tuesday after Easter.
        self._add_multiday_holiday(
            _timedelta(self._easter_sunday, -3),
            6,
            # Easter Break.
            name=tr("Veľkonočné prázdniny"),
        )

        # § 2(1)-(2) & § 3(7): classes end on Jun 30 (preceding Friday when Jun 30 is Sat-Mon);
        # classes start on Sep 1 (following Monday when Sep 1 is Fri-Sun).
        # Before Decree 72/2024 Z. z., classes started on Sep 2 under the same rule.
        classes_end = date(self._year, JUN, 30)
        if self._is_weekend(classes_end) or self._is_monday(classes_end):
            classes_end = _get_nth_weekday_from(-1, FRI, classes_end)
        classes_start = date(self._year, SEP, 1 if self._year >= 2024 else 2)
        if self._is_friday(classes_start) or self._is_weekend(classes_start):
            classes_start = _get_nth_weekday_from(1, MON, classes_start)

        self._add_multiday_holiday(
            _timedelta(classes_end, +1),
            (classes_start - classes_end).days - 1,
            # Summer Break.
            name=tr("Letné prázdniny"),
        )

        # Autumn Break.
        autumn_break_name = tr("Jesenné prázdniny")
        if self._year == 2020:
            # Shifted by Ministerial Decision 2020/17949:1-A1810 of Oct 23, 2020.
            self._add_holiday_oct_30(autumn_break_name)
            self._add_holiday_nov_2(autumn_break_name)
            self._add_holiday_nov_6(autumn_break_name)
            self._add_holiday_nov_9(autumn_break_name)
        else:
            nov_1 = date(self._year, NOV, 1)
            if self._is_thursday(nov_1):
                # Wed and Fri around All Saints' Day.
                first_day = _timedelta(nov_1, -1)
                last_day = _timedelta(nov_1, +1)
            else:
                # The two working days right before All Saints' Day.
                first_day = self.get_nth_working_day(nov_1, -2)
                last_day = self.get_nth_working_day(nov_1, -1)
            self._add_multiday_holiday(
                first_day, (last_day - first_day).days + 1, name=autumn_break_name
            )


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
