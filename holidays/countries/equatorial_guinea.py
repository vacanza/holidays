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

from holidays.calendars.gregorian import JAN
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_MON


class EquatorialGuinea(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """Equatorial Guinea holidays.

    References:
       * [Decree 9/2007](https://web.archive.org/web/20250518185011/https://boe.gob.gq/files/Decreto%20de%20Fijaci%C3%B3n%20de%20los%20D%C3%ADas%20Feriados%20en%20Guinea%20Ecuatorial.pdf)
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Equatorial_Guinea>
        * <https://web.archive.org/web/20250503042253/https://www.timeanddate.com/holidays/guineaecuatorial/>
        * <https://web.archive.org/web/20250503042610/https://gq.usembassy.gov/holiday-calendar/>
        * [2015](https://web.archive.org/web/20250421105147/https://www.guineainfomarket.com/gobierno/2015/01/01/calendario-laboral-de-guinea-ecuatorial-2015/)
        * [2016](https://web.archive.org/web/20250212174334/https://www.guineainfomarket.com/libros/2015/12/06/calendario-laboral-de-guinea-ecuatorial-2016/)
        * [2018](https://web.archive.org/web/20241005004303/https://www.guineainfomarket.com/economia/2017/12/29/calendario-laboral-guinea-ecuatorial-2018/)
        * [2019](https://web.archive.org/web/20220526022213/https://www.guineainfomarket.com/economia/2019/01/01/calendario-laboral-guinea-ecuatorial-2019/)
        * [2020](https://web.archive.org/web/20250503044753/https://www.guineainfomarket.com/cultura/2020/01/01/calendario-laboral-de-guinea-ecuatorial-2020/)
        * [2021](https://web.archive.org/web/20250503044727/https://www.guineainfomarket.com/cultura/2021/01/29/calendario-laboral-de-guinea-ecuatorial-2021/)
        * [2022](https://web.archive.org/web/20250503044746/https://www.guineainfomarket.com/cultura/2021/01/29/calendario-laboral-de-guinea-ecuatorial-2021-2/)
        * [2024](https://web.archive.org/web/20250504175804/https://www.guineainfomarket.com/business/2024/03/29/calendario-laboral-de-guinea-ecuatorial-2024/)
    """

    country = "GQ"
    default_language = "es"
    supported_languages = ("en_US", "es")
    # %s observed.
    observed_label = tr("%s (observado)")
    # Decree 9/2007.
    start_year = 2007
    subdivisions = (
        # Provinces.
        "AN",  # Annobón (Annobon).
        # Cities.
        "Akurenam",
        "Akonibe",
        "Anisok",
        "Ayene",
        "Baney",
        "Bata",
        "Bidja-Bidjan",
        "Bikurga",
        "Bitika",
        "Ebebiyin",
        "Kogo",
        "Luba",
        "Machinda",
        "Malabo",
        "Mbini",
        "Mikomeseng",
        "Mongomeyen",
        "Mongomo",
        "Niefang",
        "Nkimi",
        "Nkue",
        "Nsok-Nsomo",
        "Nsork",
        "Rebola",
    )

    subdivisions_aliases = {"Annobón": "AN", "Annobon": "AN", "Añisok": "Anisok"}

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=EquatorialGuineaStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("Año Nuevo")))

        # International Women's Day.
        self._add_womens_day(tr("Día Internacional de la Mujer"))

        # Maundy Thursday.
        self._add_holy_thursday(tr("Jueves Santo"))

        # Good Friday.
        self._add_good_friday(tr("Viernes Santo"))

        # International Labor Day.
        self._add_observed(self._add_labor_day(tr("Día Internacional del Trabajo")))

        # African Liberation Day.
        self._add_holiday_may_25(tr("Día de la liberación Africana"))

        self._add_observed(
            # President's Day.
            self._add_holiday_jun_5(tr("Natalicio de Su Excelencia el Presidente de la República"))
        )

        # Corpus Christi.
        self._add_corpus_christi_day(tr("Corpus Christi"))

        # Armed Forces Day.
        self._add_observed(self._add_holiday_aug_3(tr("Día de las Fuerzas Armadas")))

        # Constitution Day.
        self._add_observed(self._add_holiday_aug_15(tr("Día de la Constitución")))

        # Independence Day.
        self._add_observed(self._add_holiday_oct_12(tr("Día de la Independencia Nacional")))

        self._add_observed(
            self._add_immaculate_conception_day(
                # Immaculate Conception.
                tr("Festividad de la Inmaculada Concepción de María")
            )
        )

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Día de Navidad")))

    def _populate_subdiv_an_public_holidays(self):
        # Patron Saint Festival of Annobón.
        self._add_holiday_jun_13(tr("Fiesta Patronal de Annobón"))

    def _populate_subdiv_akurenam_public_holidays(self):
        # Saint Barbara
        self._add_holiday_dec_4(tr("Santa Bárbara"))

    def _populate_subdiv_akonibe_public_holidays(self):
        # Saint Pius X.
        self._add_holiday_aug_21(tr("Santo Pío X"))

    def _populate_subdiv_anisok_public_holidays(self):
        # Saints Peter and Paul.
        self._add_holiday_jun_29(tr("Santos Pedro y Pablo"))

    def _populate_subdiv_ayene_public_holidays(self):
        # Our Lady of the Assumption.
        self._add_holiday_aug_15(tr("Nuestra Señora de Asunción"))

    def _populate_subdiv_baney_public_holidays(self):
        # Santiago Apóstol.
        self._add_holiday_jul_25(tr("Santiago Apóstol"))

    def _populate_subdiv_bata_public_holidays(self):
        # Santiago Apóstol.
        self._add_holiday_jul_25(tr("Santiago Apóstol"))

    def _populate_subdiv_bidja_bidjan_public_holidays(self):
        # Exaltation of the Holy Cross.
        self._add_holiday_sep_14(tr("Exaltación de la Santa Cruz"))

    def _populate_subdiv_bikurga_public_holidays(self):
        # Assumption of Our Lady.
        self._add_holiday_aug_15(tr("Asunción de Nuestra Señora"))

    def _populate_subdiv_bitika_public_holidays(self):
        # Saint Teresa of Jesus.
        self._add_holiday_oct_15(tr("Santa Teresa de Jesús"))

    def _populate_subdiv_ebebiyin_public_holidays(self):
        # Saint Peter Claver.
        self._add_holiday_sep_9(tr("San Pedro Claver"))

    def _populate_subdiv_kogo_public_holidays(self):
        # Our Lady of Carmen.
        self._add_holiday_jul_15(tr("Nuestra Señora del Carmen"))

    def _populate_subdiv_luba_public_holidays(self):
        # Our Lady of Montserrat.
        self._add_holiday_apr_27(tr("Nuestra Señora de Montserrat"))

    def _populate_subdiv_machinda_public_holidays(self):
        # Holy Family.
        self._add_holiday_dec_30(tr("Sagrada Familia"))

    def _populate_subdiv_malabo_public_holidays(self):
        # Feast of Santa Isabel.
        self._add_holiday_nov_17(tr("Fiesta de Santa Isabel"))

    def _populate_subdiv_mbini_public_holidays(self):
        # Immaculate Heart of Mary.
        self._add_holiday_aug_22(tr("Inmaculada Corazón de Maria"))

    def _populate_subdiv_mikomeseng_public_holidays(self):
        # Virgin of Africa.
        self._add_holiday_aug_5(tr("Virgen de Africa"))

    def _populate_subdiv_mongomeyen_public_holidays(self):
        # Holy Family.
        self._add_holiday_dec_30(tr("Sagrada Familia"))

    def _populate_subdiv_mongomo_public_holidays(self):
        # Virgin of Guadalupe.
        self._add_holiday_dec_12(tr("Virgen de Guadalupe"))

    def _populate_subdiv_niefang_public_holidays(self):
        # Maria Reina.
        self._add_holiday_aug_22(tr("Maria Reina"))

    def _populate_subdiv_nkimi_public_holidays(self):
        # Santiago Apóstol.
        self._add_holiday_jul_25(tr("Santiago Apóstol"))

    def _populate_subdiv_nkue_public_holidays(self):
        # Saint Francis Xavier.
        self._add_holiday_dec_3(tr("San Francisco Javier"))

    def _populate_subdiv_nsok_nsomo_public_holidays(self):
        # Saint Peter Claver.
        self._add_holiday_sep_9(tr("San Pedro Claver"))

    def _populate_subdiv_nsork_public_holidays(self):
        # Saints Paul.
        self._add_holiday_jun_29(tr("Santos Pablo"))

    def _populate_subdiv_rebola_public_holidays(self):
        # Our Lady of Montserrat.
        self._add_holiday_apr_27(tr("Nuestra Señora de Montserrat"))


class GQ(EquatorialGuinea):
    pass


class GNQ(EquatorialGuinea):
    pass


class EquatorialGuineaStaticHolidays:
    """Equatorial Guinea special holidays.

    References:
        * [AFCON Victory Holiday](https://web.archive.org/web/20240124021813/https://www.monitor.co.ug/uganda/sports/soccer/equatorial-guinea-president-awards-team-1-million-for-afcon-victory-4500644)
    """

    special_public_holidays = {
        # AFCON Victory Against Ivory Coast.
        2024: (JAN, 23, tr("Victoria de la AFCON contra Costa de Marfil")),
    }
