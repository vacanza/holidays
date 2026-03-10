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
from gettext import gettext as tr

from holidays.calendars.gregorian import (
    APR,
    AUG,
    JAN,
    JUL,
    JUN,
    SEP,
    OCT,
    NOV,
    DEC,
    MON,
    SAT,
    _timedelta,
    _get_nth_weekday_from,
    _get_nth_weekday_of_month,
)
from holidays.constants import BANK, PUBLIC, SCHOOL
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Belgium(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Belgium holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Belgium>
        * <https://web.archive.org/web/20250331001402/https://www.belgium.be/nl/over_belgie/land/belgie_in_een_notendop/feestdagen>
        * <https://nl.wikipedia.org/wiki/Feestdagen_in_België>
        * <https://web.archive.org/web/20240816004739/https://www.nbb.be/en/about-national-bank/national-bank-belgium/public-holidays>
        * Official education calendars:
            - [Flemish Community (Vlaanderen)](https://www.vlaanderen.be/onderwijs-en-vorming/wat-mag-en-moet-op-school/schoolvakanties-vrije-dagen-en-afwezigheden/schoolvakanties)
            - [French Community (Fédération Wallonie-Bruxelles)](http://www.enseignement.be/index.php?page=23953)
            - [German-speaking Community (Deutschsprachige Gemeinschaft)](https://ostbelgienbildung.be/desktopdefault.aspx/tabid-2212/4397_read-31727/)

    Notes:
        * Belgium has three school systems with different vacation rules:
            - VLG: Flemish Community
            - WBR: French Community (Wallonia + Brussels French schools)
            - GER: German-speaking Community (Ostbelgien)
        * School holiday rules are based on official education calendars.
    """

    country = "BE"
    default_language = "nl"
    supported_categories = (BANK, PUBLIC, SCHOOL)
    supported_languages = ("de", "en_US", "fr", "nl", "uk")

    subdivisions = (
        "VLG",  # Flemish Community.
        "WBR",  # French Community (Wallonia + Brussels French schools)
        "GER",  # German-speaking Community.
    )

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Nieuwjaar"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Pasen"))

        # Easter Monday.
        self._add_easter_monday(tr("Paasmaandag"))

        # Labor Day.
        self._add_labor_day(tr("Dag van de Arbeid"))

        # Ascension Day.
        self._add_ascension_thursday(tr("O. L. H. Hemelvaart"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Pinksteren"))

        # Whit Monday.
        self._add_whit_monday(tr("Pinkstermaandag"))

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
        self._add_good_friday(tr("Goede Vrijdag"))

        # Friday after Ascension Day.
        self._add_holiday_40_days_past_easter(tr("Vrijdag na O. L. H. Hemelvaart"))

        # Bank Holiday.
        self._add_christmas_day_two(tr("Banksluitingsdag"))

    def _add_multiday_holiday(
        self, start_date: date, duration_days: int, *, name: str | None = None
    ) -> set[date]:
        """Override to start adding holidays directly from start_date."""
        return super()._add_multiday_holiday(
            _timedelta(start_date, -1),
            duration_days=duration_days,
            name=name,
        )

    def _populate_subdiv_vlg_school_holidays(self):
        """
        School holidays for the Flemish Community (Vlaamse Gemeenschap).

        Most vacation periods are rule-based and can be calculated
        algorithmically, therefore they are implemented here.
        """
        year = self._year
        easter = self._easter_sunday

        # Christmas holidays.
        name = tr("Kerstvakantie")
        christmas = self._christmas_day
        christmas_start = _get_nth_weekday_from(
            1 if self._is_weekend(christmas) else -1, MON, christmas
        )

        self._add_multiday_holiday(christmas_start, 32 - christmas_start.day, name=name)

        # Previous year's Christmas (for January spillover).
        prev_christmas = self._christmas_day.replace(year=self._year - 1)
        prev_christmas_start = _get_nth_weekday_from(
            1 if self._is_weekend(prev_christmas) else -1,
            MON,
            prev_christmas,
        )
        duration = 14 - (32 - prev_christmas_start.day)
        self._add_multiday_holiday(date(self._year, JAN, 1), duration, name=name)

        # Carnival holidays.
        carnival_raw = _timedelta(easter, days=-47)
        carnival_start = _get_nth_weekday_from(-1, MON, carnival_raw)
        self._add_multiday_holiday(carnival_start, 7, name=tr("Krokusvakantie"))

        # Easter holidays.
        # - March Easter → week before Easter.
        # - Easter after 15 April → second Monday before Easter.
        # - Otherwise → first Monday of April.
        easter_start = _get_nth_weekday_of_month(1, MON, APR, self._year)
        easter_duration = 14

        if easter.month == 3:
            easter_start = _timedelta(easter, -6)
        elif easter.day >= 16:
            easter_start = _timedelta(easter, -13)
            easter_duration = 15
        self._add_multiday_holiday(easter_start, easter_duration, name=tr("Paasvakantie"))

        # Labor Day.
        self._add_labor_day(tr("Dag van de Arbeid"))

        # Ascension Day.
        self._add_ascension_thursday(tr("O. L. H. Hemelvaart"))

        # Friday after Ascension.
        self._add_holiday_40_days_past_easter(tr("Vrijdag na O. L. H. Hemelvaart"))

        # Whit Monday.
        self._add_whit_monday(tr("Pinkstermaandag"))

        # Summer holidays.
        self._add_multiday_holiday(date(year, JUL, 1), 62, name=tr("Zomervakantie"))

        # Autumn holidays.
        nov_1 = date(year, NOV, 1)
        autumn_start = _get_nth_weekday_from(1 if self._is_sunday(nov_1) else -1, MON, nov_1)
        self._add_multiday_holiday(autumn_start, 7, name=tr("Herfstvakantie"))

        # Armistice Day.
        self._add_remembrance_day(tr("Wapenstilstand"))

    def _populate_subdiv_wbr_school_holidays(self):
        """
        School holidays for the French Community (Wallonie-Bruxelles).
        Based on the official compulsory education calendar.
        """
        year = self._year
        easter = self._easter_sunday

        # Autumn holidays.
        autumn_start = _get_nth_weekday_of_month(3, MON, OCT, year)
        self._add_multiday_holiday(autumn_start, 14, name=tr("Herfstvakantie"))

        # current year's Christmas.
        christmas = self._christmas_day
        name = tr("Kerstvakantie")
        christmas_start = _get_nth_weekday_from(
            1 if self._is_weekend(christmas) else -1, MON, christmas
        )
        self._add_multiday_holiday(christmas_start, 32 - christmas_start.day, name=name)

        # Previous year's Christmas (for January spillover).
        prev_christmas = self._christmas_day.replace(year=self._year - 1)
        prev_christmas_start = _get_nth_weekday_from(
            1 if self._is_weekend(prev_christmas) else -1,
            MON,
            prev_christmas,
        )
        duration = 14 - (32 - prev_christmas_start.day)
        self._add_multiday_holiday(date(self._year, JAN, 1), duration, name=name)

        # Carnival holidays.
        carnival_raw = _timedelta(easter, days=-49)
        carnival_start = _get_nth_weekday_from(1, MON, carnival_raw)
        self._add_multiday_holiday(carnival_start, 14, name=tr("Krokusvakantie"))

        # Spring Holidays.
        spring_start = _get_nth_weekday_of_month(4, MON, APR, year)
        self._add_multiday_holiday(spring_start, 14, name=tr("Paasvakantie"))

        # Summer holidays.
        summer_start = _get_nth_weekday_of_month(1, SAT, JUL, year)
        summer_end = _get_nth_weekday_of_month(4, MON, AUG, year)
        duration = (summer_end - summer_start).days
        self._add_multiday_holiday(summer_start, duration, name=tr("Zomervakantie"))

        # Armistice Day.
        self._add_remembrance_day(tr("Wapenstilstand"))

        # Labour Day.
        self._add_labor_day(tr("Dag van de Arbeid"))

        # French Community Day.
        self._add_holiday(tr("Feestdag van de Franse Gemeenschap"), date(year, SEP, 27))

        # Easter Monday.
        self._add_easter_monday(tr("Paasmaandag"))

        # Ascension Day.
        self._add_ascension_thursday(tr("O. L. H. Hemelvaart"))

        # Whit Monday.
        self._add_whit_monday(tr("Pinkstermaandag"))

    def _populate_subdiv_ger_school_holidays(self):
        """
        School holidays for the German-speaking Community (Deutschsprachige Gemeinschaft).

        Based on official education calendar structure.
        Most vacation periods follow the same framework as other Belgian communities,
        with Easter holidays starting on the Monday after Easter.
        """
        year = self._year
        easter = self._easter_sunday

        # Christmas holidays.
        christmas = self._christmas_day
        name = tr("Kerstvakantie")

        # if Christmas is on Monday, holiday will start that day.
        # if Christmas is on Tue-Fri, start the previous Monday.
        # if Christmas is a Sat/Sun, start the following Monday.
        christmas_start = _get_nth_weekday_from(
            1 if self._is_weekend(christmas) else -1, MON, christmas
        )
        self._add_multiday_holiday(christmas_start, 32 - christmas_start.day, name=name)

        # Previous year's Christmas (for January spillover).
        prev_christmas = self._christmas_day.replace(year=self._year - 1)
        prev_christmas_start = _get_nth_weekday_from(
            1 if self._is_weekend(prev_christmas) else -1,
            MON,
            prev_christmas,
        )
        duration = 14 - (32 - prev_christmas_start.day)
        self._add_multiday_holiday(date(self._year, JAN, 1), duration, name=name)

        # Carnival holidays.
        carnival_raw = _timedelta(easter, days=-47)
        carnival_start = _get_nth_weekday_from(-1, MON, carnival_raw)
        self._add_multiday_holiday(carnival_start, 6, name=tr("Krokusvakantie"))

        # Easter holidays.
        # Starts on the Monday after Easter.
        easter_start = _timedelta(easter, 1)
        self._add_multiday_holiday(easter_start, 13, name=tr("Paasvakantie"))

        # Summer holidays.
        self._add_multiday_holiday(date(self._year, JUN, 30), 63, name=tr("Zomervakantie"))

        # Autumn holidays.
        nov_1 = date(year, NOV, 1)
        autumn_start = _get_nth_weekday_from(1 if self._is_sunday(nov_1) else -1, MON, nov_1)
        self._add_multiday_holiday(autumn_start, 6, name=tr("Herfstvakantie"))

        # Armistice Day.
        self._add_remembrance_day(tr("Wapenstilstand"))

        # Labour Day.
        self._add_labor_day(tr("Dag van de Arbeid"))

        # German Community Day.
        self._add_holiday(tr("Feestdag van de Duitstalige Gemeenschap"), date(year, NOV, 15))

        # Easter Monday.
        self._add_easter_monday(tr("Paasmaandag"))

        # Ascension Day.
        self._add_ascension_thursday(tr("O. L. H. Hemelvaart"))

        # Whit Monday.
        self._add_whit_monday(tr("Pinkstermaandag"))

        # Christmas Eve.
        self._add_holiday(tr("Heiligavond"), date(year, DEC, 24))


class BE(Belgium):
    pass


class BEL(Belgium):
    pass
