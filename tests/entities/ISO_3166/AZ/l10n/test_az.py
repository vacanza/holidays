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

from holidays.entities.ISO_3166.AZ import AzHolidays
from tests.common import CommonCountryTests


class TestAzHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AzHolidays)

    def test_az(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Yeni il bayramı"),
            ("2023-01-02", "Yeni il bayramı"),
            ("2023-01-03", "Dünya azərbaycanlılarının həmrəyliyi günü (müşahidə olunur)"),
            ("2023-01-04", "Yeni il bayramı (müşahidə olunur)"),
            ("2023-01-20", "Ümumxalq hüzn günü"),
            ("2023-03-08", "Qadınlar günü"),
            ("2023-03-20", "Novruz bayramı"),
            ("2023-03-21", "Novruz bayramı"),
            ("2023-03-22", "Novruz bayramı"),
            ("2023-03-23", "Novruz bayramı"),
            ("2023-03-24", "Novruz bayramı"),
            ("2023-04-21", "Ramazan bayrami"),
            ("2023-04-22", "Ramazan bayrami"),
            ("2023-04-24", "Ramazan bayrami (müşahidə olunur)"),
            ("2023-05-09", "Faşizm üzərində qələbə günü"),
            ("2023-05-28", "Müstəqillik Günü"),
            ("2023-05-29", "Müstəqillik Günü (müşahidə olunur)"),
            ("2023-06-15", "Azərbaycan xalqının milli qurtuluş günü"),
            ("2023-06-26", "Azərbaycan Respublikasının Silahlı Qüvvələri günü"),
            ("2023-06-27", "İstirahət günü (24.06.2023 ilə əvəz edilmişdir)"),
            ("2023-06-28", "Qurban bayrami"),
            ("2023-06-29", "Qurban bayrami"),
            ("2023-06-30", "İstirahət günü (25.06.2023 ilə əvəz edilmişdir)"),
            ("2023-09-27", "Anım Günü"),
            ("2023-10-18", "Müstəqilliyin Bərpası Günü"),
            ("2023-11-08", "Zəfər Günü"),
            ("2023-11-09", "Azərbaycan Respublikasının Dövlət bayrağı günü"),
            ("2023-11-10", "İstirahət günü (04.11.2023 ilə əvəz edilmişdir)"),
            ("2023-11-12", "Konstitusiya Günü"),
            ("2023-11-17", "Milli Dirçəliş Günü"),
            ("2023-12-31", "Dünya azərbaycanlılarının həmrəyliyi günü"),
        )
