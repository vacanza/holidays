#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.cambodia import Cambodia, KH, KHM
from tests.common import CommonCountryTests


class TestCambodia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Cambodia, years=range(1993, 2050))

    def test_country_aliases(self):
        self.assertAliases(Cambodia, KH, KHM)

    def test_no_holidays(self):
        self.assertNoHolidays(Cambodia(years=1992))

    def test_special_holidays(self):
        self.assertHoliday(
            "2016-05-02",
            "2016-05-16",
            "2018-05-21",
            "2019-09-30",
            "2020-05-11",
            "2020-08-17",
            "2020-08-18",
            "2020-08-19",
            "2020-08-20",
            "2020-08-21",
            "2024-04-16",
        )

    def test_2022(self):
        self.assertHolidays(
            Cambodia(years=2022),
            ("2022-01-01", "ទិវាចូលឆ្នាំសាកល"),
            ("2022-01-07", "ទិវាជ័យជម្នះលើរបបប្រល័យពូជសាសន៍"),
            ("2022-03-08", "ទិវាអន្តរជាតិនារី"),
            ("2022-04-14", "ពិធីបុណ្យចូលឆ្នាំថ្មីប្រពៃណីជាតិ"),
            ("2022-04-15", "ពិធីបុណ្យចូលឆ្នាំថ្មីប្រពៃណីជាតិ"),
            ("2022-04-16", "ពិធីបុណ្យចូលឆ្នាំថ្មីប្រពៃណីជាតិ"),
            ("2022-05-01", "ទិវាពលកម្មអន្តរជាតិ"),
            ("2022-05-14", "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម ព្រះករុណា ព្រះបាទសម្តេចព្រះបរមនាថ នរោត្តម សីហមុនី"),
            ("2022-05-15", "ពិធីបុណ្យវិសាខបូជា"),
            ("2022-05-19", "ព្រះរាជពិធីច្រត់ព្រះនង្គ័ល"),
            ("2022-06-18", "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម សម្តេចព្រះមហាក្សត្រី ព្រះវររាជមាតា នរោត្តម មុនិនាថ សីហនុ"),
            ("2022-09-24", "ទិវាប្រកាសរដ្ឋធម្មនុញ្ញ; ពិធីបុណ្យភ្ផុំបិណ្ឌ"),
            ("2022-09-25", "ពិធីបុណ្យភ្ផុំបិណ្ឌ"),
            ("2022-09-26", "ពិធីបុណ្យភ្ផុំបិណ្ឌ"),
            (
                "2022-10-15",
                (
                    "ទិវាប្រារព្ឋពិធីគោរពព្រះវិញ្ញាណក្ខន្ឋ ព្រះករុណា ព្រះបាទសម្តេចព្រះ នរោត្តម "
                    "សីហនុ ព្រះមហាវីរក្សត្រ ព្រះវររាជបិតាឯករាជ្យ បូរណភាពទឹកដី "
                    "និងឯកភាពជាតិខ្មែរ ព្រះបរមរតនកោដ្ឋ"
                ),
            ),
            (
                "2022-10-29",
                (
                    "ព្រះរាជពិធីគ្រងព្រះបរមរាជសម្បត្តិ របស់ ព្រះករុណា "
                    "ព្រះបាទសម្តេចព្រះបរមនាថ នរោត្តម សីហមុនី "
                    "ព្រះមហាក្សត្រនៃព្រះរាជាណាចក្រកម្ពុជា"
                ),
            ),
            ("2022-11-07", "ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក"),
            ("2022-11-08", "ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក"),
            ("2022-11-09", "ពិធីបុណ្យឯករាជ្យជាតិ; ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក"),
        )

    def test_2023(self):
        self.assertHolidays(
            Cambodia(years=2023),
            ("2023-01-01", "ទិវាចូលឆ្នាំសាកល"),
            ("2023-01-07", "ទិវាជ័យជម្នះលើរបបប្រល័យពូជសាសន៍"),
            ("2023-03-08", "ទិវាអន្តរជាតិនារី"),
            ("2023-04-14", "ពិធីបុណ្យចូលឆ្នាំថ្មីប្រពៃណីជាតិ"),
            ("2023-04-15", "ពិធីបុណ្យចូលឆ្នាំថ្មីប្រពៃណីជាតិ"),
            ("2023-04-16", "ពិធីបុណ្យចូលឆ្នាំថ្មីប្រពៃណីជាតិ"),
            ("2023-05-01", "ទិវាពលកម្មអន្តរជាតិ"),
            ("2023-05-04", "ពិធីបុណ្យវិសាខបូជា"),
            ("2023-05-08", "ព្រះរាជពិធីច្រត់ព្រះនង្គ័ល"),
            ("2023-05-14", "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម ព្រះករុណា ព្រះបាទសម្តេចព្រះបរមនាថ នរោត្តម សីហមុនី"),
            ("2023-06-18", "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម សម្តេចព្រះមហាក្សត្រី ព្រះវររាជមាតា នរោត្តម មុនិនាថ សីហនុ"),
            ("2023-09-24", "ទិវាប្រកាសរដ្ឋធម្មនុញ្ញ"),
            ("2023-10-13", "ពិធីបុណ្យភ្ផុំបិណ្ឌ"),
            ("2023-10-14", "ពិធីបុណ្យភ្ផុំបិណ្ឌ"),
            (
                "2023-10-15",
                (
                    "ទិវាប្រារព្ឋពិធីគោរពព្រះវិញ្ញាណក្ខន្ឋ ព្រះករុណា ព្រះបាទសម្តេចព្រះ នរោត្តម "
                    "សីហនុ ព្រះមហាវីរក្សត្រ ព្រះវររាជបិតាឯករាជ្យ បូរណភាពទឹកដី "
                    "និងឯកភាពជាតិខ្មែរ ព្រះបរមរតនកោដ្ឋ; ពិធីបុណ្យភ្ផុំបិណ្ឌ"
                ),
            ),
            (
                "2023-10-29",
                (
                    "ព្រះរាជពិធីគ្រងព្រះបរមរាជសម្បត្តិ របស់ ព្រះករុណា "
                    "ព្រះបាទសម្តេចព្រះបរមនាថ នរោត្តម សីហមុនី "
                    "ព្រះមហាក្សត្រនៃព្រះរាជាណាចក្រកម្ពុជា"
                ),
            ),
            ("2023-11-09", "ពិធីបុណ្យឯករាជ្យជាតិ"),
            ("2023-11-26", "ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក"),
            ("2023-11-27", "ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក"),
            ("2023-11-28", "ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក"),
        )

    def test_day_of_victory_over_genocidal_regime(self):
        self.assertHolidayName(
            "ទិវាជ័យជម្នះលើរបបប្រល័យពូជសាសន៍", (f"{year}-01-07" for year in range(1993, 2050))
        )

    def test_sangkranta(self):
        years_sangkranta_apr14 = {
            2017,
            2018,
            2021,
            2022,
            2023,
            2025,
            2026,
            2027,
            2029,
            2030,
            2031,
        }
        for year in set(range(1993, 2050)).difference({2020}):
            if year in years_sangkranta_apr14:
                self.assertHoliday(f"{year}-04-14", f"{year}-04-15", f"{year}-04-16")
            else:
                self.assertHoliday(f"{year}-04-13", f"{year}-04-14", f"{year}-04-15")

    def test_king_sihamoni_birthday(self):
        name = "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម ព្រះករុណា ព្រះបាទសម្តេចព្រះបរមនាថ នរោត្តម សីហមុនី"
        self.assertHolidayName(name, (f"{year}-05-13" for year in range(2005, 2020)))
        self.assertHolidayName(name, (f"{year}-05-14" for year in range(2005, 2050)))
        self.assertHolidayName(name, (f"{year}-05-15" for year in range(2005, 2020)))
        self.assertNoHolidayName(name, range(1993, 2005))

    def test_national_day_of_remembrance(self):
        name = "ទិវាជាតិនៃការចងចាំ"
        self.assertHolidayName(name, (f"{year}-05-20" for year in range(2018, 2020)))
        self.assertNoHolidayName(name, range(1993, 2018), range(2020, 2050))

    def test_international_children_day(self):
        name = "ទិវាកុមារអន្តរជាតិ"
        self.assertHolidayName(name, (f"{year}-06-01" for year in range(1993, 2020)))
        self.assertNoHolidayName(name, range(2020, 2050))

    def test_queen_mother_monineath_birthday(self):
        name = "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម សម្តេចព្រះមហាក្សត្រី ព្រះវររាជមាតា នរោត្តម មុនិនាថ សីហនុ"
        self.assertHolidayName(name, (f"{year}-06-18" for year in range(1994, 2050)))
        self.assertNoHolidayName(name, 1993)

    def test_constitution_day(self):
        self.assertHolidayName(
            "ទិវាប្រកាសរដ្ឋធម្មនុញ្ញ", (f"{year}-09-24" for year in range(1993, 2050))
        )

    def test_king_sihanouk_memorial_day(self):
        name = (
            "ទិវាប្រារព្ឋពិធីគោរពព្រះវិញ្ញាណក្ខន្ឋ ព្រះករុណា ព្រះបាទសម្តេចព្រះ"
            " នរោត្តម សីហនុ ព្រះមហាវីរក្សត្រ ព្រះវររាជបិតាឯករាជ្យ បូរណភាពទឹកដី"
            " និងឯកភាពជាតិខ្មែរ ព្រះបរមរតនកោដ្ឋ"
        )
        self.assertHolidayName(name, (f"{year}-10-15" for year in range(2012, 2050)))
        self.assertNoHolidayName(name, range(1993, 2012))

    def test_paris_peace_agreement_day(self):
        name = "ទិវារំលឹកសន្ធិសញ្ញាសន្តិភាពទីក្រុងប៉ារីស"
        self.assertHolidayName(name, (f"{year}-10-23" for year in range(1993, 2020)))
        self.assertNoHolidayName(name, range(2020, 2050))

    def test_king_sihamoni_coronation_day(self):
        name = (
            "ព្រះរាជពិធីគ្រងព្រះបរមរាជសម្បត្តិ របស់ ព្រះករុណា "
            "ព្រះបាទសម្តេចព្រះបរមនាថ នរោត្តម សីហមុនី "
            "ព្រះមហាក្សត្រនៃព្រះរាជាណាចក្រកម្ពុជា"
        )
        self.assertHolidayName(name, (f"{year}-10-29" for year in range(2004, 2050)))
        self.assertNoHolidayName(name, range(1993, 2004))

    def test_national_independence_day(self):
        self.assertHolidayName("ពិធីបុណ្យឯករាជ្យជាតិ", (f"{year}-11-09" for year in range(1993, 2050)))

    def test_international_human_rights_day(self):
        name = "ទិវាសិទ្ធិមនុស្សអន្តរជាតិ"
        self.assertHolidayName(name, (f"{year}-12-10" for year in range(1993, 2020)))
        self.assertNoHolidayName(name, range(2020, 2050))

    def test_peace_day_in_cambodia(self):
        name = "ទិវាសន្តិភាពនៅកម្ពុជា"
        self.assertHolidayName(name, (f"{year}-12-29" for year in range(2024, 2050)))
        self.assertNoHolidayName(name, range(1993, 2024))

    def test_pchum_ben(self):
        name = "ពិធីបុណ្យភ្ផុំបិណ្ឌ"
        self.assertHolidayName(
            name,
            # 2 Days Celebration
            "2015-10-11",
            "2015-10-12",
            "2016-09-30",
            "2016-10-01",
            # 3 Days Celebration
            "2017-09-19",
            "2017-09-20",
            "2017-09-21",
            "2018-10-08",
            "2018-10-09",
            "2018-10-10",
            "2019-09-27",
            "2019-09-28",
            "2019-09-29",
            "2020-09-16",
            "2020-09-17",
            "2020-09-18",
            "2021-10-05",
            "2021-10-06",
            "2021-10-07",
            "2022-09-24",
            "2022-09-25",
            "2022-09-26",
            "2023-10-13",
            "2023-10-14",
            "2023-10-15",
        )

    def test_bon_om_touk(self):
        name = "ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក"
        self.assertHolidayName(
            name,
            # 3 Days Celebration
            "2015-11-24",
            "2015-11-25",
            "2015-11-26",
            "2016-11-13",
            "2016-11-14",
            "2016-11-15",
            "2017-11-02",
            "2017-11-03",
            "2017-11-04",
            "2018-11-21",
            "2018-11-22",
            "2018-11-23",
            "2019-11-10",
            "2019-11-11",
            "2019-11-12",
            "2020-10-30",
            "2020-10-31",
            "2020-11-01",
            "2021-11-18",
            "2021-11-19",
            "2021-11-20",
            "2022-11-07",
            "2022-11-08",
            "2022-11-09",
            "2023-11-26",
            "2023-11-27",
            "2023-11-28",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "ទិវាចូលឆ្នាំសាកល"),
            ("2023-01-07", "ទិវាជ័យជម្នះលើរបបប្រល័យពូជសាសន៍"),
            ("2023-03-08", "ទិវាអន្តរជាតិនារី"),
            ("2023-04-14", "ពិធីបុណ្យចូលឆ្នាំថ្មីប្រពៃណីជាតិ"),
            ("2023-04-15", "ពិធីបុណ្យចូលឆ្នាំថ្មីប្រពៃណីជាតិ"),
            ("2023-04-16", "ពិធីបុណ្យចូលឆ្នាំថ្មីប្រពៃណីជាតិ"),
            ("2023-05-01", "ទិវាពលកម្មអន្តរជាតិ"),
            ("2023-05-04", "ពិធីបុណ្យវិសាខបូជា"),
            ("2023-05-08", "ព្រះរាជពិធីច្រត់ព្រះនង្គ័ល"),
            ("2023-05-14", "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម ព្រះករុណា ព្រះបាទសម្តេចព្រះបរមនាថ នរោត្តម សីហមុនី"),
            ("2023-06-18", "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម សម្តេចព្រះមហាក្សត្រី ព្រះវររាជមាតា នរោត្តម មុនិនាថ សីហនុ"),
            ("2023-09-24", "ទិវាប្រកាសរដ្ឋធម្មនុញ្ញ"),
            ("2023-10-13", "ពិធីបុណ្យភ្ផុំបិណ្ឌ"),
            ("2023-10-14", "ពិធីបុណ្យភ្ផុំបិណ្ឌ"),
            (
                "2023-10-15",
                (
                    "ទិវាប្រារព្ឋពិធីគោរពព្រះវិញ្ញាណក្ខន្ឋ ព្រះករុណា ព្រះបាទសម្តេចព្រះ នរោត្តម "
                    "សីហនុ ព្រះមហាវីរក្សត្រ ព្រះវររាជបិតាឯករាជ្យ បូរណភាពទឹកដី "
                    "និងឯកភាពជាតិខ្មែរ ព្រះបរមរតនកោដ្ឋ; ពិធីបុណ្យភ្ផុំបិណ្ឌ"
                ),
            ),
            (
                "2023-10-29",
                (
                    "ព្រះរាជពិធីគ្រងព្រះបរមរាជសម្បត្តិ របស់ ព្រះករុណា "
                    "ព្រះបាទសម្តេចព្រះបរមនាថ នរោត្តម សីហមុនី "
                    "ព្រះមហាក្សត្រនៃព្រះរាជាណាចក្រកម្ពុជា"
                ),
            ),
            ("2023-11-09", "ពិធីបុណ្យឯករាជ្យជាតិ"),
            ("2023-11-26", "ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក"),
            ("2023-11-27", "ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក"),
            ("2023-11-28", "ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "International New Year Day"),
            ("2023-01-07", "Day of Victory over the Genocidal Regime"),
            ("2023-03-08", "International Women's Rights Day"),
            ("2023-04-14", "Khmer New Year's Day"),
            ("2023-04-15", "Khmer New Year's Day"),
            ("2023-04-16", "Khmer New Year's Day"),
            ("2023-05-01", "International Labor Day"),
            ("2023-05-04", "Visaka Bochea Day"),
            ("2023-05-08", "Royal Ploughing Ceremony"),
            ("2023-05-14", "HM King Norodom Sihamoni's Birthday"),
            ("2023-06-18", "HM Queen Norodom Monineath Sihanouk the Queen-Mother's Birthday"),
            ("2023-09-24", "Constitution Day"),
            ("2023-10-13", "Pchum Ben Day"),
            ("2023-10-14", "Pchum Ben Day"),
            ("2023-10-15", "HM King Norodom Sihanouk Mourning Day; Pchum Ben Day"),
            ("2023-10-29", "HM King Norodom Sihamoni's Coronation Day"),
            ("2023-11-09", "National Independence Day"),
            ("2023-11-26", "Water Festival"),
            ("2023-11-27", "Water Festival"),
            ("2023-11-28", "Water Festival"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2023-01-01", "วันปีใหม่สากล"),
            ("2023-01-07", "วันชัยชนะเหนือระบอบฆ่าล้างเผ่าพันธุ์เขมรแดง"),
            ("2023-03-08", "วันสตรีสากล"),
            ("2023-04-14", "เทศกาลขึ้นปีใหม่ประเพณี"),
            ("2023-04-15", "เทศกาลขึ้นปีใหม่ประเพณี"),
            ("2023-04-16", "เทศกาลขึ้นปีใหม่ประเพณี"),
            ("2023-05-01", "วันแรงงานสากล"),
            ("2023-05-04", "วันวิสาขบูชา"),
            ("2023-05-08", "พระราชพิธีบุญจรดพระนังคัลแรกนาขวัญ"),
            (
                "2023-05-14",
                (
                    "พระราชพิธีเฉลิมพระชนมพรรษา พระบาทสมเด็จพระบรมนาถ นโรดมสีหมุนี "
                    "พระมหากษัตริย์แห่งราชอาณาจักรกัมพูชา"
                ),
            ),
            ("2023-06-18", "พระราชพิธีเฉลิมพระชนมพรรษา สมเด็จพระบรมราชินี นโรดม มนีนาถ สีหนุ"),
            ("2023-09-24", "วันรัฐธรรมนูญ"),
            ("2023-10-13", "เทศกาลงานวันสาร์ทภจุมบิณฑ์เขมร"),
            ("2023-10-14", "เทศกาลงานวันสาร์ทภจุมบิณฑ์เขมร"),
            (
                "2023-10-15",
                (
                    "วันสดุดีพระบาทสมเด็จพระบรมนาถนโรดม สีหนุ พระบิดาแห่งเอกราช "
                    "บูรณภาพแห่งดินแดน และเอกภาพของชาติกัมพูชา; เทศกาลงานวันสาร์ทภจุมบิณฑ์เขมร"
                ),
            ),
            (
                "2023-10-29",
                (
                    "พระราชพิธีเฉลิมฉลองการขึ้นครองราชสมบัติ พระบาทสมเด็จพระบรมนาถ นโรดมสีหมุนี "
                    "พระมหากษัตริย์แห่งราชอาณาจักรกัมพูชา"
                ),
            ),
            ("2023-11-09", "วันประกาศเอกราชจากฝรั่งเศส"),
            ("2023-11-26", "พระราชพิธีบุญแข่งเรือลอยกระทงไฟไหว้พระจันทร์และกินข้าวเม่า"),
            ("2023-11-27", "พระราชพิธีบุญแข่งเรือลอยกระทงไฟไหว้พระจันทร์และกินข้าวเม่า"),
            ("2023-11-28", "พระราชพิธีบุญแข่งเรือลอยกระทงไฟไหว้พระจันทร์และกินข้าวเม่า"),
        )
