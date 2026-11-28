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

from unittest import TestCase

from holidays.countries.cameroon import Cameroon
from tests.common import CommonCountryTests


class TestCameroon(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Cameroon)

    def test_special_holidays(self):
        self.assertHoliday("2021-05-14", "2021-07-19")

    def test_new_years_day(self):
        name = "Jour de l'an"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_youth_day(self):
        name = "Fête de la Jeunesse"
        self.assertHolidayName(name, (f"{year}-02-11" for year in range(1966, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1966))
        obs_dts = (
            "2018-02-12",
            "2024-02-12",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_labor_day(self):
        name = "Fête du Travail"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dts = (
            "2016-05-02",
            "2022-05-03",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_national_day(self):
        name = "Fête nationale"
        self.assertHolidayName(name, (f"{year}-05-20" for year in range(1972, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1972))
        obs_dts = (
            "2012-05-21",
            "2018-05-21",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_assumption_day(self):
        name = "Assomption"
        self.assertHolidayName(name, (f"{year}-08-15" for year in self.full_range))
        obs_dts = (
            "2010-08-16",
            "2021-08-16",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        name = "Noël"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_fitr(self):
        name = "Aïd el-Fitr"
        self.assertHolidayName(
            name,
            "2018-06-15",
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2025-03-31",
            "2026-03-20",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2012-08-20",
            "2020-05-25",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_adha(self):
        name = "Aïd al-Adha"
        self.assertHolidayName(
            name,
            "2018-08-21",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2024-06-16",
            "2025-06-06",
            "2026-05-27",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2007-01-02",  # special case
            "2014-10-06",
            "2019-08-12",
            "2024-06-17",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_prophets_birthday(self):
        name = "Naissance du Prophète Mouhammad"
        self.assertHolidayName(
            name,
            "2018-11-21",
            "2019-11-10",
            "2020-10-29",
            "2021-10-19",
            "2022-10-08",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2012-02-06",
            "2019-11-11",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Jour de l'an"),
            ("2022-02-11", "Fête de la Jeunesse"),
            ("2022-04-15", "Vendredi saint"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-02", "Aïd el-Fitr"),
            ("2022-05-03", "Fête du Travail (observé)"),
            ("2022-05-20", "Fête nationale"),
            ("2022-05-26", "Ascension"),
            ("2022-07-09", "Aïd al-Adha"),
            ("2022-08-15", "Assomption"),
            ("2022-10-08", "Naissance du Prophète Mouhammad"),
            ("2022-12-25", "Noël"),
            ("2022-12-26", "Noël (observé)"),
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Jour de l'an"),
            ("2025-02-11", "Fête de la Jeunesse"),
            ("2025-03-31", "Aïd el-Fitr"),
            ("2025-04-18", "Vendredi saint"),
            ("2025-05-01", "Fête du Travail"),
            ("2025-05-20", "Fête nationale"),
            ("2025-05-29", "Ascension"),
            ("2025-06-06", "Aïd al-Adha"),
            ("2025-08-15", "Assomption"),
            ("2025-09-04", "Naissance du Prophète Mouhammad (estimé)"),
            ("2025-12-25", "Noël"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2026-01-01", "Jour de l'an"),
            ("2026-02-11", "Fête de la Jeunesse"),
            ("2026-03-20", "Aïd el-Fitr"),
            ("2026-04-03", "Vendredi saint"),
            ("2026-05-01", "Fête du Travail"),
            ("2026-05-14", "Ascension"),
            ("2026-05-20", "Fête nationale"),
            ("2026-05-27", "Aïd al-Adha"),
            ("2026-08-15", "Assomption"),
            ("2026-08-25", "Naissance du Prophète Mouhammad (estimé)"),
            ("2026-12-25", "Noël"),
        )

    def test_l10n_en_cm(self):
        self.assertLocalizedHolidays(
            "en_CM",
            ("2026-01-01", "New Year's Day"),
            ("2026-02-11", "Youth Day"),
            ("2026-03-20", "Eid al-Fitr"),
            ("2026-04-03", "Good Friday"),
            ("2026-05-01", "Labour Day"),
            ("2026-05-14", "Ascension Day"),
            ("2026-05-20", "National Day"),
            ("2026-05-27", "Eid al-Adha"),
            ("2026-08-15", "Assumption Day"),
            ("2026-08-25", "Prophet's Birthday (estimated)"),
            ("2026-12-25", "Christmas Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2026-01-01", "New Year's Day"),
            ("2026-02-11", "Youth Day"),
            ("2026-03-20", "Eid al-Fitr"),
            ("2026-04-03", "Good Friday"),
            ("2026-05-01", "Labor Day"),
            ("2026-05-14", "Ascension Day"),
            ("2026-05-20", "National Day"),
            ("2026-05-27", "Eid al-Adha"),
            ("2026-08-15", "Assumption Day"),
            ("2026-08-25", "Prophet's Birthday (estimated)"),
            ("2026-12-25", "Christmas Day"),
        )
