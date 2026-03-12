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

from holidays.countries.kosovo import Kosovo
from tests.common import CommonCountryTests


class TestKosovo(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Kosovo)

    def test_new_years_day(self):
        name = "Viti i Ri"
        self.assertHolidayName(
            name,
            (f"{year}-01-01" for year in self.full_range),
            (f"{year}-01-02" for year in self.full_range),
        )

    def test_orthodox_christmas_day(self):
        name = "Krishtlindjet Ortodokse"
        self.assertHolidayName(name, (f"{year}-01-07" for year in self.full_range))

    def test_independence_day(self):
        name = "Dita e Pavarësisë së Republikës së Kosovës"
        self.assertHolidayName(name, (f"{year}-02-17" for year in self.full_range))

    def test_constitution_day(self):
        name = "Dita e Kushtetutës së Republikës së Kosovës"
        self.assertHolidayName(name, (f"{year}-04-09" for year in self.full_range))

    def test_international_workers_day(self):
        name = "Dita Ndërkombëtare e Punës"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))

    def test_europe_day(self):
        name = "Dita e Evropës"
        self.assertHolidayName(name, (f"{year}-05-09" for year in self.full_range))

    def test_catholic_easter(self):
        name = "Pashkët Katolike"
        self.assertHolidayName(
            name,
            "2020-04-12",
            "2020-04-13",
            "2021-04-04",
            "2021-04-05",
            "2022-04-17",
            "2022-04-18",
            "2023-04-09",
            "2023-04-10",
            "2024-03-31",
            "2024-04-01",
            "2025-04-20",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_orthodox_easter(self):
        name = "Pashkët Ortodokse"
        self.assertHolidayName(
            name,
            "2020-04-19",
            "2020-04-20",
            "2021-05-02",
            "2021-05-03",
            "2022-04-24",
            "2022-04-25",
            "2023-04-16",
            "2023-04-17",
            "2024-05-05",
            "2024-05-06",
            "2025-04-20",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_eid_al_fitr(self):
        name = "Bajrami i Madh, dita e parë"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_adha(self):
        name = "Bajrami i Vogël, dita e parë"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_catholic_christmas_day(self):
        name = "Krishtlindjet Katolike"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "Viti i Ri"),
            ("2024-01-02", "Viti i Ri"),
            ("2024-01-07", "Krishtlindjet Ortodokse"),
            ("2024-02-17", "Dita e Pavarësisë së Republikës së Kosovës"),
            ("2024-03-31", "Pashkët Katolike"),
            ("2024-04-01", "Pashkët Katolike"),
            ("2024-04-09", "Dita e Kushtetutës së Republikës së Kosovës"),
            ("2024-04-10", "Bajrami i Madh, dita e parë (e vlerësuar)"),
            ("2024-05-01", "Dita Ndërkombëtare e Punës"),
            ("2024-05-05", "Pashkët Ortodokse"),
            ("2024-05-06", "Pashkët Ortodokse"),
            ("2024-05-09", "Dita e Evropës"),
            ("2024-06-16", "Bajrami i Vogël, dita e parë (e vlerësuar)"),
            ("2024-12-25", "Krishtlindjet Katolike"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Viti i Ri"),
            ("2024-01-02", "Viti i Ri"),
            ("2024-01-07", "Krishtlindjet Ortodokse"),
            ("2024-02-17", "Dita e Pavarësisë së Republikës së Kosovës"),
            ("2024-03-31", "Pashkët Katolike"),
            ("2024-04-01", "Pashkët Katolike"),
            ("2024-04-09", "Dita e Kushtetutës së Republikës së Kosovës"),
            ("2024-04-10", "Bajrami i Madh, dita e parë (e vlerësuar)"),
            ("2024-05-01", "Dita Ndërkombëtare e Punës"),
            ("2024-05-05", "Pashkët Ortodokse"),
            ("2024-05-06", "Pashkët Ortodokse"),
            ("2024-05-09", "Dita e Evropës"),
            ("2024-06-16", "Bajrami i Vogël, dita e parë (e vlerësuar)"),
            ("2024-12-25", "Krishtlindjet Katolike"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "New Year's Day"),
            ("2024-01-07", "Orthodox Christmas Day"),
            ("2024-02-17", "Independence Day"),
            ("2024-03-31", "Catholic Easter"),
            ("2024-04-01", "Catholic Easter"),
            ("2024-04-09", "Constitution Day"),
            ("2024-04-10", "Eid al-Fitr (estimated)"),
            ("2024-05-01", "International Workers' Day"),
            ("2024-05-05", "Orthodox Easter"),
            ("2024-05-06", "Orthodox Easter"),
            ("2024-05-09", "Europe Day"),
            ("2024-06-16", "Eid al-Adha (estimated)"),
            ("2024-12-25", "Catholic Christmas Day"),
        )

    def test_l10n_sr(self):
        self.assertLocalizedHolidays(
            "sr",
            ("2024-01-01", "Nova godina"),
            ("2024-01-02", "Nova godina"),
            ("2024-01-07", "Pravoslavni Božić"),
            ("2024-02-17", "Dan Nezavisnosti Republike Kosova"),
            ("2024-03-31", "Katolički Uskrs"),
            ("2024-04-01", "Katolički Uskrs"),
            ("2024-04-09", "Dan Ustava Republike Kosova"),
            ("2024-04-10", "Fiter Bajram, prvi dan (procenjeno)"),
            ("2024-05-01", "Međunarodni Dan Rada"),
            ("2024-05-05", "Pravoslavni Uskrs"),
            ("2024-05-06", "Pravoslavni Uskrs"),
            ("2024-05-09", "Dan Evrope"),
            ("2024-06-16", "Kurban Bajram, prvi dan (procenjeno)"),
            ("2024-12-25", "Katolički Božić"),
        )
