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

from datetime import date, timedelta
from gettext import gettext as tr

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
    School Holiday References:
        * [Brandenburg](https://bravors.brandenburg.de/sixcms/media.php/66/VV-Schulbetrieb-Anlage-1-2025.pdf)
        * [Berlin](https://www.berlin.de/sen/bjf/service/kalender/ferien/ferienordnung-des-landes-berlin-2024_2025-bis-2029_2030.pdf?ts=1752674587)
        * [Baden-Württemberg](https://km.baden-wuerttemberg.de/de/service/ferien)
        * [Bayern](https://www.verkuendung-bayern.de/baymbl/2022-747/)
        * [Bremen](https://www.bildung.bremen.de/ferientermine-3404)
        * [Hessen](https://kultus.hessen.de/Schulsystem/Ferien/Ferientermine)
        * [Hamburg](https://www.hamburg.de/resource/blob/134372/5bc131bdd36a604f67b361d21f7df37e/ferienordnung-hamburg-2024-2030-data.pdf)
        * [Mecklenburg-Vorpommern](https://www.landesrecht-mv.de/bsmv/document/jlr-AFer2024-2030VMVrahmen)
        * [Niedersachsen](https://www.mk.niedersachsen.de/download/98089/Ferienuebersicht_fuer_Niedersachsen_Schuljahr_2024_25_-_2029_30.pdf)
        * [Nordrhein-Westfalen(https://www.schulministerium.nrw/service/ferienordnung-fuer-nordrhein-westfalen-fuer-die-schuljahre-bis-202930)
        * [Rheinland-Pfalz](https://bm.rlp.de/service/ferientermine)
        * [Schleswig-Holstein](https://www.schleswig-holstein.de/DE/landesregierung/themen/bildung-hochschulen/ferientermine/ferientermine_node.html)
        * [Saarland](https://www.saarland.de/SharedDocs/Downloads/DE/mbk/Bildungsserver/allgemeine-informationen/ferienordnung_ab_2024_amtsblatt.pdf?__blob=publicationFile&v=1)
        * [Sachsen](https://www.schule.sachsen.de/schuljahrestermine-4793.html)
        * [Sachsen-Anhalt](https://mb.sachsen-anhalt.de/fileadmin/Bibliothek/Landesjournal/Bildung_und_Wissenschaft/Erlasse/Ferienregelung_2024_bis_2030.pdf)
        * [Thüringen](https://bildung.thueringen.de/schule/schulwesen/ferien)
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

    def _add_school_holidays_nw(self, year):
        # Helper to add a range of holidays for Nordrhein-Westfalen (NW)
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        holidays_map = []

        if year == 2025:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2025, 12, 22), date(2025, 12, 31)),
            ]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 6)),
                (tr("Sommerferien"), date(2026, 7, 20), date(2026, 9, 1)),
                (tr("Herbstferien"), date(2026, 10, 17), date(2026, 10, 31)),
                (tr("Weihnachtsferien"), date(2026, 12, 23), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Osterferien"), date(2027, 3, 22), date(2027, 4, 3)),
                (tr("Pfingsten"), date(2027, 5, 18), date(2027, 5, 18)),
                (tr("Sommerferien"), date(2027, 7, 19), date(2027, 8, 31)),
                (tr("Herbstferien"), date(2027, 10, 23), date(2027, 11, 6)),
                (tr("Weihnachtsferien"), date(2027, 12, 24), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Osterferien"), date(2028, 4, 10), date(2028, 4, 22)),
                (tr("Sommerferien"), date(2028, 7, 10), date(2028, 8, 22)),
                (tr("Herbstferien"), date(2028, 10, 23), date(2028, 11, 4)),
                (tr("Weihnachtsferien"), date(2028, 12, 21), date(2028, 12, 31)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Osterferien"), date(2029, 3, 26), date(2029, 4, 7)),
                (tr("Pfingsten"), date(2029, 5, 22), date(2029, 5, 22)),
                (tr("Sommerferien"), date(2029, 7, 2), date(2029, 8, 14)),
                (tr("Herbstferien"), date(2029, 10, 15), date(2029, 10, 27)),
                (tr("Weihnachtsferien"), date(2029, 12, 20), date(2029, 12, 31)),
            ]
        elif year == 2030:
            holidays_map = [
                (tr("Osterferien"), date(2030, 4, 15), date(2030, 4, 27)),
            ]

        for name, start, end in holidays_map:
            _add_holiday_range(name, start, end)

    def _add_school_holidays_rp(self, year):
        # Helper to add a range of holidays for Rheinland-Pfalz (RP)
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        holidays_map = []

        if year == 2025:
            holidays_map = [
                (tr("Sommerferien"), date(2025, 7, 7), date(2025, 8, 16)),
                (tr("Herbstferien"), date(2025, 10, 13), date(2025, 10, 25)),
                (tr("Weihnachtsferien"), date(2025, 12, 22), date(2025, 12, 31)),
            ]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 8)),
                (tr("Osterferien"), date(2026, 3, 30), date(2026, 4, 11)),
                (tr("Sommerferien"), date(2026, 6, 29), date(2026, 8, 8)),
                (tr("Herbstferien"), date(2026, 10, 5), date(2026, 10, 17)),
                (tr("Weihnachtsferien"), date(2026, 12, 23), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2027, 1, 1), date(2027, 1, 9)),
                (tr("Osterferien"), date(2027, 3, 22), date(2027, 4, 3)),
                (tr("Sommerferien"), date(2027, 6, 28), date(2027, 8, 7)),
                (tr("Herbstferien"), date(2027, 10, 4), date(2027, 10, 16)),
                (tr("Weihnachtsferien"), date(2027, 12, 23), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2028, 1, 1), date(2028, 1, 8)),
                (tr("Osterferien"), date(2028, 4, 10), date(2028, 4, 22)),
                (tr("Sommerferien"), date(2028, 7, 3), date(2028, 8, 12)),
                (tr("Herbstferien"), date(2028, 10, 9), date(2028, 10, 21)),
                (tr("Weihnachtsferien"), date(2028, 12, 21), date(2028, 12, 31)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2029, 1, 1), date(2029, 1, 9)),
                (tr("Osterferien"), date(2029, 3, 26), date(2029, 4, 7)),
                (tr("Sommerferien"), date(2029, 7, 16), date(2029, 8, 25)),
                (tr("Herbstferien"), date(2029, 10, 22), date(2029, 11, 3)),
                (tr("Weihnachtsferien"), date(2029, 12, 24), date(2029, 12, 31)),
            ]
        elif year == 2030:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2030, 1, 1), date(2030, 1, 10)),
                (tr("Osterferien"), date(2030, 4, 15), date(2030, 5, 1)),
            ]

        for name, start, end in holidays_map:
            _add_holiday_range(name, start, end)

    def _add_school_holidays_hb(self, year):
        # Helper to add a range of holidays for Bremen (HB)
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        holidays_map = []

        if year == 2025:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2025, 12, 22), date(2025, 12, 31)),
            ]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 5)),
                (tr("Halbjahresferien"), date(2026, 2, 2), date(2026, 2, 3)),
                (tr("Osterferien"), date(2026, 3, 23), date(2026, 4, 7)),
                (tr("Tag nach Himmelfahrt"), date(2026, 5, 15), date(2026, 5, 15)),
                (tr("Pfingsten"), date(2026, 5, 26), date(2026, 5, 26)),
                (tr("Sommerferien"), date(2026, 7, 2), date(2026, 8, 12)),
                (tr("Herbstferien"), date(2026, 10, 12), date(2026, 10, 24)),
                (tr("Weihnachtsferien"), date(2026, 12, 23), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2027, 1, 1), date(2027, 1, 9)),
                (tr("Halbjahresferien"), date(2027, 2, 1), date(2027, 2, 2)),
                (tr("Osterferien"), date(2027, 3, 22), date(2027, 4, 3)),
                (tr("Tag nach Himmelfahrt"), date(2027, 5, 7), date(2027, 5, 7)),
                (tr("Pfingsten"), date(2027, 5, 18), date(2027, 5, 18)),
                (tr("Sommerferien"), date(2027, 7, 8), date(2027, 8, 18)),
                (tr("Herbstferien"), date(2027, 10, 18), date(2027, 10, 30)),
                (tr("Weihnachtsferien"), date(2027, 12, 23), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2028, 1, 1), date(2028, 1, 8)),
                (tr("Halbjahresferien"), date(2028, 1, 31), date(2028, 2, 1)),
                (tr("Osterferien"), date(2028, 4, 10), date(2028, 4, 22)),
                (tr("Tag nach Himmelfahrt"), date(2028, 5, 26), date(2028, 5, 26)),
                (tr("Pfingsten"), date(2028, 6, 6), date(2028, 6, 6)),
                (tr("Sommerferien"), date(2028, 7, 20), date(2028, 8, 30)),
                (tr("Tag vor dem 03. Oktober"), date(2028, 10, 2), date(2028, 10, 2)),
                (tr("Herbstferien"), date(2028, 10, 23), date(2028, 11, 4)),
                (tr("Weihnachtsferien"), date(2028, 12, 27), date(2028, 12, 31)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2029, 1, 1), date(2029, 1, 6)),
                (tr("Halbjahresferien"), date(2029, 2, 1), date(2029, 2, 2)),
                (tr("Osterferien"), date(2029, 3, 19), date(2029, 4, 3)),
                (tr("Tag vor dem 01. Mai"), date(2029, 4, 30), date(2029, 4, 30)),
                (tr("Tag nach Himmelfahrt"), date(2029, 5, 11), date(2029, 5, 11)),
                (tr("Pfingsten"), date(2029, 5, 22), date(2029, 5, 22)),
                (tr("Sommerferien"), date(2029, 7, 19), date(2029, 8, 29)),
                (tr("Tage nach dem 03. Oktober"), date(2029, 10, 4), date(2029, 10, 5)),
                (tr("Herbstferien"), date(2029, 10, 22), date(2029, 11, 2)),
                (tr("Weihnachtsferien"), date(2029, 12, 21), date(2029, 12, 31)),
            ]
        elif year == 2030:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2030, 1, 1), date(2030, 1, 5)),
                (tr("Halbjahresferien"), date(2030, 1, 31), date(2030, 2, 1)),
                (tr("Osterferien"), date(2030, 4, 8), date(2030, 4, 23)),
                (tr("Tag nach Himmelfahrt"), date(2030, 5, 31), date(2030, 5, 31)),
                (tr("Pfingsten"), date(2030, 6, 11), date(2030, 6, 11)),
                (tr("Sommerferien"), date(2030, 7, 11), date(2030, 8, 21)),
            ]

        for name, start, end in holidays_map:
            _add_holiday_range(name, start, end)

    def _add_school_holidays_sl(self, year):
        # Helper to add a range of holidays for Saarland (SL)
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        holidays_map = []

        if year == 2025:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2025, 12, 22), date(2025, 12, 31)),
            ]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 2)),
                (tr("Fastnachtsferien"), date(2026, 2, 16), date(2026, 2, 20)),
                (tr("Osterferien"), date(2026, 4, 7), date(2026, 4, 17)),
                (tr("Sommerferien"), date(2026, 6, 29), date(2026, 8, 7)),
                (tr("Herbstferien"), date(2026, 10, 5), date(2026, 10, 16)),
                (tr("Weihnachtsferien"), date(2026, 12, 21), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Fastnachtsferien"), date(2027, 2, 8), date(2027, 2, 12)),
                (tr("Osterferien"), date(2027, 3, 30), date(2027, 4, 9)),
                (tr("Sommerferien"), date(2027, 6, 28), date(2027, 8, 6)),
                (tr("Herbstferien"), date(2027, 10, 4), date(2027, 10, 15)),
                (tr("Weihnachtsferien"), date(2027, 12, 20), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Fastnachtsferien"), date(2028, 2, 21), date(2028, 2, 29)),
                (tr("Osterferien"), date(2028, 4, 12), date(2028, 4, 21)),
                (tr("Sommerferien"), date(2028, 7, 3), date(2028, 8, 11)),
                (tr("Herbstferien"), date(2028, 10, 9), date(2028, 10, 20)),
                (tr("Weihnachtsferien"), date(2028, 12, 20), date(2028, 12, 31)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2029, 1, 1), date(2029, 1, 2)),
                (tr("Fastnachtsferien"), date(2029, 2, 12), date(2029, 2, 16)),
                (tr("Osterferien"), date(2029, 3, 26), date(2029, 4, 6)),
                (tr("Pfingstferien"), date(2029, 5, 22), date(2029, 5, 25)),
                (tr("Sommerferien"), date(2029, 7, 16), date(2029, 8, 24)),
                (tr("Herbstferien"), date(2029, 10, 22), date(2029, 11, 2)),
                (tr("Weihnachtsferien"), date(2029, 12, 21), date(2029, 12, 31)),
            ]
        elif year == 2030:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2030, 1, 1), date(2030, 1, 4)),
                (tr("Fastnachtsferien"), date(2030, 2, 25), date(2030, 3, 5)),
                (tr("Osterferien"), date(2030, 4, 15), date(2030, 4, 26)),
                (tr("Sommerferien"), date(2030, 7, 22), date(2030, 8, 30)),
            ]

        for name, start, end in holidays_map:
            _add_holiday_range(name, start, end)

    def _add_school_holidays_th(self, year):
        # Helper to add a range of holidays for Thüringen (TH)
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        holidays_map = []

        if year == 2025:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2025, 12, 22), date(2025, 12, 31)),
            ]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 3)),
                (tr("Winterferien"), date(2026, 2, 16), date(2026, 2, 21)),
                (tr("Osterferien"), date(2026, 4, 7), date(2026, 4, 17)),
                (tr("Schulfreier Tag"), date(2026, 5, 15), date(2026, 5, 15)),
                (tr("Sommerferien"), date(2026, 7, 4), date(2026, 8, 14)),
                (tr("Herbstferien"), date(2026, 10, 12), date(2026, 10, 24)),
                (tr("Weihnachtsferien"), date(2026, 12, 23), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2027, 1, 1), date(2027, 1, 2)),
                (tr("Winterferien"), date(2027, 2, 1), date(2027, 2, 6)),
                (tr("Osterferien"), date(2027, 3, 22), date(2027, 4, 3)),
                (tr("Schulfreier Tag"), date(2027, 5, 7), date(2027, 5, 7)),
                (tr("Sommerferien"), date(2027, 7, 10), date(2027, 8, 20)),
                (tr("Herbstferien"), date(2027, 10, 9), date(2027, 10, 23)),
                (tr("Weihnachtsferien"), date(2027, 12, 23), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Winterferien"), date(2028, 2, 7), date(2028, 2, 12)),
                (tr("Osterferien"), date(2028, 4, 3), date(2028, 4, 15)),
                (tr("Schulfreier Tag"), date(2028, 5, 26), date(2028, 5, 26)),
                (tr("Sommerferien"), date(2028, 7, 22), date(2028, 9, 1)),
                (tr("Herbstferien"), date(2028, 10, 23), date(2028, 11, 3)),
                (tr("Weihnachtsferien"), date(2028, 12, 23), date(2028, 12, 31)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2029, 1, 1), date(2029, 1, 5)),
                (tr("Winterferien"), date(2029, 2, 12), date(2029, 2, 17)),
                (tr("Osterferien"), date(2029, 3, 26), date(2029, 4, 7)),
                (tr("Schulfreier Tag"), date(2029, 5, 11), date(2029, 5, 11)),
                (tr("Sommerferien"), date(2029, 7, 21), date(2029, 8, 31)),
                (tr("Herbstferien"), date(2029, 10, 22), date(2029, 11, 3)),
                (tr("Weihnachtsferien"), date(2029, 12, 22), date(2029, 12, 31)),
            ]
        elif year == 2030:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2030, 1, 1), date(2030, 1, 4)),
                (tr("Winterferien"), date(2030, 2, 11), date(2030, 2, 16)),
                (tr("Osterferien"), date(2030, 4, 8), date(2030, 4, 20)),
                (tr("Schulfreier Tag"), date(2030, 5, 31), date(2030, 5, 31)),
                (tr("Sommerferien"), date(2030, 7, 13), date(2030, 8, 23)),
            ]

        for name, start, end in holidays_map:
            _add_holiday_range(name, start, end)

    def _add_school_holidays_sh(self, year):
        # Helper to add a range of holidays for Schleswig-Holstein (SH)
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        holidays_map = []

        if year == 2025:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2025, 12, 19), date(2025, 12, 31)),
            ]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 6)),
                (tr("Osterferien"), date(2026, 3, 26), date(2026, 4, 10)),
                (tr("Himmelfahrt"), date(2026, 5, 15), date(2026, 5, 15)),
                (tr("Sommerferien"), date(2026, 7, 4), date(2026, 8, 15)),
                (tr("Herbstferien"), date(2026, 10, 12), date(2026, 10, 24)),
                (tr("Weihnachtsferien"), date(2026, 12, 21), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Osterferien"), date(2027, 3, 30), date(2027, 4, 10)),
                (tr("Himmelfahrt"), date(2027, 5, 7), date(2027, 5, 7)),
                (tr("Sommerferien"), date(2027, 7, 3), date(2027, 8, 14)),
                (tr("Herbstferien"), date(2027, 10, 11), date(2027, 10, 23)),
                (tr("Weihnachtsferien"), date(2027, 12, 23), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2028, 1, 1), date(2028, 1, 8)),
                (tr("Osterferien"), date(2028, 4, 3), date(2028, 4, 15)),
                (tr("Himmelfahrt"), date(2028, 5, 26), date(2028, 5, 26)),
                (tr("Sommerferien"), date(2028, 6, 24), date(2028, 8, 4)),
                (tr("Herbstferien"), date(2028, 10, 16), date(2028, 10, 30)),
                (tr("Weihnachtsferien"), date(2028, 12, 21), date(2028, 12, 31)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Osterferien"), date(2029, 3, 23), date(2029, 4, 6)),
                (tr("Himmelfahrt"), date(2029, 5, 11), date(2029, 5, 11)),
                (tr("Sommerferien"), date(2029, 6, 23), date(2029, 8, 3)),
                (tr("Herbstferien"), date(2029, 10, 8), date(2029, 10, 19)),
                (tr("Weihnachtsferien"), date(2029, 12, 21), date(2029, 12, 31)),
            ]
        elif year == 2030:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2030, 1, 1), date(2030, 1, 8)),
                (tr("Osterferien"), date(2030, 4, 8), date(2030, 4, 20)),
                (tr("Himmelfahrt"), date(2030, 5, 31), date(2030, 5, 31)),
                (tr("Sommerferien"), date(2030, 7, 8), date(2030, 8, 17)),
                (tr("Herbstferien"), date(2030, 10, 14), date(2030, 10, 25)),
                (tr("Weihnachtsferien"), date(2030, 12, 20), date(2030, 12, 31)),
            ]
        elif year == 2031:
            holidays_map = [
                (tr("Osterferien"), date(2031, 3, 28), date(2031, 4, 10)),
                (tr("Himmelfahrt"), date(2031, 5, 23), date(2031, 5, 23)),
                (tr("Weihnachtsferien"), date(2031, 1, 1), date(2031, 1, 6)),
            ]

        for name, start, end in holidays_map:
            _add_holiday_range(name, start, end)

    def _add_school_holidays_sn(self, year):
        # Helper to add a range of holidays for Sachsen (SN)
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        holidays_map = []

        if year == 2025:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2025, 12, 22), date(2025, 12, 31)),
            ]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 2)),
                (tr("Winterferien"), date(2026, 2, 9), date(2026, 2, 21)),
                (tr("Osterferien"), date(2026, 4, 3), date(2026, 4, 10)),
                (tr("Sommerferien"), date(2026, 7, 4), date(2026, 8, 14)),
                (tr("Unterrichtsfreier Tag"), date(2026, 5, 15), date(2026, 5, 15)),
                (tr("Herbstferien"), date(2026, 10, 12), date(2026, 10, 24)),
                (tr("Weihnachtsferien"), date(2026, 12, 23), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2027, 1, 1), date(2027, 1, 2)),
                (tr("Winterferien"), date(2027, 2, 8), date(2027, 2, 19)),
                (tr("Osterferien"), date(2027, 3, 26), date(2027, 4, 2)),
                (tr("Pfingstferien"), date(2027, 5, 15), date(2027, 5, 18)),
                (tr("Unterrichtsfreier Tag"), date(2027, 5, 7), date(2027, 5, 7)),
                (tr("Sommerferien"), date(2027, 7, 10), date(2027, 8, 20)),
                (tr("Herbstferien"), date(2027, 10, 11), date(2027, 10, 23)),
                (tr("Weihnachtsferien"), date(2027, 12, 23), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2028, 1, 1), date(2028, 1, 1)),
                (tr("Winterferien"), date(2028, 2, 14), date(2028, 2, 26)),
                (tr("Osterferien"), date(2028, 4, 14), date(2028, 4, 22)),
                (tr("Unterrichtsfreier Tag"), date(2028, 5, 26), date(2028, 5, 26)),
                (tr("Sommerferien"), date(2028, 7, 22), date(2028, 9, 1)),
                (tr("Herbstferien"), date(2028, 10, 23), date(2028, 11, 3)),
                (tr("Weihnachtsferien"), date(2028, 12, 23), date(2028, 12, 31)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2029, 1, 1), date(2029, 1, 1)),
                (tr("Winterferien"), date(2029, 2, 5), date(2029, 2, 16)),
                (tr("Osterferien"), date(2029, 3, 29), date(2029, 4, 6)),
                (tr("Pfingstferien"), date(2029, 5, 19), date(2029, 5, 22)),
                (tr("Unterrichtsfreier Tag"), date(2029, 5, 11), date(2029, 5, 11)),
                (tr("Sommerferien"), date(2029, 7, 21), date(2029, 8, 31)),
                (tr("Herbstferien"), date(2029, 10, 22), date(2029, 11, 2)),
                (tr("Weihnachtsferien"), date(2029, 12, 22), date(2029, 12, 31)),
            ]
        elif year == 2030:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2030, 1, 1), date(2030, 1, 4)),
                (tr("Winterferien"), date(2030, 2, 18), date(2030, 3, 1)),
                (tr("Osterferien"), date(2030, 4, 19), date(2030, 4, 26)),
                (tr("Pfingstferien"), date(2030, 6, 8), date(2030, 6, 11)),
                (tr("Unterrichtsfreier Tag"), date(2030, 5, 31), date(2030, 5, 31)),
                (tr("Sommerferien"), date(2030, 7, 13), date(2030, 8, 23)),
            ]

        for name, start, end in holidays_map:
            _add_holiday_range(name, start, end)

    def _add_school_holidays_st(self, year):
        # Helper to add a range of holidays for Sachsen-Anhalt (ST)
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        holidays_map = []

        if year == 2025:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2025, 12, 22), date(2025, 12, 31)),
            ]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 5)),
                (tr("Winterferien"), date(2026, 1, 31), date(2026, 2, 6)),
                (tr("Osterferien"), date(2026, 3, 30), date(2026, 4, 4)),
                (tr("Pfingstferien"), date(2026, 5, 26), date(2026, 5, 29)),
                (tr("Sommerferien"), date(2026, 7, 4), date(2026, 8, 14)),
                (tr("Herbstferien"), date(2026, 10, 19), date(2026, 10, 30)),
                (tr("Weihnachtsferien"), date(2026, 12, 21), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2027, 1, 1), date(2027, 1, 5)),
                (tr("Winterferien"), date(2027, 2, 1), date(2027, 2, 6)),
                (tr("Osterferien"), date(2027, 3, 22), date(2027, 3, 27)),
                (tr("Pfingstferien"), date(2027, 5, 15), date(2027, 5, 22)),
                (tr("Sommerferien"), date(2027, 7, 10), date(2027, 8, 20)),
                (tr("Herbstferien"), date(2027, 10, 18), date(2027, 10, 23)),
                (tr("Weihnachtsferien"), date(2027, 12, 20), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Winterferien"), date(2028, 2, 7), date(2028, 2, 12)),
                (tr("Osterferien"), date(2028, 4, 10), date(2028, 4, 22)),
                (tr("Pfingstferien"), date(2028, 6, 3), date(2028, 6, 10)),
                (tr("Sommerferien"), date(2028, 7, 22), date(2028, 9, 1)),
                (tr("Beweglicher Ferientag"), date(2028, 10, 2), date(2028, 10, 2)),
                (tr("Herbstferien"), date(2028, 10, 30), date(2028, 11, 3)),
                (tr("Weihnachtsferien"), date(2028, 12, 21), date(2028, 12, 31)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2029, 1, 1), date(2029, 1, 5)),
                (tr("Winterferien"), date(2029, 2, 5), date(2029, 2, 10)),
                (tr("Osterferien"), date(2029, 3, 26), date(2029, 3, 31)),
                (tr("Beweglicher Ferientag"), date(2029, 4, 30), date(2029, 4, 30)),
                (tr("Pfingstferien"), date(2029, 5, 11), date(2029, 5, 25)),
                (tr("Sommerferien"), date(2029, 7, 21), date(2029, 8, 31)),
                (tr("Herbstferien"), date(2029, 10, 29), date(2029, 11, 2)),
                (tr("Weihnachtsferien"), date(2029, 12, 21), date(2029, 12, 31)),
            ]
        elif year == 2030:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2030, 1, 1), date(2030, 1, 5)),
                (tr("Winterferien"), date(2030, 2, 4), date(2030, 2, 8)),
                (tr("Osterferien"), date(2030, 4, 8), date(2030, 4, 20)),
                (tr("Beweglicher Ferientag"), date(2030, 5, 31), date(2030, 5, 31)),
                (tr("Pfingstferien"), date(2030, 6, 3), date(2030, 6, 8)),
                (tr("Sommerferien"), date(2030, 7, 13), date(2030, 8, 23)),
            ]

        for name, start, end in holidays_map:
            _add_holiday_range(name, start, end)

    def _add_school_holidays_bw(self, year):
        # Helper to add a range of holidays for Baden-Württemberg
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        holidays_map = []

        if year == 2025:
            holidays_map = [
                (tr("Sommerferien"), date(2025, 7, 31), date(2025, 9, 13)),
                (tr("Herbstferien"), date(2025, 10, 27), date(2025, 10, 30)),
                (tr("Weihnachtsferien"), date(2025, 12, 22), date(2025, 12, 31)),
            ]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 5)),
                (tr("Osterferien"), date(2026, 3, 30), date(2026, 4, 11)),
                (tr("Pfingstferien"), date(2026, 5, 26), date(2026, 6, 5)),
                (tr("Sommerferien"), date(2026, 7, 30), date(2026, 9, 12)),
                (tr("Herbstferien"), date(2026, 10, 26), date(2026, 10, 30)),
                (tr("Weihnachtsferien"), date(2026, 12, 23), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2027, 1, 1), date(2027, 1, 9)),
                (tr("Osterferien"), date(2027, 3, 30), date(2027, 4, 3)),
                (tr("Pfingstferien"), date(2027, 5, 18), date(2027, 5, 29)),
                (tr("Sommerferien"), date(2027, 7, 29), date(2027, 9, 11)),
                (tr("Herbstferien"), date(2027, 11, 2), date(2027, 11, 6)),
                (tr("Weihnachtsferien"), date(2027, 12, 23), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2028, 1, 1), date(2028, 1, 8)),
                (tr("Osterferien"), date(2028, 4, 18), date(2028, 4, 22)),
                (tr("Pfingstferien"), date(2028, 6, 6), date(2028, 6, 17)),
                (tr("Sommerferien"), date(2028, 7, 27), date(2028, 9, 9)),
                (tr("Herbstferien"), date(2028, 10, 30), date(2028, 11, 3)),
                (tr("Weihnachtsferien"), date(2028, 12, 23), date(2028, 12, 31)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2029, 1, 1), date(2029, 1, 5)),
                (tr("Osterferien"), date(2029, 3, 26), date(2029, 4, 7)),
                (tr("Pfingstferien"), date(2029, 5, 22), date(2029, 6, 1)),
                (tr("Sommerferien"), date(2029, 7, 26), date(2029, 9, 8)),
                (tr("Herbstferien"), date(2029, 10, 29), date(2029, 11, 2)),
                (tr("Weihnachtsferien"), date(2029, 12, 22), date(2029, 12, 31)),
            ]
        elif year == 2030:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2030, 1, 1), date(2030, 1, 5)),
                (tr("Osterferien"), date(2030, 4, 15), date(2030, 4, 26)),
                (tr("Pfingstferien"), date(2030, 6, 11), date(2030, 6, 21)),
            ]

        for name, start, end in holidays_map:
            _add_holiday_range(name, start, end)

    def _add_school_holidays_by(self, year):
        # Helper to add a range of holidays for Bayern (BY)
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        holidays_map = []

        if year == 2025:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2025, 12, 22), date(2025, 12, 31)),
            ]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 5)),
                (tr("Frühjahrsferien"), date(2026, 2, 16), date(2026, 2, 20)),
                (tr("Osterferien"), date(2026, 3, 30), date(2026, 4, 10)),
                (tr("Pfingstferien"), date(2026, 5, 26), date(2026, 6, 5)),
                (tr("Sommerferien"), date(2026, 8, 3), date(2026, 9, 14)),
                (
                    tr("Tage um Allerheiligen"),
                    date(2026, 11, 2),
                    date(2026, 11, 6),
                ),
                (tr("Weihnachtsferien"), date(2026, 12, 24), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2027, 1, 1), date(2027, 1, 8)),
                (tr("Frühjahrsferien"), date(2027, 2, 8), date(2027, 2, 12)),
                (tr("Osterferien"), date(2027, 3, 22), date(2027, 4, 2)),
                (tr("Pfingstferien"), date(2027, 5, 18), date(2027, 5, 28)),
                (tr("Sommerferien"), date(2027, 8, 2), date(2027, 9, 13)),
                (
                    tr(" Tage um Allerheiligen"),
                    date(2027, 11, 2),
                    date(2027, 11, 5),
                ),
                (tr("Weihnachtsferien"), date(2027, 12, 24), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2028, 1, 1), date(2028, 1, 7)),
                (tr("Frühjahrsferien"), date(2028, 2, 28), date(2028, 3, 3)),
                (tr("Osterferien"), date(2028, 4, 10), date(2028, 4, 21)),
                (tr("Pfingstferien"), date(2028, 6, 6), date(2028, 6, 16)),
                (tr("Sommerferien"), date(2028, 7, 31), date(2028, 9, 11)),
                (
                    tr("Tage um Allerheiligen"),
                    date(2028, 10, 30),
                    date(2028, 11, 3),
                ),
                (tr("Weihnachtsferien"), date(2028, 12, 23), date(2028, 12, 31)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2029, 1, 1), date(2029, 1, 5)),
                (tr("Frühjahrsferien"), date(2029, 2, 12), date(2029, 2, 16)),
                (tr("Osterferien"), date(2029, 3, 26), date(2029, 4, 6)),
                (tr("Pfingstferien"), date(2029, 5, 22), date(2029, 6, 1)),
                (tr("Sommerferien"), date(2029, 7, 30), date(2029, 9, 10)),
                (
                    tr("Tage um Allerheiligen"),
                    date(2029, 10, 29),
                    date(2029, 11, 2),
                ),
                (tr("Weihnachtsferien"), date(2029, 12, 24), date(2029, 12, 31)),
            ]
        elif year == 2030:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2030, 1, 1), date(2030, 1, 4)),
                (tr("Frühjahrsferien"), date(2030, 3, 4), date(2030, 3, 8)),
                (tr("Osterferien"), date(2030, 4, 15), date(2030, 4, 26)),
                (tr("Pfingstferien"), date(2030, 6, 11), date(2030, 6, 21)),
            ]

        for name, start, end in holidays_map:
            _add_holiday_range(name, start, end)

    def _add_school_holidays_be(self, year):
        # Helper to add a range of holidays for Berlin (BE)
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        holidays_map = []

        if year == 2025:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2025, 12, 22), date(2025, 12, 31)),
            ]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 2)),
                (tr("Winterferien"), date(2026, 2, 2), date(2026, 2, 7)),
                (tr("Osterferien"), date(2026, 3, 30), date(2026, 4, 10)),
                (tr("Unterrichtsfreier Tag nach AZVO"), date(2026, 5, 15), date(2026, 5, 15)),
                (tr("Pfingstferien"), date(2026, 5, 26), date(2026, 5, 26)),
                (tr("Sommerferien"), date(2026, 7, 9), date(2026, 8, 22)),
                (tr("Herbstferien"), date(2026, 10, 19), date(2026, 10, 31)),
                (tr("Weihnachtsferien"), date(2026, 12, 23), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2027, 1, 1), date(2027, 1, 2)),
                (tr("Winterferien"), date(2027, 2, 1), date(2027, 2, 6)),
                (tr("Osterferien"), date(2027, 3, 22), date(2027, 4, 2)),
                (tr("Unterrichtsfreier Tag nach AZVO"), date(2027, 5, 7), date(2027, 5, 7)),
                (tr("Pfingstferien"), date(2027, 5, 18), date(2027, 5, 19)),
                (tr("Sommerferien"), date(2027, 7, 1), date(2027, 8, 14)),
                (tr("Herbstferien"), date(2027, 10, 11), date(2027, 10, 23)),
                (tr("Weihnachtsferien"), date(2027, 12, 22), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2028, 1, 1), date(2028, 1, 2)),
                (tr("Winterferien"), date(2028, 1, 31), date(2028, 2, 5)),
                (tr("Osterferien"), date(2028, 4, 10), date(2028, 4, 22)),
                (tr("Unterrichtsfreier Tag nach AZVO"), date(2028, 5, 26), date(2028, 5, 26)),
                (tr("Pfingstferien"), date(2028, 6, 1), date(2028, 6, 2)),
                (tr("Sommerferien"), date(2028, 7, 1), date(2028, 8, 12)),
                (tr("Herbstferien"), date(2028, 10, 2), date(2028, 10, 14)),
                (tr("Weihnachtsferien"), date(2028, 12, 22), date(2028, 12, 31)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2029, 1, 1), date(2029, 1, 4)),
                (tr("Winterferien"), date(2029, 1, 29), date(2029, 2, 3)),
                (tr("Osterferien"), date(2029, 3, 26), date(2029, 4, 6)),
                (tr("Unterrichtsfreie Tage"), date(2029, 3, 9), date(2029, 3, 9)),
                (tr("Unterrichtsfreie Tage"), date(2029, 4, 30), date(2029, 4, 30)),
                (tr("Unterrichtsfreier Tag nach AZVO"), date(2029, 5, 11), date(2029, 5, 11)),
                (tr("Pfingstferien"), date(2029, 5, 22), date(2029, 5, 25)),
                (tr("Sommerferien"), date(2029, 7, 1), date(2029, 8, 11)),
                (tr("Herbstferien"), date(2029, 10, 1), date(2029, 10, 12)),
                (tr("Weihnachtsferien"), date(2029, 12, 21), date(2029, 12, 31)),
            ]
        elif year == 2030:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2030, 1, 1), date(2030, 1, 4)),
                (tr("Winterferien"), date(2030, 2, 4), date(2030, 2, 9)),
                (tr("Osterferien"), date(2030, 4, 15), date(2030, 4, 26)),
                (tr("Unterrichtsfreier Tag nach AZVO"), date(2030, 5, 31), date(2030, 5, 31)),
                (tr("Pfingstferien"), date(2030, 6, 7), date(2030, 6, 7)),
                (tr("Sommerferien"), date(2030, 7, 4), date(2030, 8, 17)),
            ]

        for name, start, end in holidays_map:
            _add_holiday_range(name, start, end)

    def _add_school_holidays_mv(self, year):
        # Helper to add a range of holidays for Mecklenburg-Vorpommern (MV)
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        holidays_map = []

        if year == 2025:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2025, 12, 20), date(2025, 12, 31)),
            ]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 3)),
                (tr("Winterferien"), date(2026, 2, 9), date(2026, 2, 20)),
                (tr("Osterferien"), date(2026, 3, 30), date(2026, 4, 8)),
                (tr("Pfingstferien"), date(2026, 5, 22), date(2026, 5, 26)),
                (tr("Zusätzliche feststehende Ferientage"), date(2026, 5, 15), date(2026, 5, 15)),
                (tr("Sommerferien"), date(2026, 7, 13), date(2026, 8, 22)),
                (tr("Herbstferien"), date(2026, 10, 15), date(2026, 10, 24)),
                (tr("Weihnachtsferien"), date(2026, 12, 21), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2027, 1, 1), date(2027, 1, 2)),
                (tr("Winterferien"), date(2027, 2, 8), date(2027, 2, 19)),
                (tr("Osterferien"), date(2027, 3, 24), date(2027, 4, 2)),
                (tr("Pfingstferien"), date(2027, 5, 14), date(2027, 5, 18)),
                (tr("Zusätzliche feststehende Ferientage"), date(2027, 5, 7), date(2027, 5, 7)),
                (tr("Sommerferien"), date(2027, 7, 5), date(2027, 8, 14)),
                (tr("Herbstferien"), date(2027, 10, 14), date(2027, 10, 23)),
                (tr("Weihnachtsferien"), date(2027, 12, 22), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2028, 1, 1), date(2028, 1, 2)),
                (tr("Winterferien"), date(2028, 2, 5), date(2028, 2, 17)),
                (tr("Osterferien"), date(2028, 4, 12), date(2028, 4, 21)),
                (tr("Pfingstferien"), date(2028, 6, 2), date(2028, 6, 6)),
                (tr("Zusätzliche feststehende Ferientage"), date(2028, 5, 26), date(2028, 5, 26)),
                (tr("Sommerferien"), date(2028, 6, 26), date(2028, 8, 5)),
                (tr("Herbstferien"), date(2028, 10, 23), date(2028, 10, 28)),
                (tr("Weihnachtsferien"), date(2028, 12, 22), date(2028, 12, 31)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2029, 1, 1), date(2029, 1, 4)),
                (tr("Winterferien"), date(2029, 2, 5), date(2029, 2, 16)),
                (tr("Osterferien"), date(2029, 3, 28), date(2029, 4, 6)),
                (tr("Pfingstferien"), date(2029, 5, 18), date(2029, 5, 22)),
                (tr("Zusätzliche feststehende Ferientage"), date(2029, 3, 9), date(2029, 3, 9)),
                (tr("Zusätzliche feststehende Ferientage"), date(2029, 4, 30), date(2029, 4, 30)),
                (tr("Zusätzliche feststehende Ferientage"), date(2029, 3, 30), date(2029, 3, 30)),
                (tr("Zusätzliche feststehende Ferientage"), date(2029, 4, 30), date(2029, 4, 30)),
                (tr("Zusätzliche feststehende Ferientage"), date(2029, 5, 11), date(2029, 5, 11)),
                (tr("Sommerferien"), date(2029, 6, 18), date(2029, 7, 28)),
                (tr("Herbstferien"), date(2029, 10, 22), date(2029, 10, 27)),
                (tr("Weihnachtsferien"), date(2029, 12, 21), date(2029, 12, 31)),
            ]
        elif year == 2030:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2030, 1, 1), date(2030, 1, 4)),
                (tr("Winterferien"), date(2030, 2, 4), date(2030, 2, 15)),
                (tr("Osterferien"), date(2030, 4, 17), date(2030, 4, 26)),
                (tr("Pfingstferien"), date(2030, 6, 7), date(2030, 6, 11)),
                (tr("Sommerferien"), date(2030, 7, 1), date(2030, 8, 10)),
            ]

        for name, start, end in holidays_map:
            _add_holiday_range(name, start, end)

    def _add_school_holidays_ni(self, year):
        # Helper to add a range of holidays for Niedersachsen (NI)
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        holidays_map = []

        if year == 2025:
            holidays_map = [(tr("Weihnachtsferien"), date(2025, 12, 22), date(2025, 12, 31))]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 5)),
                (tr("Halbjahresferien"), date(2026, 2, 2), date(2026, 2, 3)),
                (tr("Osterferien"), date(2026, 3, 23), date(2026, 4, 7)),
                (
                    tr("Ferien in Verbindung mit dem 1. Mai und Himmelfahrt"),
                    date(2026, 5, 15),
                    date(2026, 5, 15),
                ),
                (tr("Pfingstferien"), date(2026, 5, 26), date(2026, 5, 26)),
                (tr("Sommerferien"), date(2026, 7, 2), date(2026, 8, 12)),
                (tr("Herbstferien"), date(2026, 10, 12), date(2026, 10, 24)),
                (tr("Weihnachtsferien"), date(2026, 12, 23), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2027, 1, 1), date(2027, 1, 9)),
                (tr("Halbjahresferien"), date(2027, 2, 1), date(2027, 2, 2)),
                (tr("Osterferien"), date(2027, 3, 22), date(2027, 4, 3)),
                (
                    tr("Ferien in Verbindung mit dem 1. Mai und Himmelfahrt"),
                    date(2027, 5, 7),
                    date(2027, 5, 7),
                ),
                (tr("Pfingstferien"), date(2027, 5, 18), date(2027, 5, 18)),
                (tr("Sommerferien"), date(2027, 7, 8), date(2027, 8, 18)),
                (tr("Herbstferien"), date(2027, 10, 16), date(2027, 10, 30)),
                (tr("Weihnachtsferien"), date(2027, 12, 23), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2028, 1, 1), date(2028, 1, 8)),
                (tr("Halbjahresferien"), date(2028, 1, 31), date(2028, 2, 1)),
                (tr("Osterferien"), date(2028, 4, 10), date(2028, 4, 22)),
                (
                    tr("Ferien in Verbindung mit dem 1. Mai und Himmelfahrt"),
                    date(2028, 5, 26),
                    date(2028, 5, 26),
                ),
                (tr("Pfingstferien"), date(2028, 6, 6), date(2028, 6, 6)),
                (tr("Sommerferien"), date(2028, 7, 20), date(2028, 8, 30)),
                (tr("Herbstferien"), date(2028, 10, 2), date(2028, 10, 2)),
                (tr("Herbstferien"), date(2028, 10, 23), date(2028, 11, 4)),
                (tr("Weihnachtsferien"), date(2028, 12, 27), date(2028, 12, 31)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2029, 1, 1), date(2029, 1, 6)),
                (tr("Halbjahresferien"), date(2029, 2, 1), date(2029, 2, 2)),
                (tr("Osterferien"), date(2029, 3, 19), date(2029, 4, 3)),
                (
                    tr("Ferien in Verbindung mit dem 1. Mai und Himmelfahrt"),
                    date(2029, 4, 30),
                    date(2029, 4, 30),
                ),
                (
                    tr("Ferien in Verbindung mit dem 1. Mai und Himmelfahrt"),
                    date(2029, 5, 11),
                    date(2029, 5, 11),
                ),
                (tr("Pfingstferien"), date(2029, 5, 22), date(2029, 5, 22)),
                (tr("Sommerferien"), date(2029, 7, 19), date(2029, 8, 29)),
                (tr("Herbstferien"), date(2029, 10, 4), date(2029, 10, 5)),
                (tr("Herbstferien"), date(2029, 10, 22), date(2029, 11, 2)),
                (tr("Weihnachtsferien"), date(2029, 12, 21), date(2029, 12, 31)),
            ]
        elif year == 2030:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2030, 1, 1), date(2030, 1, 5)),
                (tr("Halbjahresferien"), date(2030, 1, 31), date(2030, 2, 1)),
                (tr("Osterferien"), date(2030, 4, 8), date(2030, 4, 23)),
                (
                    tr("Ferien in Verbindung mit dem 1. Mai und Himmelfahrt"),
                    date(2030, 5, 31),
                    date(2030, 5, 31),
                ),
                (tr("Pfingstferien"), date(2030, 6, 11), date(2030, 6, 11)),
                (tr("Sommerferien"), date(2030, 7, 11), date(2030, 8, 21)),
            ]

        for name, start, end in holidays_map:
            _add_holiday_range(name, start, end)

    def _add_school_holidays_bb(self, year):
        # Helper to add a range of holidays for Brandenburg (BB)
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        holidays_map = []

        if year == 2025:
            # Part of the 2025/2026 Christmas range (only 2025 portion)
            holidays_map = [
                (tr("Weihnachtsferien"), date(2025, 12, 22), date(2025, 12, 31)),
            ]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 2)),
                (tr("Winterferien"), date(2026, 2, 2), date(2026, 2, 7)),
                (tr("Osterferien"), date(2026, 3, 30), date(2026, 4, 10)),
                (tr("Pfingsten"), date(2026, 5, 26), date(2026, 5, 26)),
                (tr("Variabler Ferientag"), date(2026, 5, 13), date(2026, 5, 13)),
                (tr("Variabler Ferientag"), date(2026, 5, 15), date(2026, 5, 15)),
                (tr("Variabler Ferientag"), date(2026, 5, 18), date(2026, 5, 18)),
                (tr("Sommerferien"), date(2026, 7, 9), date(2026, 8, 22)),
                (tr("Herbstferien"), date(2026, 10, 19), date(2026, 10, 30)),
                (tr("Weihnachtsferien"), date(2026, 12, 23), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2027, 1, 1), date(2027, 1, 2)),
                (tr("Winterferien"), date(2027, 2, 1), date(2027, 2, 6)),
                (tr("Osterferien"), date(2027, 3, 22), date(2027, 4, 3)),
                (tr("Pfingsten"), date(2027, 5, 18), date(2027, 5, 18)),
                (tr("Variabler Ferientag"), date(2027, 5, 7), date(2027, 5, 7)),
                (tr("Sommerferien"), date(2027, 7, 1), date(2027, 8, 14)),
                (tr("Herbstferien"), date(2027, 10, 11), date(2027, 10, 23)),
                (tr("Weihnachtsferien"), date(2027, 12, 23), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Winterferien"), date(2028, 1, 31), date(2028, 2, 5)),
                (tr("Osterferien"), date(2028, 4, 10), date(2028, 4, 22)),
                (tr("Variabler Ferientag"), date(2028, 5, 26), date(2028, 5, 26)),
                (tr("Sommerferien"), date(2028, 6, 29), date(2028, 8, 12)),
                (tr("Herbstferien"), date(2028, 10, 2), date(2028, 10, 14)),
                (tr("Variabler Ferientag"), date(2028, 10, 30), date(2028, 10, 30)),
                (tr("Weihnachtsferien"), date(2028, 12, 22), date(2028, 12, 31)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2029, 1, 1), date(2029, 1, 2)),
                (tr("Winterferien"), date(2029, 1, 29), date(2029, 2, 3)),
                (tr("Osterferien"), date(2029, 3, 26), date(2029, 4, 6)),
                (tr("Pfingsten"), date(2029, 5, 22), date(2029, 5, 22)),
                (tr("Variabler Ferientag"), date(2029, 4, 30), date(2029, 4, 30)),
                (tr("Variabler Ferientag"), date(2029, 5, 11), date(2029, 5, 11)),
                (tr("Sommerferien"), date(2029, 6, 28), date(2029, 8, 11)),
            ]

        for name, start, end in holidays_map:
            _add_holiday_range(name, start, end)

    def _add_school_holidays_he(self, year):
        # Helper to add a range of holidays for Hessen (HE)
        def _add_holiday_range(name, start_date, end_date):
            current_date = start_date
            while current_date <= end_date:
                if current_date.year == self._year:
                    self._add_holiday(name, current_date.month, current_date.day)
                current_date += timedelta(days=1)

        holidays_map = []

        if year == 2025:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2025, 12, 22), date(2025, 12, 31)),
            ]
        elif year == 2026:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2026, 1, 1), date(2026, 1, 10)),
                (tr("Osterferien"), date(2026, 3, 30), date(2026, 4, 10)),
                (tr("Sommerferien"), date(2026, 6, 29), date(2026, 8, 7)),
                (tr("Herbstferien"), date(2026, 10, 5), date(2026, 10, 17)),
                (tr("Weihnachtsferien"), date(2026, 12, 23), date(2026, 12, 31)),
            ]
        elif year == 2027:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2027, 1, 1), date(2027, 1, 10)),
                (tr("Osterferien"), date(2027, 3, 22), date(2027, 4, 2)),
                (tr("Sommerferien"), date(2027, 6, 28), date(2027, 8, 6)),
                (tr("Herbstferien"), date(2027, 10, 4), date(2027, 10, 16)),
                (tr("Weihnachtsferien"), date(2027, 12, 23), date(2027, 12, 31)),
            ]
        elif year == 2028:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2028, 1, 1), date(2028, 1, 11)),
                (tr("Osterferien"), date(2028, 4, 3), date(2028, 4, 14)),
                (tr("Sommerferien"), date(2028, 7, 3), date(2028, 8, 11)),
                (tr("Herbstferien"), date(2028, 10, 9), date(2028, 10, 20)),
                (tr("Weihnachtsferien"), date(2028, 12, 27), date(2028, 12, 31)),
            ]
        elif year == 2029:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2029, 1, 1), date(2029, 1, 11)),
                (tr("Osterferien"), date(2029, 3, 29), date(2029, 4, 13)),
                (tr("Sommerferien"), date(2029, 7, 16), date(2029, 8, 24)),
                (tr("Herbstferien"), date(2029, 10, 15), date(2029, 10, 26)),
                (tr("Weihnachtsferien"), date(2029, 12, 24), date(2029, 12, 31)),
            ]
        elif year == 2030:
            holidays_map = [
                (tr("Weihnachtsferien"), date(2030, 1, 1), date(2030, 1, 11)),
                (tr("Osterferien"), date(2030, 4, 8), date(2030, 4, 22)),
                (tr("Sommerferien"), date(2030, 7, 22), date(2030, 8, 30)),
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
        if self.subdiv == "BB" and SCHOOL in self.categories:
            self._add_school_holidays_bb(year)
            for dt in list(self.keys()):
                if dt.year != year:
                    self.pop(dt)
        if self.subdiv == "HB" and SCHOOL in self.categories:
            self._add_school_holidays_hb(year)
            for dt in list(self.keys()):
                if dt.year != year:
                    self.pop(dt)
        if self.subdiv == "BW" and SCHOOL in self.categories:
            self._add_school_holidays_bw(year)
            for dt in list(self.keys()):
                if dt.year != year:
                    self.pop(dt)
        if self.subdiv == "BY" and SCHOOL in self.categories:
            self._add_school_holidays_by(year)
            for dt in list(self.keys()):
                if dt.year != year:
                    self.pop(dt)
        if self.subdiv == "BE" and SCHOOL in self.categories:
            self._add_school_holidays_be(year)
            for dt in list(self.keys()):
                if dt.year != year:
                    self.pop(dt)
        if self.subdiv == "MV" and SCHOOL in self.categories:
            self._add_school_holidays_mv(year)
            for dt in list(self.keys()):
                if dt.year != year:
                    self.pop(dt)
        if self.subdiv == "RP" and SCHOOL in self.categories:
            self._add_school_holidays_rp(year)
            for dt in list(self.keys()):
                if dt.year != year:
                    self.pop(dt)
        if self.subdiv == "SL" and SCHOOL in self.categories:
            self._add_school_holidays_sl(year)
            for dt in list(self.keys()):
                if dt.year != year:
                    self.pop(dt)
        if self.subdiv == "NI" and SCHOOL in self.categories:
            self._add_school_holidays_ni(year)
            for dt in list(self.keys()):
                if dt.year != year:
                    self.pop(dt)
        if self.subdiv == "NW" and SCHOOL in self.categories:
            self._add_school_holidays_nw(year)
            for dt in list(self.keys()):
                if dt.year != year:
                    self.pop(dt)
        if self.subdiv == "HE" and SCHOOL in self.categories:
            self._add_school_holidays_he(year)
            for dt in list(self.keys()):
                if dt.year != year:
                    self.pop(dt)
        if self.subdiv == "TH" and SCHOOL in self.categories:
            self._add_school_holidays_th(year)
            for dt in list(self.keys()):
                if dt.year != year:
                    self.pop(dt)
        if self.subdiv == "SH" and SCHOOL in self.categories:
            self._add_school_holidays_sh(year)
            for dt in list(self.keys()):
                if dt.year != year:
                    self.pop(dt)
        if self.subdiv == "SN" and SCHOOL in self.categories:
            self._add_school_holidays_sn(year)
            for dt in list(self.keys()):
                if dt.year != year:
                    self.pop(dt)
        if self.subdiv == "ST" and SCHOOL in self.categories:
            self._add_school_holidays_st(year)
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
