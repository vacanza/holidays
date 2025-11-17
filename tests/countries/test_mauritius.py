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

from holidays.countries.mauritius import Mauritius
from tests.common import CommonCountryTests


class TestMauritius(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1988, 2050)
        super().setUpClass(Mauritius, years=years)
        cls.no_estimated_holidays = Mauritius(years=years, islamic_show_estimated=False)

    def test_special_holidays(self):
        self.assertHolidayName("Public Holiday", "2019-07-29", "2019-09-09")

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1988, 2050)))

    def test_day_after_new_years_day(self):
        self.assertHolidayName(
            "Day after New Year's Day", (f"{year}-01-02" for year in range(1988, 2050))
        )

    def test_abolition_of_slavery_day(self):
        self.assertHolidayName(
            "Abolition of Slavery", (f"{year}-02-01" for year in range(1988, 2050))
        )

    def test_independence_and_republic_day(self):
        self.assertHolidayName(
            "Independence and Republic Day", (f"{year}-03-12" for year in range(1988, 2050))
        )

    def test_labour_day(self):
        self.assertHolidayName("Labour Day", (f"{year}-05-01" for year in range(1988, 2050)))

    def test_assumption_day(self):
        name = "Assumption of the Blessed Virgin Mary"
        self.assertHolidayName(name, (f"{year}-08-15" for year in range(2016, 2050, 2)))
        self.assertNoHolidayName(name, range(1988, 2016), range(2017, 2050, 2))

    def test_all_saints_day(self):
        name = "All Saints' Day"
        self.assertHolidayName(
            name, (f"{year}-11-01" for year in (*range(1988, 2016), *range(2017, 2050, 2)))
        )
        self.assertNoHolidayName(name, range(2016, 2050, 2))

    def test_arrival_of_indentured_labourers_day(self):
        self.assertHolidayName(
            "Arrival of Indentured Labourers", (f"{year}-11-02" for year in range(1988, 2050))
        )

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1988, 2050)))

    def test_chinese_spring_festival(self):
        name = "Chinese Spring Festival"
        self.assertHolidayName(
            name,
            "2021-02-12",
            "2022-02-01",
            "2023-01-22",
            "2024-02-10",
            "2025-01-29",
        )
        self.assertHolidayName(name, range(1988, 2050))

    def test_eid_al_fitr(self):
        name = "Eid-ul-Fitr"
        self.assertHolidayName(
            name,
            "2021-05-14",
            "2022-05-03",
            "2023-04-22",
            "2024-04-11",
            "2025-04-01",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1988, 2050))

    def test_thaipusam(self):
        name = "Thaipoosam Cavadee"
        self.assertHolidayName(
            name,
            "2021-01-28",
            "2022-01-18",
            "2023-02-04",
            "2024-01-25",
            "2025-02-11",
        )
        self.assertHolidayName(name, range(1988, 2050))

    def test_maha_shivaratri(self):
        name = "Maha Shivaratree"
        self.assertHolidayName(
            name,
            "2021-03-11",
            "2022-03-01",
            "2023-02-18",
            "2024-03-08",
            "2025-02-26",
        )
        self.assertHolidayName(name, range(2001, 2036))

    def test_ougadi(self):
        name = "Ougadi"
        self.assertHolidayName(
            name,
            "2021-04-13",
            "2022-04-02",
            "2023-03-22",
            "2024-04-09",
            "2025-03-30",
        )
        self.assertHolidayName(name, range(2001, 2036))

    def test_ganesh_chaturthi(self):
        name = "Ganesh Chaturthi"
        self.assertHolidayName(
            name,
            "2021-09-11",
            "2022-09-01",
            "2023-09-20",
            "2024-09-08",
            "2025-08-28",
        )
        self.assertHolidayName(name, range(2001, 2036))

    def test_diwali(self):
        name = "Divali"
        self.assertHolidayName(
            name,
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-10-31",
            "2025-10-20",
        )
        self.assertHolidayName(name, range(2001, 2036))

    def test_2024(self):
        self.assertHolidays(
            Mauritius(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "Day after New Year's Day"),
            ("2024-01-25", "Thaipoosam Cavadee"),
            ("2024-02-01", "Abolition of Slavery"),
            ("2024-02-10", "Chinese Spring Festival"),
            ("2024-03-08", "Maha Shivaratree"),
            ("2024-03-12", "Independence and Republic Day"),
            ("2024-04-09", "Ougadi"),
            ("2024-04-11", "Eid-ul-Fitr"),
            ("2024-05-01", "Labour Day"),
            ("2024-08-15", "Assumption of the Blessed Virgin Mary"),
            ("2024-09-08", "Ganesh Chaturthi"),
            ("2024-10-31", "Divali"),
            ("2024-11-02", "Arrival of Indentured Labourers"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-01-02", "Day after New Year's Day"),
            ("2025-01-29", "Chinese Spring Festival"),
            ("2025-02-01", "Abolition of Slavery"),
            ("2025-02-11", "Thaipoosam Cavadee"),
            ("2025-02-26", "Maha Shivaratree"),
            ("2025-03-12", "Independence and Republic Day"),
            ("2025-03-30", "Ougadi"),
            ("2025-04-01", "Eid-ul-Fitr"),
            ("2025-05-01", "Labour Day"),
            ("2025-08-28", "Ganesh Chaturthi"),
            ("2025-10-20", "Divali"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-11-02", "Arrival of Indentured Labourers"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-02", "Day after New Year's Day"),
            ("2025-01-29", "Chinese Spring Festival"),
            ("2025-02-01", "Abolition of Slavery"),
            ("2025-02-11", "Thaipusam"),
            ("2025-02-26", "Maha Shivaratri"),
            ("2025-03-12", "Independence and Republic Day"),
            ("2025-03-30", "Ugadi"),
            ("2025-04-01", "Eid al-Fitr"),
            ("2025-05-01", "Labor Day"),
            ("2025-08-28", "Ganesh Chaturthi"),
            ("2025-10-20", "Diwali"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-11-02", "Arrival of Indentured Laborers"),
            ("2025-12-25", "Christmas Day"),
        )
