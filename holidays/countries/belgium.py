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
    MAR,
    APR,
    MAY,
    JUL,
    AUG,
    SEP,
    NOV,
    MON,
    FRI,
    _timedelta,
    _get_nth_weekday_from,
    _get_nth_weekday_of_month,
)
from holidays.constants import BANK, PUBLIC, SCHOOL
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.helpers import tr
from holidays.holiday_base import HolidayBase


class Belgium(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Belgium holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Belgium>
        * <https://web.archive.org/web/20250331001402/https://www.belgium.be/nl/over_belgie/land/belgie_in_een_notendop/feestdagen>
        * <https://nl.wikipedia.org/wiki/Feestdagen_in_België>
        * <https://web.archive.org/web/20240816004739/https://www.nbb.be/en/about-national-bank/national-bank-belgium/public-holidays>
        * Flemish Community school holidays:
            * [Besluit van de Vlaamse Regering van 17 april 1991, art. 4-5](https://codex.vlaanderen.be/Portals/Codex/documenten/1000373.html)
            * [Besluit van de Vlaamse Regering van 31 augustus 2001, art. 7](https://codex.vlaanderen.be/Portals/Codex/documenten/1008428.html)
            * [Schoolvakanties](https://www.vlaanderen.be/onderwijs-en-vorming/wat-mag-en-moet-op-school/schoolvakanties-vrije-dagen-en-afwezigheden/schoolvakanties)
        * French Community school holidays:
            * [Décret du 31 mars 2022 relatif à l'adaptation des rythmes scolaires annuels, art. 3-4](https://etaamb.openjustice.be/fr/decret-du-31-mars-2022_n2022040888)
            * [Calendriers scolaires 2009-2025](https://web.archive.org/web/20210205180850/http://www.enseignement.be/index.php?page=23953)
            * [Calendriers scolaires 2026-2029](https://web.archive.org/web/20260907033123/https://www.enseignement.be/calendrier-scolaire)
        * German-speaking Community school holidays:
            * [Schulkalender und Ferienregelung](https://ostbelgienbildung.be/desktopdefault.aspx/tabid-2212/4397_read-31727/)
            * [Osterferien im Jahr 2025 in der DG](https://ostbelgiendirekt.be/fg-schuljahr-2024-2025-394972)
            * [Feiertage und Schulferien 2026 in der DG](https://ostbelgiendirekt.be/feiertage-und-schulferien-2026-433031)
            * [Tag der Deutschsprachigen Gemeinschaft](https://de.wikipedia.org/wiki/Tag_der_Deutschsprachigen_Gemeinschaft)

    Subdivisions are the Communities in charge of education, used for `SCHOOL` holidays.
    """

    country = "BE"
    default_language = "nl"
    subdivisions = (
        "Flemish",  # Flemish Community.
        "French",  # French Community.
        "German",  # German-speaking Community.
    )
    supported_categories = (BANK, PUBLIC, SCHOOL)
    supported_languages = ("de", "en_US", "fr", "nl", "uk")

    # Labor Day.
    labor_day = tr("Dag van de Arbeid")

    # Ascension Day.
    ascension_day = tr("O. L. H. Hemelvaart")

    # Friday after Ascension Day.
    friday_after_ascension_day = tr("Vrijdag na O. L. H. Hemelvaart")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, BelgiumStaticHolidays)
        super().__init__(*args, **kwargs)

    def _add_multiday_holiday(
        self, start_date: date, duration_days: int, *, name: str | None = None
    ) -> set[date]:
        """Add a multi-day holiday starting from `start_date` (inclusive)."""
        return super()._add_multiday_holiday(
            _timedelta(start_date, -1), duration_days=duration_days, name=name
        )

    def _add_autumn_break(self, name):
        # Monday of the week of Nov 1 (Nov 2 if Nov 1 is on Sunday) → 1 week.
        nov_1 = date(self._year, NOV, 1)
        autumn_start = _get_nth_weekday_from(1 if self._is_sunday(nov_1) else -1, MON, nov_1)
        self._add_multiday_holiday(autumn_start, 7, name=name)

    def _add_christmas_break(self, name) -> date:
        # Monday of the week of Dec 25 (next Monday if Dec 25 is on weekend) → 2 weeks.
        christmas = self._christmas_day
        christmas_start = _get_nth_weekday_from(
            1 if self._is_weekend(christmas) else -1, MON, christmas
        )
        self._add_multiday_holiday(christmas_start, 32 - christmas_start.day, name=name)

        # January part of the previous year's break.
        new_year = date(self._year, JAN, 1)
        january_duration = (4 - new_year.weekday()) % 7 + 3
        self._add_multiday_holiday(new_year, january_duration, name=name)
        return _timedelta(new_year, january_duration - 1)

    def _add_carnival_break(self, name):
        # Carnival Monday (7th Monday before Easter) → 1 week.
        self._add_multiday_holiday(_timedelta(self._easter_sunday, -48), 7, name=name)

    def _add_easter_break(self, name):
        # 1st Monday of April → 2 weeks.
        # If Easter is in March: Easter Monday → 2 weeks.
        # If Easter is on or after Apr 15: 2nd Monday before Easter → until Easter Monday.
        easter_sunday = self._easter_sunday
        easter_start = _get_nth_weekday_of_month(1, MON, APR, self._year)
        easter_duration = 14
        if easter_sunday.month == MAR:
            easter_start = _timedelta(easter_sunday, +1)
        elif easter_sunday.day >= 15:
            easter_start = _timedelta(easter_sunday, -13)
            easter_duration = 15
        self._add_multiday_holiday(easter_start, easter_duration, name=name)

    def _add_summer_break(self, name):
        # Jul 1 → Aug 31.
        self._add_multiday_holiday(date(self._year, JUL, 1), 62, name=name)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Nieuwjaar"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Pasen"))

        # Easter Monday.
        self._add_easter_monday(tr("Paasmaandag"))

        # Labor Day.
        self._add_labor_day(self.labor_day)

        # Ascension Day.
        self._add_ascension_thursday(self.ascension_day)

        # Pentecost.
        self._add_pentecost(tr("Pinksteren"))

        # Pentecost Monday.
        self._add_pentecost_monday(tr("Pinkstermaandag"))

        # National Day.
        self._add_holiday_jul_21(tr("Nationale feestdag"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("O. L. V. Hemelvaart"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Allerheiligen"))

        # Armistice Day.
        self._add_remembrance_day(tr("Wapenstilstand"))

        # Christmas Day.
        self._add_christmas_day(tr("Kerstmis"))

    def _populate_bank_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Goede vrijdag"))

        # Friday after Ascension Day.
        self._add_holiday_40_days_past_easter(self.friday_after_ascension_day)

        # Bank Holiday.
        self._add_christmas_day_two(tr("Banksluitingsdag"))

    def _populate_subdiv_flemish_school_holidays(self):
        if self._year <= 2009:
            return

        # Christmas Break.
        self._add_christmas_break(tr("Kerstvakantie"))

        # Carnival Break.
        self._add_carnival_break(tr("Krokusvakantie"))

        # Easter Break.
        self._add_easter_break(tr("Paasvakantie"))

        # Labor Day.
        self._add_labor_day(self.labor_day)

        # Ascension Day.
        self._add_ascension_thursday(self.ascension_day)

        # Friday after Ascension Day.
        self._add_holiday_40_days_past_easter(self.friday_after_ascension_day)

        # Pentecost Monday.
        self._add_pentecost_monday(tr("Pinkstermaandag"))

        # Summer Break.
        self._add_summer_break(tr("Zomervakantie"))

        # Autumn Break.
        self._add_autumn_break(tr("Herfstvakantie"))

        # Armistice Day.
        self._add_remembrance_day(tr("Wapenstilstand"))

    def _populate_subdiv_french_school_holidays(self):
        if self._year <= 2009:
            return

        # The same rules as in other communities applied until the 2021-2022 school year.
        # Since 2022-2023 the school year starts on the last Monday of August, ends on the first
        # Friday of July and alternates 7 (or 8) weeks of classes with 2 weeks of break.

        # Christmas Break.
        christmas_break_end = self._add_christmas_break(tr("Kerstvakantie"))

        if self._year >= 2023:
            # 8th Monday after the Christmas Break → 2 weeks.
            # 7th Monday after the Christmas Break instead if that is Carnival Monday.
            carnival_start = _timedelta(christmas_break_end, +50)
            carnival_monday = _timedelta(self._easter_sunday, -48)
            if carnival_monday == _timedelta(carnival_start, -7):
                carnival_start = carnival_monday
            # Carnival Break.
            self._add_multiday_holiday(carnival_start, 14, name=tr("Krokusvakantie"))

            # Monday of the week of May 1 → 2 weeks.
            spring_start = _get_nth_weekday_from(-1, MON, date(self._year, MAY, 1))
            # Easter Break.
            self._add_multiday_holiday(spring_start, 14, name=tr("Paasvakantie"))

            # Easter Monday.
            self._add_easter_monday(tr("Paasmaandag"))

            # Only if the school year (185 class days before deductions) still has at least
            # 180 class days once the individual days off and Mardi Gras itself are deducted.
            easter_sunday = self._easter_sunday
            spring_end = _timedelta(spring_start, +13)
            days_off = (
                date(self._year - 1, SEP, 27),
                date(self._year - 1, NOV, 11),
                _timedelta(easter_sunday, +1),
                _timedelta(easter_sunday, +39),
                _timedelta(easter_sunday, +50),
            )
            days_off_count = sum(
                not self._is_weekend(dt) and not spring_start <= dt <= spring_end
                for dt in days_off
            ) + self._is_sunday(date(self._year - 1, NOV, 1))
            mardi_gras = _timedelta(easter_sunday, -47)
            if days_off_count <= 4 and not carnival_start <= mardi_gras <= _timedelta(
                carnival_start, +13
            ):
                # Mardi Gras.
                self._add_carnival_tuesday(tr("Vastenavond"))
        else:
            # Carnival Break.
            self._add_carnival_break(tr("Krokusvakantie"))

            # Easter Break.
            self._add_easter_break(tr("Paasvakantie"))

            # Labor Day.
            self._add_labor_day(self.labor_day)

        # Ascension Day.
        self._add_ascension_thursday(self.ascension_day)

        # Pentecost Monday.
        self._add_pentecost_monday(tr("Pinkstermaandag"))

        # Jul 1 (since 2023: day after the 1st Friday of July) → Aug 31 (since 2022: day before
        # the school year start, i.e. 44 weeks and 5 days before the next 1st Friday of July).
        summer_start = (
            _timedelta(_get_nth_weekday_of_month(1, FRI, JUL, self._year), +1)
            if self._year >= 2023
            else date(self._year, JUL, 1)
        )
        summer_end = (
            _timedelta(_get_nth_weekday_of_month(1, FRI, JUL, self._year + 1), -313)
            if self._year >= 2022
            else date(self._year, AUG, 31)
        )
        # Summer Break.
        self._add_multiday_holiday(
            summer_start, (summer_end - summer_start).days + 1, name=tr("Zomervakantie")
        )

        # French Community Day.
        self._add_holiday_sep_27(tr("Feestdag van de Franse Gemeenschap"))

        if self._year >= 2022:
            # 2nd Monday before the week of Nov 1 → 2 weeks.
            nov_1 = date(self._year, NOV, 1)
            # Autumn Break.
            self._add_multiday_holiday(
                _get_nth_weekday_from(-2, MON, nov_1), 14, name=tr("Herfstvakantie")
            )

            if self._is_sunday(nov_1):
                # All Souls' Day.
                self._add_all_souls_day(tr("Allerzielen"))
        else:
            # Autumn Break.
            self._add_autumn_break(tr("Herfstvakantie"))

        # Armistice Day.
        self._add_remembrance_day(tr("Wapenstilstand"))

    def _populate_subdiv_german_school_holidays(self):
        if self._year <= 2009:
            return

        # Christmas Break.
        self._add_christmas_break(tr("Kerstvakantie"))

        # Carnival Break.
        self._add_carnival_break(tr("Krokusvakantie"))

        # Easter Break.
        name = tr("Paasvakantie")
        if self._year >= 2025:
            # Easter Monday → 2 weeks.
            self._add_multiday_holiday(_timedelta(self._easter_sunday, +1), 14, name=name)
        else:
            self._add_easter_break(name)

        # Labor Day.
        self._add_labor_day(self.labor_day)

        # Ascension Day.
        self._add_ascension_thursday(self.ascension_day)

        # Pentecost Monday.
        self._add_pentecost_monday(tr("Pinkstermaandag"))

        # Summer Break.
        self._add_summer_break(tr("Zomervakantie"))

        # Autumn Break.
        self._add_autumn_break(tr("Herfstvakantie"))

        # Armistice Day.
        self._add_remembrance_day(tr("Wapenstilstand"))

        # German-speaking Community Day.
        self._add_holiday_nov_15(tr("Feestdag van de Duitstalige Gemeenschap"))


class BE(Belgium):
    pass


class BEL(Belgium):
    pass


class BelgiumStaticHolidays:
    """Belgium special holidays.

    References:
        * [Calendriers scolaires 2014-2015 à 2020-2021](https://web.archive.org/web/20210205180850/http://www.enseignement.be/index.php?page=23953)
    """

    # Bridge Holiday.
    bridge_holiday = tr("Brugdag")

    friday_after_ascension_day = Belgium.friday_after_ascension_day

    special_french_school_holidays = {
        2015: (MAY, 15, friday_after_ascension_day),
        2016: (
            (MAY, 4, bridge_holiday),
            (MAY, 6, friday_after_ascension_day),
        ),
        2020: (MAY, 22, friday_after_ascension_day),
        2021: (
            (APR, 30, bridge_holiday),
            (MAY, 14, friday_after_ascension_day),
        ),
    }
