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

from holidays.constants import PUBLIC
from holidays.countries.austria import Austria
from holidays.helpers import tr
from holidays.mixins.child_entity import ChildEntity


class ViennaStockExchange(ChildEntity, Austria):
    """Vienna Stock Exchange (Wiener Börse) holidays.

    The exchange is closed on Austrian public holidays falling on weekdays, and also on
    Good Friday, Christmas Eve and New Year's Eve. Since 2019 it trades on Epiphany,
    Ascension Day, Corpus Christi, Assumption Day, All Saints' Day and Immaculate
    Conception, and since 2023 also on Whit Monday.

    References:
        * [2018](https://web.archive.org/web/20180126183959/https://www.wienerborse.at/en/trading/trading-information/trading-calendar/)
        * [2019](https://web.archive.org/web/20191117153341/https://www.wienerborse.at/uploads/u/cms/files/handel/boersenfeiertage-2019.pdf)
        * [2020](https://web.archive.org/web/20191117153341/https://www.wienerborse.at/uploads/u/cms/files/handel/boersenfeiertage-2020.pdf)
        * [2021](https://web.archive.org/web/20201203043444/https://www.wienerborse.at/uploads/u/cms/files/handel/boersenfeiertage-2021.pdf)
        * [2022](https://web.archive.org/web/20211217091016/https://www.wienerborse.at/uploads/u/cms/files/handel/boersenfeiertage-2022.pdf)
        * [2023](https://web.archive.org/web/20230129190521/https://www.wienerborse.at/uploads/u/cms/files/trading/stock-exchange-holidays-2023-en.pdf)
        * [2024](https://web.archive.org/web/20240207120546/https://www.wienerborse.at/uploads/u/cms/files/trading/stock-exchange-holidays-2024-en.pdf)
        * [2025](https://web.archive.org/web/20260103203227/https://www.wienerborse.at/uploads/u/cms/files/trading/stock-exchange-holidays-2025-en.pdf)
        * [2026](https://web.archive.org/web/20251218144117/https://www.wienerborse.at/uploads/u/cms/files/trading/stock-exchange-holidays-2026-en.pdf)
        * [2027](https://www.wienerborse.at/uploads/u/cms/files/trading/stock-exchange-holidays-2027-en.pdf)
    """

    country = None  # type: ignore[assignment]
    market = "XWBO"
    parent_entity = Austria
    parent_entity_subdivision_code = "9"
    supported_categories = (PUBLIC,)
    start_year = 2018

    def _add_holiday(self, name, *args):
        if self._is_weekend(*args):
            return None

        return super()._add_holiday(name, *args)

    def _populate_public_holidays(self):
        if self._year <= 2018:
            super()._populate_public_holidays()
        else:
            # New Year's Day.
            self._add_new_years_day(tr("Neujahr"))

            # Easter Monday.
            self._add_easter_monday(tr("Ostermontag"))

            # Labor Day.
            self._add_labor_day(tr("Staatsfeiertag"))

            if self._year <= 2022:
                # Pentecost Monday.
                self._add_pentecost_monday(tr("Pfingstmontag"))

            # National Day.
            self._add_holiday_oct_26(tr("Nationalfeiertag"))

            # Christmas Day.
            self._add_christmas_day(tr("Christtag"))

            # Saint Stephen's Day.
            self._add_christmas_day_two(tr("Stephanstag"))

        # Good Friday.
        self._add_good_friday(tr("Karfreitag"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Heiliger Abend"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Silvester"))


class XWBO(ViennaStockExchange):
    pass


class WBAG(ViennaStockExchange):
    pass
