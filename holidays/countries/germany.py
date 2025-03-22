#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars.gregorian import MAY, JUN, OCT
from holidays.constants import CATHOLIC, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class Germany(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Germany holidays.

    This class doesn't return any holidays before 1990-10-03.

    Before that date the current Germany was separated into the "German Democratic
    Republic" and the "Federal Republic of Germany" which both had somewhat
    different holidays. Since this class is called "Germany" it doesn't really
     make sense to include the days from the two former countries.

    "Mariä Himmelfahrt" is only a holiday in Bavaria (BY) and "Fronleichnam"
    in Saxony (SN) and Thuringia (TH) if municipality is mostly catholic which
    in term depends on census data. It's listed in "CATHOLIC" category for these provinces.
    """

    country = "DE"
    default_language = "de"
    supported_categories = (CATHOLIC, PUBLIC)
    supported_languages = ("de", "en_US", "th", "uk")
    subdivisions = (
        # ISO 3166-2:DE
        "BB",
        "BE",
        "BW",
        "BY",
        "HB",
        "HE",
        "HH",
        "MV",
        "NI",
        "NW",
        "RP",
        "SH",
        "SL",
        "SN",
        "ST",
        "TH",
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
    _deprecated_subdivisions = ("BYP",)
    start_year = 1990

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, GermanyStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year >= 1991:
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
        if self._year >= 1991:
            # Easter Sunday.
            self._add_easter_sunday(tr("Ostersonntag"))

            # Whit Sunday.
            self._add_whit_sunday(tr("Pfingstsonntag"))

        # Reformation Day.
        self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_be_public_holidays(self):
        if self._year >= 2019:
            # International Women's Day.
            self._add_womens_day(tr("Internationaler Frauentag"))

    def _populate_subdiv_bw_public_holidays(self):
        if self._year >= 1991:
            # Epiphany.
            self._add_epiphany_day(tr("Heilige Drei Könige"))

            # Corpus Christi.
            self._add_corpus_christi_day(tr("Fronleichnam"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_by_public_holidays(self):
        if self._year >= 1991:
            self._add_epiphany_day(tr("Heilige Drei Könige"))
            self._add_corpus_christi_day(tr("Fronleichnam"))

        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_by_catholic_holidays(self):
        if self._year >= 1991:
            # Assumption Day.
            self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

    def _populate_subdiv_hb_public_holidays(self):
        if self._year >= 2018:
            self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_he_public_holidays(self):
        if self._year >= 1991:
            self._add_corpus_christi_day(tr("Fronleichnam"))

    def _populate_subdiv_hh_public_holidays(self):
        if self._year >= 2018:
            self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_mv_public_holidays(self):
        if self._year >= 2023:
            self._add_womens_day(tr("Internationaler Frauentag"))

        self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_ni_public_holidays(self):
        if self._year >= 2018:
            self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_nw_public_holidays(self):
        if self._year >= 1991:
            self._add_corpus_christi_day(tr("Fronleichnam"))

        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_rp_public_holidays(self):
        if self._year >= 1991:
            self._add_corpus_christi_day(tr("Fronleichnam"))

        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_sh_public_holidays(self):
        if self._year >= 2018:
            self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_sl_public_holidays(self):
        if self._year >= 1991:
            self._add_corpus_christi_day(tr("Fronleichnam"))
            self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_sn_public_holidays(self):
        self._add_holiday_oct_31(tr("Reformationstag"))

        if self._year >= 1995:
            self._add_holiday_1st_wed_before_nov_22(tr("Buß- und Bettag"))

    def _populate_subdiv_sn_catholic_holidays(self):
        if self._year >= 1991:
            self._add_corpus_christi_day(tr("Fronleichnam"))

    def _populate_subdiv_st_public_holidays(self):
        if self._year >= 1991:
            self._add_epiphany_day(tr("Heilige Drei Könige"))

        self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_th_public_holidays(self):
        if self._year >= 2019:
            # World Children's Day.
            self._add_holiday_sep_20(tr("Weltkindertag"))

        self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_th_catholic_holidays(self):
        if self._year >= 1991:
            self._add_corpus_christi_day(tr("Fronleichnam"))


class DE(Germany):
    pass


class DEU(Germany):
    pass


class GermanyStaticHolidays:
    """
    References:

    * <https://www.stuttgarter-zeitung.de/inhalt.reformationstag-2017-einmalig-bundesweiter-feiertag.b7e189b3-a33d-41a3-a0f4-141cd13df54e.html>
    * <https://www.bbc.com/news/world-europe-52574748>
    * <https://gesetze.berlin.de/bsbe/document/jlr-FeiertGBEV8P1>
    """

    special_public_holidays = {
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
