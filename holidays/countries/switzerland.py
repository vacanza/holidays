#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import timedelta as td
from gettext import gettext as tr

from holidays.calendars.gregorian import APR, THU, _get_nth_weekday_of_month
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Switzerland(HolidayBase, ChristianHolidays, InternationalHolidays):
    country = "CH"
    default_language = "de"
    subdivisions = (
        "AG",  # Aargau
        "AR",  # Appenzell Ausserrhoden
        "AI",  # Appenzell Innerrhoden
        "BL",  # Basel-Landschaft
        "BS",  # Basel-Stadt
        "BE",  # Bern
        "FR",  # Fribourg
        "GE",  # Geneva
        "GL",  # Glarus
        "GR",  # Graubünden
        "JU",  # Jura
        "LU",  # Luzern
        "NE",  # Neuchâtel
        "NW",  # Nidwalden
        "OW",  # Obwalden
        "SG",  # St. Gallen
        "SH",  # Schaffhausen
        "SZ",  # Schwyz
        "SO",  # Solothurn
        "TG",  # Thurgau
        "TI",  # Ticino
        "UR",  # Uri
        "VD",  # Vaud
        "VS",  # Valais
        "ZG",  # Zug
        "ZH",  # Zürich
    )
    supported_languages = ("de", "en_US", "fr", "it", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day(tr("Neujahrestag"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Ostern"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Auffahrt"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Pfingsten"))

        if year >= 1291:
            # National Day.
            self._add_holiday_aug_1(tr("Nationalfeiertag"))

        # Christmas Day.
        self._add_christmas_day(tr("Weihnachten"))

    def _add_subdiv_holidays(self):
        if not self.subdiv:
            return None

        if self.subdiv != "VS":
            # Good Friday.
            self._add_good_friday(tr("Karfreitag"))

            # Easter Monday.
            self._add_easter_monday(tr("Ostermontag"))

            # Whit Monday.
            self._add_whit_monday(tr("Pfingstmontag"))

        if self.subdiv not in {"GE", "JU", "NE", "VD", "VS"}:
            # St. Stephen's Day.
            self._add_christmas_day_two(tr("Stephanstag"))

        super()._add_subdiv_holidays()

    def _add_subdiv_ag_holidays(self):
        # Berchtold's Day.
        self._add_new_years_day_two(tr("Berchtoldstag"))

    def _add_subdiv_ar_holidays(self):
        pass

    def _add_subdiv_ai_holidays(self):
        # Corpus Christi.
        self._add_corpus_christi_day(tr("Fronleichnam"))

        # Assumption of Mary.
        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Allerheiligen"))

        # Immaculate Conception.
        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

    def _add_subdiv_bl_holidays(self):
        # Labor Day.
        self._add_labor_day(tr("Tag der Arbeit"))

    def _add_subdiv_bs_holidays(self):
        self._add_labor_day(tr("Tag der Arbeit"))

    def _add_subdiv_be_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

    def _add_subdiv_fr_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

    def _add_subdiv_ge_holidays(self):
        # Thursday after the first Sunday of September
        # Genevan Fast.
        self._add_holiday_4_days_past_1st_sun_of_sep(tr("Genfer Bettag"))

        # Restoration Day.
        self._add_holiday_dec_31(tr("Wiederherstellung der Republik"))

    def _add_subdiv_gl_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

        # Näfelser Fahrt (first Thursday in April but not in Holy Week)
        if self._year >= 1835:
            dt = _get_nth_weekday_of_month(1, THU, APR, self._year)
            self._add_holiday(
                # Battle of Naefels Victory Day.
                tr("Näfelser Fahrt"),
                dt + td(days=+7) if dt == self._easter_sunday + td(days=-3) else dt,
            )

        self._add_all_saints_day(tr("Allerheiligen"))

    def _add_subdiv_gr_holidays(self):
        pass

    def _add_subdiv_ju_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))
        self._add_labor_day(tr("Tag der Arbeit"))
        self._add_corpus_christi_day(tr("Fronleichnam"))

        # Independence Day.
        self._add_holiday_jun_23(tr("Fest der Unabhängigkeit"))
        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))
        self._add_all_saints_day(tr("Allerheiligen"))

    def _add_subdiv_lu_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))
        self._add_corpus_christi_day(tr("Fronleichnam"))
        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))
        self._add_all_saints_day(tr("Allerheiligen"))
        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

    def _add_subdiv_ne_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

        # Republic Day.
        self._add_holiday_mar_1(tr("Jahrestag der Ausrufung der Republik"))
        self._add_labor_day(tr("Tag der Arbeit"))

        if self._is_sunday(self._christmas_day):
            self._add_christmas_day_two(tr("Stephanstag"))

    def _add_subdiv_nw_holidays(self):
        # St. Joseph's Day.
        self._add_saint_josephs_day(tr("Josefstag"))
        self._add_corpus_christi_day(tr("Fronleichnam"))
        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))
        self._add_all_saints_day(tr("Allerheiligen"))
        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

    def _add_subdiv_ow_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))
        self._add_corpus_christi_day(tr("Fronleichnam"))
        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        # St. Nicholas of Flüe.
        self._add_holiday_sep_25(tr("Bruder Klaus"))
        self._add_all_saints_day(tr("Allerheiligen"))
        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

    def _add_subdiv_sg_holidays(self):
        self._add_all_saints_day(tr("Allerheiligen"))

    def _add_subdiv_sh_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))
        self._add_labor_day(tr("Tag der Arbeit"))

    def _add_subdiv_sz_holidays(self):
        # Epiphany.
        self._add_epiphany_day(tr("Heilige Drei Könige"))
        self._add_saint_josephs_day(tr("Josefstag"))
        self._add_corpus_christi_day(tr("Fronleichnam"))
        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))
        self._add_all_saints_day(tr("Allerheiligen"))
        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

    def _add_subdiv_so_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))
        self._add_labor_day(tr("Tag der Arbeit"))

    def _add_subdiv_tg_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))
        self._add_labor_day(tr("Tag der Arbeit"))

    def _add_subdiv_ti_holidays(self):
        self._add_epiphany_day(tr("Heilige Drei Könige"))
        self._add_saint_josephs_day(tr("Josefstag"))
        self._add_labor_day(tr("Tag der Arbeit"))
        self._add_corpus_christi_day(tr("Fronleichnam"))

        # Saints Peter and Paul.
        self._add_saints_peter_and_paul_day(tr("Peter und Paul"))
        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))
        self._add_all_saints_day(tr("Allerheiligen"))
        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

    def _add_subdiv_ur_holidays(self):
        self._add_epiphany_day(tr("Heilige Drei Könige"))
        self._add_saint_josephs_day(tr("Josefstag"))
        self._add_corpus_christi_day(tr("Fronleichnam"))
        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))
        self._add_all_saints_day(tr("Allerheiligen"))
        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

    def _add_subdiv_vd_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

        # Monday after the third Sunday of September
        # Prayer Monday.
        self._add_holiday_1_day_past_3rd_sun_of_sep(tr("Bettagsmontag"))

    def _add_subdiv_vs_holidays(self):
        self._add_saint_josephs_day(tr("Josefstag"))
        self._add_corpus_christi_day(tr("Fronleichnam"))
        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))
        self._add_all_saints_day(tr("Allerheiligen"))
        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

    def _add_subdiv_zg_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))
        self._add_corpus_christi_day(tr("Fronleichnam"))
        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))
        self._add_all_saints_day(tr("Allerheiligen"))
        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

    def _add_subdiv_zh_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))
        self._add_labor_day(tr("Tag der Arbeit"))


class CH(Switzerland):
    pass


class CHE(Switzerland):
    pass
