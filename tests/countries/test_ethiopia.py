#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from holidays.countries.ethiopia import Ethiopia, ET, ETH
from tests.common import TestCase


class TestEthiopia(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Ethiopia)

    def test_country_aliases(self):
        self.assertCountryAliases(Ethiopia, ET, ETH)

    # Check isleap loops
    def test_not_holiday(self):
        self.assertNotIn(date(2019, 9, 11), self.holidays)
        self.assertNotIn(date(2019, 9, 27), self.holidays)
        self.assertNotIn(date(2019, 9, 13), self.holidays)
        self.assertNotIn(date(1940, 5, 5), self.holidays)
        self.assertNotIn(date(1990, 5, 28), self.holidays)
        self.assertNotIn(date(1971, 9, 13), self.holidays)
        self.assertNotIn(date(1970, 9, 12), self.holidays)
        self.assertNotIn(date(1993, 9, 13), self.holidays)
        self.assertNotIn(date(1994, 9, 12), self.holidays)

    def test_2019(self):
        self.assertIn(date(2019, 1, 7), self.holidays)
        self.assertIn(date(2019, 1, 19), self.holidays)
        self.assertIn(date(2019, 3, 2), self.holidays)
        self.assertIn(date(2019, 4, 28), self.holidays)
        self.assertIn(date(2019, 4, 26), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 5, 5), self.holidays)
        self.assertIn(date(2019, 5, 28), self.holidays)
        self.assertIn(date(2019, 9, 12), self.holidays)
        self.assertIn(date(2019, 9, 28), self.holidays)
        self.assertIn(date(2019, 11, 10), self.holidays)
        self.assertIn(date(1975, 9, 13), self.holidays)
        self.assertIn(date(1976, 9, 12), self.holidays)

    def test_2020(self):
        self.assertIn(date(2020, 9, 11), self.holidays)
        self.assertIn(date(2020, 9, 27), self.holidays)

    def test_ethiopian_christmas(self):
        self.assertIn(date(2019, 1, 7), self.holidays)

    def test_ethiopian_ephiphany(self):
        self.assertIn(date(2019, 1, 19), self.holidays)

    def test_adwa_victory(self):
        self.assertIn(date(2019, 3, 2), self.holidays)

    def test_easter_good_friday(self):
        self.assertIn(date(2019, 4, 26), self.holidays)

    def test_easter(self):
        self.assertIn(date(2019, 4, 28), self.holidays)

    def test_labour_day(self):
        self.assertIn(date(2019, 5, 1), self.holidays)

    def test_patriots_day(self):
        self.assertNotIn(date(1940, 5, 5), self.holidays)
        self.assertIn(date(2019, 5, 5), self.holidays)

    def test_downfall_of_dergue(self):
        self.assertIn(date(2019, 5, 28), self.holidays)

    def test_formation_of_dergue(self):
        self.assertIn(date(1982, 9, 12), self.holidays)
        self.assertIn(date(1983, 9, 13), self.holidays)

    def test_hijri_based(self):
        self.holidays = Ethiopia(years=[2019])
        # eid_alfitr
        self.assertIn(date(2019, 6, 4), self.holidays)
        # eid_aladha
        self.assertIn(date(2019, 8, 11), self.holidays)
        # muhammad's birthday
        self.assertIn(date(2019, 11, 10), self.holidays)

    def test_pre_1897(self):
        self.assertNotIn(date(1896, 3, 2), self.holidays)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-07", "ገና"),
            ("2022-01-19", "ጥምቀት"),
            ("2022-03-02", "አድዋ"),
            ("2022-04-22", "ስቅለት"),
            ("2022-04-24", "ፋሲካ"),
            ("2022-05-01", "የሰራተኞች ቀን"),
            ("2022-05-02", "ኢድ አልፈጥር* (*ግምት)"),
            ("2022-05-05", "የአርበኞች ቀን"),
            ("2022-05-28", "ደርግ የወደቀበት ቀን"),
            ("2022-07-09", "አረፋ* (*ግምት)"),
            ("2022-07-10", "አረፋ* (*ግምት)"),
            ("2022-09-11", "አዲስ ዓመት እንቁጣጣሽ"),
            ("2022-09-27", "መስቀል"),
            ("2022-10-08", "መውሊድ* (*ግምት)"),
            ("2022-10-09", "መውሊድ* (*ግምት)"),
        )

    def test_l10n_en_ar(self):
        self.assertLocalizedHolidays(
            "ar",
            ("2022-01-07", "عيد الميلاد"),
            ("2022-01-19", "عيد الغطاس"),
            ("2022-03-02", "العدوة"),
            ("2022-04-22", "جمعة جيدة"),
            ("2022-04-24", "عيد الفصح"),
            ("2022-05-01", "يوم العمال"),
            ("2022-05-02", "(تقدير*) *عيد الفطر"),
            ("2022-05-05", "يوم الوطنيين"),
            ("2022-05-28", "يوم سقوط ديرج"),
            ("2022-07-09", "(تقدير*) *عيد الأضحى"),
            ("2022-07-10", "(تقدير*) *عيد الأضحى"),
            ("2022-09-11", "السنة الإثيوبية الجديدة"),
            ("2022-09-27", "العثور على الصليب الحقيقي"),
            ("2022-10-08", "(تقدير*) *عيد المولد النبوي"),
            ("2022-10-09", "(تقدير*) *عيد المولد النبوي"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-07", "Orthodox Christmas Day"),
            ("2022-01-19", "Orthodox Epiphany Day"),
            ("2022-03-02", "Adwa Victory Day"),
            ("2022-04-22", "Orthodox Good Friday"),
            ("2022-04-24", "Orthodox Easter Sunday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Eid al-Fitr* (*estimated)"),
            ("2022-05-05", "Patriots Day"),
            ("2022-05-28", "Downfall of Dergue Regime Day"),
            ("2022-07-09", "Eid al-Adha* (*estimated)"),
            ("2022-07-10", "Eid al-Adha* (*estimated)"),
            ("2022-09-11", "Ethiopian New Year's Day"),
            ("2022-09-27", "Finding of True Cross"),
            ("2022-10-08", "Prophet Muhammad's Birthday* (*estimated)"),
            ("2022-10-09", "Prophet Muhammad's Birthday* (*estimated)"),
        )
