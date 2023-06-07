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

from holidays.countries.cambodia import Cambodia, KH, KHM
from tests.common import TestCase


class TestCambodia(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            Cambodia,
            years=range(1993, 2077),
            years_non_observed=range(1993, 2077),
        )

    def test_country_aliases(self):
        self.assertCountryAliases(Cambodia, KH, KHM)

    def test_no_holidays(self):
        self.assertNoHolidays(Cambodia(years=1992))

    def test_special_holidays(self):
        self.assertHoliday(
            "2020-08-17",
            "2020-08-18",
            "2020-08-19",
            "2020-08-20",
            "2020-08-21",
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
            (
                "2022-05-14",
                (
                    "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម ព្រះករុណា "
                    "ព្រះបាទសម្តេចព្រះបរមនាថ នរោត្តម សីហមុនី"
                ),
            ),
            ("2022-05-15", "ពិធីបុណ្យវិសាខបូជា"),
            ("2022-05-19", "ព្រះរាជពិធីច្រត់ព្រះនង្គ័ល"),
            (
                "2022-06-18",
                (
                    "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម សម្តេចព្រះមហាក្សត្រី "
                    "ព្រះវររាជមាតា នរោត្តម មុនិនាថ​ សីហនុ"
                ),
            ),
            ("2022-09-24", "ទិវាប្រកាសរដ្ឋធម្មនុញ្ញ; ពិធីបុណ្យភ្ផុំបិណ្ឌ"),
            ("2022-09-25", "ពិធីបុណ្យភ្ផុំបិណ្ឌ"),
            ("2022-09-26", "ពិធីបុណ្យភ្ផុំបិណ្ឌ"),
            (
                "2022-10-15",
                (
                    "ទិវាប្រារព្ឋពិធីគោរពព្រះវិញ្ញាណក្ខន្ឋ ព្រះករុណា "
                    "ព្រះបាទសម្តេចព្រះ នរោត្តម សីហនុ ព្រះមហាវីរក្សត្រ "
                    "ព្រះវររាជបិតាឯករាជ្យ បូរណភាពទឹកដី និងឯកភាពជាតិខ្មែរ "
                    "ព្រះបរមរតនកោដ្ឋ"
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
            (
                "2022-11-07",
                "ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក",
            ),
            (
                "2022-11-08",
                "ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក",
            ),
            (
                "2022-11-09",
                (
                    "ពិធីបុណ្យឯករាជ្យជាតិ; ព្រះរាជពិធីបុណ្យអុំទូក "
                    "បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក"
                ),
            ),
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
            (
                "2023-05-14",
                (
                    "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម ព្រះករុណា "
                    "ព្រះបាទសម្តេចព្រះបរមនាថ នរោត្តម សីហមុនី"
                ),
            ),
            (
                "2023-06-18",
                (
                    "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម សម្តេចព្រះមហាក្សត្រី "
                    "ព្រះវររាជមាតា នរោត្តម មុនិនាថ​ សីហនុ"
                ),
            ),
            ("2023-09-24", "ទិវាប្រកាសរដ្ឋធម្មនុញ្ញ"),
            ("2023-10-13", "ពិធីបុណ្យភ្ផុំបិណ្ឌ"),
            ("2023-10-14", "ពិធីបុណ្យភ្ផុំបិណ្ឌ"),
            (
                "2023-10-15",
                (
                    "ទិវាប្រារព្ឋពិធីគោរពព្រះវិញ្ញាណក្ខន្ឋ ព្រះករុណា "
                    "ព្រះបាទសម្តេចព្រះ នរោត្តម សីហនុ ព្រះមហាវីរក្សត្រ "
                    "ព្រះវររាជបិតាឯករាជ្យ បូរណភាពទឹកដី និងឯកភាពជាតិខ្មែរ "
                    "ព្រះបរមរតនកោដ្ឋ; ពិធីបុណ្យភ្ផុំបិណ្ឌ"
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
            (
                "2023-11-26",
                "ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក",
            ),
            (
                "2023-11-27",
                "ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក",
            ),
            (
                "2023-11-28",
                "ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក",
            ),
        )

    def test_day_of_victory_over_genocidal_regime(self):
        self.assertHolidaysName(
            "ទិវាជ័យជម្នះលើរបបប្រល័យពូជសាសន៍",
            (f"{year}-01-07" for year in range(1993, 2058)),
        )

    def test_sangkranta(self):
        sangkranta_years_apr14 = (2017, 2018, 2021, 2022, 2023)
        for year in range(1993, 2058):
            if year != 2020:
                if year in sangkranta_years_apr14:
                    self.assertHoliday(
                        f"{year}-04-14", f"{year}-04-15", f"{year}-04-16"
                    )
                else:
                    self.assertHoliday(
                        f"{year}-04-13", f"{year}-04-14", f"{year}-04-15"
                    )

    def test_king_sihamoni_birthday(self):
        name = (
            "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម ព្រះករុណា "
            "ព្រះបាទសម្តេចព្រះបរមនាថ នរោត្តម សីហមុនី"
        )
        self.assertNoHolidayName(name, 2004)
        self.assertHolidaysName(
            name, (f"{year}-05-13" for year in range(2005, 2020))
        )
        self.assertHolidaysName(
            name, (f"{year}-05-14" for year in range(2005, 2058))
        )
        self.assertHolidaysName(
            name, (f"{year}-05-15" for year in range(2005, 2020))
        )

    def test_national_day_of_remembrance(self):
        name = "ទិវាជាតិនៃការចងចាំ"
        self.assertNoHolidayName(name, 2017)
        self.assertHolidaysName(
            name, (f"{year}-05-20" for year in range(2018, 2020))
        )
        self.assertNoHolidayName(name, 2020)

    def test_international_children_day(self):
        name = "ទិវាកុមារអន្តរជាតិ"
        self.assertHolidaysName(
            name,
            (f"{year}-06-01" for year in range(1993, 2020)),
        )
        self.assertNoHolidayName(name, 2020)

    def test_queen_mother_monineath_birthday(self):
        name = (
            "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម សម្តេចព្រះមហាក្សត្រី "
            "ព្រះវររាជមាតា នរោត្តម មុនិនាថ​ សីហនុ"
        )
        self.assertNoHolidayName(name, 1993)
        self.assertHolidaysName(
            name, (f"{year}-06-18" for year in range(1994, 2058))
        )

    def test_constitution_day(self):
        self.assertHolidaysName(
            "ទិវាប្រកាសរដ្ឋធម្មនុញ្ញ",
            (f"{year}-09-24" for year in range(1993, 2058)),
        )

    def test_king_sihanouk_memorial_day(self):
        name = (
            "ទិវាប្រារព្ឋពិធីគោរពព្រះវិញ្ញាណក្ខន្ឋ ព្រះករុណា ព្រះបាទសម្តេចព្រះ"
            " នរោត្តម សីហនុ ព្រះមហាវីរក្សត្រ ព្រះវររាជបិតាឯករាជ្យ បូរណភាពទឹកដី"
            " និងឯកភាពជាតិខ្មែរ ព្រះបរមរតនកោដ្ឋ"
        )
        self.assertNoHolidayName(name, 2011)
        self.assertHolidaysName(
            name,
            (f"{year}-10-15" for year in range(2012, 2058)),
        )

    def test_paris_peace_agreement_day(self):
        name = "ទិវារំលឹកសន្ធិសញ្ញាសន្តិភាពទីក្រុងប៉ារីស"
        self.assertHolidaysName(
            name,
            (f"{year}-10-23" for year in range(1993, 2020)),
        )
        self.assertNoHolidayName(name, 2020)

    def test_king_sihamoni_coronation_day(self):
        name = (
            "ព្រះរាជពិធីគ្រងព្រះបរមរាជសម្បត្តិ របស់ ព្រះករុណា "
            "ព្រះបាទសម្តេចព្រះបរមនាថ នរោត្តម សីហមុនី "
            "ព្រះមហាក្សត្រនៃព្រះរាជាណាចក្រកម្ពុជា"
        )
        self.assertNoHolidayName(name, 2003)
        self.assertHolidaysName(
            name, (f"{year}-10-29" for year in range(2004, 2058))
        )

    def test_national_independence_day(self):
        self.assertHolidaysName(
            "ពិធីបុណ្យឯករាជ្យជាតិ",
            (f"{year}-11-09" for year in range(1993, 2058)),
        )

    def test_international_human_rights_day(self):
        name = "ទិវាសិទ្ធិមនុស្សអន្តរជាតិ"
        self.assertHolidaysName(
            name,
            (f"{year}-12-10" for year in range(1993, 2020)),
        )
        self.assertNoHolidayName(name, 2020)

    def test_meak_bochea(self):
        name = "ពិធីបុណ្យមាឃបូជា"
        dt = (
            "2015-02-03",
            "2016-02-22",
            "2017-02-11",
            "2018-01-31",
            "2019-02-19",
        )
        self.assertHolidaysName(name, dt)
        self.assertNoHolidayName(name, Cambodia(years=2058))

    def test_visaka_bochea(self):
        name = "ពិធីបុណ្យវិសាខបូជា"
        dt = (
            "2015-05-02",
            "2016-05-20",
            "2017-05-10",
            "2018-04-29",
            "2019-05-18",
            "2020-05-06",
            "2021-04-26",
            "2022-05-15",
            "2023-05-04",
        )
        self.assertHolidaysName(name, dt)
        self.assertNoHolidayName(name, Cambodia(years=2058))

    def test_preah_neangkoal(self):
        name = "ព្រះរាជពិធីច្រត់ព្រះនង្គ័ល"
        dt = (
            "2015-05-06",
            "2016-05-24",
            "2017-05-14",
            "2018-05-03",
            "2019-05-22",
            "2020-05-10",
            "2021-04-30",
            "2022-05-19",
            "2023-05-08",
        )
        self.assertHolidaysName(name, dt)
        self.assertNoHolidayName(name, Cambodia(years=2058))

    def test_pchum_ben(self):
        name = "ពិធីបុណ្យភ្ផុំបិណ្ឌ"
        dt = (
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
        self.assertHolidaysName(name, dt)
        self.assertNoHolidayName(name, Cambodia(years=2058))

    def test_bon_om_touk(self):
        name = "ព្រះរាជពិធីបុណ្យអុំទូក បណ្តែតប្រទីប និងសំពះព្រះខែអកអំបុក"
        dt = (
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
        self.assertHolidaysName(name, dt)
        self.assertNoHolidayName(name, Cambodia(years=2058))
