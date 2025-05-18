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
        * <https://web.archive.org/web/20250503042253/https://boe.gob.gq/files/Decreto%20de%20Fijación%20de%20los%20Días%20Feriados%20en%20Guinea%20Ecuatorial.pdf>
        * <https://web.archive.org/web/20250503042253/https://en.wikipedia.org/wiki/Public_holidays_in_Equatorial_Guinea>
        * <https://web.archive.org/web/20250503042253/https://www.timeanddate.com/holidays/guineaecuatorial/>
        * <https://web.archive.org/web/20250503042253/https://gq.usembassy.gov/holiday-calendar/>
        * <https://web.archive.org/web/20250503044712/https://www.guineainfomarket.com/business/2024/03/29/calendario-laboral-de-guinea-ecuatorial-2024/>
        * [President's Day](https://web.archive.org/web/20250503042253/https://www.officeholidays.com/holidays/equatorial-guinea/equatorial-guinea-presidents-day)
        * [AFCON Victory Holiday](https://web.archive.org/web/20250503042253/https://www.timeanddate.com/holidays/equatorialguinea/afcon-victory-vs-ivory-coast)

    """

    country = "GQ"
    default_language = "es"
    supported_languages = ("en_US", "es")
    # %s observed.
    observed_label = tr("%s (observado)")
    # On 12 October 1968, Equatorial Guinea gained independence from Spain.
    start_year = 1969
    subdivisions = (
        "AN",  # Annobón (Annobon).
        "BN",  # Bioko Norte (North Bioko).
        "BS",  # Bioko Sur (South Bioko).
        "CS",  # Centro Sur (South Center).
        "KN",  # Kié-Ntem (Kie-Ntem).
        "LI",  # Litoral (Coast).
        "WN",  # Wele-Nzas (Wele-Nzas).
    )
    subdivisions_aliases = {
        "Annobón": "AN",
        "Annobon": "AN",
        "Bioko Norte": "BN",
        "North Bioko": "BN",
        "Bioko Sur": "BS",
        "South Bioko": "BS",
        "Centro Sur": "CS",
        "South Center": "CS",
        "Kié-Ntem": "KN",
        "Kie-Ntem": "KN",
        "Litoral": "LI",
        "Coast": "LI",
        "Wele-Nzas": "WN",
    }

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

        # Good Friday.
        self._add_observed(self._add_good_friday(tr("Viernes Santo")))

        # Labor Day.
        self._add_observed(self._add_labor_day(tr("Día del Trabajo")))

        if self._year >= 1979:
            # President's Day.
            self._add_observed(self._add_holiday_jun_5(tr("Día del Presidente")))

        # Corpus Christi.
        self._add_observed(self._add_corpus_christi_day(tr("Corpus Christi")))

        if self._year >= 1979:
            # Armed Forces Day.
            self._add_observed(self._add_holiday_aug_3(tr("Día de las Fuerzas Armadas")))

        if self._year >= 1982:
            # Fundamental Law Day.
            self._add_observed(self._add_holiday_aug_15(tr("Día de la Ley Fundamental")))

        # Independence Day.
        self._add_observed(self._add_holiday_oct_12(tr("Día de Independencia")))

        # Feast of the Immaculate Conception.
        self._add_observed(
            self._add_immaculate_conception_day(tr("Fiesta de Inmaculada Concepción"))
        )

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Día de Navidad")))

    def _populate_subdiv_an_public_holidays(self):
        # Patron Saint Festival of Annobón.
        self._add_holiday_jun_13(tr("Fiesta Patronal de Annobón"))

    def _populate_subdiv_bn_public_holidays(self):
        # Our Lady of Montserrat.
        self._add_holiday_apr_27(tr("Nuestra Señora de Montserrat"))

        # Santiago Apóstol.
        self._add_holiday_jul_25(tr("Santiago Apóstol"))

        # Feast of Santa Isabel.
        self._add_holiday_nov_17(tr("Fiesta de Santa Isabel"))

    def _populate_subdiv_bs_public_holidays(self):
        # Our Lady of Montserrat.
        self._add_holiday_apr_27(tr("Nuestra Señora de Montserrat"))

    def _populate_subdiv_cs_public_holidays(self):
        # Santiago Apóstol.
        self._add_holiday_jul_25(tr("Santiago Apóstol"))

        # Assumption of Our Lady Patroness of Bikurga.
        self._add_holiday_aug_15(tr("Asunción de Nuestra Señora Patrona de Bikurga"))

        # Maria Reina.
        self._add_holiday_aug_22(tr("Maria Reina"))

        # Saint Barbara
        self._add_holiday_dec_4(tr("Santa Bárbara"))

    def _populate_subdiv_kn_public_holidays(self):
        # Virgin of Africa.
        self._add_holiday_aug_5(tr("Virgen de Africa"))

        # Saint Peter Claver.
        self._add_holiday_sep_9(tr("San Pedro Claver"))

        # Exaltation of the Holy Cross.
        self._add_holiday_sep_14(tr("Exaltación de la Santa Cruz"))

        # Saint Francis Xavier.
        self._add_holiday_dec_3(tr("San Francisco Javier"))

    def _populate_subdiv_li_public_holidays(self):
        # Our Lady of Carmen.
        self._add_holiday_jul_15(tr("Nuestra Señora del Carmen"))

        # Santiago Apóstol.
        self._add_holiday_jul_25(tr("Santiago Apóstol"))

        # Immaculate Heart of Mary.
        self._add_holiday_aug_22(tr("Inmaculada Corazón de Maria"))

        # Saint Teresa of Jesus.
        self._add_holiday_oct_15(tr("Santa Teresa de Jesús"))

        # Holy Family.
        self._add_holiday_dec_30(tr("Sagrada Familia"))

    def _populate_subdiv_wn_public_holidays(self):
        # Saints Peter and Paul.
        self._add_holiday_jun_29(tr("Santos Pedro y Pablo"))

        # Our Lady of Asunción.
        self._add_holiday_aug_15(tr("Nuestra señora de Asunción"))

        # Saint Pius X.
        self._add_holiday_aug_21(tr("Santo Pío X"))

        # Virgin of Guadalupe.
        self._add_holiday_dec_12(tr("Virgen de Guadalupe"))

        # Holy Family.
        self._add_holiday_dec_30(tr("Sagrada Familia"))


class GQ(EquatorialGuinea):
    pass


class GNQ(EquatorialGuinea):
    pass


class EquatorialGuineaStaticHolidays:
    special_public_holidays = {
        # AFCON Victory Against Ivory Coast.
        2024: (JAN, 23, tr("Victoria de la AFCON contra Costa de Marfil")),
    }
