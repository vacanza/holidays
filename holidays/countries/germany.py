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
from datetime import date, timedelta

from holidays.calendars.gregorian import MAY, JUN, OCT
from holidays.constants import CATHOLIC, PUBLIC, SCHOOL
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class Germany(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Germany holidays.

    References:
        * <https://de.wikipedia.org/wiki/Feiertag_(Deutschland)>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Germany>
        * [German Unity Day](https://web.archive.org/web/20251011161644/https://www.gesetze-im-internet.de/einigvtr/art_2.html)

    Subdivisions Holidays References:
        * [Brandenburg](https://web.archive.org/web/20251002092001/https://bravors.brandenburg.de/gesetze/ftg_2015)
        * [Berlin](https://web.archive.org/web/20250518234750/http://gesetze.berlin.de/bsbe/document/jlr-FeiertGBEV10P1)
        * [Baden-Württemberg](https://web.archive.org/web/20240914215438/https://www.landesrecht-bw.de/bsbw/document/jlr-FeiertGBWpP1)
        * [Bayern](https://web.archive.org/web/20250906201237/https://www.gesetze-bayern.de/Content/Document/BayFTG/true)
        * [Bremen](https://web.archive.org/web/20240430101614/https://www.transparenz.bremen.de/metainformationen/gesetz-ueber-die-sonn-gedenk-und-feiertage-vom-12-november-1954-145882)
        * [Hessen](https://web.archive.org/web/20250421183249/http://www.rv.hessenrecht.hessen.de/bshe/document/jlr-FeiertGHE1952rahmen)
        * [Hamburg](https://web.archive.org/web/20250618110249/https://www.landesrecht-hamburg.de/bsha/document/jlr-FeiertGHAV3P1)
        * [Mecklenburg-Vorpommern](https://web.archive.org/web/20250222090126/https://www.landesrecht-mv.de/bsmv/document/jlr-FTGMVV3P2)
        * [Niedersachsen](https://web.archive.org/web/20250627100126/https://voris.wolterskluwer-online.de/browse/document/b724111b-6c20-3862-b111-589842acacba)
        * [Nordrhein-Westfalen](https://web.archive.org/web/20250717194916/https://recht.nrw.de/lmi/owa/br_bes_detail?bes_id=3367&aufgehoben=N&det_id=144445&anw_nr=2&menu=1&sg=0)
        * [Rheinland-Pfalz](https://web.archive.org/web/20250521153233/http://www.landesrecht.rlp.de/bsrp/document/jlr-FeiertGRPpP2)
        * [Schleswig-Holstein](https://web.archive.org/web/20250812223916/https://www.gesetze-rechtsprechung.sh.juris.de/bssh/document/jlr-FeiertGSH2004V3P2)
        * [Saarland](https://web.archive.org/web/20250124112139/http://recht.saarland.de/bssl/document/jlr-FeiertGSL1976V6P2)
        * [Sachsen](https://web.archive.org/web/20250808020452/https://www.revosax.sachsen.de/vorschrift/3997-SaechsSFG)
        * [Sachsen-Anhalt](https://web.archive.org/web/20250615214949/http://www.landesrecht.sachsen-anhalt.de/bsst/document/jlr-FeiertGSTpP2)
        * [Thüringen](https://web.archive.org/web/20250712163548/http://landesrecht.thueringen.de/bsth/document/jlr-FeiertGTHV5P2)
    Hamburg School Holiday Reference:
        * <https://www.hamburg.de/resource/blob/134372/5bc131bdd36a604f67b361d21f7df37e/ferienordnung-hamburg-2024-2030-data.pdf>
    !!! note "Note"
        "Mariä Himmelfahrt" is only a holiday in Bavaria (BY) and "Fronleichnam"
        in Saxony (SN) and Thuringia (TH) if municipality is mostly catholic which
        in term depends on census data. It's listed in "CATHOLIC" category for these provinces.
    """

    country = "DE"
    default_language = "de"
    # Germany reunification was completed on Oct 3, 1990.
    start_year = 1991
    subdivisions = (
        # States.
        "BB",  # Brandenburg.
        "BE",  # Berlin.
        "BW",  # Baden-Württemberg.
        "BY",  # Bayern.
        "HB",  # Bremen.
        "HE",  # Hessen.
        "HH",  # Hamburg.
        "MV",  # Mecklenburg-Vorpommern.
        "NI",  # Niedersachsen.
        "NW",  # Nordrhein-Westfalen.
        "RP",  # Rheinland-Pfalz.
        "SH",  # Schleswig-Holstein.
        "SL",  # Saarland.
        "SN",  # Sachsen.
        "ST",  # Sachsen-Anhalt.
        "TH",  # Thüringen.
        # Cities.
        "Augsburg",
    )
    subdivisions_aliases = {
        "Brandenburg": "BB",
        "Berlin": "BE",
        "Baden-Württemberg": "BW",
        "Bayern": "BY",
        "Bremen": "HB",
        "Hessen": "HE",
        "Hamburg": "HH",
        "Mecklenburg-Vorpommern": "MV",
        "Niedersachsen": "NI",
        "Nordrhein-Westfalen": "NW",
        "Rheinland-Pfalz": "RP",
        "Schleswig-Holstein": "SH",
        "Saarland": "SL",
        "Sachsen": "SN",
        "Sachsen-Anhalt": "ST",
        "Thüringen": "TH",
    }
    supported_categories = (CATHOLIC, PUBLIC, SCHOOL)
    supported_languages = ("de", "en_US", "th", "uk")
    _deprecated_subdivisions = ("BYP",)

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, GermanyStaticHolidays)
        super().__init__(*args, **kwargs)
        # Disable automatic expansion after initial population to avoid
        # implicitly populating adjacent years when checking membership
        # (keeps per-year population semantics for school holiday checks).
        self.expand = False

    def _add_school_holidays_hh(self, year):
        # Helper to add a range of holidays
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    # Ensure holiday is added for the populated year by passing
                    # month and day to _add_holiday so it constructs the date
                    # using `self._year` (prevents cross-year leakage).
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        # Definition of holidays as (Name, Start Date, End Date)
        # For single days, Start Date == End Date
        holidays_map = []

        if year == 2025:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2025, 12, 17), date(2025, 12, 31)),
            ]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 2)),
                (tr("Halbjahrespause"), date(2026, 1, 30), date(2026, 1, 30)),
                (tr("Frühjahrsferien"), date(2026, 3, 2), date(2026, 3, 13)),
                (tr("Himmelfahrt/Pfingsten"), date(2026, 5, 11), date(2026, 5, 15)),
                (tr("Sommerferien"), date(2026, 7, 9), date(2026, 8, 19)),
                (tr("Herbstferien"), date(2026, 10, 19), date(2026, 10, 30)),
                (tr("Weihnachtsferien"), date(2026, 12, 21), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2027, 1, 1), date(2027, 1, 1)),
                (tr("Halbjahrespause"), date(2027, 1, 29), date(2027, 1, 29)),
                (tr("Frühjahrsferien"), date(2027, 3, 1), date(2027, 3, 12)),
                (tr("Himmelfahrt/Pfingsten"), date(2027, 5, 7), date(2027, 5, 14)),
                (tr("Sommerferien"), date(2027, 7, 1), date(2027, 8, 11)),
                (tr("Herbstferien"), date(2027, 10, 11), date(2027, 10, 22)),
                (tr("Weihnachtsferien"), date(2027, 12, 20), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Halbjahrespause"), date(2028, 1, 28), date(2028, 1, 28)),
                (tr("Frühjahrsferien"), date(2028, 3, 6), date(2028, 3, 17)),
                (tr("Himmelfahrt/Pfingsten"), date(2028, 5, 22), date(2028, 5, 26)),
                (tr("Sommerferien"), date(2028, 7, 3), date(2028, 8, 11)),
                (tr("Herbstferien"), date(2028, 10, 2), date(2028, 10, 13)),
                (tr("Brückentag"), date(2028, 10, 30), date(2028, 10, 30)),
                (tr("Weihnachtsferien"), date(2028, 12, 18), date(2028, 12, 29)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Halbjahrespause"), date(2029, 2, 2), date(2029, 2, 2)),
                (tr("Frühjahrsferien"), date(2029, 3, 5), date(2029, 3, 16)),
                (tr("Himmelfahrt/Pfingsten"), date(2029, 5, 11), date(2029, 5, 18)),
                (tr("Sommerferien"), date(2029, 7, 2), date(2029, 8, 10)),
                (tr("Herbstferien"), date(2029, 10, 1), date(2029, 10, 12)),
                (tr("Weihnachtsferien"), date(2029, 12, 21), date(2029, 12, 31)),
            ]
        elif year == 2030:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2030, 1, 1), date(2030, 1, 4)),
                (tr("Halbjahrespause"), date(2030, 2, 1), date(2030, 2, 1)),
                (tr("Frühjahrsferien"), date(2030, 3, 4), date(2030, 3, 15)),
                (tr("Himmelfahrt/Pfingsten"), date(2030, 5, 20), date(2030, 5, 24)),
                (tr("Brückentag"), date(2030, 5, 31), date(2030, 5, 31)),
                (tr("Sommerferien"), date(2030, 7, 4), date(2030, 8, 14)),
            ]
            
        for name, start, end in holidays_map:
            _add_holiday_range(name, start, end)

    def _populate(self, year):
															 
        super()._populate(year)

											  
        if self.subdiv == "HH" and SCHOOL in self.categories:
            self._add_school_holidays_hh(year)
            # Ensure no holidays from other years were accidentally added
            # (defensive cleanup for cross-year ranges).
            for dt in list(self.keys()):
                if dt.year != year:
                    self.pop(dt)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Neujahr"))

        # Good Friday.
        self._add_good_friday(tr("Karfreitag"))

        # Easter Monday.
        self._add_easter_monday(tr("Ostermontag"))

        # Labor Day.
        self._add_labor_day(tr("Erster Mai"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Christi Himmelfahrt"))

        # Whit Monday.
        self._add_whit_monday(tr("Pfingstmontag"))

        # German Unity Day.
        self._add_holiday_oct_3(tr("Tag der Deutschen Einheit"))

        if self._year <= 1994:
            # Repentance and Prayer Day.
            self._add_holiday_1st_wed_before_nov_22(tr("Buß- und Bettag"))

        # Christmas Day.
        self._add_christmas_day(tr("Erster Weihnachtstag"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Zweiter Weihnachtstag"))

        if self.subdiv == "BYP":
            self._populate_subdiv_by_public_holidays()

    def _populate_subdiv_bb_public_holidays(self):
        # Easter Sunday.
        self._add_easter_sunday(tr("Ostersonntag"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Pfingstsonntag"))

        # Reformation Day.
        self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_be_public_holidays(self):
        if self._year >= 2019:
            # Women's Day.
            self._add_womens_day(tr("Frauentag"))

    def _populate_subdiv_bw_public_holidays(self):
        # Epiphany.
        self._add_epiphany_day(tr("Heilige Drei Könige"))

        # Corpus Christi.
        self._add_corpus_christi_day(tr("Fronleichnam"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_by_public_holidays(self):
        # Epiphany.
        self._add_epiphany_day(tr("Heilige Drei Könige"))

        # Corpus Christi.
        self._add_corpus_christi_day(tr("Fronleichnam"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_by_catholic_holidays(self):
        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

    def _populate_subdiv_hb_public_holidays(self):
        if self._year >= 2018:
            # Reformation Day.
            self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_he_public_holidays(self):
        # Corpus Christi.
        self._add_corpus_christi_day(tr("Fronleichnam"))

    def _populate_subdiv_hh_public_holidays(self):
        if self._year >= 2018:
            # Reformation Day.
            self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_mv_public_holidays(self):
        if self._year >= 2023:
            # Women's Day.
            self._add_womens_day(tr("Frauentag"))

        # Reformation Day.
        self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_ni_public_holidays(self):
        if self._year >= 2018:
            # Reformation Day.
            self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_nw_public_holidays(self):
        # Corpus Christi.
        self._add_corpus_christi_day(tr("Fronleichnam"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_rp_public_holidays(self):
        # Corpus Christi.
        self._add_corpus_christi_day(tr("Fronleichnam"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_sh_public_holidays(self):
        if self._year >= 2018:
            # Reformation Day.
            self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_sl_public_holidays(self):
        # Corpus Christi.
        self._add_corpus_christi_day(tr("Fronleichnam"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_sn_public_holidays(self):
        # Reformation Day.
        self._add_holiday_oct_31(tr("Reformationstag"))

        if self._year >= 1995:
            # Repentance and Prayer Day.
            self._add_holiday_1st_wed_before_nov_22(tr("Buß- und Bettag"))

    def _populate_subdiv_sn_catholic_holidays(self):
        # Corpus Christi.
        self._add_corpus_christi_day(tr("Fronleichnam"))

    def _populate_subdiv_st_public_holidays(self):
        # Epiphany.
        self._add_epiphany_day(tr("Heilige Drei Könige"))

        # Reformation Day.
        self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_th_public_holidays(self):
        if self._year >= 2019:
            # World Children's Day.
            self._add_holiday_sep_20(tr("Weltkindertag"))

        # Reformation Day.
        self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_th_catholic_holidays(self):
        # Corpus Christi.
        self._add_corpus_christi_day(tr("Fronleichnam"))

    def _populate_subdiv_augsburg_public_holidays(self):
        self._populate_subdiv_by_public_holidays()

        # Augsburg Peace Festival.
        self._add_holiday_aug_8(tr("Augsburger Hohes Friedensfest"))


class DE(Germany):
    pass


class DEU(Germany):
    pass


class GermanyStaticHolidays:
    """Germany special holidays.

    References:
        * <https://web.archive.org/web/20241127055605/https://www.stuttgarter-zeitung.de/inhalt.reformationstag-2017-einmalig-bundesweiter-feiertag.b7e189b3-a33d-41a3-a0f4-141cd13df54e.html>
        * <https://web.archive.org/web/20250415233518/https://www.bbc.com/news/world-europe-52574748>
        * <https://web.archive.org/web/20241219151307/https://gesetze.berlin.de/bsbe/document/jlr-FeiertGBEV8P1>
    """

    special_public_holidays = {
        # Reformation Day.
        2017: (OCT, 31, tr("Reformationstag")),
    }

    special_be_public_holidays = {
        2020: (
            MAY,
            8,
            # 75th anniversary of the liberation from Nazism and
            # the end of the Second World War in Europe.
            tr(
                "75. Jahrestag der Befreiung vom Nationalsozialismus "
                "und der Beendigung des Zweiten Weltkriegs in Europa"
            ),
        ),
        2025: (
            MAY,
            8,
            # 80th anniversary of the liberation from Nazism and
            # the end of the Second World War in Europe.
            tr(
                "80. Jahrestag der Befreiung vom Nationalsozialismus "
                "und der Beendigung des Zweiten Weltkriegs in Europa"
            ),
        ),
        # 75th anniversary of the East German uprising of 1953.
        2028: (JUN, 17, tr("75. Jahrestag des Aufstandes vom 17. Juni 1953")),
    }
