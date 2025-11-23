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

from holidays.constants import WORKDAY
from holidays.countries.ethiopia import Ethiopia
from tests.common import CommonCountryTests


class TestEthiopia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1976, 2050)
        super().setUpClass(Ethiopia, years=years)
        cls.no_estimated_holidays = Ethiopia(years=years, islamic_show_estimated=False)
        cls.workday_holidays = Ethiopia(categories=WORKDAY, years=years)

    def test_christmas_day(self):
        self.assertHolidayName("የገና ወይም የልደት በዓል", (f"{year}-01-07" for year in range(1976, 2050)))

    def test_ephiphany(self):
        self.assertHolidayName(
            "የጥምቀት በዓል",
            (f"{year}-01-19" for year in range(1976, 2050) if year % 4 != 0),
            (f"{year}-01-20" for year in range(1976, 2050) if year % 4 == 0),
        )

    def test_adwa_victory_day(self):
        name = "የአድዋ ድል በዓል"
        self.assertHolidayName(name, (f"{year}-03-02" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, range(1976, 1996))

    def test_good_friday(self):
        name = "የስቅለት በዓል"
        self.assertHolidayName(
            name,
            "2018-04-06",
            "2019-04-26",
            "2020-04-17",
            "2021-04-30",
            "2022-04-22",
            "2023-04-14",
            "2024-05-03",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1976, 2050))

    def test_easter_sunday(self):
        name = "የትንሳኤ(ፋሲካ) በዓል"
        self.assertHolidayName(
            name,
            "2018-04-08",
            "2019-04-28",
            "2020-04-19",
            "2021-05-02",
            "2022-04-24",
            "2023-04-16",
            "2024-05-05",
            "2025-04-20",
        )
        self.assertHolidayName(name, range(1976, 2050))

    def test_international_workers_day(self):
        self.assertHolidayName(
            "የዓለም የሠራተኞች (የላብአደሮች) ቀን", (f"{year}-05-01" for year in range(1976, 2050))
        )

    def test_ethiopian_patriots_victory_day(self):
        self.assertHolidayName(
            "የአርበኞች (የድል) ቀን በዓል", (f"{year}-05-05" for year in range(1976, 2050))
        )

    def test_downfall_of_the_dergue_regime_day(self):
        name = "ደርግ የወደቀበት ቀን"
        self.assertHolidayName(name, (f"{year}-05-28" for year in range(1992, 2050)))
        self.assertNoHolidayName(name, range(1976, 1992))

    def test_ethiopian_new_year(self):
        self.assertHolidayName(
            "የዘመን መለወጫ (እንቁጣጣሽ) በዓል",
            (f"{year}-09-11" for year in range(1976, 2050) if year % 4 != 3),
            (f"{year}-09-12" for year in range(1976, 2050) if year % 4 == 3),
        )

    def test_finding_of_true_cross(self):
        self.assertHolidayName(
            "የመስቀል በዓል",
            (f"{year}-09-27" for year in range(1976, 2050) if year % 4 != 3),
            (f"{year}-09-28" for year in range(1976, 2050) if year % 4 == 3),
        )

    def test_popular_revolution_commemoration_day(self):
        name = "የአብዮት ቀን"
        self.assertHolidayName(
            name,
            (f"{year}-09-12" for year in range(1976, 1991) if year % 4 != 3),
            (f"{year}-09-13" for year in range(1976, 1991) if year % 4 == 3),
        )
        self.assertNoHolidayName(name, range(1991, 2050))

    def test_october_revolution_day(self):
        name = "የጥቅምት አብዮት ቀን"
        self.assertHolidayName(name, (f"{year}-11-07" for year in range(1976, 1991)))
        self.assertNoHolidayName(name, range(1991, 2050))

    def test_eid_al_fitr(self):
        name = "የኢድ አልፈጥር"
        self.assertHolidayName(
            name,
            "2018-06-15",
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1976, 2050))

    def test_eid_al_adha(self):
        name = "የኢድ አልአድሃ (አረፋ)"
        self.assertHolidayName(
            name,
            "2018-08-22",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1976, 2050))

    def test_prophets_birthday(self):
        name = "የመውሊድ በዓል"
        self.assertHolidayName(
            name,
            "2018-11-21",
            "2019-11-10",
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1976, 2050))

    def test_ethiopian_martyrs_day(self):
        name = "የሰማዕታት ቀን"
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-02-20" for year in range(1976, 2050))
        )
        self.assertNoHolidayName(name)

    def test_nations_nationality_and_peoples_day(self):
        name = "የብሔር ብሔረሰቦች ቀን"
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-12-09" for year in range(2006, 2050))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(1976, 2006))
        self.assertNoHolidayName(name)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-07", "የገና ወይም የልደት በዓል"),
            ("2022-01-19", "የጥምቀት በዓል"),
            ("2022-02-20", "የሰማዕታት ቀን"),
            ("2022-03-02", "የአድዋ ድል በዓል"),
            ("2022-04-22", "የስቅለት በዓል"),
            ("2022-04-24", "የትንሳኤ(ፋሲካ) በዓል"),
            ("2022-05-01", "የዓለም የሠራተኞች (የላብአደሮች) ቀን"),
            ("2022-05-02", "የኢድ አልፈጥር"),
            ("2022-05-05", "የአርበኞች (የድል) ቀን በዓል"),
            ("2022-05-28", "ደርግ የወደቀበት ቀን"),
            ("2022-07-09", "የኢድ አልአድሃ (አረፋ)"),
            ("2022-09-11", "የዘመን መለወጫ (እንቁጣጣሽ) በዓል"),
            ("2022-09-27", "የመስቀል በዓል"),
            ("2022-10-08", "የመውሊድ በዓል"),
            ("2022-12-09", "የብሔር ብሔረሰቦች ቀን"),
        )

    def test_l10n_ar(self):
        self.assertLocalizedHolidays(
            "ar",
            ("2022-01-07", "عيد الميلاد الإثيوبي (جنا)"),
            ("2022-01-19", "عيد الغطاس الإثيوبي (طمقت)"),
            ("2022-02-20", "يوم الشهداء"),
            ("2022-03-02", "عيد النصر في معركة عدوا"),
            ("2022-04-22", "جمعة الآلام (سقلَت)"),
            ("2022-04-24", "عيد القيامة (فاسيكا)"),
            ("2022-05-01", "اليوم العالمي للعمال"),
            ("2022-05-02", "عيد الفطر"),
            ("2022-05-05", "يوم انتصار الوطنيين الإثيوبيين"),
            ("2022-05-28", "يوم سقوط نظام الدرج"),
            ("2022-07-09", "عيد الأضحى"),
            ("2022-09-11", "رأس السنة الإثيوبية (إنكوتاتاش)"),
            ("2022-09-27", "عيد الصليب (مسقل)"),
            ("2022-10-08", "عيد المولد النبوي"),
            ("2022-12-09", "يوم الأمم والقوميات والشعوب"),
        )

    def test_l10n_en_et(self):
        self.assertLocalizedHolidays(
            "en_ET",
            ("2022-01-07", "Christmas Holiday"),
            ("2022-01-19", "Epiphany"),
            ("2022-02-20", "Ethiopian Martyrs' Day"),
            ("2022-03-02", "Adwa Victory Day"),
            ("2022-04-22", "Good Friday"),
            ("2022-04-24", "Easter"),
            ("2022-05-01", "International Workers' Day"),
            ("2022-05-02", "Eid al-Fitr"),
            ("2022-05-05", "Ethiopian Patriots' Victory Day"),
            ("2022-05-28", "Downfall of the Dergue Regime Day"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-09-11", "New Year (Enkutatash)"),
            ("2022-09-27", "Meskel Holiday"),
            ("2022-10-08", "Mawlid"),
            (
                "2022-12-09",
                "Ethiopian National Unity Day (Ethiopian Nations and Nationalities) Day",
            ),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-07", "Christmas Day"),
            ("2022-01-19", "Epiphany"),
            ("2022-02-20", "Ethiopian Martyrs' Day"),
            ("2022-03-02", "Adwa Victory Day"),
            ("2022-04-22", "Good Friday"),
            ("2022-04-24", "Easter Sunday"),
            ("2022-05-01", "International Workers' Day"),
            ("2022-05-02", "Eid al-Fitr"),
            ("2022-05-05", "Ethiopian Patriots' Victory Day"),
            ("2022-05-28", "Downfall of the Dergue Regime Day"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-09-11", "Ethiopian New Year"),
            ("2022-09-27", "Finding of True Cross"),
            ("2022-10-08", "Prophet's Birthday"),
            ("2022-12-09", "Nations, Nationalities and Peoples Day"),
        )
