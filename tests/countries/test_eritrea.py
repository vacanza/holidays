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

from holidays.countries.eritrea import Eritrea
from tests.common import CommonCountryTests


class TestEritrea(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Eritrea)

    def test_new_years_day(self):
        self.assertHolidayName("ሓዲሽ ዓመት", (f"{year}-01-01" for year in self.full_range))

    def test_orthodox_christmas(self):
        self.assertHolidayName("ልደት", (f"{year}-01-07" for year in self.full_range))

    def test_epiphany(self):
        self.assertHolidayName(
            "ጥምቀት",
            (f"{year}-01-19" for year in self.full_range if year % 4 != 0),
            (f"{year}-01-20" for year in self.full_range if year % 4 == 0),
        )

    def test_womens_day(self):
        self.assertHolidayName("መዓልቲ ኣነስቲ", (f"{year}-03-08" for year in self.full_range))

    def test_good_friday(self):
        name = "ዓርቢ ስቅለት"
        self.assertHolidayName(
            name,
            "2020-04-17",
            "2021-04-30",
            "2022-04-22",
            "2023-04-14",
            "2024-05-03",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_orthodox_easter(self):
        name = "ፋሲካ"
        self.assertHolidayName(
            name,
            "2020-04-19",
            "2021-05-02",
            "2022-04-24",
            "2023-04-16",
            "2024-05-05",
            "2025-04-20",
        )
        self.assertHolidayName(name, self.full_range)

    def test_international_workers_day(self):
        self.assertHolidayName(
            "ዓለማዊ መዓልቲ ሰራሕተኛታት", (f"{year}-05-01" for year in self.full_range)
        )

    def test_independence_day(self):
        self.assertHolidayName("መዓልቲ ናጽነት", (f"{year}-05-24" for year in self.full_range))

    def test_martyrs_day(self):
        self.assertHolidayName("መዓልቲ ስውኣት", (f"{year}-06-20" for year in self.full_range))

    def test_revolution_day(self):
        self.assertHolidayName("ባሕቲ መስከረም", (f"{year}-09-01" for year in self.full_range))

    def test_ethiopian_new_year(self):
        self.assertHolidayName(
            "ሓድሽ ዓመት ግእዝ",
            (f"{year}-09-11" for year in self.full_range if year % 4 != 3),
            (f"{year}-09-12" for year in self.full_range if year % 4 == 3),
        )

    def test_finding_of_the_true_cross(self):
        self.assertHolidayName(
            "መስቀል",
            (f"{year}-09-27" for year in self.full_range if year % 4 != 3),
            (f"{year}-09-28" for year in self.full_range if year % 4 == 3),
        )

    def test_prophets_birthday(self):
        name = "መውሊድ"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_fitr(self):
        name = "ዒድ ኣልፈጥር"
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
        name = "ዒድ ኣልኣድሓ"
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

    def test_fenkil_day(self):
        name = "ፈንቅል"
        self.assertNoHolidayName(name)
        self.assertGovernmentHolidayName(name, (f"{year}-02-10" for year in self.full_range))

    def test_2020(self):
        self.assertHolidaysInYear(
            2020,
            ("2020-01-01", "ሓዲሽ ዓመት"),
            ("2020-01-07", "ልደት"),
            ("2020-01-20", "ጥምቀት"),
            ("2020-03-08", "መዓልቲ ኣነስቲ"),
            ("2020-04-17", "ዓርቢ ስቅለት"),
            ("2020-04-19", "ፋሲካ"),
            ("2020-05-01", "ዓለማዊ መዓልቲ ሰራሕተኛታት"),
            ("2020-05-24", "መዓልቲ ናጽነት; ዒድ ኣልፈጥር (ግምት)"),
            ("2020-06-20", "መዓልቲ ስውኣት"),
            ("2020-07-31", "ዒድ ኣልኣድሓ (ግምት)"),
            ("2020-09-01", "ባሕቲ መስከረም"),
            ("2020-09-11", "ሓድሽ ዓመት ግእዝ"),
            ("2020-09-27", "መስቀል"),
            ("2020-10-29", "መውሊድ (ግምት)"),
        )

    def test_2020_government(self):
        self.assertGovernmentHolidaysInYear(
            2020,
            ("2020-02-10", "ፈንቅል"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "ሓዲሽ ዓመት"),
            ("2022-01-07", "ልደት"),
            ("2022-01-19", "ጥምቀት"),
            ("2022-02-10", "ፈንቅል"),
            ("2022-03-08", "መዓልቲ ኣነስቲ"),
            ("2022-04-22", "ዓርቢ ስቅለት"),
            ("2022-04-24", "ፋሲካ"),
            ("2022-05-01", "ዓለማዊ መዓልቲ ሰራሕተኛታት"),
            ("2022-05-02", "ዒድ ኣልፈጥር (ግምት)"),
            ("2022-05-24", "መዓልቲ ናጽነት"),
            ("2022-06-20", "መዓልቲ ስውኣት"),
            ("2022-07-09", "ዒድ ኣልኣድሓ (ግምት)"),
            ("2022-09-01", "ባሕቲ መስከረም"),
            ("2022-09-11", "ሓድሽ ዓመት ግእዝ"),
            ("2022-09-27", "መስቀል"),
            ("2022-10-08", "መውሊድ (ግምት)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-07", "Orthodox Christmas"),
            ("2022-01-19", "Epiphany"),
            ("2022-02-10", "Fenkil Day"),
            ("2022-03-08", "Women's Day"),
            ("2022-04-22", "Good Friday"),
            ("2022-04-24", "Orthodox Easter"),
            ("2022-05-01", "International Workers' Day"),
            ("2022-05-02", "Eid al-Fitr (estimated)"),
            ("2022-05-24", "Independence Day"),
            ("2022-06-20", "Martyrs' Day"),
            ("2022-07-09", "Eid al-Adha (estimated)"),
            ("2022-09-01", "Revolution Day"),
            ("2022-09-11", "Ethiopian New Year"),
            ("2022-09-27", "Finding of the True Cross"),
            ("2022-10-08", "Prophet's Birthday (estimated)"),
        )

    def test_l10n_ar(self):
        self.assertLocalizedHolidays(
            "ar",
            ("2022-01-01", "رأس السنة الميلادية"),
            ("2022-01-07", "عيد الميلاد الأرثوذكسي"),
            ("2022-01-19", "عيد الغطاس"),
            ("2022-02-10", "يوم فنكل"),
            ("2022-03-08", "اليوم العالمي للمرأة"),
            ("2022-04-22", "الجمعة العظيمة"),
            ("2022-04-24", "عيد القيامة الأرثوذكسي"),
            ("2022-05-01", "اليوم العالمي للعمال"),
            ("2022-05-02", "عيد الفطر (تقديري)"),
            ("2022-05-24", "عيد الاستقلال"),
            ("2022-06-20", "يوم الشهداء"),
            ("2022-07-09", "عيد الأضحى (تقديري)"),
            ("2022-09-01", "عيد الثورة"),
            ("2022-09-11", "رأس السنة الجعزية"),
            ("2022-09-27", "عيد الصليب"),
            ("2022-10-08", "المولد النبوي الشريف (تقديري)"),
        )
