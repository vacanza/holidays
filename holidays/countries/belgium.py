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

from holidays.calendars.gregorian import (
    date,
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
            - Flemish Community (Vlaanderen)
            <https://www.vlaanderen.be/onderwijs-en-vorming/wat-mag-en-moet-op-school/schoolvakanties-vrije-dagen-en-afwezigheden/schoolvakanties>
            - French Community (Fédération Wallonie-Bruxelles)
            <http://www.enseignement.be/index.php?page=23953>
            - German-speaking Community (Deutschsprachige Gemeinschaft)
            <https://ostbelgienbildung.be/desktopdefault.aspx/tabid-2212/4397_read-31727/>

    Notes:
        * Belgium has three school systems with different vacation rules:
            - VLG: Flemish Community
            - WBR: French Community (Wallonia + Brussels French schools)
            - GER: German-speaking Community (Ostbelgien)
        * Only fixed and well-defined school holidays are implemented.
        * Variable vacation periods are either calculated (VLG) or intentionally
        left unimplemented (WBR, GER) because they are published yearly by ministerial decree.
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
        if (holiday_name := name or self.get(start_date)) is None:
            raise ValueError(f"Cannot infer holiday name for date {start_date!r}.")

        return {
            d
            for delta in range(duration_days)
            if (d := self._add_holiday(holiday_name, _timedelta(start_date, delta)))
        }

    def _populate_subdiv_vlg_school_holidays(self):
        """
        School holidays for the Flemish Community (Vlaamse Gemeenschap).

        Most vacation periods are rule-based and can be calculated
        algorithmically, therefore they are implemented here.
        """
        year = self._year
        easter = self._easter_sunday

        # Christmas Holidays : Monday of the week of 25 Dec → 2 weeks
        # Since Christmas holidays start in December and continue into January,
        # we need to add the holiday for both the current and previous year.
        # Current year's Christmas
        christmas = date(year, 12, 25)
        # if Christmas is on Monday, holiday will start that day.
        # if Christmas is on Tue-Fri, start the previous Monday.
        # if Christmas is a Sat/Sun, start the following Monday.
        start = _get_nth_weekday_from(-1 if christmas.weekday() <= 4 else 1, 0, christmas)
        self._add_multiday_holiday(start, 13, name=tr("Kerstvakantie"))

        # Previous year's Christmas (for January spillover)
        prev_christmas = date(year - 1, 12, 25)
        prev_start = _get_nth_weekday_from(
            -1 if prev_christmas.weekday() <= 4 else 1,
            0,
            prev_christmas,
        )
        self._add_multiday_holiday(prev_start, 14, name=tr("Kerstvakantie"))

        # Carnival: Easter - 48 days → previous Sunday → 1 week
        krokus_raw = _timedelta(easter, days=-47)
        krokus_start = _get_nth_weekday_from(-1, 0, krokus_raw)
        self._add_multiday_holiday(krokus_start, 7, name=tr("Krokusvakantie"))

        # Easter Holidays: Easter period → 2 weeks
        # If the Easter Sunday is in March:
        # - Paasvakantie starts the week
        # before Easter Sunday (Monday)
        # If the Easter Sunday is after April 15:
        # - Paasvakantie starts the second Monday
        # before Easter Sunday
        # Otherwise:
        # - Paasvakantie starts the first Monday of April
        if easter.month == 3:
            paas_start = _get_nth_weekday_from(1, 0, easter)
            paas_end = _timedelta(paas_start, days=14)
        elif easter > date(year, 4, 15):
            # second Monday before Easter
            paas_start = _get_nth_weekday_from(-2, 0, easter)
            paas_end = _timedelta(paas_start, days=15)
        else:
            paas_start = _get_nth_weekday_of_month(1, 0, 4, year)
            paas_end = _timedelta(paas_start, days=14)
        self._add_multiday_holiday(
            paas_start, (paas_end - paas_start).days, name=tr("Paasvakantie")
        )

        # Labour Day
        self._add_labor_day(tr("Dag van de Arbeid"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Hemelvaart"))

        # Friday after Ascension (Ascension = Easter + 39 days, so Friday = Easter + 40 days)
        ascension_friday = _timedelta(easter, days=40)
        self._add_holiday(tr("Vrijdag na Hemelvaart"), ascension_friday)

        # Whit Monday / Pentecost Monday.
        self._add_whit_monday(tr("Pinkstermaandag"))

        # Summer Holidays: From 1 July to 31 August (fixed period)
        start = date(year, 7, 1)
        end = date(year, 9, 1)
        self._add_multiday_holiday(start, (end - start).days, name=tr("Zomervakantie"))

        # Autumn Holidays: Monday of the week of 1 Nov → 1 week
        # If 1 Nov is a Monday, the holiday starts that day.
        # If 1 Nov is a Tuesday-Friday, the holiday starts on the previous Monday.
        # If 1 Nov is a Saturday or Sunday, start the week after (i.e., on 2 Nov or 3 Nov).
        nov_1 = date(year, 11, 1)
        start = _get_nth_weekday_from(-1 if nov_1.weekday() <= 5 else 1, 0, nov_1)
        self._add_multiday_holiday(start, 7, name=tr("Herfstvakantie"))

        # Armistice Day (End of World War I).
        self._add_remembrance_day(tr("Wapenstilstand"))

    def _populate_subdiv_wbr_school_holidays(self):
        """
        School holidays for Wallonia (French Community + German-speaking schools).
        Only fixed and well-defined days are implemented.
        Vacation periods are defined yearly by ministerial decree and are intentionally
        left unimplemented.
        """
        year = self._year
        # Armistice Day
        self._add_remembrance_day(tr("Jour de l'Armistice"))

        # Labour Day
        self._add_labor_day(tr("Fête du Travail"))

        # French Community Day
        self._add_holiday(tr("Fête de la Communauté française"), date(year, 9, 27))

        # Easter Monday.
        self._add_easter_monday(tr("Lundi de Pâques"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Jeudi de l'Ascension"))

        # Whit Monday.
        self._add_whit_monday(tr("Lundi de Pentecôte"))

        # NOT IMPLEMENTED:
        # - Vacances d'automne (Autumn holidays)
        # - Vacances d'hiver (Christmas holidays)
        # - Congé de détente (Carnival holidays)
        # - Vacances de printemps (Spring holidays)
        # - Vacances d'été (Summer holidays)
        # - Congé d'automne (Toussaint / All saints)

        # These vary each year and are published by official decree.

    def _populate_subdiv_ger_school_holidays(self):
        """
        School holidays for the German-speaking Community (Ostbelgien).

        Dates are published yearly by decree.
        Only fixed and well-defined days are implemented.
        Vacation periods are intentionally
        left unimplemented.
        """
        year = self._year

        # Armistice Day.
        self._add_remembrance_day(tr("Tag des Waffenstillstands"))

        # Labour Day
        self._add_labor_day(tr("Tag der Arbeit"))

        # German Community Day.
        self._add_holiday(tr("Feiertag der Deutschsprachigen Gemeinschaft"), date(year, 11, 15))

        # Easter Monday.
        self._add_easter_monday(tr("Ostermontag"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Christi Himmelfahrt"))

        # Whit Monday.
        self._add_whit_monday(tr("Pfingstmontag"))

        # NOT IMPLEMENTED:
        # - Herbstferien (Autumn holidays)
        # - Weihnachtsferien (Christmas holidays)
        # - Karnevalsferien (Carnival holidays)
        # - Osterferien (Easter holidays)
        # - Sommerferien (Summer holidays)
        # These vary each year and are published by official decree.


class BE(Belgium):
    pass


class BEL(Belgium):
    pass
