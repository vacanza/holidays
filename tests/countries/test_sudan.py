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

from holidays.countries.sudan import Sudan
from tests.common import CommonCountryTests


class TestSudan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Sudan)

    def test_independence_day(self):
        self.assertHolidayName(
            "عيد الإستقلال", (f"{year}-01-01" for year in range(self.start_year, self.end_year))
        )

    def test_coptic_christmas(self):
        name = "عيد الميلاد المجيد"
        self.assertHolidayName(
            name,
            (
                f"{year}-01-07"
                for year in (*range(self.start_year, 2011), *range(2019, self.end_year))
            ),
        )
        self.assertNoHolidayName(name, range(2011, 2019))

    def test_christmas_day(self):
        name = "عيد الميلاد"
        self.assertHolidayName(
            name,
            (
                f"{year}-12-25"
                for year in (*range(self.start_year, 2011), *range(2019, self.end_year))
            ),
        )
        self.assertNoHolidayName(name, range(2011, 2019))

    def test_coptic_easter(self):
        name = "عيد الفصح القبطي"
        self.assertHolidayName(
            name,
            "2019-04-28",
            "2020-04-19",
            "2021-05-02",
            "2022-04-24",
            "2023-04-16",
            "2024-05-05",
            "2025-04-20",
        )
        self.assertHolidayName(name, range(self.start_year, 2011), range(2019, self.end_year))
        self.assertNoHolidayName(name, range(2011, 2019))

    def test_islamic_new_year(self):
        name = "رأس السنة الهجرية"
        self.assertHolidayName(
            name,
            "2020-08-20",
            "2021-08-11",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(self.start_year, self.end_year))

    def test_prophets_birthday(self):
        name = "المولد النبوي الشريف"
        self.assertHolidayName(
            name,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-28",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(self.start_year, self.end_year))

    def test_eid_al_fitr(self):
        name = "عيد الفطر المبارك"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-01",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(self.start_year, self.end_year))
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 3, set(range(self.start_year, 2020)) - {2000}
        )
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 4, set(range(2020, self.end_year)) - {2033}
        )

    def test_eid_al_adha(self):
        name = "عيد الأضحى المبارك"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-10",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(self.start_year, self.end_year))
        self.assertIslamicNoEstimatedHolidayNameCount(
            name,
            5,
            set(range(self.start_year, self.end_year)) - {2006, 2007, 2039},
        )

    def test_weekend(self):
        for dt in (
            "2008-01-18",  # FRI.
            "2008-01-25",  # FRI.
            "2008-01-26",  # SAT.
            "2008-02-01",  # FRI.
            "2008-02-02",  # SAT.
        ):
            self.assertTrue(self.holidays.is_weekend(dt))

        for dt in (
            "2008-01-17",  # THU.
            "2008-01-19",  # SAT.
            "2008-01-20",  # SUN.
            "2008-01-24",  # THU.
            "2008-01-27",  # SUN.
        ):
            self.assertFalse(self.holidays.is_weekend(dt))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "عيد الإستقلال"),
            ("2022-01-07", "عيد الميلاد المجيد"),
            ("2022-04-24", "عيد الفصح القبطي"),
            ("2022-05-01", "عيد الفطر المبارك"),
            ("2022-05-02", "عيد الفطر المبارك"),
            ("2022-05-03", "عيد الفطر المبارك"),
            ("2022-05-04", "عيد الفطر المبارك"),
            ("2022-07-09", "عيد الأضحى المبارك"),
            ("2022-07-10", "عيد الأضحى المبارك"),
            ("2022-07-11", "عيد الأضحى المبارك"),
            ("2022-07-12", "عيد الأضحى المبارك"),
            ("2022-07-13", "عيد الأضحى المبارك"),
            ("2022-07-30", "رأس السنة الهجرية"),
            ("2022-10-08", "المولد النبوي الشريف"),
            ("2022-12-25", "عيد الميلاد"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "Independence Day"),
            ("2022-01-07", "Coptic Christmas"),
            ("2022-04-24", "Coptic Easter"),
            ("2022-05-01", "Eid al-Fitr"),
            ("2022-05-02", "Eid al-Fitr"),
            ("2022-05-03", "Eid al-Fitr"),
            ("2022-05-04", "Eid al-Fitr"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-07-10", "Eid al-Adha"),
            ("2022-07-11", "Eid al-Adha"),
            ("2022-07-12", "Eid al-Adha"),
            ("2022-07-13", "Eid al-Adha"),
            ("2022-07-30", "Islamic New Year"),
            ("2022-10-08", "Prophet's Birthday"),
            ("2022-12-25", "Christmas Day"),
        )
