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
from unittest import TestCase

from holidays.calendars.gregorian import MON, SUN
from holidays.constants import PUBLIC, SCHOOL
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    ObservedRule,
    SAT_SUN_TO_NEXT_MON,
)


class CategoriesStub(ObservedHolidayBase):
    subdivisions = ("SD",)
    supported_categories = (PUBLIC, SCHOOL)
    observed_label = "%s (observed)"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_school_holidays(self):
        self._add_holiday_dec_25("School Holiday")
        self._add_holiday_dec_26("School Holiday")

    def _populate_subdiv_sd_public_holidays(self):
        # Observes all holidays of the date.
        self._add_observed(self._add_holiday_dec_25("Christmas Day"))
        # Moves all holidays of the date.
        self._move_holiday(self._add_holiday_dec_26("Boxing Day"))


class TestObservedHolidayBase(TestCase):
    SUNDAY = date(2024, 5, 12)
    MONDAY = date(2024, 5, 13)
    SUN_TO_NONE = ObservedRule({SUN: None})
    MON_TO_TUE = ObservedRule({MON: +1})

    def setUp(self):
        self.ohb = ObservedHolidayBase(observed_rule=ObservedRule({MON: None}))
        self.ohb.observed_label = "%s (Observed Label)"
        self.ohb._populate(2024)

    def test_categories_population_isolation(self):
        # 2027-12-25 and 2027-12-26 are Saturday and Sunday.
        public_holidays = {
            date(2027, 12, 25): "Christmas Day",
            date(2027, 12, 27): "Boxing Day (observed); Christmas Day (observed)",
        }
        school_holidays = {
            date(2027, 12, 25): "School Holiday",
            date(2027, 12, 26): "School Holiday",
        }
        self.assertEqual(dict(CategoriesStub(subdiv="SD", years=2027)), public_holidays)
        self.assertEqual(
            dict(CategoriesStub(subdiv="SD", years=2027, categories=SCHOOL)), school_holidays
        )
        self.assertEqual(
            dict(CategoriesStub(subdiv="SD", years=2027, categories=(PUBLIC, SCHOOL))),
            {
                date(2027, 12, 25): "Christmas Day; School Holiday",
                date(2027, 12, 26): "School Holiday",
                date(2027, 12, 27): "Boxing Day (observed); Christmas Day (observed)",
            },
        )

    def test_get_observed_date(self):
        self.assertIsNone(self.ohb._get_observed_date(self.SUNDAY, rule=self.SUN_TO_NONE))

    def test_observed_rules(self):
        self.assertEqual(
            (False, None),
            self.ohb._add_observed(
                self.ohb._add_holiday("Test Holiday", self.SUNDAY), rule=self.SUN_TO_NONE
            ),
        )

        self.assertEqual(
            (True, date(2024, 5, 14)),
            self.ohb._add_observed(
                self.ohb._add_holiday("Test Holiday", self.MONDAY), rule=self.MON_TO_TUE
            ),
        )

        self.assertEqual(
            dict(self.ohb),
            {
                date(2024, 5, 13): "Test Holiday",
                date(2024, 5, 14): "Test Holiday (Observed Label)",
            },
            self.ohb,
        )
