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

from holidays.countries.tajikistan import Tajikistan, TJ, TJK
from tests.common import CommonCountryTests


class TestTajikistan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1992, 2050)
        super().setUpClass(Tajikistan, years=years)
        cls.no_estimated_holidays = Tajikistan(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Tajikistan, TJ, TJK)

    def test_no_holidays(self):
        self.assertNoHolidays(Tajikistan(years=1991))

    def test_new_years_day(self):
        self.assertHolidayName("Соли Нав", (f"{year}-01-01" for year in range(1992, 2050)))

    def test_mothers_day(self):
        self.assertHolidayName("Рӯзи Модар", (f"{year}-03-08" for year in range(1992, 2050)))

    def test_nowruz(self):
        name = "Иди байналмилалии Наврӯз"
        self.assertHolidayName(name, (f"{year}-03-21" for year in range(1992, 2050)))
        self.assertHolidayName(name, (f"{year}-03-22" for year in range(1992, 2050)))
        self.assertHolidayName(name, (f"{year}-03-23" for year in range(2003, 2050)))
        self.assertHolidayName(name, (f"{year}-03-24" for year in range(2006, 2050)))
        self.assertNoHolidayName(name, (f"{year}-03-23" for year in range(1992, 2003)))
        self.assertNoHolidayName(name, (f"{year}-03-24" for year in range(1992, 2006)))

    def test_workers_day(self):
        name = "Рӯзи байналхалқии якдилии меҳнаткашон"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1992, 2017)))
        self.assertNoHolidayName(name, range(2017, 2050))

    def test_victory_day(self):
        self.assertHolidayName(
            "Рӯзи Ғалаба дар Ҷанги Бузурги Ватанӣ", (f"{year}-05-09" for year in range(1992, 2050))
        )

    def test_unity_day(self):
        name = "Рӯзи Ваҳдати миллӣ"
        self.assertHolidayName(name, (f"{year}-06-27" for year in range(1998, 2050)))
        self.assertNoHolidayName(name, range(1992, 1998))

    def test_independence_day(self):
        self.assertHolidayName(
            "Рӯзи Истиқлолияти давлатии Ҷумҳурии Тоҷикистон",
            (f"{year}-09-09" for year in range(1992, 2050)),
        )

    def test_constitution_day(self):
        name = "Рӯзи Конститутсияи Ҷумҳурии Тоҷикистон"
        self.assertHolidayName(name, (f"{year}-11-06" for year in range(1994, 2050)))
        self.assertNoHolidayName(name, range(1992, 1994))

    def test_eid_al_fitr(self):
        name = "Рӯзи иди Рамазон"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-22",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1992, 2050))

    def test_eid_al_adha(self):
        name = "Рӯзи иди Қурбон"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1992, 2050))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Соли Нав"),
            ("2024-03-08", "Рӯзи Модар"),
            ("2024-03-21", "Иди байналмилалии Наврӯз"),
            ("2024-03-22", "Иди байналмилалии Наврӯз"),
            ("2024-03-23", "Иди байналмилалии Наврӯз"),
            ("2024-03-24", "Иди байналмилалии Наврӯз"),
            ("2024-04-10", "Рӯзи иди Рамазон"),
            ("2024-05-09", "Рӯзи Ғалаба дар Ҷанги Бузурги Ватанӣ"),
            ("2024-06-16", "Рӯзи иди Қурбон"),
            ("2024-06-27", "Рӯзи Ваҳдати миллӣ"),
            ("2024-09-09", "Рӯзи Истиқлолияти давлатии Ҷумҳурии Тоҷикистон"),
            ("2024-11-06", "Рӯзи Конститутсияи Ҷумҳурии Тоҷикистон"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-08", "Mother's Day"),
            ("2024-03-21", "International Nowruz Day"),
            ("2024-03-22", "International Nowruz Day"),
            ("2024-03-23", "International Nowruz Day"),
            ("2024-03-24", "International Nowruz Day"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-05-09", "Victory Day"),
            ("2024-06-16", "Eid al-Adha"),
            ("2024-06-27", "National Unity Day"),
            ("2024-09-09", "Independence Day"),
            ("2024-11-06", "Constitution Day"),
        )

    def test_l10n_ru(self):
        self.assertLocalizedHolidays(
            "ru",
            ("2024-01-01", "Новый год"),
            ("2024-03-08", "День Матери"),
            ("2024-03-21", "Международный праздник Навруз"),
            ("2024-03-22", "Международный праздник Навруз"),
            ("2024-03-23", "Международный праздник Навруз"),
            ("2024-03-24", "Международный праздник Навруз"),
            ("2024-04-10", "Ураза-байрам"),
            ("2024-05-09", "День Победы в Великой Отечественной войне"),
            ("2024-06-16", "Курбан-байрам"),
            ("2024-06-27", "День Национального единства"),
            ("2024-09-09", "День Государственной независимости Республики Таджикистан"),
            ("2024-11-06", "День Конституции Республики Таджикистан"),
        )
