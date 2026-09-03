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

from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
    SAT_SUN_TO_NONE,
    SAT_SUN_TO_PREV_FRI,
)


class Euronext(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Euronext Stock Exchanges holidays.

    References:
        * https://web.archive.org/web/20260417160659/https://www.euronext.com/en/trading/trading-hours-holidays

    """

    market = "Euronext"
    start_year = 2021
    default_language = "en_US"
    supported_languages = ("en_US", "fr", "it", "nl", "no", "pt_PT")
    supported_categories = (HALF_DAY, PUBLIC)

    subdivisions = (
        "XAMS",
        "XBRU",
        "XDUB",
        "XLIS",
        "XMIL",
        "XOSL",
        "XPAR",
    )

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NONE)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        self.subdiv = getattr(self, "parent_entity_subdivision_code", self.subdiv)
        is_xdub = self.subdiv == "XDUB"

        self._move_holiday(
            # New Year's Day.
            self._add_new_years_day(tr("New Year's Day")),
            rule=SAT_SUN_TO_NEXT_MON if is_xdub else self._observed_rule,
        )

        self._move_holiday(
            # Christmas Day.
            self._add_christmas_day(tr("Christmas Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE if is_xdub else self._observed_rule,
        )

        self._move_holiday(
            # Boxing Day.
            self._add_christmas_day_two(tr("Boxing Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE if is_xdub else self._observed_rule,
        )

        self._move_holiday(
            # St. Stephen's Day.
            self._add_christmas_day_two(tr("Stephen's Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE if is_xdub else self._observed_rule,
        )

        # Labour Day.
        self._move_holiday(self._add_labor_day(tr("Labour Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

    def _populate_half_day_holidays(self):
        code = getattr(self, "parent_entity_subdivision_code", self.subdiv)
        if code == "XMIL":
            return

        # %s (Half Day Trading).
        half_day_label = tr("%s (Half Day Trading)")

        subdiv_method = (
            getattr(self, f"_populate_subdiv_{code.lower()}_half_day_holidays", None)
            if code
            else None
        )

        if subdiv_method:
            subdiv_method()
        else:
            self._move_holiday(
                self._add_christmas_eve(
                    # Christmas Eve.
                    self._format_holiday_name(half_day_label, tr("Christmas Eve"))
                )
            )
            self._move_holiday(
                self._add_new_years_eve(
                    # New Year's Eve.
                    self._format_holiday_name(half_day_label, tr("New Year's Eve"))
                )
            )

    def _populate_subdiv_xdub_public_holidays(self):
        # May Bank Holiday.
        self._add_holiday_1st_mon_of_may(tr("May Bank Holiday"))

    def _populate_subdiv_xdub_half_day_holidays(self):
        # %s (Half Day Trading).
        half_day_label = tr("%s (Half Day Trading)")

        self._move_holiday(
            self._add_christmas_eve(
                # Christmas Eve.
                self._format_holiday_name(half_day_label, tr("Christmas Eve"))
            ),
            rule=SAT_SUN_TO_PREV_FRI,
        )

        self._move_holiday(
            self._add_new_years_eve(
                # New Year's Eve.
                self._format_holiday_name(half_day_label, tr("New Year's Eve"))
            ),
            rule=SAT_SUN_TO_PREV_FRI,
        )

    def _populate_subdiv_xmil_public_holidays(self):
        # Assumption of Mary.
        self._move_holiday(self._add_assumption_of_mary_day(tr("Assumption of Mary")))

        # Christmas Eve.
        self._move_holiday(self._add_christmas_eve(tr("Christmas Eve")))

        # New Year's Eve.
        self._move_holiday(self._add_new_years_eve(tr("New Year's Eve")))

    def _populate_subdiv_xosl_public_holidays(self):
        # Constitution Day.
        self._move_holiday(self._add_holiday_may_17(tr("Constitution Day")))

        # Christmas Eve.
        self._move_holiday(self._add_christmas_eve(tr("Christmas Eve")))

        # New Year's Eve.
        self._move_holiday(self._add_new_years_eve(tr("New Year's Eve")))

        # Maundy Thursday.
        self._add_holy_thursday(tr("Maundy Thursday"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Ascension Day"))

        # Whit Monday.
        self._add_pentecost_monday(tr("Whit Monday"))

    def _populate_subdiv_xosl_half_day_holidays(self):
        # %s (Half Day Trading).
        half_day_label = tr("%s (Half Day Trading)")

        self._add_holy_wednesday(
            # Wednesday before Maundy Thursday.
            self._format_holiday_name(half_day_label, tr("Wednesday before Maundy Thursday"))
        )


class XAMS(Euronext):
    """Euronext Amsterdam."""

    parent_entity = Euronext
    parent_entity_subdivision_code = "XAMS"


class XBRU(Euronext):
    """Euronext Brussels."""

    parent_entity = Euronext
    parent_entity_subdivision_code = "XBRU"


class XDUB(Euronext):
    """Euronext Dublin."""

    parent_entity = Euronext
    parent_entity_subdivision_code = "XDUB"


class XLIS(Euronext):
    """Euronext Lisbon."""

    parent_entity = Euronext
    parent_entity_subdivision_code = "XLIS"


class XMIL(Euronext):
    """Euronext Milan."""

    parent_entity = Euronext
    parent_entity_subdivision_code = "XMIL"


class XOSL(Euronext):
    """Euronext Oslo."""

    parent_entity = Euronext
    parent_entity_subdivision_code = "XOSL"


class XPAR(Euronext):
    """Euronext Paris."""

    parent_entity = Euronext
    parent_entity_subdivision_code = "XPAR"
