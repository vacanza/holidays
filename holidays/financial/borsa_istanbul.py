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

from holidays.calendars.gregorian import FEB
from holidays.constants import HALF_DAY, PUBLIC
from holidays.countries.turkey import TurkeyIslamicHolidays
from holidays.groups import InternationalHolidays, IslamicHolidays, StaticHolidays
from holidays.helpers import tr
from holidays.holiday_base import HolidayBase


class BorsaIstanbul(HolidayBase, InternationalHolidays, IslamicHolidays, StaticHolidays):
    """Borsa Istanbul (BIST) holidays.

    Borsa İstanbul market holidays follow Turkey's national and religious
    holidays. On the eve of Ramadan Feast, the eve of Feast of the Sacrifice,
    and on October 28th the market closes early (half-day holidays).

    References:
        * [2025 holiday schedule](https://borsaIstanbul.com/files/precious-metals-and-diamond-market-2025-holiday-schedule.pdf)
        * [Trading principles for public holidays of 2025](https://www.kap.org.tr/en/api/BildirimPdf/1368625)
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Turkey>
    """

    market = "XIST"
    default_language = "tr"
    # %s (estimated).
    estimated_label = tr("%s (tahmini)")
    supported_categories = (HALF_DAY, PUBLIC)
    supported_languages = ("en_US", "tr")
    # Istanbul Stock Exchange (1986-2012), succeeded by Borsa İstanbul A.Ş. in 2013.
    start_year = 1986

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=TurkeyIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, BorsaIstanbulStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Yılbaşı"))

        # National Sovereignty and Children's Day.
        self._add_holiday_apr_23(tr("Ulusal Egemenlik ve Çocuk Bayramı"))

        if self._year >= 2009:
            # Labour and Solidarity Day.
            self._add_labor_day(tr("Emek ve Dayanışma Günü"))

        # Commemoration of Atatürk, Youth and Sports Day.
        self._add_holiday_may_19(tr("Atatürk'ü Anma, Gençlik ve Spor Bayramı"))

        if self._year >= 2017:
            # Democracy and National Unity Day.
            self._add_holiday_jul_15(tr("Demokrasi ve Millî Birlik Günü"))

        # Victory Day.
        self._add_holiday_aug_30(tr("Zafer Bayramı"))

        # Republic Day.
        self._add_holiday_oct_29(tr("Cumhuriyet Bayramı"))

        # Ramadan Feast.
        name = tr("Ramazan Bayramı")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)

        # Feast of the Sacrifice.
        name = tr("Kurban Bayramı")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        self._add_eid_al_adha_day_three(name)
        self._add_eid_al_adha_day_four(name)

    def _populate_half_day_holidays(self):
        # %s (from 1pm).
        begin_time_label = tr("%s (saat 13.00'ten)")

        self._add_holiday_oct_28(
            # Republic Day.
            self._format_holiday_name(begin_time_label, tr("Cumhuriyet Bayramı"))
        )

        self._add_eid_al_fitr_eve(
            # Ramadan Feast.
            self._format_holiday_name(begin_time_label, tr("Ramazan Bayramı"))
        )

        # Feast of the Sacrifice.
        self._add_arafah_day(self._format_holiday_name(begin_time_label, tr("Kurban Bayramı")))


class XIST(BorsaIstanbul):
    pass


class BIST(BorsaIstanbul):
    pass


class BorsaIstanbulStaticHolidays:
    """Borsa Istanbul (BIST) special holidays.

    References:
        * [Turkey - Market Closure 08 February 2023](https://research.ftserussell.com/products/index-notices/home/getnotice/?id=2606994)
    """

    special_public_holidays = {
        2023: (
            # Market Closed (Earthquake).
            (FEB, 8, tr("Market Closed (Earthquake)")),
            (FEB, 9, tr("Market Closed (Earthquake)")),
            (FEB, 10, tr("Market Closed (Earthquake)")),
            (FEB, 13, tr("Market Closed (Earthquake)")),
            (FEB, 14, tr("Market Closed (Earthquake)")),
        ),
    }
