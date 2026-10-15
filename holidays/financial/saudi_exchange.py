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

from holidays.calendars.gregorian import FEB, MAR, APR, MAY, JUN, JUL, AUG, NOV, FRI, SAT
from holidays.countries.saudi_arabia import SaudiArabiaIslamicHolidays
from holidays.groups import IslamicHolidays, StaticHolidays
from holidays.helpers import tr
from holidays.observed_holiday_base import ObservedHolidayBase, FRI_TO_PREV_THU, SAT_TO_NEXT_SUN


class SaudiExchange(ObservedHolidayBase, IslamicHolidays, StaticHolidays):
    """Saudi Exchange (Tadawul) holidays.

    The exchange is closed on Founding Day, National Day, and for Eid al-Fitr and
    Eid al-Adha. The Eid closures are announced every year and usually run longer
    than the Eid days themselves.

    References:
        * [Trading Cycle and Times](https://web.archive.org/web/20250803185737/https://www.saudiexchange.sa/wps/portal/saudiexchange/rules-guidance/capital-market-overview/trading-cycle-and-times)
        * [Saudi Exchange Holiday Calendar](https://web.archive.org/web/20260219054238/https://www.saudiexchange.sa/wps/portal/saudiexchange/about-saudi-exchange/exchange-media-centre/saudi-exchange-holiday-calendar)

    Historical data:
        * [Eid al-Adha 2020](https://web.archive.org/web/20261013082049/https://www.argaam.com/en/article/articledetail/id/1387677)
        * [National Day 2020](https://web.archive.org/web/20261013082224/https://www.argaam.com/en/article/articledetail/id/1405995)
        * [Eid al-Fitr 2021](https://web.archive.org/web/20261013082222/https://www.argaam.com/en/article/articledetail/id/1457396)
        * [Eid al-Fitr 2022](https://web.archive.org/web/20261013082252/https://www.argaam.com/en/article/articledetail/id/1544157)
        * [World Cup holiday 2022](https://web.archive.org/web/20260102150208/https://www.khaleejtimes.com/world/gulf/saudi-arabia-declares-public-holiday-after-historic-fifa-world-cup-win)
    """

    market = "XSAU"
    default_language = "ar"
    # %s (estimated).
    estimated_label = tr("%s (تقديري)")
    # %s (observed).
    observed_label = tr("%s (يوم تعويضي)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (يوم تعويضي تقديري)")
    supported_languages = ("ar", "en_US", "ur_PK")
    start_year = 2020
    weekend = {FRI, SAT}

    def __init__(self, *args, islamic_show_estimated: bool = False, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        IslamicHolidays.__init__(
            self, cls=SaudiArabiaIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, SaudiExchangeStaticHolidays)
        kwargs.setdefault("observed_rule", FRI_TO_PREV_THU + SAT_TO_NEXT_SUN)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year >= 2022:
            # Founding Day.
            self._add_observed(self._add_holiday_feb_22(tr("يوم التأسيس")))

        # Eid al-Fitr Holiday.
        name = tr("عطلة عيد الفطر")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)
        self._add_eid_al_fitr_day_four(name)

        # Day of Arafah.
        self._add_arafah_day(tr("يوم عرفة"))

        # Eid al-Adha Holiday.
        name = tr("عطلة عيد الأضحى")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        self._add_eid_al_adha_day_three(name)
        self._add_eid_al_adha_day_four(name)

        # National Day.
        self._add_observed(self._add_holiday_sep_23(tr("اليوم الوطني")))


class XSAU(SaudiExchange):
    pass


class SaudiExchangeStaticHolidays:
    """Saudi Exchange (Tadawul) special holidays.

    Extra days of the yearly Eid closures that fall outside the Eid days.
    """

    # Eid al-Fitr Holiday.
    eid_al_fitr_holiday = tr("عطلة عيد الفطر")

    # Eid al-Adha Holiday.
    eid_al_adha_holiday = tr("عطلة عيد الأضحى")

    special_public_holidays = {
        2020: (
            (MAY, 28, eid_al_fitr_holiday),
            (JUL, 29, eid_al_adha_holiday),
            (AUG, 4, eid_al_adha_holiday),
        ),
        2021: (
            (MAY, 11, eid_al_fitr_holiday),
            (MAY, 12, eid_al_fitr_holiday),
            (JUL, 18, eid_al_adha_holiday),
        ),
        2022: (
            (MAY, 1, eid_al_fitr_holiday),
            (JUL, 7, eid_al_adha_holiday),
            # Holiday for the National Team's Victory in the World Cup.
            (NOV, 23, tr("عطلة فوز المنتخب في كأس العالم")),
        ),
        2023: (
            (APR, 18, eid_al_fitr_holiday),
            (APR, 19, eid_al_fitr_holiday),
            (APR, 20, eid_al_fitr_holiday),
            (JUN, 25, eid_al_adha_holiday),
            (JUN, 26, eid_al_adha_holiday),
        ),
        2024: (
            (APR, 7, eid_al_fitr_holiday),
            (APR, 8, eid_al_fitr_holiday),
            (APR, 9, eid_al_fitr_holiday),
            (JUN, 20, eid_al_adha_holiday),
        ),
        2025: (JUN, 10, eid_al_adha_holiday),
        2026: (
            (MAR, 17, eid_al_fitr_holiday),
            (MAR, 18, eid_al_fitr_holiday),
            (MAR, 19, eid_al_fitr_holiday),
            (MAY, 24, eid_al_adha_holiday),
            (MAY, 25, eid_al_adha_holiday),
        ),
        2027: (
            (MAR, 7, eid_al_fitr_holiday),
            (MAR, 8, eid_al_fitr_holiday),
            (MAY, 20, eid_al_adha_holiday),
        ),
        2028: (
            (MAR, 1, eid_al_fitr_holiday),
            (MAR, 2, eid_al_fitr_holiday),
            (MAY, 3, eid_al_adha_holiday),
            (MAY, 9, eid_al_adha_holiday),
        ),
        2029: (
            (FEB, 12, eid_al_fitr_holiday),
            (FEB, 13, eid_al_fitr_holiday),
            (FEB, 18, eid_al_fitr_holiday),
            (APR, 22, eid_al_adha_holiday),
        ),
    }
