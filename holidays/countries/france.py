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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class France(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Official French holidays.

    Some provinces have specific holidays, only those are included in the
    PROVINCES, because these provinces have different administrative status,
    which makes it difficult to enumerate.

    For religious holidays usually happening on Sundays (Easter, Pentecost),
    only the following Monday is considered a holiday.

    Primary sources:
        https://fr.wikipedia.org/wiki/Fêtes_et_jours_fériés_en_France
        https://www.service-public.fr/particuliers/vosdroits/F2405
    """

    country = "FR"
    default_language = "fr"
    supported_languages = ("en_US", "fr", "uk")
    subdivisions = (
        "BL",  # Saint-Barthélemy.
        "GES",  # Alsace, Champagne-Ardenne, Lorraine(Moselle).
        "GP",  # Guadeloupe.
        "GY",  # Guyane.
        "MF",  # Saint-Martin.
        "MQ",  # Martinique.
        "NC",  # Nouvelle-Calédonie,
        "PF",  # Polynésie Française.
        "RE",  # La Réunion.
        "WF",  # Wallis-et-Futuna.
        "YT",  # Mayotte.
    )
    subdivisions_aliases = {
        "Saint-Barthélemy": "BL",
        "Alsace": "GES",
        "Champagne-Ardenne": "GES",
        "Lorraine": "GES",
        "Guadeloupe": "GP",
        "Guyane": "GY",
        "Saint-Martin": "MF",
        "Martinique": "MQ",
        "Nouvelle-Calédonie": "NC",
        "Polynésie Française": "PF",
        "La Réunion": "RE",
        "Wallis-et-Futuna": "WF",
        "Mayotte": "YT",
    }

    _deprecated_subdivisions = (
        "Alsace-Moselle",
        "Guadeloupe",
        "Guyane",
        "La Réunion",
        "Martinique",
        "Mayotte",
        "Métropole",
        "Nouvelle-Calédonie",
        "Polynésie Française",
        "Saint-Barthélémy",
        "Saint-Martin",
        "Wallis-et-Futuna",
    )
    start_year = 1801

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Civil holidays.
        if self._year >= 1811:
            # New Year's Day.
            self._add_new_years_day(tr("Jour de l'an"))

        if self._year >= 1919:
            self._add_labor_day(
                # Labor Day.
                tr("Fête du Travail")
                if self._year >= 1948
                # Labor and Social Concord Day.
                else tr("Fête du Travail et de la Concorde sociale")
            )

        if 1953 <= self._year <= 1959 or self._year >= 1982:
            # Victory Day.
            self._add_world_war_two_victory_day(tr("Fête de la Victoire"))

        if self._year >= 1880:
            # National Day.
            self._add_holiday_jul_14(tr("Fête nationale"))

        if self._year >= 1918:
            # Armistice Day.
            self._add_holiday_nov_11(tr("Armistice"))

        # Religious holidays.

        if self._year >= 1886:
            # Easter Monday.
            self._add_easter_monday(tr("Lundi de Pâques"))

            if self._year not in {2005, 2006, 2007}:
                # Whit Monday.
                self._add_whit_monday(tr("Lundi de Pentecôte"))

        if self._year >= 1802:
            # Ascension Day.
            self._add_ascension_thursday(tr("Ascension"))
            # Assumption Day.
            self._add_assumption_of_mary_day(tr("Assomption"))
            # All Saints' Day.
            self._add_all_saints_day(tr("Toussaint"))
            # Christmas Day.
            self._add_christmas_day(tr("Noël"))

        if self.subdiv == "Alsace-Moselle":
            self._populate_subdiv_ges_public_holidays()
        elif self.subdiv == "Guadeloupe":
            self._populate_subdiv_gp_public_holidays()
        elif self.subdiv == "Guyane":
            self._populate_subdiv_gy_public_holidays()
        elif self.subdiv == "La Réunion":
            self._populate_subdiv_re_public_holidays()
        elif self.subdiv == "Martinique":
            self._populate_subdiv_mq_public_holidays()
        elif self.subdiv == "Mayotte":
            self._populate_subdiv_yt_public_holidays()
        elif self.subdiv == "Nouvelle-Calédonie":
            self._populate_subdiv_nc_public_holidays()
        elif self.subdiv == "Polynésie Française":
            self._populate_subdiv_pf_public_holidays()
        elif self.subdiv == "Saint-Barthélémy":
            self._populate_subdiv_bl_public_holidays()
        elif self.subdiv == "Saint-Martin":
            self._populate_subdiv_mf_public_holidays()
        elif self.subdiv == "Wallis-et-Futuna":
            self._populate_subdiv_wf_public_holidays()

    # Saint Barthelemy.
    def _populate_subdiv_bl_public_holidays(self):
        # Abolition of slavery.
        self._add_holiday_oct_9(tr("Abolition de l'esclavage"))

    # Alsace, Champagne-Ardenne, Lorraine(Moselle).
    def _populate_subdiv_ges_public_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Vendredi saint"))

        # Saint Stephen's Day.
        self._add_christmas_day_two(tr("Saint Étienne"))

    # Guadeloupe.
    def _populate_subdiv_gp_public_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Vendredi saint"))

        # Mi-Careme.
        self._add_holiday_24_days_prior_easter(tr("Mi-Carême"))

        # Abolition of slavery.
        self._add_holiday_may_27(tr("Abolition de l'esclavage"))

        # Feast of Victor Schoelcher.
        self._add_holiday_jul_21(tr("Fête de Victor Schoelcher"))

    # Guyane.
    def _populate_subdiv_gy_public_holidays(self):
        # Abolition of slavery.
        self._add_holiday_jun_10(tr("Abolition de l'esclavage"))

    # Saint Martin.
    def _populate_subdiv_mf_public_holidays(self):
        if self._year >= 2018:
            # Abolition of slavery.
            self._add_holiday_may_28(tr("Abolition de l'esclavage"))

    # Martinique.
    def _populate_subdiv_mq_public_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Vendredi saint"))

        # Abolition of slavery.
        self._add_holiday_may_22(tr("Abolition de l'esclavage"))

        # Feast of Victor Schoelcher.
        self._add_holiday_jul_21(tr("Fête de Victor Schoelcher"))

    # New Caledonia.
    def _populate_subdiv_nc_public_holidays(self):
        # Citizenship Day.
        self._add_holiday_sep_24(tr("Fête de la Citoyenneté"))

    # French Polynesia.
    def _populate_subdiv_pf_public_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Vendredi saint"))

        # Missionary Day.
        self._add_holiday_mar_5(tr("Arrivée de l'Évangile"))

        # Internal Autonomy Day.
        self._add_holiday_jun_29(tr("Fête de l'autonomie"))

    # Reunion.
    def _populate_subdiv_re_public_holidays(self):
        if self._year >= 1981:
            # Abolition of slavery.
            self._add_holiday_dec_20(tr("Abolition de l'esclavage"))

    #  Wallis and Futuna.
    def _populate_subdiv_wf_public_holidays(self):
        # Feast of Saint Peter Chanel.
        self._add_holiday_apr_28(tr("Saint Pierre Chanel"))

        # Festival of the territory.
        self._add_holiday_jul_29(tr("Fête du Territoire"))

    # Mayotte.
    def _populate_subdiv_yt_public_holidays(self):
        # Abolition of slavery.
        self._add_holiday_apr_27(tr("Abolition de l'esclavage"))


class FR(France):
    """FR is also used by dateutil (Friday), so be careful with this one."""

    pass


class FRA(France):
    pass
