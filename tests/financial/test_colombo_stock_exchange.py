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

import unittest
from datetime import date

from holidays.financial.colombo_stock_exchange import ColomboStockExchange


class TestColomboStockExchange(unittest.TestCase):
    def setUp(self):
        self.holidays = ColomboStockExchange(language="si_LK")

        self.holidays_half_day = ColomboStockExchange(categories=("half_day"), language="si_LK")

    def test_market_code(self):
        self.assertEqual(self.holidays.market, "XCOL")

    def test_eager_year_population(self):
        hol = ColomboStockExchange(years=[2020])
        self.assertEqual(hol.years, {2020})
        self.assertIn("2020-01-01", hol)

    def test_eager_year_population_positional(self):
        hol = ColomboStockExchange([2020])
        self.assertEqual(hol.years, {2020})
        self.assertIn("2020-01-01", hol)

    def test_base_srilanka_holidays(self):
        self.assertIn(date(2020, 2, 4), self.holidays)
        self.assertNotIn("2021-05-02", self.holidays)
        self.assertNotIn("2021-12-26", self.holidays)

    def test_ad_hoc_closures(self):
        expected_ad_hoc_closures = (
            ("2018-01-15", "විශේෂ බැංකු නිවාඩු දිනය"),
            ("2018-02-05", "ජාතික දින නිවාඩුව"),
            ("2018-04-30", "වෙසක් නිවාඩුව"),
            ("2019-01-01", "CSE සාමාන්‍ය නිවාඩු දිනය"),
            (
                "2019-04-15",
                "ඉරිදා දිනක යෙදෙන සිංහල හා දෙමළ අලුත් අවුරුදු දිනය වෙනුවට විශේෂ බැංකු නිවාඩුව",
            ),
            (
                "2019-05-20",
                "ඉරිදා දිනක යෙදෙන වෙසක් පුර පසළොස්වක පෝය දිනට පසු දිනය වෙනුවට විශේෂ බැංකු නිවාඩුව",
            ),
            (
                "2019-11-11",
                "ඉරිදා දිනක යෙදෙන නබි නායකතුමාගේ උපන් දිනය වෙනුවට විශේෂ බැංකු නිවාඩුව",
            ),
            ("2020-01-01", "CSE සාමාන්‍ය නිවාඩු දිනය"),
            ("2020-03-20", "COVID-19 හේතුවෙන් වෙළඳපොළ වසා දැමීම"),
            (
                "2020-04-14",
                "ඉරිදා දිනක යෙදෙන සිංහල හා දෙමළ අලුත් අවුරුදු දිනට පෙර දිනය වෙනුවට විශේෂ බැංකු නිවාඩුව",
            ),
            ("2021-01-01", "CSE සාමාන්‍ය නිවාඩු දිනය"),
            ("2022-05-02", "ඉරිදා දිනක යෙදෙන මැයි දිනය වෙනුවට අතිරේක නිවාඩුව"),
            (
                "2022-10-10",
                "ඉරිදා දිනක යෙදෙන නබි නායකතුමාගේ උපන් දිනය වෙනුවට අතිරේක නිවාඩුව",
            ),
            ("2022-12-26", "ඉරිදා දිනක යෙදෙන නත්තල් උත්සව දිනය වෙනුවට අතිරේක නිවාඩුව"),
            (
                "2023-01-16",
                "ඉරිදා දිනක යෙදෙන දෙමළ තෛපොංගල් දිනය වෙනුවට අතිරේක නිවාඩුව",
            ),
            ("2024-01-01", "CSE සාමාන්‍ය නිවාඩු දිනය"),
            ("2024-02-05", "ඉරිදා දිනක යෙදෙන නිදහස් සමරු දිනය වෙනුවට අතිරේක නිවාඩුව"),
            ("2025-01-01", "සාමාන්‍ය නිවාඩු දිනය"),
            ("2025-04-15", "විශේෂ බැංකු නිවාඩු දිනය"),
            ("2026-01-01", "CSE සාමාන්‍ය නිවාඩු දිනය"),
        )
        for dt_str, name in expected_ad_hoc_closures:
            year, month, day = (int(x) for x in dt_str.split("-"))
            self.assertIn(date(year, month, day), self.holidays)
            self.assertIn(name, self.holidays.get(dt_str))

    def test_half_days(self):
        expected_half_days = (
            ("2018-04-13", "සිංහල හා දෙමළ අලුත් අවුරුදු දිනට පෙර දිනය"),
            (
                "2019-04-12",
                "සෙනසුරාදා දිනක යෙදෙන සිංහල හා දෙමළ අලුත් අවුරුදු දිනට පෙර දිනය වෙනුවට විශේෂ බැංකු අර්ධ නිවාඩුව",
            ),
            (
                "2021-04-30",
                "සෙනසුරාදා දිනක යෙදෙන මැයි දිනය වෙනුවට අතිරේක අර්ධ නිවාඩුව",
            ),
            (
                "2021-12-24",
                "සෙනසුරාදා දිනක යෙදෙන නත්තල් උත්සව දිනය වෙනුවට අතිරේක අර්ධ නිවාඩුව",
            ),
            (
                "2023-02-03",
                "සෙනසුරාදා දිනක යෙදෙන නිදහස් සමරු දිනය වෙනුවට අතිරේක අර්ධ නිවාඩුව",
            ),
            (
                "2023-05-04",
                "සෙනසුරාදා දිනක යෙදෙන වෙසක් පුර පසළොස්වක පෝය දිනට පසු දිනය වෙනුවට අතිරේක අර්ධ නිවාඩුව",
            ),
            (
                "2024-04-10",
                "සෙනසුරාදා දිනක යෙදෙන සිංහල හා දෙමළ අලුත් අවුරුදු දිනය වෙනුවට අතිරේක අර්ධ නිවාඩුව",
            ),
        )
        for dt_str, name in expected_half_days:
            year, month, day = (int(x) for x in dt_str.split("-"))
            self.assertIn(date(year, month, day), self.holidays_half_day)
            self.assertIn(name, self.holidays_half_day.get(dt_str))
