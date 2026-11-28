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

from holidays.calendars.gregorian import APR
from holidays.constants import PUBLIC
from holidays.countries.malaysia import Malaysia
from holidays.groups import StaticHolidays
from holidays.helpers import tr
from holidays.mixins.child_entity import ChildEntity


class BursaMalaysia(ChildEntity, Malaysia):
    """Bursa Malaysia (MYX) holidays.

    The exchange follows Malaysian federal public holidays observed in the
    Federal Territory of Kuala Lumpur. Weekend holidays are excluded; when a
    public holiday falls on Sunday, the following Monday observed holiday
    is kept. `Malaysia` does not observe Awal Muharam, but Bursa still closes
    on the following Monday when it falls on Sunday.

    References:
        * [Bursa Malaysia holiday calendar](https://web.archive.org/web/20260911115934/https://www.bursamalaysia.com/about_bursa/about_us/calendar)
        * [Closure for Awal Muharam, Jul 8, 2024](https://www.thestar.com.my/business/business-news/2024/07/03/bursa-malaysia-to-close-on-july-8-for-awal-muharram)
        * [Closure for Chinese New Year, Feb 17-18, 2026](https://www.thestar.com.my/business/business-news/2026/02/11/bursa-malaysia-closed-for-cny-holiday-on-feb-17-18)
        * [Closure for Eid al-Fitr, Mar 20-23, 2026](https://www.thestar.com.my/business/business-news/2026/03/18/bursa-malaysia-subsidiaries-to-be-closed-in-conjunction-with-hari-raya-aidilfitri)
        * [Closure for Eid al-Adha, Agong's Birthday and Vesak, May 27 and Jun 1-2, 2026](https://www.thestar.com.my/business/business-news/2026/05/20/bursa-malaysia-closed-for-public-holidays-on-may-27-june-1-2)

    Historical data:
        * [2007-04-26](https://www.upi.com/Top_News/2007/04/26/Malaysias-new-king-installed/38011177613216/)
    """

    country = None  # type: ignore[assignment]
    market = "XKLS"
    parent_entity = Malaysia
    parent_entity_subdivision_code = "14"
    subdivisions: tuple[str, ...] = ()
    subdivisions_aliases: dict[str, str] = {}
    supported_categories = (PUBLIC,)
    start_year = 2000

    def __init__(self, *args, **kwargs):
        StaticHolidays.__init__(self, BursaMalaysiaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_subdiv_holidays(self) -> None:
        # Malaysia adds Awal Muharam but does not put it in `dts_observed`.
        # Bursa still closes on the following Monday when it falls on Sunday
        # (e.g. 2024-07-08).
        if self._year >= 1995:
            for dt, _estimated in self._islamic_calendar.hijri_new_year_dates(self._year):
                if dt.year == self._year:
                    self.dts_observed.add(dt)

        super()._populate_subdiv_holidays()

        for dt in tuple(dt for dt in self if dt.year == self._year):
            if self._is_weekend(dt):
                self.pop(dt)


class XKLS(BursaMalaysia):
    pass


class MYX(BursaMalaysia):
    pass


class BursaMalaysiaStaticHolidays:
    """Bursa Malaysia special holidays."""

    special_public_holidays = {
        2007: (
            # Day of Installation of the 13th Yang di-Pertuan Agong.
            (APR, 26, tr("Hari Pertabalan Yang di-Pertuan Agong ke-13")),
        ),
    }
