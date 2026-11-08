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

from holidays.financial.qatar_stock_exchange import QatarStockExchange
from tests.common import CommonFinancialTests


class TestQatarStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(QatarStockExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_special_holidays(self):
        self.assertHolidayName("عطلة رسمية", "2013-06-25")
        self.assertHolidayName("حداد رسمي", "2026-07-13", "2026-07-14", "2026-07-15", "2026-07-16")

    def test_l10n_official_mourning(self):
        dts = ("2026-07-13", "2026-07-14", "2026-07-15", "2026-07-16")
        for language, name in (("en_US", "Official Mourning"), ("ur_PK", "سرکاری سوگ")):
            self.assertHolidayName(name, QatarStockExchange(years=2026, language=language), dts)

    def test_weekend_holidays_are_not_trading_days(self):
        self.assertNoHoliday(
            "2016-01-01",
            "2016-07-08",
            "2018-06-15",
            "2018-06-16",
            "2020-12-18",
            "2021-01-01",
            "2021-12-18",
            "2022-01-01",
            "2023-04-21",
            "2023-04-22",
            "2025-06-06",
            "2025-06-07",
            "2026-03-20",
            "2026-03-21",
        )

    def test_new_years_day(self):
        name = "رأس السنة الميلادية"
        self.assertHolidayName(
            name,
            "2012-01-01",
            "2013-01-01",
            "2014-01-01",
            "2015-01-01",
            "2017-01-01",
            "2018-01-01",
            "2019-01-01",
            "2020-01-01",
            "2023-01-01",
            "2024-01-01",
            "2025-01-01",
            "2026-01-01",
        )

    def test_national_sport_day(self):
        name = "اليوم الوطني للرياضة"
        self.assertHolidayName(
            name,
            "2012-02-14",
            "2013-02-12",
            "2014-02-11",
            "2015-02-10",
            "2016-02-09",
            "2017-02-14",
            "2018-02-13",
            "2019-02-12",
            "2020-02-11",
            "2021-02-09",
            "2022-02-08",
            "2023-02-14",
            "2024-02-13",
            "2025-02-11",
            "2026-02-10",
        )
        self.assertNoHolidayName(name, 2011)

    def test_march_bank_holiday(self):
        name = "عطلة البنك"
        self.assertHolidayName(
            name,
            "2011-03-06",
            "2012-03-04",
            "2013-03-03",
            "2014-03-02",
            "2015-03-01",
            "2016-03-06",
            "2017-03-05",
            "2018-03-04",
            "2019-03-03",
            "2020-03-01",
            "2021-03-07",
            "2022-03-06",
            "2023-03-05",
            "2024-03-03",
            "2025-03-02",
            "2026-03-01",
        )

    def test_national_day(self):
        name = "اليوم الوطني لقطر"
        self.assertHolidayName(
            name,
            "2011-12-18",
            "2012-12-18",
            "2013-12-18",
            "2013-12-19",
            "2014-12-18",
            "2015-12-20",
            "2016-12-18",
            "2017-12-17",
            "2017-12-18",
            "2018-12-18",
            "2019-12-18",
            "2019-12-19",
            "2020-12-17",
            "2021-12-19",
            "2022-12-18",
            "2023-12-17",
            "2023-12-18",
            "2024-12-18",
            "2024-12-19",
            "2025-12-18",
        )

    def test_eid_al_fitr(self):
        self.assertHolidayName(
            "عيد الفطر",
            "2011-08-31",
            "2011-09-01",
            "2015-07-19",
            "2015-07-20",
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2025-03-30",
            "2025-03-31",
            "2025-04-01",
        )
        self.assertHolidayName(
            "عطلة عيد الفطر",
            "2011-08-30",
            "2013-08-11",
            "2013-08-12",
            "2014-07-31",
            "2015-07-21",
            "2016-07-10",
            "2017-06-28",
            "2017-06-29",
            "2018-06-18",
            "2018-06-19",
            "2020-05-27",
            "2020-05-28",
            "2021-05-12",
            "2021-05-16",
            "2022-05-01",
            "2022-05-05",
            "2023-04-24",
            "2023-04-25",
            "2024-04-09",
            "2025-04-02",
            "2025-04-03",
            "2026-03-19",
            "2026-03-23",
        )

    def test_eid_al_adha(self):
        self.assertHolidayName(
            "عيد الأضحى",
            "2011-11-06",
            "2011-11-07",
            "2011-11-08",
            "2015-09-23",
            "2015-09-24",
            "2020-08-02",
            "2025-06-08",
        )
        self.assertHolidayName(
            "عطلة عيد الأضحى",
            "2012-10-25",
            "2012-10-29",
            "2013-10-13",
            "2013-10-14",
            "2014-10-07",
            "2014-10-08",
            "2014-10-09",
            "2015-09-27",
            "2015-09-28",
            "2016-09-13",
            "2016-09-14",
            "2016-09-15",
            "2017-09-03",
            "2017-09-04",
            "2017-09-05",
            "2018-08-19",
            "2018-08-20",
            "2018-08-21",
            "2020-07-30",
            "2020-08-03",
            "2020-08-04",
            "2021-07-18",
            "2021-07-19",
            "2022-07-12",
            "2023-06-27",
            "2025-06-05",
            "2025-06-09",
            "2026-05-26",
        )

    def test_2025(self):
        self.assertHolidays(
            QatarStockExchange(years=2025),
            ("2025-01-01", "رأس السنة الميلادية"),
            ("2025-01-02", "عطلة رأس السنة"),
            ("2025-02-11", "اليوم الوطني للرياضة"),
            ("2025-03-02", "عطلة البنك"),
            ("2025-03-30", "عيد الفطر"),
            ("2025-03-31", "عيد الفطر"),
            ("2025-04-01", "عيد الفطر"),
            ("2025-04-02", "عطلة عيد الفطر"),
            ("2025-04-03", "عطلة عيد الفطر"),
            ("2025-06-05", "عطلة عيد الأضحى"),
            ("2025-06-08", "عيد الأضحى"),
            ("2025-06-09", "عطلة عيد الأضحى"),
            ("2025-12-18", "اليوم الوطني لقطر"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2013-01-01", "رأس السنة الميلادية"),
            ("2013-02-12", "اليوم الوطني للرياضة"),
            ("2013-03-03", "عطلة البنك"),
            ("2013-06-25", "عطلة رسمية"),
            ("2013-08-08", "عيد الفطر"),
            ("2013-08-11", "عطلة عيد الفطر"),
            ("2013-08-12", "عطلة عيد الفطر"),
            ("2013-10-13", "عطلة عيد الأضحى"),
            ("2013-10-14", "عطلة عيد الأضحى"),
            ("2013-10-15", "عيد الأضحى"),
            ("2013-10-16", "عيد الأضحى"),
            ("2013-10-17", "عيد الأضحى"),
            ("2013-12-18", "اليوم الوطني لقطر"),
            ("2013-12-19", "اليوم الوطني لقطر"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2013-01-01", "New Year's Day"),
            ("2013-02-12", "National Sports Day"),
            ("2013-03-03", "March Bank Holiday"),
            ("2013-06-25", "Public Holiday"),
            ("2013-08-08", "Eid al-Fitr"),
            ("2013-08-11", "Eid al-Fitr Holiday"),
            ("2013-08-12", "Eid al-Fitr Holiday"),
            ("2013-10-13", "Eid al-Adha Holiday"),
            ("2013-10-14", "Eid al-Adha Holiday"),
            ("2013-10-15", "Eid al-Adha"),
            ("2013-10-16", "Eid al-Adha"),
            ("2013-10-17", "Eid al-Adha"),
            ("2013-12-18", "Qatar National Day"),
            ("2013-12-19", "Qatar National Day"),
        )

    def test_l10n_ur_pk(self):
        self.assertLocalizedHolidays(
            "ur_PK",
            ("2013-01-01", "نئے سال کا دن"),
            ("2013-02-12", "کھیلوں کا قومی دن"),
            ("2013-03-03", "بینک کی تعطیل"),
            ("2013-06-25", "سرکاری تعطیل"),
            ("2013-08-08", "عید الفطر"),
            ("2013-08-11", "عید الفطر کی تعطیل"),
            ("2013-08-12", "عید الفطر کی تعطیل"),
            ("2013-10-13", "عید الاضحی کی تعطیل"),
            ("2013-10-14", "عید الاضحی کی تعطیل"),
            ("2013-10-15", "عید الاضحی"),
            ("2013-10-16", "عید الاضحی"),
            ("2013-10-17", "عید الاضحی"),
            ("2013-12-18", "قطر کا قومی دن"),
            ("2013-12-19", "قطر کا قومی دن"),
        )
