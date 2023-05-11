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

from holidays.countries.brunei import Brunei, BN, BRN
from tests.common import TestCase


class TestBrunei(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            Brunei,
            years=range(1984, 2077),
            years_non_observed=range(1984, 2077),
        )

    def test_country_aliases(self):
        self.assertCountryAliases(Brunei, BN, BRN)

    def test_no_holidays(self):
        self.assertNoHolidays(Brunei(years=1983))

    def test_special_holidays(self):
        self.assertHoliday("2017-10-05")

    def test_2022(self):
        self.assertHolidays(
            Brunei(years=2022),
            ("2022-01-01", "Awal Tahun Masihi"),
            ("2022-02-01", "Tahun Baru Cina"),
            ("2022-02-23", "Hari Kebangsaan"),
            ("2022-02-28", "Israk dan Mikraj* (*anggaran)"),
            ("2022-04-03", "Hari Pertama Berpuasa* (*anggaran)"),
            (
                "2022-04-04",
                "Hari Pertama Berpuasa* (*anggaran) - Diperhatikan",
            ),
            ("2022-04-19", "Hari Nuzul Al-Quran* (*anggaran)"),
            ("2022-05-02", "Hari Raya Aidil Fitri* (*anggaran)"),
            ("2022-05-03", "Hari Raya Aidil Fitri* (*anggaran)"),
            ("2022-05-04", "Hari Raya Aidil Fitri* (*anggaran)"),
            ("2022-05-31", "Hari Angkatan Bersenjata Diraja Brunei"),
            ("2022-07-09", "Hari Raya Aidil Adha* (*anggaran)"),
            ("2022-07-15", "Hari Keputeraan KDYMM Sultan Brunei"),
            (
                "2022-07-16",
                "Hari Keputeraan KDYMM Sultan Brunei - Diperhatikan",
            ),
            ("2022-07-30", "Awal Tahun Hijrah* (*anggaran)"),
            ("2022-10-08", "Maulidur Rasul* (*anggaran)"),
            ("2022-12-25", "Hari Natal"),
        )

    def test_2023(self):
        self.assertHolidays(
            Brunei(years=2023),
            ("2023-01-01", "Awal Tahun Masihi"),
            ("2023-01-02", "Awal Tahun Masihi - Diperhatikan"),
            ("2023-01-22", "Tahun Baru Cina"),
            ("2023-01-23", "Tahun Baru Cina - Diperhatikan"),
            ("2023-02-18", "Israk dan Mikraj* (*anggaran)"),
            ("2023-02-23", "Hari Kebangsaan"),
            ("2023-03-23", "Hari Pertama Berpuasa* (*anggaran)"),
            ("2023-04-08", "Hari Nuzul Al-Quran* (*anggaran)"),
            (
                "2023-04-22",
                "Hari Raya Aidil Fitri* (*anggaran) - Diperhatikan",
            ),
            ("2023-04-23", "Hari Raya Aidil Fitri* (*anggaran)"),
            ("2023-04-24", "Hari Raya Aidil Fitri* (*anggaran)"),
            ("2023-04-25", "Hari Raya Aidil Fitri* (*anggaran)"),
            ("2023-05-31", "Hari Angkatan Bersenjata Diraja Brunei"),
            ("2023-06-29", "Hari Raya Aidil Adha* (*anggaran)"),
            ("2023-07-15", "Hari Keputeraan KDYMM Sultan Brunei"),
            ("2023-07-19", "Awal Tahun Hijrah* (*anggaran)"),
            ("2023-09-28", "Maulidur Rasul* (*anggaran)"),
            ("2023-12-25", "Hari Natal"),
        )

    def test_national_day(self):
        self.assertHoliday(f"{year}-02-23" for year in range(1984, 2077))

        self.assertNoNonObservedHoliday(
            "2001-02-24",
            "2003-02-24",
            "2007-02-24",
            "2014-02-24",
            "2018-02-24",
            "2020-02-24",
        )

    def test_armed_forces_day(self):
        self.assertHoliday(f"{year}-05-31" for year in range(1984, 2077))

        self.assertNoNonObservedHoliday(
            "2002-06-01",
            "2009-06-01",
            "2013-06-01",
            "2015-06-01",
            "2019-06-01",
            "2020-06-01",
        )

    def test_sultan_hassanal_bolkiah_birthday(self):
        self.assertHoliday(f"{year}-07-15" for year in range(1984, 2077))

        self.assertNoNonObservedHoliday(
            "2001-07-16",
            "2005-07-16",
            "2007-07-16",
            "2011-07-16",
            "2012-07-16",
            "2016-07-16",
            "2018-07-16",
            "2022-07-16",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            (
                ("2023-01-01", "Awal Tahun Masihi"),
                ("2023-01-02", "Awal Tahun Masihi - Diperhatikan"),
                ("2023-02-23", "Hari Kebangsaan"),
                ("2023-05-31", "Hari Angkatan Bersenjata Diraja Brunei"),
                ("2023-07-15", "Hari Keputeraan KDYMM Sultan Brunei"),
            ),
            "ms",
        )

    def test_l10n_en(self):
        self.assertLocalizedHolidays(
            (
                ("2023-01-01", "New Year's Day"),
                ("2023-01-02", "New Year's Day (Observed)"),
                ("2023-02-23", "National Day"),
                ("2023-05-31", "Armed Forces Day"),
                ("2023-07-15", "Sultan Hassanal Bolkiah's Birthday"),
            ),
            "en_US",
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            (
                ("2023-01-01", "วันขึ้นปีใหม่"),
                ("2023-01-02", "ชดเชยวันขึ้นปีใหม่"),
                ("2023-02-23", "วันชาติบรูไน"),
                ("2023-05-31", "วันกองทัพบรูไน"),
                (
                    "2023-07-15",
                    (
                        "วันเฉลิมพระชนมพรรษาสมเด็จพระราชาธิบดี"
                        "สุลต่านฮัสซานัล โบลเกียห์"
                    ),
                ),
            ),
            "th",
        )
