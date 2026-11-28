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
from holidays.countries.sweden import Sweden
from holidays.helpers import tr


class NasdaqStockholm(Sweden):
    """Nasdaq Stockholm (XSTO) holidays.

    Nasdaq Stockholm is closed on weekdays falling on New Year's Day, Epiphany,
    Good Friday, Easter Monday, May Day, Ascension Day, National Day, Midsummer
    Eve, Christmas Eve, Christmas Day, Second Day of Christmas and New Year's
    Eve.

    Equities have half trading days (close at 13:00 CET) on weekdays falling on
    Twelfth Night, Maundy Thursday, Walpurgis Night, the day before Ascension
    Day and All Saints' Eve.

    The exchange does not close or shorten equities trading on the other Swedish
    bank or optional days (the squeeze day after Ascension, and the days before
    Pentecost Eve, Midsummer Eve, Christmas Eve and New Year's Eve).

    References:
        * <https://www.nasdaq.com/european-market-activity/trading-hours>
        * [2024-2027](https://web.archive.org/web/20250728231639/https://www.nasdaq.com/european-market-activity/trading-hours)
    """

    country = None  # type: ignore[assignment]
    market = "XSTO"
    parent_entity = Sweden
    # The BANK, DE_FACTO and OPTIONAL categories are specific to the country entity.
    supported_categories = (HALF_DAY, PUBLIC)  # type: ignore[assignment]
    start_year = 2024

    def _add_holiday(self, name, *args):
        if self._is_weekend(*args):
            return None

        return super()._add_holiday(name, *args)

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        # Midsummer Eve.
        self._add_holiday_1st_fri_from_jun_19(tr("Midsommarafton"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Julafton"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Nyårsafton"))

    def _populate_half_day_holidays(self):
        # Twelfth Night.
        self._add_holiday_jan_5(tr("Trettondagsafton"))

        # Maundy Thursday.
        self._add_holy_thursday(tr("Skärtorsdagen"))

        # Walpurgis Night.
        self._add_holiday_apr_30(tr("Valborgsmässoafton"))

        # Day before Ascension Day.
        self._add_holiday_38_days_past_easter(tr("Dag före Kristi himmelsfärdsdag"))

        # All Saints' Eve.
        self._add_holiday_1st_fri_from_oct_30(tr("Allahelgonsafton"))


class XSTO(NasdaqStockholm):
    pass
