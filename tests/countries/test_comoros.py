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

from holidays.countries.comoros import Comoros, KM, COM
from tests.common import CommonCountryTests


class TestComoros(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1976, 2050)
        super().setUpClass(Comoros, years=years)
        cls.no_estimated_holidays = Comoros(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Comoros, KM, COM)

    def test_no_holidays(self):
        self.assertNoHolidays(Comoros(years=1975))

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1976, 2050)))

    def test_cheikh_al_maarouf_day(self):
        self.assertHolidayName(
            "Cheikh al Maarouf", (f"{year}-03-18" for year in range(1976, 2050))
        )

    def test_labour_day(self):
        self.assertHolidayName("Labour Day", (f"{year}-05-01" for year in range(1976, 2050)))

    def test_national_day(self):
        self.assertHolidayName("National Day", (f"{year}-07-06" for year in range(1976, 2050)))

    def test_maore_day(self):
        self.assertHolidayName("Maore Day", (f"{year}-11-12" for year in range(1976, 2050)))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1976, 2050)))

    def test_eid_al_fitr(self):
        name = "Eid al-Fitr"
        self.assertHolidayName(
            f"{name} (estimated)",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1976, 2050))

    def test_eid_al_adha(self):
        name = "Eid al-Adha"
        self.assertHolidayName(
            f"{name} (estimated)",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1976, 2050))

    def test_islamic_new_year(self):
        name = "Islamic New Year"
        self.assertHolidayName(
            f"{name} (estimated)",
            "2020-08-20",
            "2021-08-09",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1976, 2050))

    def test_prophets_birthday(self):
        name = "The Prophet's Birthday"
        self.assertHolidayName(
            f"{name} (estimated)",
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1976, 2050))

    def test_the_prophets_ascension_day(self):
        name = "The Prophet's Ascension"
        self.assertHolidayName(
            f"{name} (estimated)",
            "2020-03-22",
            "2021-03-11",
            "2022-02-28",
            "2023-02-18",
            "2024-02-08",
            "2025-01-27",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1976, 2050))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-02-28", "The Prophet's Ascension (estimated)"),
            ("2022-03-18", "Cheikh al Maarouf"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Eid al-Fitr (estimated)"),
            ("2022-07-06", "National Day"),
            ("2022-07-09", "Eid al-Adha (estimated)"),
            ("2022-07-30", "Islamic New Year (estimated)"),
            ("2022-10-08", "The Prophet's Birthday (estimated)"),
            ("2022-11-12", "Maore Day"),
            ("2022-12-25", "Christmas Day"),
        )
