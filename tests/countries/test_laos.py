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

from holidays.constants import PUBLIC
from holidays.countries.laos import Laos, LA, LAO
from tests.common import TestCase


class TestLaos(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Laos, years=range(1975, 2058), years_non_observed=range(2018, 2058))

    def test_country_aliases(self):
        self.assertCountryAliases(Laos, LA, LAO)

    def test_no_holidays(self):
        self.assertNoHolidays(Laos(years=1974))

    def test_2022_public(self):
        self.assertHolidays(
            Laos(categories=(PUBLIC,), years=2022),
            ("2022-01-01", "ວັນປີໃໝ່ສາກົນ"),
            ("2022-01-03", "ພັກຊົດເຊີຍວັນປີໃໝ່ສາກົນ"),
            ("2022-03-08", "ວັນແມ່ຍິງສາກົນ"),
            ("2022-04-14", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-15", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-16", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-18", "ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ"),
            ("2022-05-01", "ວັນກຳມະກອນສາກົນ"),
            ("2022-05-02", "ພັກຊົດເຊີຍວັນກຳມະກອນສາກົນ"),
            ("2022-12-02", "ວັນຊາດ"),
        )

    def test_2023_public(self):
        self.assertHolidays(
            Laos(categories=(PUBLIC,), years=2023),
            ("2023-01-01", "ວັນປີໃໝ່ສາກົນ"),
            ("2023-01-02", "ພັກຊົດເຊີຍວັນປີໃໝ່ສາກົນ"),
            ("2023-03-08", "ວັນແມ່ຍິງສາກົນ"),
            ("2023-04-14", "ບຸນປີໃໝ່ລາວ"),
            ("2023-04-15", "ບຸນປີໃໝ່ລາວ"),
            ("2023-04-16", "ບຸນປີໃໝ່ລາວ"),
            ("2023-04-17", "ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ"),
            ("2023-04-18", "ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ"),
            ("2023-05-01", "ວັນກຳມະກອນສາກົນ"),
            ("2023-12-02", "ວັນຊາດ"),
            ("2023-12-04", "ພັກຊົດເຊີຍວັນຊາດ"),
        )

    def test_new_years_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1975, 2058))

        self.assertNoNonObservedHoliday(
            "2022-01-03",
            "2023-01-02",
        )

    def test_lao_peoples_armed_force_day(self):
        self.assertHoliday(f"{year}-01-20" for year in range(1975, 2058))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "ວັນປີໃໝ່ສາກົນ"),
            ("2022-01-03", "ພັກຊົດເຊີຍວັນປີໃໝ່ສາກົນ"),
            ("2022-03-08", "ວັນແມ່ຍິງສາກົນ"),
            ("2022-04-14", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-15", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-16", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-18", "ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ"),
            ("2022-05-01", "ວັນກຳມະກອນສາກົນ"),
            ("2022-05-02", "ພັກຊົດເຊີຍວັນກຳມະກອນສາກົນ"),
            ("2022-12-02", "ວັນຊາດ"),
        )

    def test_l10n_en_US(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (in lieu)"),
            ("2022-03-08", "International Women's Rights Day"),
            ("2022-04-14", "Lao New Year's Day"),
            ("2022-04-15", "Lao New Year's Day"),
            ("2022-04-16", "Lao New Year's Day"),
            ("2022-04-18", "Lao New Year's Day (in lieu)"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day (in lieu)"),
            ("2022-12-02", "Lao National Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "วันปีใหม่สากล"),
            ("2022-01-03", "ชดเชยวันปีใหม่สากล"),
            ("2022-03-08", "วันสตรีสากล"),
            ("2022-04-14", "วันปีใหม่ลาว"),
            ("2022-04-15", "วันปีใหม่ลาว"),
            ("2022-04-16", "วันปีใหม่ลาว"),
            ("2022-04-18", "ชดเชยวันปีใหม่ลาว"),
            ("2022-05-01", "วันแรงงานสากล"),
            ("2022-05-02", "ชดเชยวันแรงงานสากล"),
            ("2022-12-02", "วันชาติ สปป. ลาว"),
        )