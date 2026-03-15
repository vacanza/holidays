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

#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly.

from unittest import TestCase

from holidays.countries.pakistan import Pakistan
from tests.common import CommonCountryTests


class TestPakistan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1948, 2050)
        super().setUpClass(Pakistan, years=years)
        cls.no_estimated_holidays = Pakistan(years=years, islamic_show_estimated=False)

    def test_kashmir_day(self):
        name = "Kashmir Solidarity Day"
        self.assertHolidayName(name, (f"{year}-02-05" for year in range(1990, 2050)))
        self.assertNoHolidayName(name, range(1948, 1990))

    def test_pakistan_day(self):
        name = "Pakistan Day"
        self.assertHolidayName(name, (f"{year}-03-23" for year in range(1956, 2050)))
        self.assertNoHolidayName(name, range(1948, 1956))

    def test_labour_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1972, 2050)))
        self.assertNoHolidayName(name, range(1948, 1972))

    def test_youm_e_takbeer(self):
        name = "Youm-e-Takbeer"
        self.assertHolidayName(name, (f"{year}-05-28" for year in range(2024, 2050)))
        self.assertNoHolidayName(name, range(1948, 2024))

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-08-14" for year in range(1948, 2050)))

    def test_iqbal_day(self):
        name = "Iqbal Day"
        self.assertHolidayName(
            name, (f"{year}-11-09" for year in (*range(1948, 2015), *range(2022, 2050)))
        )
        self.assertNoHolidayName(name, range(2015, 2022))

    def test_quaid_e_azam_day(self):
        self.assertHolidayName("Quaid-e-Azam Day", (f"{year}-12-25" for year in range(1948, 2050)))

    def test_day_after_christmas(self):
        self.assertHolidayName(
            "Day after Christmas", (f"{year}-12-26" for year in range(2026, 2050))
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-01-23", "Basant Panchami"),
            ("2024-02-05", "Kashmir Solidarity Day"),
            ("2024-02-16", "Shiv Ratri"),
            ("2024-03-03", "Dulhandi"),
            ("2024-03-04", "Holi"),
            ("2024-03-23", "Pakistan Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-31", "Easter Sunday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-10", "Eid-ul-Fitr"),
            ("2024-04-11", "Eid-ul-Fitr"),
            ("2024-04-12", "Eid-ul-Fitr"),
            ("2024-04-14", "Baisakhi"),
            ("2024-04-21", "Eid-e-Rizwan (Bahai)"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-24", "Buddha Purnima"),
            ("2024-05-28", "Youm-e-Takbeer"),
            ("2024-06-17", "Eid-ul-Adha"),
            ("2024-06-18", "Eid-ul-Adha"),
            ("2024-06-19", "Eid-ul-Adha"),
            ("2024-07-15", "Ashura"),
            ("2024-07-16", "Ashura"),
            ("2024-08-14", "Independence Day"),
            ("2024-08-15", "Nauroze (Parsi New Year)"),
            ("2024-08-20", "Birthday of Lord Zoroaster (Khordad Sal)"),
            ("2024-09-04", "Krishna Janmashtami"),
            ("2024-09-17", "Eid Milad-un-Nabi"),
            ("2024-10-19", "Durga Puja"),
            ("2024-10-20", "Dussehra"),
            ("2024-10-26", "Dussehra Holiday"),
            ("2024-10-30", "Diwali"),
            ("2024-11-09", "Iqbal Day"),
            ("2024-11-24", "Birthday of Guru Nanak Dev Ji"),
            ("2024-11-30", "Birthday of Guru Valmiki Ji"),
            ("2024-12-25", "Quaid-e-Azam Day"),
            ("2024-12-26", "Day after Christmas"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-23", "Basant Panchami"),
            ("2024-02-05", "Kashmir Solidarity Day"),
            ("2024-02-16", "Shiv Ratri"),
            ("2024-03-03", "Dulhandi"),
            ("2024-03-04", "Holi"),
            ("2024-03-23", "Pakistan Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-31", "Easter Sunday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-04-11", "Eid al-Fitr"),
            ("2024-04-12", "Eid al-Fitr"),
            ("2024-04-14", "Baisakhi"),
            ("2024-04-21", "Eid-e-Rizwan (Bahai)"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-24", "Buddha Purnima"),
            ("2024-05-28", "Youm-e-Takbeer"),
            ("2024-06-17", "Eid al-Adha"),
            ("2024-06-18", "Eid al-Adha"),
            ("2024-06-19", "Eid al-Adha"),
            ("2024-07-15", "Ashura"),
            ("2024-07-16", "Ashura"),
            ("2024-08-14", "Independence Day"),
            ("2024-08-15", "Nauroze (Parsi New Year)"),
            ("2024-08-20", "Birthday of Lord Zoroaster (Khordad Sal)"),
            ("2024-09-04", "Krishna Janmashtami"),
            ("2024-09-17", "Prophet's Birthday"),
            ("2024-10-19", "Durga Puja"),
            ("2024-10-20", "Dussehra"),
            ("2024-10-26", "Dussehra Holiday"),
            ("2024-10-30", "Diwali"),
            ("2024-11-09", "Iqbal Day"),
            ("2024-11-24", "Birthday of Guru Nanak Dev Ji"),
            ("2024-11-30", "Birthday of Guru Valmiki Ji"),
            ("2024-12-25", "Quaid-e-Azam Day"),
            ("2024-12-26", "Day after Christmas"),
        )

    def test_l10n_ur_pk(self):
        self.assertLocalizedHolidays(
            "ur_PK",
            ("2024-01-01", "نیا سال"),
            ("2024-01-23", "بسنت پنچمی"),
            ("2024-02-05", "یوم یکجہتی کشمیر"),
            ("2024-02-16", "شیو راتری"),
            ("2024-03-03", "دلہنڈی"),
            ("2024-03-04", "ہولی"),
            ("2024-03-23", "یوم پاکستان"),
            ("2024-03-29", "گڈ فرائیڈے"),
            ("2024-03-31", "ایسٹر سنڈے"),
            ("2024-04-01", "ایسٹر پیر"),
            ("2024-04-10", "عید الفطر"),
            ("2024-04-11", "عید الفطر"),
            ("2024-04-12", "عید الفطر"),
            ("2024-04-14", "بیساکھی"),
            ("2024-04-21", "عید رضوان (بہائی)"),
            ("2024-05-01", "یوم مزدور"),
            ("2024-05-24", "بدھ پورنیما"),
            ("2024-05-28", "یوم تکبیر"),
            ("2024-06-17", "عید الاضحی"),
            ("2024-06-18", "عید الاضحی"),
            ("2024-06-19", "عید الاضحی"),
            ("2024-07-15", "عاشورہ"),
            ("2024-07-16", "عاشورہ"),
            ("2024-08-14", "یوم آزادی"),
            ("2024-08-15", "نوروز (پارسی نیا سال)"),
            ("2024-08-20", "یوم پیدائش لارڈ زرتشت (خورداد سال)"),
            ("2024-09-04", "کرشن جنم اشٹمی"),
            ("2024-09-17", "عید میلاد النبی"),
            ("2024-10-19", "درگا پوجا"),
            ("2024-10-20", "دسہرہ"),
            ("2024-10-26", "دسہرہ چھٹی"),
            ("2024-10-30", "دیوالی"),
            ("2024-11-09", "یوم اقبال"),
            ("2024-11-24", "گرونانک دیو جی کا یوم پیدائش"),
            ("2024-11-30", "گرو والمیکی جی کا یوم پیدائش"),
            ("2024-12-25", "یوم قائداعظم"),
            ("2024-12-26", "کرسمس کے بعد کا دن"),
        )
