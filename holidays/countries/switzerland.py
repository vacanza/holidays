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

from holidays.calendars.gregorian import APR, THU, _timedelta, _get_nth_weekday_of_month
from holidays.constants import HALF_DAY, OPTIONAL, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, MON_ONLY, TUE_TO_NONE, SAT_TO_NONE


class Switzerland(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
        - https://www.bj.admin.ch/dam/bj/de/data/publiservice/service/zivilprozessrecht/kant-feiertage.pdf
        - https://de.wikipedia.org/wiki/Feiertage_in_der_Schweiz
        - https://en.wikipedia.org/wiki/Public_holidays_in_Switzerland
    """

    country = "CH"
    default_language = "de"
    subdivisions = (
        "AG",  # Aargau
        "AI",  # Appenzell Innerrhoden
        "AR",  # Appenzell Ausserrhoden
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
    supported_categories = (HALF_DAY, OPTIONAL, PUBLIC)
    supported_languages = ("de", "en_US", "fr", "it", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Neujahrestag"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Auffahrt"))

        # National Day.
        self._add_holiday_aug_1(tr("Nationalfeiertag"))

        # Christmas Day.
        self._add_christmas_day(tr("Weihnachten"))

    def _populate_subdiv_ag_public_holidays(self):
        # Berchtold's Day.
        self._add_new_years_day_two(tr("Berchtoldstag"))

        # Good Friday.
        self._add_good_friday(tr("Karfreitag"))

        # Easter Monday.
        self._add_easter_monday(tr("Ostermontag"))

        # Labor Day.
        self._add_labor_day(tr("Tag der Arbeit"))

        # Whit Monday.
        self._add_whit_monday(tr("Pfingstmontag"))

        # Corpus Christi.
        self._add_corpus_christi_day(tr("Fronleichnam"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Allerheiligen"))

        # Immaculate Conception.
        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

        # Saint Stephen's Day.
        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_ar_public_holidays(self):
        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_observed(
            self._add_christmas_day_two(tr("Stephanstag")), rule=TUE_TO_NONE + SAT_TO_NONE
        )

    def _populate_subdiv_ai_public_holidays(self):
        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_corpus_christi_day(tr("Fronleichnam"))

        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        self._add_all_saints_day(tr("Allerheiligen"))

        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

        self._add_observed(
            self._add_christmas_day_two(tr("Stephanstag")), rule=TUE_TO_NONE + SAT_TO_NONE
        )

    def _populate_subdiv_bl_public_holidays(self):
        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_labor_day(tr("Tag der Arbeit"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_bs_public_holidays(self):
        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_labor_day(tr("Tag der Arbeit"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_be_public_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_fr_public_holidays(self):
        self._add_good_friday(tr("Karfreitag"))

    def _populate_subdiv_fr_optional_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_ge_public_holidays(self):
        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        # Genevan Fast.
        self._add_holiday_4_days_past_1st_sun_of_sep(tr("Genfer Bettag"))

        # Restoration Day.
        self._add_holiday_dec_31(tr("Wiederherstellung der Republik"))

    def _populate_subdiv_gl_public_holidays(self):
        # Näfelser Fahrt (first Thursday in April but not in Holy Week)
        if self._year >= 1835:
            dt = _get_nth_weekday_of_month(1, THU, APR, self._year)
            self._add_holiday(
                # Battle of Naefels Victory Day.
                tr("Näfelser Fahrt"),
                _timedelta(dt, +7) if dt == _timedelta(self._easter_sunday, -3) else dt,
            )

        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_all_saints_day(tr("Allerheiligen"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_gl_optional_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

    def _populate_subdiv_gr_public_holidays(self):
        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_gr_optional_holidays(self):
        self._add_good_friday(tr("Karfreitag"))

    def _populate_subdiv_ju_public_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_labor_day(tr("Tag der Arbeit"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_corpus_christi_day(tr("Fronleichnam"))

        # Independence Day.
        self._add_holiday_jun_23(tr("Fest der Unabhängigkeit"))

        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_lu_public_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_corpus_christi_day(tr("Fronleichnam"))

        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        self._add_all_saints_day(tr("Allerheiligen"))

        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_ne_public_holidays(self):
        self._add_observed(
            self._add_new_years_day_two(tr("Berchtoldstag")),
            rule=MON_ONLY,  # Jan 2 is public holiday only when it falls on Monday.
        )

        # Republic Day.
        self._add_holiday_mar_1(tr("Jahrestag der Ausrufung der Republik"))

        self._add_good_friday(tr("Karfreitag"))

        self._add_labor_day(tr("Tag der Arbeit"))

        self._add_corpus_christi_day(tr("Fronleichnam"))

        self._add_observed(self._add_christmas_day_two(tr("Stephanstag")), rule=MON_ONLY)

    def _populate_subdiv_nw_public_holidays(self):
        # Saint Joseph's Day.
        self._add_saint_josephs_day(tr("Josefstag"))

        self._add_good_friday(tr("Karfreitag"))

        self._add_corpus_christi_day(tr("Fronleichnam"))

        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        self._add_all_saints_day(tr("Allerheiligen"))

        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

    def _populate_subdiv_nw_optional_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_ow_public_holidays(self):
        self._add_good_friday(tr("Karfreitag"))

        self._add_corpus_christi_day(tr("Fronleichnam"))

        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        # Saint Nicholas of Flüe.
        self._add_holiday_sep_25(tr("Bruder Klaus"))

        self._add_all_saints_day(tr("Allerheiligen"))

        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

    def _populate_subdiv_ow_optional_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_sg_public_holidays(self):
        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_all_saints_day(tr("Allerheiligen"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_sg_optional_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

    def _populate_subdiv_sh_public_holidays(self):
        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_labor_day(tr("Tag der Arbeit"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_sh_optional_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

    def _populate_subdiv_sz_public_holidays(self):
        # Epiphany.
        self._add_epiphany_day(tr("Heilige Drei Könige"))

        self._add_saint_josephs_day(tr("Josefstag"))

        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_corpus_christi_day(tr("Fronleichnam"))

        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        self._add_all_saints_day(tr("Allerheiligen"))

        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_so_public_holidays(self):
        self._add_good_friday(tr("Karfreitag"))

    def _populate_subdiv_so_half_day_holidays(self):
        self._add_labor_day(tr("Tag der Arbeit"))

    def _populate_subdiv_so_optional_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

    def _populate_subdiv_tg_public_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

        self._add_labor_day(tr("Tag der Arbeit"))

        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_ti_public_holidays(self):
        self._add_epiphany_day(tr("Heilige Drei Könige"))

        self._add_saint_josephs_day(tr("Josefstag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_labor_day(tr("Tag der Arbeit"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_corpus_christi_day(tr("Fronleichnam"))

        # Saints Peter and Paul.
        self._add_saints_peter_and_paul_day(tr("Peter und Paul"))

        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        self._add_all_saints_day(tr("Allerheiligen"))

        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_ur_public_holidays(self):
        self._add_epiphany_day(tr("Heilige Drei Könige"))

        self._add_saint_josephs_day(tr("Josefstag"))

        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_corpus_christi_day(tr("Fronleichnam"))

        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        self._add_all_saints_day(tr("Allerheiligen"))

        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

        self._add_observed(
            self._add_christmas_day_two(tr("Stephanstag")), rule=TUE_TO_NONE + SAT_TO_NONE
        )

    def _populate_subdiv_vd_public_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        # Prayer Monday.
        self._add_holiday_1_day_past_3rd_sun_of_sep(tr("Bettagsmontag"))

    def _populate_subdiv_vs_public_holidays(self):
        self._add_saint_josephs_day(tr("Josefstag"))

        self._add_corpus_christi_day(tr("Fronleichnam"))

        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        self._add_all_saints_day(tr("Allerheiligen"))

        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

    def _populate_subdiv_vs_optional_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_zg_public_holidays(self):
        self._add_good_friday(tr("Karfreitag"))

        self._add_corpus_christi_day(tr("Fronleichnam"))

        self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        self._add_all_saints_day(tr("Allerheiligen"))

        self._add_immaculate_conception_day(tr("Mariä Empfängnis"))

    def _populate_subdiv_zg_optional_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_christmas_day_two(tr("Stephanstag"))

    def _populate_subdiv_zh_public_holidays(self):
        self._add_new_years_day_two(tr("Berchtoldstag"))

        self._add_good_friday(tr("Karfreitag"))

        self._add_easter_monday(tr("Ostermontag"))

        self._add_labor_day(tr("Tag der Arbeit"))

        self._add_whit_monday(tr("Pfingstmontag"))

        self._add_christmas_day_two(tr("Stephanstag"))


class CH(Switzerland):
    pass


class CHE(Switzerland):
    pass
