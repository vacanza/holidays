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

import os
from pathlib import Path
from unittest import TestCase, skipUnless

import holidays
from holidays import HolidayBase

CHECKOUT_ROOT = Path(__file__).resolve().parents[1]
REQUIRE_INSTALLED_HOLIDAYS = os.environ.get("REQUIRE_INSTALLED_HOLIDAYS") == "1"


class TestHolidaysImports(TestCase):
    def assertImport(self, name):  # noqa: N802
        self.assertTrue(hasattr(holidays, name), f"Import error: `from holidays import {name}`")

    def test_constants(self):
        for name in ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN", "WEEKEND"):
            self.assertImport(name)

    def test_holidays_base(self):
        for name in ("DateLike", "HolidayBase", "HolidaySum"):
            self.assertImport(name)

    def test_subpackage_entities(self):
        from holidays import countries, financial

        self.assertTrue(issubclass(countries.US, countries.UnitedStates))
        self.assertTrue(issubclass(financial.NYSE, financial.NewYorkStockExchange))
        self.assertIsInstance(countries.US(), HolidayBase)
        self.assertIsInstance(financial.NYSE(), HolidayBase)

    def test_top_level_entities(self):
        for name in ("US", "USA", "UnitedStates", "CA", "NYSE", "XNYS", "ECB"):
            self.assertImport(name)

        self.assertIsInstance(holidays.US(), HolidayBase)
        self.assertIsInstance(holidays.NYSE(), HolidayBase)

    def test_utils(self):
        for name in (
            "country_holidays",
            "CountryHoliday",
            "financial_holidays",
            "list_localized_countries",
            "list_localized_financial",
            "list_supported_countries",
            "list_supported_financial",
        ):
            self.assertImport(name)

    def test_utils_instantiate_entities(self):
        us_holidays = holidays.country_holidays("US")
        nyse_holidays = holidays.financial_holidays("NYSE")

        self.assertIsInstance(us_holidays, HolidayBase)
        self.assertIsInstance(nyse_holidays, HolidayBase)
        self.assertIn("US", holidays.list_supported_countries())
        self.assertIn("XNYS", holidays.list_supported_financial())

    def test_version_matches_version_file(self):
        """Installed __version__ must match VERSION (exact or pre-release .devN prefix)."""
        expected = (CHECKOUT_ROOT / "VERSION").read_text(encoding="utf-8").strip()
        actual = holidays.__version__
        self.assertTrue(
            actual == expected or actual.startswith(f"{expected}."),
            f"holidays.__version__={actual!r} does not match VERSION={expected!r}",
        )


@skipUnless(REQUIRE_INSTALLED_HOLIDAYS, "Requires REQUIRE_INSTALLED_HOLIDAYS=1 (build tests)")
class TestHolidaysInstalledPackage(TestCase):
    def test_package_loaded_from_install(self):
        """Source `holidays/` is removed; the imported package must be the install."""
        package_file = Path(holidays.__file__).resolve()
        checkout_package = (CHECKOUT_ROOT / "holidays").resolve()

        self.assertFalse(
            checkout_package.exists(),
            "Source holidays/ must be removed when REQUIRE_INSTALLED_HOLIDAYS=1",
        )
        try:
            package_file.relative_to(CHECKOUT_ROOT)
        except ValueError:
            return
        self.fail(f"Expected installed package outside checkout, got {package_file}")
