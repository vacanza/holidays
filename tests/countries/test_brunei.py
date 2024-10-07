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

from holidays.countries.brunei import Brunei, BN, BRN
from tests.common import CommonCountryTests


class TestBrunei(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Brunei, years=range(1984, 2077), years_non_observed=range(1984, 2077))

    def test_country_aliases(self):
        self.assertAliases(Brunei, BN, BRN)

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
            ("2022-03-01", "Israk dan Mikraj"),
            ("2022-04-03", "Hari Pertama Berpuasa"),
            ("2022-04-04", "Hari Pertama Berpuasa (diperhatikan)"),
            ("2022-04-19", "Hari Nuzul Al-Quran"),
            ("2022-05-03", "Hari Raya Aidil Fitri"),
            ("2022-05-04", "Hari Raya Aidil Fitri"),
            ("2022-05-05", "Hari Raya Aidil Fitri"),
            ("2022-05-31", "Hari Angkatan Bersenjata Diraja Brunei"),
            ("2022-07-10", "Hari Raya Aidil Adha"),
            ("2022-07-11", "Hari Raya Aidil Adha (diperhatikan)"),
            ("2022-07-15", "Hari Keputeraan KDYMM Sultan Brunei"),
            ("2022-07-16", "Hari Keputeraan KDYMM Sultan Brunei (diperhatikan)"),
            ("2022-07-30", "Awal Tahun Hijrah"),
            ("2022-10-08", "Maulidur Rasul"),
            ("2022-12-25", "Hari Natal"),
            ("2022-12-26", "Hari Natal (diperhatikan)"),
        )

    def test_2023(self):
        self.assertHolidays(
            Brunei(years=2023),
            ("2023-01-01", "Awal Tahun Masihi"),
            ("2023-01-02", "Awal Tahun Masihi (diperhatikan)"),
            ("2023-01-22", "Tahun Baru Cina"),
            ("2023-01-23", "Tahun Baru Cina (diperhatikan)"),
            ("2023-02-18", "Israk dan Mikraj"),
            ("2023-02-23", "Hari Kebangsaan"),
            ("2023-03-23", "Hari Pertama Berpuasa"),
            ("2023-04-08", "Hari Nuzul Al-Quran"),
            ("2023-04-22", "Hari Raya Aidil Fitri"),
            ("2023-04-23", "Hari Raya Aidil Fitri"),
            ("2023-04-24", "Hari Raya Aidil Fitri"),
            ("2023-04-25", "Hari Raya Aidil Fitri (diperhatikan)"),
            ("2023-05-31", "Hari Angkatan Bersenjata Diraja Brunei"),
            ("2023-06-29", "Hari Raya Aidil Adha"),
            ("2023-07-15", "Hari Keputeraan KDYMM Sultan Brunei"),
            ("2023-07-19", "Awal Tahun Hijrah"),
            ("2023-09-28", "Maulidur Rasul"),
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
            ("2023-01-01", "Awal Tahun Masihi"),
            ("2023-01-02", "Awal Tahun Masihi (diperhatikan)"),
            ("2023-01-22", "Tahun Baru Cina"),
            ("2023-01-23", "Tahun Baru Cina (diperhatikan)"),
            ("2023-02-18", "Israk dan Mikraj"),
            ("2023-02-23", "Hari Kebangsaan"),
            ("2023-03-23", "Hari Pertama Berpuasa"),
            ("2023-04-08", "Hari Nuzul Al-Quran"),
            ("2023-04-22", "Hari Raya Aidil Fitri"),
            ("2023-04-23", "Hari Raya Aidil Fitri"),
            ("2023-04-24", "Hari Raya Aidil Fitri"),
            ("2023-04-25", "Hari Raya Aidil Fitri (diperhatikan)"),
            ("2023-05-31", "Hari Angkatan Bersenjata Diraja Brunei"),
            ("2023-06-29", "Hari Raya Aidil Adha"),
            ("2023-07-15", "Hari Keputeraan KDYMM Sultan Brunei"),
            ("2023-07-19", "Awal Tahun Hijrah"),
            ("2023-09-28", "Maulidur Rasul"),
            ("2023-12-25", "Hari Natal"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-22", "Lunar New Year"),
            ("2023-01-23", "Lunar New Year (observed)"),
            ("2023-02-18", "Isra' and Mi'raj"),
            ("2023-02-23", "National Day"),
            ("2023-03-23", "First Day of Ramadan"),
            ("2023-04-08", "Anniversary of the revelation of the Quran"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-23", "Eid al-Fitr"),
            ("2023-04-24", "Eid al-Fitr"),
            ("2023-04-25", "Eid al-Fitr (observed)"),
            ("2023-05-31", "Armed Forces Day"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-07-15", "Sultan Hassanal Bolkiah's Birthday"),
            ("2023-07-19", "Islamic New Year"),
            ("2023-09-28", "Prophet's Birthday"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2023-01-01", "วันขึ้นปีใหม่"),
            ("2023-01-02", "ชดเชยวันขึ้นปีใหม่"),
            ("2023-01-22", "วันตรุษจีน"),
            ("2023-01-23", "ชดเชยวันตรุษจีน"),
            ("2023-02-18", "วันเมี๊ยะราจ"),
            ("2023-02-23", "วันชาติบรูไน"),
            ("2023-03-23", "วันแรกการถือศีลอด"),
            ("2023-04-08", "วันนูซุลอัลกุรอาน"),
            ("2023-04-22", "วันอีฎิ้ลฟิตริ"),
            ("2023-04-23", "วันอีฎิ้ลฟิตริ"),
            ("2023-04-24", "วันอีฎิ้ลฟิตริ"),
            ("2023-04-25", "ชดเชยวันอีฎิ้ลฟิตริ"),
            ("2023-05-31", "วันกองทัพบรูไน"),
            ("2023-06-29", "วันอีดิ้ลอัฎฮา"),
            ("2023-07-15", "วันเฉลิมพระชนมพรรษาสมเด็จพระราชาธิบดีสุลต่านฮัสซานัล โบลเกียห์"),
            ("2023-07-19", "วันขึ้นปีใหม่อิสลาม"),
            ("2023-09-28", "วันเมาลิดนบี"),
            ("2023-12-25", "วันคริสต์มาส"),
        )
