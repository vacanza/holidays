#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.iraq import Iraq, IQ, IRQ
from tests.common import CommonCountryTests


class TestIraq(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Iraq)

    def test_country_aliases(self):
        self.assertAliases(Iraq, IQ, IRQ)

    def test_no_holidays(self):
        """Test that no holidays are returned for years before start_year."""
        # Test the year just before start_year
        h = Iraq(years=1932)
        self.assertNoHolidays(h)

        # Test a much earlier year
        h = Iraq(years=1900)
        self.assertEqual(len(h), 0)

        # Test that no holidays are returned for a range of early years
        h = Iraq(years=[1900, 1901, 1902])
        self.assertEqual(len(h), 0)

        # Test that holidays are returned for the start year
        h = Iraq(years=1933)
        self.assertGreater(len(h), 0)

        # Test that _populate_public_holidays returns None for early years
        h = Iraq()
        h._year = 1900  # Manually set the year to test the early return
        self.assertIsNone(h._populate_public_holidays())

    def test_2021(self):
        self.assertHolidays(
            ("2021-01-01", "رأس السنة الجديدة"),
            ("2021-01-06", "يوم الجيش"),
            ("2021-03-21", "نوروز"),
            ("2021-05-01", "عيد العمال"),
            ("2021-05-13", "عيد الفطر"),
            ("2021-05-14", "عيد الفطر"),
            ("2021-05-15", "عيد الفطر"),
            ("2021-07-14", "اليوم الوطني"),
            ("2021-07-20", "عيد الأضحى"),
            ("2021-07-21", "عيد الأضحى"),
            ("2021-07-22", "عيد الأضحى"),
            ("2021-07-23", "عيد الأضحى"),
            ("2021-08-09", "رأس السنة الهجرية"),
            ("2021-08-19", "عاشوراء"),
            ("2021-10-03", "اليوم الوطني"),
            ("2021-10-18", "المولد النبوي الشريف"),
            ("2021-12-10", "يوم النصر"),
            ("2021-12-25", "يوم عيد الميلاد"),
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "رأس السنة الجديدة"),
            ("2022-01-06", "يوم الجيش"),
            ("2022-03-21", "نوروز"),
            ("2022-05-01", "عيد العمال"),
            ("2022-05-02", "عيد الفطر"),
            ("2022-05-03", "عيد الفطر"),
            ("2022-05-04", "عيد الفطر"),
            ("2022-07-09", "عيد الأضحى"),
            ("2022-07-10", "عيد الأضحى"),
            ("2022-07-11", "عيد الأضحى"),
            ("2022-07-12", "عيد الأضحى"),
            ("2022-07-13", "عيد الأضحى"),
            ("2022-07-14", "يوم الجمهورية"),
            ("2022-07-30", "رأس السنة الهجرية"),
            ("2022-08-08", "عاشوراء"),
            ("2022-10-03", "اليوم الوطني"),
            ("2022-10-08", "المولد النبوي الشريف"),
            ("2022-12-10", "يوم النصر"),
            ("2022-12-25", "يوم عيد الميلاد"),
        )

    def test_eid_al_ghadir(self):
        """Test Eid al-Ghadir holiday which is not observed in 2021 and 2022."""
        # Test 2021 - should not have Eid al-Ghadir
        h = Iraq(years=2021)
        self.assertNotIn("2021-07-19", h)  # Eid al-Ghadir date in 2021

        # Test 2022 - should not have Eid al-Ghadir
        h = Iraq(years=2022)
        self.assertNotIn("2022-07-08", h)  # Eid al-Ghadir date in 2022

        # Test 2023 - should have Eid al-Ghadir
        h = Iraq(years=2023)
        self.assertIn("2023-07-07", h)  # Eid al-Ghadir date in 2023
        self.assertEqual(h["2023-07-07"], "عيد الغدير")

    def test_special_holidays(self):
        """Test special holidays including Easter and Sukkot."""
        h = Iraq(years=2024, include_special=True)

        # Test Easter Sunday and Monday
        self.assertIn("2024-03-31", h)  # Easter Sunday 2024
        self.assertEqual(h["2024-03-31"], "عيد الفصح")
        self.assertIn("2024-04-01", h)  # Easter Monday 2024
        self.assertEqual(h["2024-04-01"], "عيد الفصح")

        # Test Sukkot
        self.assertIn("2024-10-17", h)  # First day of Sukkot 2024
        self.assertEqual(h["2024-10-17"], "عيد العُرش")

        # Test Passover
        self.assertIn("2024-04-23", h)  # First day of Passover 2024
        self.assertEqual(h["2024-04-23"], "عيد الفصح")

        # Test that special holidays are not included by default
        h_default = Iraq(years=2024)
        self.assertNotIn("2024-03-31", h_default)  # Easter Sunday should not be present
        self.assertNotIn("2024-10-17", h_default)  # Sukkot should not be present
        self.assertNotIn("2024-04-23", h_default)  # Passover should not be present

    def test_islamic_show_estimated(self):
        """Test that islamic_show_estimated parameter works correctly."""
        # Test with islamic_show_estimated=False
        h = Iraq(years=2023, islamic_show_estimated=False)
        self.assertIn("2023-07-19", h)  # Islamic New Year
        self.assertEqual(h["2023-07-19"], "رأس السنة الهجرية")  # No estimated label

        # Test with islamic_show_estimated=True (default)
        h = Iraq(years=2023)
        self.assertIn("2023-07-19", h)  # Islamic New Year
        self.assertEqual(h["2023-07-19"], "رأس السنة الهجرية (تقديري)")  # With estimated label
