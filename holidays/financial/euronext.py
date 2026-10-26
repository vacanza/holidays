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
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.helpers import tr
from holidays.mixins.child_entity import ChildEntity
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_PREV_FRI,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
    SAT_SUN_TO_NONE,
)


class Euronext(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Euronext holidays.

    Euronext cash and derivatives markets (Amsterdam, Brussels, Dublin, Lisbon, Milan, Oslo
    and Paris) share a common holiday calendar with a small number of market-specific closures.

    References:
        * [2019-2020](https://web.archive.org/web/20191229072655/https://www.euronext.com/en/trade/trading-hours-holidays)
        * [Oslo 2019-2020](https://web.archive.org/web/20191214032113/https://www.oslobors.no/ob_eng/Oslo-Boers/About-Oslo-Boers/Opening-hours)
        * [2021-2026](https://web.archive.org/web/20261014184052/https://www.euronext.com/en/trading/trading-hours-holidays)
    """

    # Euronext N.V. stock ticker.
    market = "ENX"
    default_language = "en_GB"
    supported_languages = ("en_GB", "en_US", "fr", "it", "nl", "no", "pt_PT")
    supported_categories = (HALF_DAY, PUBLIC)
    subdivisions: tuple[str, ...] = (
        "XAMS",  # Amsterdam.
        "XBRU",  # Brussels.
        "XDUB",  # Dublin.
        "XLIS",  # Lisbon.
        "XMIL",  # Milan.
        "XOSL",  # Oslo.
        "XPAR",  # Paris.
    )
    start_year = 2019

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NONE)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._move_holiday_forced(self._add_new_years_day(tr("New Year's Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Labor Day.
        self._move_holiday_forced(self._add_labor_day(tr("Labour Day")))

        # Christmas Day.
        self._move_holiday_forced(self._add_christmas_day(tr("Christmas Day")))

        # Saint Stephen's Day.
        self._move_holiday_forced(self._add_christmas_day_two(tr("Saint Stephen's Day")))

    def _populate_half_day_holidays(self):
        if self.subdiv in {"XMIL", "XOSL"}:
            return None

        close_label = (
            # %s (markets close at 12:30pm).
            tr("%s (markets close at 12:30pm)")
            if self.subdiv == "XDUB"
            # %s (markets close at 2:05pm CET).
            else tr("%s (markets close at 2:05pm CET)")
        )

        # Christmas Eve.
        self._move_holiday_forced(
            self._add_christmas_eve(self._format_holiday_name(close_label, tr("Christmas Eve"))),
        )

        # New Year's Eve.
        self._move_holiday_forced(
            self._add_new_years_eve(self._format_holiday_name(close_label, tr("New Year's Eve"))),
        )

    def _populate_subdiv_xdub_public_holidays(self):
        if self._year >= 2021:
            # Irish May Bank Holiday.
            self._add_holiday_1st_mon_of_may(tr("Irish May Bank Holiday"))

        self._move_holiday_forced(
            # New Year's Day.
            self._add_new_years_day(tr("New Year's Day")),
            rule=SAT_SUN_TO_NEXT_MON,
        )

        self._move_holiday_forced(
            # Christmas Day.
            self._add_christmas_day(tr("Christmas Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE,
        )

        self._move_holiday_forced(
            # Saint Stephen's Day.
            self._add_christmas_day_two(tr("Saint Stephen's Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE,
        )

    def _populate_subdiv_xdub_half_day_holidays(self):
        # %s (markets close at 12:30pm).
        close_12_30pm_label = tr("%s (markets close at 12:30pm)")

        self._move_holiday_forced(
            self._add_christmas_eve(
                # Christmas Eve.
                self._format_holiday_name(close_12_30pm_label, tr("Christmas Eve"))
            ),
            rule=SAT_SUN_TO_PREV_FRI,
        )
        self._move_holiday_forced(
            self._add_new_years_eve(
                # New Year's Eve.
                self._format_holiday_name(close_12_30pm_label, tr("New Year's Eve"))
            ),
            rule=SAT_SUN_TO_PREV_FRI,
        )

    def _populate_subdiv_xmil_public_holidays(self):
        if self._year <= 2022:
            return None

        # Assumption Day.
        self._move_holiday_forced(self._add_assumption_of_mary_day(tr("Assumption Day")))

        # Christmas Eve and New Year's Eve are full-day closures.
        # Christmas Eve.
        self._move_holiday_forced(self._add_christmas_eve(tr("Christmas Eve")))

        # New Year's Eve.
        self._move_holiday_forced(self._add_new_years_eve(tr("New Year's Eve")))

    def _populate_subdiv_xosl_public_holidays(self):
        # Maundy Thursday.
        self._add_holy_thursday(tr("Maundy Thursday"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Ascension Day"))

        # Constitution Day.
        self._move_holiday_forced(self._add_holiday_may_17(tr("Constitution Day")))

        # Pentecost Monday.
        self._add_pentecost_monday(tr("Whit Monday"))

        # Christmas Eve.
        self._move_holiday_forced(self._add_christmas_eve(tr("Christmas Eve")))

        # New Year's Eve.
        self._move_holiday_forced(self._add_new_years_eve(tr("New Year's Eve")))

    def _populate_subdiv_xosl_half_day_holidays(self):
        # %s (markets close at 13:00 CET).
        close_1pm_label = tr("%s (markets close at 13:00 CET)")

        self._add_holiday_4_days_prior_easter(
            # Wednesday before Easter.
            self._format_holiday_name(close_1pm_label, tr("Wednesday before Easter"))
        )


class ENX(Euronext):
    pass


class XPAR(Euronext):
    pass


class XAMS(ChildEntity, Euronext):
    parent_entity = Euronext
    parent_entity_subdivision_code = "XAMS"


class XBRU(ChildEntity, Euronext):
    parent_entity = Euronext
    parent_entity_subdivision_code = "XBRU"


class XDUB(ChildEntity, Euronext):
    parent_entity = Euronext
    parent_entity_subdivision_code = "XDUB"


class XLIS(ChildEntity, Euronext):
    parent_entity = Euronext
    parent_entity_subdivision_code = "XLIS"


class XMIL(ChildEntity, Euronext):
    parent_entity = Euronext
    parent_entity_subdivision_code = "XMIL"


class XOSL(ChildEntity, Euronext):
    parent_entity = Euronext
    parent_entity_subdivision_code = "XOSL"
