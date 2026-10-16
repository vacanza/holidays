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

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, APR, OCT
from holidays.groups import (
    ChristianHolidays,
    IslamicHolidays,
    InternationalHolidays,
    StaticHolidays,
)
from holidays.helpers import tr
from holidays.holiday_base import HolidayBase


class Comoros(
    HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """Comoros holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_the_Comoros>
        * [2021 Prophet's Birthday](https://web.archive.org/web/20250712053206/https://scontent-del1-2.xx.fbcdn.net/v/t39.30808-6/471586197_1113861707132176_3696210890184034016_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=833d8c&_nc_ohc=3hfvuVNGVbMQ7kNvwHvrgbW&_nc_oc=AdnuDzvtcvdBJMoN-qSW7Pnx2fnzj2TFgwMSRklpM_Na-5AaB9y8D0U5BINcxL-vVL0&_nc_zt=23&_nc_ht=scontent-del1-2.xx&_nc_gid=HWC_59SRsyDfwGxku5bqXw&oh=00_AfSk0LCPS7PARPjdX5-vfM_lr7WxZnrkA9jRyrdUFhoyMQ&oe=68736290)
    """

    country = "KM"
    default_language = "fr"
    # %s (estimated).
    estimated_label = tr("%s (estimé)")
    # Independence from France on July 6, 1975.
    start_year = 1976
    supported_languages = ("ar", "en_US", "fr")

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=ComorosIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, ComorosStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Jour de l'an"))

        # Cheikh al Maarouf Day.
        self._add_holiday_mar_18(tr("Journée Cheikh Al Maarouf"))

        # Labor Day.
        self._add_labor_day(tr("Fête du Travail"))

        # National Day.
        self._add_holiday_jul_6(tr("Fête nationale"))

        if self._year >= 2006:
            # Maore Day.
            self._add_holiday_nov_12(tr("Journée Maoré"))

        # Christmas Day.
        self._add_christmas_day(tr("Noël"))

        # Islamic New Year.
        self._add_islamic_new_year_day(tr("Nouvel an musulman"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("Maoulid"))

        # Isra' and Mi'raj.
        self._add_isra_and_miraj_day(tr("Miradj"))

        # Eid al-Fitr.
        name = tr("Id-El-Fitr")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)

        # Eid al-Adha.
        name = tr("Id-El-Kabir")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)


class KM(Comoros):
    pass


class COM(Comoros):
    pass


class ComorosIslamicHolidays(_CustomIslamicHolidays):
    MAWLID_DATES = {
        2021: (OCT, 19),
    }


class ComorosStaticHolidays:
    """Comoros special holidays.

    References:
        * [Décret N°24-056PR](https://web.archive.org/web/20250717033820/https://munganyo.km/decrees/225)
        * [Décret N°25-008PR](https://web.archive.org/web/20250715223159/https://munganyo.km/decrees/374)
    """

    special_public_holidays = {
        # National Holiday.
        2024: (APR, 13, tr("Jour férié national")),
        # Election Partial Day Holiday.
        2025: (JAN, 30, tr("Journée chômée partielle d'élection")),
    }
