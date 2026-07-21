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

from holidays.constants import HALF_DAY, PUBLIC
from holidays.countries.south_africa import SouthAfrica
from holidays.observed_holiday_base import SAT_SUN_TO_NONE


class JohannesburgStockExchange(SouthAfrica):
    """Johannesburg Stock Exchange (JSE) holidays.

    References:
        [2019](https://web.archive.org/web/20230103093400/https://clientportal.jse.co.za/Content/JSE%20Trading%20Dates%20and%20Calendars%20Items/JSE%20Market%20Notice%202019%20Markets%20Calendar.pdf)
        [2020](https://web.archive.org/web/20220123212248/https://clientportal.jse.co.za/Content/JSE%20Trading%20Dates%20and%20Calendars%20Items/JSE%20Market%20Notice%2030319%20All%20Markets%20-%20Calendar%202020.pdf)
        [2021](https://web.archive.org/web/20220123222115/https://clientportal.jse.co.za/Content/JSE%20Trading%20Dates%20and%20Calendars%20Items/JSE%20Market%20Notice%2051720%20All%20Markets%20-%20Updated%20JSE%20Markets%20Calendar%202021.pdf)
        [2022](https://web.archive.org/web/20250914180247/https://clientportal.jse.co.za/Content/JSE%20Trading%20Dates%20and%20Calendars%20Items/JSE%20Markets%20Calendar%202022%20Market%20Notice%20updated.pdf)
        [2023](https://web.archive.org/web/20250914175608/https://clientportal.jse.co.za/Content/JSE%20Trading%20Dates%20and%20Calendars%20Items/JSE%20Market%20Notice%2051122%20All%20Markets%20-%20JSE%20Markets%20Calendar%202023.pdf)
        [2024](https://web.archive.org/web/20240614114810/https://clientportal.jse.co.za/Content/JSE%20Trading%20Dates%20and%20Calendars%20Items/JSE%20Market%20Notice%2006124%20All%20Markets%20-%20JSE%20Markets%20Calendar%202024%20-%20Updated.pdf)
        [2025](https://web.archive.org/web/20251122211135/https://clientportal.jse.co.za/Content/JSE%20Trading%20Dates%20and%20Calendars%20Items/JSE%20Market%20Notice%2030524%20All%20Markets%20-%20JSE%20Markets%20Calendar%202025.pdf)
        [2026](https://web.archive.org/web/20260123013926/https://clientportal.jse.co.za/Content/JSE%20Trading%20Dates%20and%20Calendars%20Items/JSE%20Market%20Notice%2038025%20All%20Markets%20-%20JSE%20Markets%20Calendar%202026.pdf)
    """

    country = None  # type: ignore[assignment]
    market = "XJSE"
    parent_entity = SouthAfrica
    supported_categories: tuple[str, ...] = (HALF_DAY, PUBLIC)  # type: ignore[assignment]
    start_year = 2000
    observed_label = "%s"

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        for dt in tuple(self):
            if self._is_weekend(dt):
                self.pop(dt)

    def _populate_half_day_holidays(self):
        # %s (markets close at 12:00 p.m. SAST).
        pause_label = "%s (markets close at 12:00 p.m. SAST)"

        self._move_holiday(
            # Christmas Eve.
            self._add_christmas_eve(self._format_holiday_name(pause_label, "Christmas Eve")),
            rule=SAT_SUN_TO_NONE,
        )

        self._move_holiday(
            # New Year's Eve.
            self._add_new_years_eve(self._format_holiday_name(pause_label, "New Year's Eve")),
            rule=SAT_SUN_TO_NONE,
        )


class XJSE(JohannesburgStockExchange):
    pass


class JSE(JohannesburgStockExchange):
    pass
