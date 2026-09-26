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

from holidays.calendars.gregorian import DEC
from holidays.constants import HALF_DAY, PUBLIC
from holidays.countries.colombia import Colombia
from holidays.groups import StaticHolidays
from holidays.helpers import tr


class BolsaDeValoresDeColombia(Colombia, StaticHolidays):
    """Bolsa de Valores de Colombia (BVC) holidays.

    BVC follows the Colombian public holiday calendar (including the holidays moved
    to the following Monday) and does not trade on the last business day of the year,
    which it declares a non-trading day ("día no bursátil") every year. When
    December 31 falls on a weekend, the closure moves to the preceding Friday.

    References:
        * [Días no hábiles bursátiles](https://www.bvc.com.co/dias-no-habiles-bursatiles)

    Historical data:
        * [2009](https://web.archive.org/web/20091228031820/http://www.bvc.com.co/pps/tibco/portalbvc/Home/Mercados/dianobursatil)
        * [2010](https://web.archive.org/web/20110707053005/http://www.bvc.com.co/pps/tibco/portalbvc/Home/Mercados/dianobursatil?action=dummy)
        * [2011](https://web.archive.org/web/20120509113348/http://www.bvc.com.co/pps/tibco/portalbvc/Home/Mercados/dianobursatil?action=dummy)
        * [2014](https://web.archive.org/web/20150315070212/http://www.bvc.com.co/pps/tibco/portalbvc/Home/Mercados/dianobursatil?action=dummy)
        * [2015](https://web.archive.org/web/20160322082620/http://www.bvc.com.co/pps/tibco/portalbvc/Home/Mercados/dianobursatil?action=dummy)
        * [2016](https://web.archive.org/web/20170202211610/http://www.bvc.com.co/pps/tibco/portalbvc/Home/Mercados/dianobursatil?action=dummy)
        * [2017](https://web.archive.org/web/20250717220732/https://camaraderiesgo.com/wp-content/uploads/2017/12/Boletin-Informativo-55-del-12-de-diciembre-de-2017.pdf)
        * [2018](https://web.archive.org/web/20190721154053/https://www.bvc.com.co/pps/tibco/portalbvc/Home/Mercados/dianobursatil?action=dummy)
        * [2019](https://web.archive.org/web/20200805163533/https://bvc.com.co/pps/tibco/portalbvc/Home/Mercados/dianobursatil?action=dummy)
        * [2020](https://web.archive.org/web/20210124190358/https://bvc.com.co/pps/tibco/portalbvc/Home/Mercados/dianobursatil?action=dummy)
        * [2021](https://web.archive.org/web/20220125080217/https://www.bvc.com.co/pps/tibco/portalbvc/Home/Mercados/dianobursatil)
        * [2022](https://web.archive.org/web/20240629235632/https://camaraderiesgo.com/wp-content/uploads/2022/12/Boletin-Informativo-Horario-fin-de-ano-2022.pdf)
        * [2023](https://web.archive.org/web/20250503165413/https://camaraderiesgo.com/wp-content/uploads/2023/12/Boletin-Informativo-Horario-fin-de-ano-2023.pdf)
        * [2024](https://web.archive.org/web/20260926074615/https://camaraderiesgo.com/wp-content/uploads/2024/10/Boletin-Informatvo-Horario-fin-de-ano-2024-1.pdf)
    """

    country = None  # type: ignore[assignment]
    market = "XBOG"
    parent_entity = Colombia
    supported_categories = (HALF_DAY, PUBLIC)
    supported_languages = ("en_US", "es")  # type: ignore[assignment]
    start_year = 2008

    def __init__(self, *args, **kwargs):
        StaticHolidays.__init__(self, BolsaDeValoresDeColombiaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        self._add_holiday(
            # Year-end market holiday.
            tr("Día no bursátil de fin de año"),
            self._get_next_workday(self._next_year_new_years_day, -1),
        )


class XBOG(BolsaDeValoresDeColombia):
    pass


class BVC(BolsaDeValoresDeColombia):
    pass


class BolsaDeValoresDeColombiaStaticHolidays:
    """Bolsa de Valores de Colombia (BVC) special holidays.

    When December 24 is a trading day, the equity spot market and the Mercado Global
    Colombiano (MGC) close at 1:00 p.m., aligned with the New York Stock Exchange.
    Only the years with a source are listed.

    References:
        * [2018](https://web.archive.org/web/20260926080617/http://gyhinvestments.com/images/boyaca/CircularUnicaBVCactualizada20180521Circular005Normativo015.pdf)
        * [2019](https://web.archive.org/web/20241112170153/https://www.larepublica.co/finanzas/bolsa-de-valores-de-colombia-revelo-horarios-para-este-24-y-31-de-diciembre-2942461)
        * [2020](https://web.archive.org/web/20210124190358/https://bvc.com.co/pps/tibco/portalbvc/Home/Mercados/dianobursatil?action=dummy)
        * [2021](https://web.archive.org/web/20220125080217/https://www.bvc.com.co/pps/tibco/portalbvc/Home/Mercados/dianobursatil)
        * [2025](https://web.archive.org/web/20260926074758/https://www.bloomberglinea.com/mercados/las-bolsas-operan-el-24-y-el-25-de-diciembre-asi-sera-en-america-latina-y-wall-street/)
    """

    # %s (markets close at 1:00pm).
    early_close_label = tr("%s (el mercado cierra a las 13:00)")

    # Christmas Eve.
    christmas_eve = tr("Nochebuena")

    special_half_day_holidays = {
        2018: (DEC, 24, (early_close_label, christmas_eve)),
        2019: (DEC, 24, (early_close_label, christmas_eve)),
        2020: (DEC, 24, (early_close_label, christmas_eve)),
        2021: (DEC, 24, (early_close_label, christmas_eve)),
        2025: (DEC, 24, (early_close_label, christmas_eve)),
    }
