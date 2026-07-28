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
from holidays.countries.south_korea import SouthKorea


class KoreaExchange(SouthKorea):
    """Korea Exchange (KRX) holidays.

    References:
        * <https://web.archive.org/web/20260521141319/https://global.krx.co.kr/contents/GLB/05/0501/0501110000/GLB0501110000.jsp>
    """

    country = None  # type: ignore[assignment]
    market = "XKRX"
    parent_entity = SouthKorea
    supported_categories: tuple[str, ...] = (PUBLIC,)  # type: ignore[assignment]
    start_year = 2000

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        if self._year <= 2025:
            # Workers' Day.
            self._add_labor_day(tr("근로자의날"))

        self._add_holiday(
            # End of Year Holiday.
            tr("연말휴장일"),
            self._get_next_workday(self._next_year_new_years_day, -1),
        )

        for dt in tuple(self.keys()):
            if self._is_weekend(dt):
                self.pop(dt)


class XKRX(KoreaExchange):
    pass


class KRX(KoreaExchange):
    pass
