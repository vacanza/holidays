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

from holidays.constants import OPTIONAL, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Portugal(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays
    in Portugal.

    References:
        - https://en.wikipedia.org/wiki/Public_holidays_in_Portugal
        - `Labour Day <https://www.e-konomista.pt/dia-do-trabalhador/>`_
        - Portugal Day - Decreto 17.171
        - Restoration of Independence Day - Gazeta de Lisboa, 8 de Dezembro
          de 1823 (n.º 290), pp. 1789 e 1790
        - Azores
            - https://files.dre.pt/1s/1980/08/19200/23052305.pdf
        - Madeira
            - https://files.dre.pt/1s/1979/11/25900/28782878.pdf
            - https://files.dre.pt/1s/1989/02/02800/04360436.pdf
            - https://files.dre.pt/1s/2002/11/258a00/71837183.pdf
    """

    country = "PT"
    default_language = "pt_PT"
    supported_categories = (OPTIONAL, PUBLIC)

    # https://en.wikipedia.org/wiki/ISO_3166-2:PT
    subdivisions = (
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "20",
        "30",
    )
    _deprecated_subdivisions = ("Ext",)
    supported_languages = ("en_US", "pt_PT")

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        self._add_new_years_day(tr("Ano Novo"))

        # Carnival is no longer a holiday, but some companies let workers off.
        # TODO: recollect the years in which it was a public holiday.

        # Good Friday.
        self._add_good_friday(tr("Sexta-feira Santa"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Páscoa"))

        # Revoked holidays in 2013–2015.
        if self._year <= 2012 or self._year >= 2016:
            self._add_corpus_christi_day(tr("Corpo de Deus"))
            if self._year >= 1910:
                self._add_holiday_oct_5(tr("Implantação da República"))
            self._add_all_saints_day(tr("Dia de Todos os Santos"))
            if self._year >= 1823:
                self._add_holiday_dec_1(tr("Restauração da Independência"))

        if self._year >= 1974:
            self._add_holiday_apr_25(tr("Dia da Liberdade"))
            self._add_labor_day(tr("Dia do Trabalhador"))

        if self._year >= 1911:
            if 1933 <= self._year <= 1973:
                self._add_holiday_jun_10(tr("Dia de Camões, de Portugal e da Raça"))
            elif self._year >= 1978:
                self._add_holiday_jun_10(
                    tr("Dia de Portugal, de Camões e das Comunidades Portuguesas")
                )
            else:
                self._add_holiday_jun_10(tr("Dia de Portugal"))

        self._add_assumption_of_mary_day(tr("Assunção de Nossa Senhora"))
        self._add_immaculate_conception_day(tr("Imaculada Conceição"))
        self._add_christmas_day(tr("Dia de Natal"))

    def _populate_optional_holidays(self):
        """
        Adds extended days that most people have as a bonus from their
        companies:

        - Carnival
        - the day before and after xmas
        - the day before the new year
        - Lisbon's city holiday
        """

        # TODO: add bridging days:
        # - get Holidays that occur on Tuesday  and add Monday (-1 day)
        # - get Holidays that occur on Thursday and add Friday (+1 day)

        self._add_carnival_monday(tr("Carnaval"))
        self._add_holiday_jun_13(tr("Dia de Santo António"))
        self._add_christmas_eve(tr("Véspera de Natal"))
        self._add_christmas_day_two(tr("26 de Dezembro"))
        self._add_new_years_eve(tr("Véspera de Ano Novo"))

    def _add_subdiv_holidays(self):
        if self._year >= 1911:
            super()._add_subdiv_holidays()

        if self.subdiv == "Ext":
            self._populate_optional_holidays()

    def _add_subdiv_01_public_holidays(self):
        self._add_holiday_may_12(tr("Dia de Santa Joana"))

    def _add_subdiv_02_public_holidays(self):
        self._add_ascension_thursday(tr("Quinta-feira da Ascensão"))

    def _add_subdiv_03_public_holidays(self):
        self._add_saint_johns_day(tr("Dia de São João"))

    def _add_subdiv_04_public_holidays(self):
        self._add_holiday_aug_22(tr("Dia de Nossa Senhora das Graças"))

    def _add_subdiv_05_public_holidays(self):
        self._add_holiday(
            tr("Dia de Nossa Senhora de Mércoles"), self._easter_sunday + td(days=+16)
        )

    def _add_subdiv_06_public_holidays(self):
        self._add_holiday_jul_4(tr("Dia de Santa Isabel"))

    def _add_subdiv_07_public_holidays(self):
        self._add_holiday_jun_29(tr("Dia de São Pedro"))

    def _add_subdiv_08_public_holidays(self):
        self._add_holiday_sep_7(tr("Dia do Município de Faro"))

    def _add_subdiv_09_public_holidays(self):
        self._add_holiday_nov_27(tr("Dia do Município da Guarda"))

    def _add_subdiv_10_public_holidays(self):
        self._add_holiday_may_22(tr("Dia do Município de Leiria"))

    def _add_subdiv_11_public_holidays(self):
        self._add_holiday_jun_13(tr("Dia de Santo António"))

    def _add_subdiv_12_public_holidays(self):
        self._add_holiday_may_23(tr("Dia do Município de Portalegre"))

    def _add_subdiv_13_public_holidays(self):
        self._add_saint_johns_day(tr("Dia de São João"))

    def _add_subdiv_14_public_holidays(self):
        self._add_saint_josephs_day(tr("Dia de São José"))

    def _add_subdiv_15_public_holidays(self):
        self._add_holiday_sep_15(tr("Dia de Bocage"))

    def _add_subdiv_16_public_holidays(self):
        self._add_holiday_aug_20(tr("Dia de Nossa Senhora da Agonia"))

    def _add_subdiv_17_public_holidays(self):
        self._add_holiday_jun_13(tr("Dia de Santo António"))

    def _add_subdiv_18_public_holidays(self):
        self._add_holiday_sep_21(tr("Dia de São Mateus"))

    def _add_subdiv_20_public_holidays(self):
        if self._year >= 1981:
            self._add_whit_monday(tr("Dia da Região Autónoma dos Açores"))

    def _add_subdiv_30_public_holidays(self):
        if self._year >= 1979:
            self._add_holiday_jul_1(
                tr("Dia da Região Autónoma da Madeira e das Comunidades Madeirenses")
                if self._year >= 1989
                else tr("Dia da Região Autónoma da Madeira")
            )

        if self._year >= 2002:
            self._add_christmas_day_two(tr("Primeira Oitava"))


class PT(Portugal):
    pass


class PRT(Portugal):
    pass
