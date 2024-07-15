#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.entities.ISO_3166.KH import KhHolidays
from tests.common import CommonCountryTests


class TestKhHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(KhHolidays)

    def test_km(self):
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
            (
                "2023-05-14",
                "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម ព្រះករុណា ព្រះបាទសម្តេចព្រះបរមនាថ នរោត្តម សីហមុនី",
            ),
            (
                "2023-06-18",
                "ព្រះរាជពិធីបុណ្យចម្រើនព្រះជន្ម សម្តេចព្រះមហាក្សត្រី ព្រះវររាជមាតា នរោត្តម មុនិនាថ សីហនុ",
            ),
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
