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

#  tests/countries/test_bhutan.py
#  ------------------------------
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

from holidays.countries.bhutan import Bhutan, BT, BTN
from tests.common import CommonCountryTests


class TestBhutan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1970, 2050)
        super().setUpClass(Bhutan, years=years)

    def test_country_aliases(self):
        self.assertAliases(Bhutan, BT, BTN)

    def test_no_holidays_before_start_year(self):
        self.assertNoHolidays(Bhutan(years=1969))

    def test_fixed_holidays(self):
        # Nyilo (Winter Solstice)
        self.assertHoliday(f"{year}-01-02" for year in range(1970, 2050))

        # King's Birthday (Day 1)
        self.assertHoliday(f"{year}-02-21" for year in range(1970, 2050))

        # King's Birthday (Day 2)
        self.assertHoliday(f"{year}-02-22" for year in range(1970, 2050))

        # King's Birthday (Day 3)
        self.assertHoliday(f"{year}-02-23" for year in range(1970, 2050))

        # Birth Anniversary of Third Druk Gyalpo
        self.assertHoliday(f"{year}-05-02" for year in range(1970, 2050))

        # Coronation of King Jigme Khesar Namgyel
        self.assertHoliday(f"{year}-11-01" for year in range(1970, 2050))

        # Birth Anniversary of Fourth Druk Gyalpo
        self.assertHoliday(f"{year}-11-11" for year in range(1970, 2050))

        # National Day
        self.assertHoliday(f"{year}-12-17" for year in range(1970, 2050))

    def test_tibetan_based_holidays(self):
        # Losar (Tibetan New Year) - sample dates
        self.assertHoliday("2022-03-03", "2024-02-11", "2025-02-28")

        # Blessed Rainy Day - sample dates
        self.assertHoliday("2022-09-23", "2024-09-23", "2025-09-23")

        # Dashain - sample dates
        self.assertHoliday("2022-10-5", "2024-10-12", "2025-10-02")

    def test_l10n_en_us_2024_dates(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-02", "Nyilo."),  # Nyilo (Winter Solstice)
            ("2024-01-12", "Day of Offering."),  # Day of Offering
            ("2024-02-11", "Losar."),  # Losar (Tibetan New Year)
            ("2024-02-21", "King's Birthday (Day 1)."),  # King's Birthday (Day 1)
            ("2024-02-22", "King's Birthday (Day 2)."),  # King's Birthday (Day 2)
            ("2024-02-23", "King's Birthday (Day 3)."),  # King's Birthday (Day 3)
            ("2024-04-18", "Death of Zhabdrung."),  # Death of Zhabdrung
            (
                "2024-05-02",
                "Birth Anniversary of Third Druk Gyalpo.",
            ),  # Third Druk Gyalpo's Birth Anniversary
            ("2024-05-23", "Buddha Parinirvana."),  # Buddha Parinirvana
            ("2024-06-16", "Birth of Guru Rinpoche."),  # Birth of Guru Rinpoche
            ("2024-07-10", "Buddha's First Sermon."),  # Buddha's First Sermon
            ("2024-09-23", "Blessed Rainy Day."),  # Blessed Rainy Day
            ("2024-10-12", "Dashain."),  # Dashain
            (
                "2024-11-01",
                "Jigme Khesar Namgyel's Coronation.",
            ),  # Coronation of King Jigme Khesar Namgyel
            (
                "2024-11-11",
                "Birth Anniversary of the Fourth Druk Gyalpo.",
            ),  # Fourth Druk Gyalpo's Birth Anniversary / Constitution Day
            ("2024-12-17", "National Day."),
        )
