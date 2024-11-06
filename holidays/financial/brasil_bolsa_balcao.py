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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class BrasilBolsaBalcao(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Official regulations:
        - `Decreto n. 155-B, de 14.01.1890 <https://www2.camara.leg.br/legin/fed/decret/1824-1899/decreto-155-b-14-janeiro-1890-517534-publicacaooriginal-1-pe.html>`_
        - `Decreto n. 19.488, de 15.12.1930 <https://www2.camara.leg.br/legin/fed/decret/1930-1939/decreto-19488-15-dezembro-1930-508040-republicacao-85201-pe.html>`_
        - `Lei n. 14.759, de 21.12.2023 <https://www2.camara.leg.br/legin/fed/lei/2023/lei-14759-21-dezembro-2023-795091-publicacaooriginal-170522-pl.html>`_
        - `Resolução n. 2.516, de 29.06.1998 <https://www.bcb.gov.br/pre/normativos/res/1998/pdf/res_2516_v2_P.pdf>`_
    Historical data:
        - `Feriados ANBIMA 2001-2099 <https://www.anbima.com.br/feriados>`_
        - `Calendario de negociação B3 <https://www.b3.com.br/pt_br/solucoes/plataformas/puma-trading-system/para-participantes-e-traders/calendario-de-negociacao/feriados>`_
    """

    market = "BVMF"

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        if year <= 1889:
            # Decreto n. 155-B, de 14.01.1890
            # Curiously enough, 1890 is also the year of foundation of the
            # São Paulo Stock Exchange, which would later become the B3.
            return None

        super()._populate(year)

        self._add_new_years_day("Confraternização Universal")
        self._add_carnival_monday("Carnaval")
        self._add_carnival_tuesday("Carnaval")

        if year < 2000:
            # Resolução n. 2.516, de 29.06.1998
            self._add_holy_thursday("Quinta-feira Santa")

        self._add_good_friday("Sexta-feira Santa")

        if year not in {1931, 1932}:
            # Tiradentes' Day
            self._add_holiday_apr_21("Tiradentes")

        if year >= 1925:
            self._add_labor_day("Dia do Trabalhador")

        self._add_corpus_christi_day("Corpus Christi")

        # Independence Day
        self._add_holiday_sep_7("Independência do Brasil")

        if year <= 1930 or year >= 1980:
            # Our Lady of Aparecida
            self._add_holiday_oct_12("Nossa Senhora Aparecida")

        self._add_all_souls_day("Finados")

        # Republic Proclamation Day
        self._add_holiday_nov_15("Proclamação da República")

        if year >= 2024:
            # Lei n. 14.759, de 21.12.2023
            # National Day of Zumbi and Black Awareness
            self._add_holiday_nov_20("Dia Nacional de Zumbi e da Consciência Negra")

        if year >= 1922:
            self._add_christmas_day("Natal")


class BVMF(BrasilBolsaBalcao):
    pass


class B3(BrasilBolsaBalcao):
    pass
