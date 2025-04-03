#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.constants import OPTIONAL, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class CapeVerde(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Cape Verde holidays.

    References:
        * [Public holidays in Cape Verde](https://en.wikipedia.org/wiki/Public_holidays_in_Cape_Verde)
        * [Today's and Upcoming Holidays in Cape Verde](https://www.timeanddate.com/holidays/cape-verde/)
        * [Democracy Day](https://www.officeholidays.com/holidays/cape-verde/cape-verde-democracy-day)
        * [National Heroes Day](https://www.officeholidays.com/holidays/cape-verde/guinea-bissau-national-heroes-day)
        * [Feriados Bancários - Banco de Cabo Verde](https://www.bcv.cv/pt/SistemadePagamentos/feriados_bancarios/Paginas/FeriadosBancarios.aspx)
        * [Feriados Públicos - Feel Cabo Verde](https://feelcaboverde.com/feriados-publicos/)
        * [Public Holidays - Feel Cape Verde](https://feelcaboverde.com/en/public-holidays-cape-verde/)
        * [List of Cape Verde's subdivision ISO codes](https://www.iso.org/obp/ui/#iso:code:3166:CV)
    """

    country = "CV"
    default_language = "pt_CV"
    start_year = 1976
    subdivisions = (
        # Municipalities.
        "BR",  # Brava.
        "BV",  # Boa Vista.
        "CA",  # Santa Catarina.
        "CF",  # Santa Catarina do Fogo.
        "CR",  # Santa Cruz.
        "MA",  # Maio.
        "MO",  # Mosteiros.
        "PA",  # Paul.
        "PN",  # Porto Novo.
        "PR",  # Praia.
        "RB",  # Ribeira Brava.
        "RG",  # Ribeira Grande.
        "RS",  # Ribeira Grande de Santiago.
        "SD",  # São Domingos.
        "SF",  # São Filipe.
        "SL",  # Sal.
        "SM",  # São Miguel.
        "SO",  # São Lourenço dos Órgãos.
        "SS",  # São Salvador do Mundo.
        "SV",  # São Vicente.
        "TA",  # Tarrafal.
        "TS",  # Tarrafal de São Nicolau.
    )
    subdivisions_aliases = {
        # Municipalities.
        "Brava": "BR",
        "Boa Vista": "BV",
        "Santa Catarina": "CA",
        "Santa Catarina do Fogo": "CF",
        "Santa Cruz": "CR",
        "Maio": "MA",
        "Mosteiros": "MO",
        "Paul": "PA",
        "Porto Novo": "PN",
        "Praia": "PR",
        "Ribeira Brava": "RB",
        "Ribeira Grande": "RG",
        "Ribeira Grande de Santiago": "RS",
        "São Domingos": "SD",
        "São Filipe": "SF",
        "Sal": "SL",
        "São Miguel": "SM",
        "São Lourenço dos Órgãos": "SO",
        "São Salvador do Mundo": "SS",
        "São Vicente": "SV",
        "Tarrafal": "TA",
        "Tarrafal de São Nicolau": "TS",
    }
    supported_categories = (OPTIONAL, PUBLIC)
    supported_languages = ("de", "en_US", "es", "fr", "pt_CV")

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Ano Novo"))

        if self._year >= 1991:
            # Democracy and Freedom Day.
            self._add_holiday_jan_13(tr("Dia da Liberdade e Democracia"))

        # National Heroes Day.
        self._add_holiday_jan_20(tr("Dia da Nacionalidade e dos Heróis Nacionais"))

        # Ash Wednesday.
        self._add_ash_wednesday(tr("Quarta-feira de Cinzas"))

        # Good Friday.
        self._add_good_friday(tr("Sexta-feira Santa"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Páscoa"))

        # Worker's Day.
        self._add_labor_day(tr("Dia do Trabalhador"))

        # International Children's Day.
        self._add_childrens_day(tr("Dia Mundial da Criança"))

        # Independence Day.
        self._add_holiday_jul_5(tr("Dia da Independência Nacional"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Dia da Assunção"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Dia de Todos os Santos"))

        # Christmas Day.
        self._add_christmas_day(tr("Natal"))

    def _populate_optional_holidays(self):
        # Holy Thursday.
        self._add_holy_thursday(tr("Quinta-Feira Santa"))

        # Mother's Day.
        self._add_holiday_2nd_sun_of_may(tr("Dia das Mães"))

        # Father's Day.
        self._add_holiday_3rd_sun_of_jun(tr("Dia dos Pais"))

    def _populate_subdiv_br_public_holidays(self):
        # Brava Municipal Day.
        self._add_holiday_jun_24(tr("Dia do Município da Brava"))

    def _populate_subdiv_bv_public_holidays(self):
        # Municipal Day.
        self._add_holiday_jul_4(tr("Dia do Município"))

    def _populate_subdiv_ma_public_holidays(self):
        # Maio Municipal Day.
        self._add_holiday_sep_8(tr("Dia do Município do Maio"))

    def _populate_subdiv_pr_public_holidays(self):
        # Praia City Day.
        self._add_holiday_apr_29(tr("Dia da Cidade da Praia"))

        # Praia Municipal Day.
        self._add_holiday_may_19(tr("Dia do Município da Praia"))

    def _populate_subdiv_rb_public_holidays(self):
        # Ribeira Brava Municipal Day.
        self._add_holiday_dec_6(tr("Dia do Município de Ribeira Brava"))

    def _populate_subdiv_rs_public_holidays(self):
        # Ribeira Grande de Santiago Municipal Day.
        self._add_holiday_jan_31(tr("Dia do Município de Ribeira Grande de Santiago"))

    def _populate_subdiv_sl_public_holidays(self):
        # Municipal Day.
        self._add_holiday_sep_15(tr("Dia do Município"))

    def _populate_subdiv_sv_public_holidays(self):
        # São Vicente Municipal Day.
        self._add_holiday_jan_22(tr("Dia do Município de São Vicente"))

        # Carnival Tuesday.
        self._add_carnival_tuesday(tr("Terça-feira de Carnaval"))

    def _populate_subdiv_ts_public_holidays(self):
        # Tarrafal de São Nicolau Municipal Day.
        self._add_holiday_aug_2(tr("Dia do Município do Tarrafal de São Nicolau"))


class CV(CapeVerde):
    pass


class CAV(CapeVerde):
    pass
