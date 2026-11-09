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

from holidays.calendars.gregorian import JAN, DEC
from holidays.calendars.luxembourg_school import (
    ALL_SAINTS_BREAK,
    CARNIVAL_BREAK,
    CHRISTMAS_BREAK,
    EASTER_BREAK,
    LUXEMBOURG_SCHOOL_HOLIDAYS,
    PENTECOST_BREAK,
    SUMMER_BREAK,
)
from holidays.constants import BANK, PUBLIC, SCHOOL
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.helpers import tr
from holidays.holiday_base import HolidayBase


class Luxembourg(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Luxembourg holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Luxembourg>
        * <https://web.archive.org/web/20250625132138/https://www.bcl.lu/en/About/Opening-days/index.html>
        * School holidays:
            * [Règlement grand-ducal du 31 juillet 1980](https://web.archive.org/web/20260406050409/https://legilux.public.lu/eli/etat/leg/rgd/1980/07/31/n1/jo)
            * [Vacances et congés scolaires](https://web.archive.org/web/20260325100918/https://men.public.lu/fr/vacances-scolaires.html)
            * Calendars of each school year: see `holidays/calendars/luxembourg_school.py`.

    School holidays are available from the 1980/81 school year.
    """

    country = "LU"
    default_language = "lb"
    supported_categories = (BANK, PUBLIC, SCHOOL)
    supported_languages = ("de", "en_US", "fr", "lb", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    @staticmethod
    def _get_school_holiday_names() -> dict[int, str]:
        return {
            # All Saints' Break.
            ALL_SAINTS_BREAK: tr("Allerhellegevakanz"),
            # Christmas Break.
            CHRISTMAS_BREAK: tr("Chrëschtvakanz"),
            # Carnival Break.
            CARNIVAL_BREAK: tr("Fuesvakanz"),
            # Easter Break.
            EASTER_BREAK: tr("Ouschtervakanz"),
            # Pentecost Break.
            PENTECOST_BREAK: tr("Päischtvakanz"),
            # Summer Break.
            SUMMER_BREAK: tr("Summervakanz"),
        }

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Neijoerschdag"))

        # Easter Monday.
        self._add_easter_monday(tr("Ouschterméindeg"))

        # Labor Day.
        self._add_labor_day(tr("Dag vun der Aarbecht"))

        if self._year >= 2019:
            # Europe Day.
            self._add_europe_day(tr("Europadag"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Christi Himmelfaart"))

        # Pentecost Monday.
        self._add_pentecost_monday(tr("Péngschtméindeg"))

        # National Day.
        self._add_holiday_jun_23(tr("Nationalfeierdag"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Léiffrawëschdag"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Allerhellgen"))

        # Christmas Day.
        self._add_christmas_day(tr("Chrëschtdag"))

        # Saint Stephen's Day.
        self._add_christmas_day_two(tr("Stiefesdag"))

    def _populate_bank_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Karfreideg"))

        # Christmas Eve (afternoon).
        self._add_christmas_eve(tr("Hellegowend (nomëtteg)"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Silvester"))

    def _populate_school_holidays(self):
        school_holiday_names = self._get_school_holiday_names()
        for (
            start_year_offset,
            start_month,
            start_day,
            end_year_offset,
            end_month,
            end_day,
            holiday_id,
        ) in LUXEMBOURG_SCHOOL_HOLIDAYS.get(self._year, ()):
            name = school_holiday_names[holiday_id]
            start_date = date(self._year + start_year_offset, start_month, start_day)
            end_date = date(self._year + end_year_offset, end_month, end_day)
            active_start = max(start_date, date(self._year, JAN, 1))
            active_end = min(end_date, date(self._year, DEC, 31))
            self._add_holiday(name, active_start)
            self._add_multiday_holiday(active_start, (active_end - active_start).days, name=name)


class LU(Luxembourg):
    pass


class LUX(Luxembourg):
    pass
