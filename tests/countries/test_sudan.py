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

from holidays.countries import Sudan, SD, SDN
from tests.common import CommonCountryTests


class TestSudan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Sudan, years=range(1985, 2050))
        cls.no_estimated_holidays = Sudan(years=range(1985, 2050), islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Sudan, SD, SDN)

    def test_no_holidays(self):
        self.assertNoHolidays(Sudan(years=1984))

    def test_independence_day(self):
        self.assertHolidayName("عيد الإستقلال", (f"{year}-01-01" for year in range(1985, 2050)))

    def test_coptic_christmas(self):
        self.assertHolidayName(
            "عيد الميلاد المجيد", (f"{year}-01-07" for year in range(1985, 2050))
        )

    def test_orthodox_christmas(self):
        self.assertHolidayName(
            "عيد الميلاد الأرثوذكسي", (f"{year}-01-25" for year in range(1985, 2050))
        )

    def test_coptic_easter(self):
        name = "عيد القيامة المجيد"
        self.assertHolidayName(name, "1985-04-14", "2022-04-24", "2024-05-05")
        self.assertHolidayName(name, self.no_estimated_holidays, range(1985, 2050))

    def test_islamic_new_year(self):
        name = "رأس السنة الهجرية"
        self.assertHolidayName(
            name,
            "2020-08-20",
            "2021-08-11",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1985, 2050))

    def test_prophets_birthday(self):
        name = "المولد النبوي الشريف"
        self.assertHolidayName(
            name,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1985, 2050))

    def test_eid_al_fitr(self):
        name = "عيد الفطر المبارك"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-01",
            "2023-04-21",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1985, 2050))

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
        self.assertHolidayName(name, self.no_estimated_holidays, range(1985, 2050))

    def test_christmas_day(self):
        self.assertHolidayName("يوم عيد الميلاد", (f"{year}-12-25" for year in range(1985, 2050)))

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "Independence Day"),
            ("2022-01-07", "Coptic Christmas"),
            ("2022-01-25", "Orthodox Christmas"),
            ("2022-04-24", "Coptic Easter"),
            ("2022-04-25", "Coptic Easter (observed)"),
            ("2022-05-01", "Eid al-Fitr"),
            ("2022-05-02", "Eid al-Fitr (observed)"),
            ("2022-07-10", "Eid al-Adha"),
            ("2022-07-11", "Eid al-Adha (observed)"),
            ("2022-07-30", "Islamic New Year"),
            ("2022-10-08", "Prophet's Birthday"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "عيد الإستقلال"),
            ("2022-01-07", "عيد الميلاد المجيد"),
            ("2022-01-25", "عيد الميلاد الأرثوذكسي"),
            ("2022-04-24", "عيد القيامة المجيد"),
            ("2022-04-25", "عيد القيامة المجيد (ملاحظة)"),
            ("2022-05-01", "عيد الفطر المبارك"),
            ("2022-05-02", "عيد الفطر المبارك (ملاحظة)"),
            ("2022-07-10", "عيد الأضحى المبارك"),
            ("2022-07-11", "عيد الأضحى المبارك (ملاحظة)"),
            ("2022-07-30", "رأس السنة الهجرية"),
            ("2022-10-08", "المولد النبوي الشريف"),
            ("2022-12-25", "يوم عيد الميلاد"),
            ("2022-12-26", "يوم عيد الميلاد (ملاحظة)"),
        )
