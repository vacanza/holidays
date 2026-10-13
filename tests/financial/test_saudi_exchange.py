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

from holidays.financial.saudi_exchange import SaudiExchange
from tests.common import CommonFinancialTests


class TestSaudiExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SaudiExchange)

    def test_special_holidays(self):
        self.assertHoliday("2022-11-23")

    def test_founding_day(self):
        name = "يوم التأسيس"
        self.assertHolidayName(name, (f"{year}-02-22" for year in range(2022, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2022))
        self.assertHolidayName(f"{name} (يوم تعويضي)", "2025-02-23")

    def test_eid_al_fitr(self):
        self.assertHolidayName(
            "عطلة عيد الفطر",
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2020-05-27",
            "2020-05-28",
            "2021-05-11",
            "2021-05-12",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2021-05-16",
            "2022-05-01",
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2022-05-05",
            "2023-04-18",
            "2023-04-19",
            "2023-04-20",
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2023-04-24",
            "2024-04-07",
            "2024-04-08",
            "2024-04-09",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2024-04-13",
            "2025-03-30",
            "2025-03-31",
            "2025-04-01",
            "2025-04-02",
            "2026-03-17",
            "2026-03-18",
            "2026-03-19",
            "2026-03-20",
            "2026-03-21",
            "2026-03-22",
            "2026-03-23",
            "2027-03-07",
            "2027-03-08",
            "2027-03-09",
            "2027-03-10",
            "2027-03-11",
            "2027-03-12",
            "2028-02-26",
            "2028-02-27",
            "2028-02-28",
            "2028-02-29",
            "2028-03-01",
            "2028-03-02",
            "2029-02-12",
            "2029-02-13",
            "2029-02-14",
            "2029-02-15",
            "2029-02-16",
            "2029-02-17",
            "2029-02-18",
        )
        self.assertNoHoliday("2021-05-10", "2021-05-17", "2022-04-28", "2022-05-08")

    def test_arafah_day(self):
        name = "يوم عرفة"
        self.assertHolidayName(
            name,
            "2020-07-30",
            "2021-07-19",
            "2022-07-08",
            "2023-06-27",
            "2024-06-15",
            "2025-06-05",
            "2026-05-26",
            "2027-05-15",
            "2028-05-04",
            "2029-04-23",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_adha(self):
        self.assertHolidayName(
            "عطلة عيد الأضحى",
            "2020-07-29",
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2020-08-03",
            "2020-08-04",
            "2021-07-18",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2021-07-23",
            "2022-07-07",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2022-07-12",
            "2023-06-25",
            "2023-06-26",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2023-07-01",
            "2024-06-16",
            "2024-06-17",
            "2024-06-18",
            "2024-06-19",
            "2024-06-20",
            "2025-06-06",
            "2025-06-07",
            "2025-06-08",
            "2025-06-09",
            "2025-06-10",
            "2026-05-24",
            "2026-05-25",
            "2026-05-27",
            "2026-05-28",
            "2026-05-29",
            "2026-05-30",
            "2027-05-16",
            "2027-05-17",
            "2027-05-18",
            "2027-05-19",
            "2027-05-20",
            "2028-05-03",
            "2028-05-05",
            "2028-05-06",
            "2028-05-07",
            "2028-05-08",
            "2028-05-09",
            "2029-04-22",
            "2029-04-24",
            "2029-04-25",
            "2029-04-26",
            "2029-04-27",
        )

    def test_national_day(self):
        name = "اليوم الوطني"
        self.assertHolidayName(
            name,
            "2020-09-23",
            "2021-09-23",
            "2022-09-23",
            "2023-09-23",
            "2024-09-23",
            "2025-09-23",
            "2026-09-23",
        )
        self.assertHolidayName(name, self.full_range)
        self.assertHolidayName(f"{name} (يوم تعويضي)", "2022-09-22", "2023-09-24")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-02-22", "يوم التأسيس"),
            ("2023-04-18", "عطلة عيد الفطر"),
            ("2023-04-19", "عطلة عيد الفطر"),
            ("2023-04-20", "عطلة عيد الفطر"),
            ("2023-04-21", "عطلة عيد الفطر"),
            ("2023-04-22", "عطلة عيد الفطر"),
            ("2023-04-23", "عطلة عيد الفطر"),
            ("2023-04-24", "عطلة عيد الفطر"),
            ("2023-06-25", "عطلة عيد الأضحى"),
            ("2023-06-26", "عطلة عيد الأضحى"),
            ("2023-06-27", "يوم عرفة"),
            ("2023-06-28", "عطلة عيد الأضحى"),
            ("2023-06-29", "عطلة عيد الأضحى"),
            ("2023-06-30", "عطلة عيد الأضحى"),
            ("2023-07-01", "عطلة عيد الأضحى"),
            ("2023-09-23", "اليوم الوطني"),
            ("2023-09-24", "اليوم الوطني (يوم تعويضي)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-02-22", "Founding Day Holiday"),
            ("2023-04-18", "Eid al-Fitr Holiday"),
            ("2023-04-19", "Eid al-Fitr Holiday"),
            ("2023-04-20", "Eid al-Fitr Holiday"),
            ("2023-04-21", "Eid al-Fitr Holiday"),
            ("2023-04-22", "Eid al-Fitr Holiday"),
            ("2023-04-23", "Eid al-Fitr Holiday"),
            ("2023-04-24", "Eid al-Fitr Holiday"),
            ("2023-06-25", "Eid al-Adha Holiday"),
            ("2023-06-26", "Eid al-Adha Holiday"),
            ("2023-06-27", "Day of Arafah"),
            ("2023-06-28", "Eid al-Adha Holiday"),
            ("2023-06-29", "Eid al-Adha Holiday"),
            ("2023-06-30", "Eid al-Adha Holiday"),
            ("2023-07-01", "Eid al-Adha Holiday"),
            ("2023-09-23", "National Day Holiday"),
            ("2023-09-24", "National Day Holiday (observed)"),
        )

    def test_l10n_ur_pk(self):
        self.assertLocalizedHolidays(
            "ur_PK",
            ("2023-02-22", "یوم تاسیس"),
            ("2023-04-18", "عید الفطر کی تعطیل"),
            ("2023-04-19", "عید الفطر کی تعطیل"),
            ("2023-04-20", "عید الفطر کی تعطیل"),
            ("2023-04-21", "عید الفطر کی تعطیل"),
            ("2023-04-22", "عید الفطر کی تعطیل"),
            ("2023-04-23", "عید الفطر کی تعطیل"),
            ("2023-04-24", "عید الفطر کی تعطیل"),
            ("2023-06-25", "عید الاضحی کی تعطیل"),
            ("2023-06-26", "عید الاضحی کی تعطیل"),
            ("2023-06-27", "یوم عرفہ"),
            ("2023-06-28", "عید الاضحی کی تعطیل"),
            ("2023-06-29", "عید الاضحی کی تعطیل"),
            ("2023-06-30", "عید الاضحی کی تعطیل"),
            ("2023-07-01", "عید الاضحی کی تعطیل"),
            ("2023-09-23", "قومی دن"),
            ("2023-09-24", "قومی دن (منایا گیا)"),
        )
