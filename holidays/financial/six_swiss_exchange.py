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

from datetime import date
from gettext import gettext as tr

from holidays.constants import PUBLIC
from holidays.countries.switzerland import Switzerland
from holidays.mixins.child_entity import ChildEntity


class SIXSwissExchange(ChildEntity, Switzerland):
    """SIX Swiss Exchange (SIX) holidays.

    References:
        [2018](https://web.archive.org/web/20260712044834/https://www.six-group.com/dam/download/sites/education/preparatory-documentation/trading-module/trading-guide.pdf)
        [2019](https://web.archive.org/web/20260712044834/https://www.six-group.com/dam/download/sites/education/preparatory-documentation/trading-module/trading-guide.pdf)
        [2021](https://web.archive.org/web/20211102133818/https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides/trading-calendar-2021.pdf)
        [2022](https://web.archive.org/web/20220420104843/https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides/trading-calendar-2022.pdf)
        [2023](https://web.archive.org/web/20220626051815/https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides/trading-calendar-2023.pdf)
        [2024](https://web.archive.org/web/20240521040627/https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides/trading-calendar-2024.pdf)
        [2025](https://web.archive.org/web/20250908065713/https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides/trading-calendar-2025.pdf)
        [2026](https://web.archive.org/web/20251225182641/https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides/trading-calendar-2026.pdf)
    """

    country = None  # type: ignore[assignment]
    market = "XSWX"
    parent_entity = Switzerland
    parent_entity_subdivision_code = "ZH"
    supported_categories: tuple[str] = (PUBLIC,)
    start_year = 2000

    def _add_holiday(self, name: str, *args) -> date | None:
        dt = args if len(args) > 1 else args[0]
        dt = dt if isinstance(dt, date) else date(self._year, *dt)
        if self._is_weekend(dt):
            return None
        return super()._add_holiday(name, dt)

    def _populate_public_holidays(self) -> None:
        super()._populate_public_holidays()

        # Saint Berchtold's Day.
        self._add_new_years_day_two(tr("Berchtoldstag"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Heiligabend"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Vortag vor Neujahr"))


class XSWX(SIXSwissExchange):
    pass


class SIX(SIXSwissExchange):
    pass
