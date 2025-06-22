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

from holidays.countries.libya import Libya, LY, LBY
from tests.common import CommonCountryTests


class TestSaudiArabia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1968, 2050)
        super().setUpClass(Libya, years=years)
        cls.no_estimated_holidays = Libya(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Libya, LY, LBY)

    def test_anniversary_of_the_february_17_revolution(self):
        self.assertHolidayName("ثورة 17 فبراير", (f"{year}-02-17" for year in range(2012, 2050)))

    def test_labor_day(self):
        self.assertHolidayName("عيد العمال", (f"{year}-05-01" for year in range(2012, 2050)))

    def test_martyrs_day(self):
        self.assertHolidayName("يوم الشهيد", (f"{year}-09-16" for year in range(2012, 2050)))

    def test_liberation_day(self):
        self.assertHolidayName("يوم التحرير", (f"{year}-10-23" for year in range(2012, 2050)))

    def test_independence_day(self):
        self.assertHolidayName("عيد الاستقلال", (f"{year}-12-24" for year in range(2012, 2050)))

    def test_prophets_birthday(self):
        name = "ذكرى المولد النبوي الشريف"
        self.assertHolidayName(
            name, "2020-10-29", "2021-10-19", "2022-10-08", "2023-09-27", "2024-09-15"
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2012, 2050))

    def test_isra_and_miraj(self):
        name = "ليلة المعراج"
        self.assertHolidayName(
            f"(تقدير) {name}", "2021-03-11", "2022-02-28", "2023-02-18", "2024-02-08", "2025-01-27"
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2012, 2050))

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        self.assertHolidayName(
            name,
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2025-03-31",
            "2025-04-01",
            "2025-04-02",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2012, 2050))

    def test_day_of_arafah(self):
        name = "يوم عرفة"
        self.assertHolidayName(
            name,
            "2020-07-30",
            "2021-07-19",
            "2022-07-08",
            "2023-06-27",
            "2024-06-15",
            "2025-06-05",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2012, 2050))

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        self.assertHolidayName(
            name,
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2024-06-16",
            "2024-06-17",
            "2024-06-18",
            "2025-06-06",
            "2025-06-07",
            "2025-06-08",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2012, 2050))

    def test_2024(self):
        self.assertHolidays(
            Libya(years=2024),
            ("2024-02-08", "(تقدير) ليلة المعراج"),
            ("2024-02-17", "ثورة 17 فبراير"),
            ("2024-04-10", "عيد الفطر"),
            ("2024-04-11", "عيد الفطر"),
            ("2024-04-12", "عيد الفطر"),
            ("2024-05-01", "عيد العمال"),
            ("2024-06-15", "يوم عرفة"),
            ("2024-06-16", "عيد الأضحى"),
            ("2024-06-17", "عيد الأضحى"),
            ("2024-06-18", "عيد الأضحى"),
            ("2024-09-15", "ذكرى المولد النبوي الشريف"),
            ("2024-09-16", "يوم الشهيد"),
            ("2024-10-23", "يوم التحرير"),
            ("2024-12-24", "عيد الاستقلال"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-27", "(تقدير) ليلة المعراج"),
            ("2025-02-17", "ثورة 17 فبراير"),
            ("2025-03-31", "عيد الفطر"),
            ("2025-04-01", "عيد الفطر"),
            ("2025-04-02", "عيد الفطر"),
            ("2025-05-01", "عيد العمال"),
            ("2025-06-05", "يوم عرفة"),
            ("2025-06-06", "عيد الأضحى"),
            ("2025-06-07", "عيد الأضحى"),
            ("2025-06-08", "عيد الأضحى"),
            ("2025-09-04", "(تقدير) ذكرى المولد النبوي الشريف"),
            ("2025-09-16", "يوم الشهيد"),
            ("2025-10-23", "يوم التحرير"),
            ("2025-12-24", "عيد الاستقلال"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-27", "Isra' and Mi'raj (estimated)"),
            ("2025-02-17", "Anniversary of the February 17 Revolution"),
            ("2025-03-31", "Eid al-Fitr"),
            ("2025-04-01", "Eid al-Fitr"),
            ("2025-04-02", "Eid al-Fitr"),
            ("2025-05-01", "Labor Day"),
            ("2025-06-05", "Day of Arafah"),
            ("2025-06-06", "Eid al-Adha"),
            ("2025-06-07", "Eid al-Adha"),
            ("2025-06-08", "Eid al-Adha"),
            ("2025-09-04", "Prophet's Birthday (estimated)"),
            ("2025-09-16", "Martyrs' Day"),
            ("2025-10-23", "Liberation Day"),
            ("2025-12-24", "Independence Day"),
        )
