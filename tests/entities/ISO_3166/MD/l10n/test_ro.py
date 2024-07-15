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

from holidays.entities.ISO_3166.MD import MdHolidays
from tests.common import CommonCountryTests


class TestMdHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MdHolidays)

    def test_ro(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Anul Nou"),
            ("2022-01-07", "Nașterea lui Iisus Hristos (Crăciunul pe stil vechi)"),
            ("2022-01-08", "Nașterea lui Iisus Hristos (Crăciunul pe stil vechi)"),
            ("2022-03-08", "Ziua internatională a femeii"),
            ("2022-04-24", "Paștele"),
            ("2022-04-25", "Paștele"),
            ("2022-05-01", "Ziua internaţională a solidarităţii oamenilor muncii"),
            ("2022-05-02", "Paștele blajinilor"),
            (
                "2022-05-09",
                "Ziua Europei; Ziua Victoriei și a comemorării eroilor "
                "căzuţi pentru Independenţa Patriei",
            ),
            ("2022-06-01", "Ziua Ocrotirii Copilului"),
            ("2022-08-27", "Ziua independenţei Republicii Moldova"),
            ("2022-08-31", "Limba noastră"),
            ("2022-12-25", "Nașterea lui Iisus Hristos (Crăciunul pe stil nou)"),
        )
