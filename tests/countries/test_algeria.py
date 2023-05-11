from holidays.countries.algeria import Algeria, DZ, DZA
from tests.common import TestCase


class TestAlgeria(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Algeria)

    def test_country_aliases(self):
        self.assertCountryAliases(Algeria, DZ, DZA)

    def test_2022(self):
        self.assertHoliday("2022-01-01")
        self.assertHoliday("2022-01-12")
        self.assertHoliday("2022-05-01")
        self.assertHoliday("2022-05-02")
        self.assertHoliday("2022-05-03")
        self.assertHoliday("2022-07-05")
        self.assertHoliday("2022-07-09")
        self.assertHoliday("2022-07-10")
        self.assertHoliday("2022-11-01")

    def test_new_year_day(self):
        self.assertHoliday("2022-01-01", "2023-01-01")

    def test_independence_day(self):
        self.assertNoHoliday("1961-07-05")
        self.assertHoliday("1962-07-05")

    def test_revolution_day(self):
        self.assertNoHoliday("1962-11-01")
        self.assertHoliday("1963-11-01")

    def test_amazigh_new_year(self):
        self.assertNoHoliday("2017-01-12")
        self.assertHoliday("2018-01-12")
        self.assertHoliday("2023-01-12")

    def test_labour_day(self):
        self.assertHoliday("2021-05-01")
        self.assertHoliday("2022-05-01")
        self.assertHoliday("2023-05-01")
        self.assertNoHoliday("2023-05-02")

    def test_islamic_holidays(self):
        # Eid al-Fitr - Feast Festive
        self.assertHoliday("2023-04-21")
        self.assertHoliday("2023-04-22")
        self.assertNoHoliday("2023-04-23")

        # Eid al-Adha - Scarfice Festive
        self.assertHoliday("2023-06-29")
        self.assertHoliday("2023-06-30")
        self.assertHoliday("2023-06-28")
        self.assertNoHoliday("2023-07-02")

        # Islamic New Year
        self.assertHoliday(
            "2008-01-10",
            "2008-12-29",
            "2020-08-20",
        )
        # Ashura
        self.assertHoliday("2023-07-28")
        self.assertNoHoliday("2023-07-29")

        # Mawlid / Prophet's Birthday
        self.assertHoliday("2021-10-18")
        self.assertHoliday("2023-09-27")
        self.assertNoHoliday("2021-10-19")
        self.assertNoHoliday("2023-09-28")
