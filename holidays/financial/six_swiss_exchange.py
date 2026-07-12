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

from holidays.constants import PUBLIC
from holidays.countries.switzerland import Switzerland
from holidays.mixins.child_entity import ChildEntity
from holidays.observed_holiday_base import SAT_TO_NONE, SUN_TO_NONE


class SIXSwissExchange(ChildEntity, Switzerland):  # type: ignore[assignment, misc]
    """SIX Swiss Exchange holidays.

    References:
        [2018](https://web.archive.org/web/20260712044834/https://www.six-group.com/dam/download/sites/education/preparatory-documentation/trading-module/trading-guide.pdf)
        [2019](https://web.archive.org/web/20260712044834/https://www.six-group.com/dam/download/sites/education/preparatory-documentation/trading-module/trading-guide.pdf)
        [2022](https://web.archive.org/web/20220420104843/https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides/trading-calendar-2022.pdf)
        [2023](https://web.archive.org/web/20220626051815/https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides/trading-calendar-2023.pdf)
        [2024](https://web.archive.org/web/20240910205011/https://www.six-group.com/en/market-data/news-tools/trading-currency-holiday-calendar.html#/#/)
        [2025](https://web.archive.org/web/20250908065713/https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides/trading-calendar-2025.pdf)
        [2026](https://web.archive.org/web/20251225182641/https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides/trading-calendar-2026.pdf)
    """

    country = None  # type: ignore[assignment]
    market = "XSWX"
    parent_entity = Switzerland
    parent_entity_subdivision_code = "ZH"
    supported_categories = (PUBLIC,)  # type: ignore[assignment]
    start_year = 2000

    _weekend_to_none_rule = SAT_TO_NONE + SUN_TO_NONE

    def _populate_public_holidays(self) -> None:
        super()._populate_public_holidays()

        # Saint Berchtold's Day
        self._add_new_years_day_two(tr("Berchtoldstag"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Heiligabend"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Vortag vor Neujahr"))

    def _populate(self, year: int) -> None:
        super()._populate(year)

        if self.observed:
            for dt in tuple(self.keys()):
                if dt.year == year:
                    self._move_holiday_forced(dt, rule=self._weekend_to_none_rule)


class XSWX(SIXSwissExchange):
    pass


class SIX(SIXSwissExchange):
    pass
