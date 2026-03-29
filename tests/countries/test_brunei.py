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

from unittest import TestCase

from holidays.countries.brunei import Brunei
from tests.common import CommonCountryTests


class TestBrunei(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Brunei)

    def test_special_holidays(self):
        self.assertHoliday(
            "1998-08-10",
            "2004-09-09",
            "2017-10-05",
        )

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Awal Tahun Masihi"),
            ("2022-02-01", "Tahun Baru Cina"),
            ("2022-02-23", "Hari Kebangsaan"),
            ("2022-02-28", "Israk dan Mikraj"),
            ("2022-04-03", "Hari Pertama Berpuasa"),
            ("2022-04-04", "Hari Pertama Berpuasa (diperhatikan)"),
            ("2022-04-19", "Hari Nuzul Al-Quran"),
            ("2022-05-02", "Hari Raya Aidil Fitri"),
            ("2022-05-03", "Hari Raya Aidil Fitri"),
            ("2022-05-04", "Hari Raya Aidil Fitri"),
            ("2022-05-31", "Hari Angkatan Bersenjata Diraja Brunei"),
            ("2022-07-09", "Hari Raya Aidil Adha"),
            ("2022-07-15", "Hari Keputeraan KDYMM Sultan Brunei"),
            ("2022-07-16", "Hari Keputeraan KDYMM Sultan Brunei (diperhatikan)"),
            ("2022-07-30", "Awal Tahun Hijrah"),
            ("2022-10-08", "Maulidur Rasul"),
            ("2022-12-25", "Hari Natal"),
            ("2022-12-26", "Hari Natal (diperhatikan)"),
        )

    def test_2023(self):
        self.assertHolidaysInYear(
            2023,
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

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "Awal Tahun Masihi"),
            ("2024-02-08", "Israk dan Mikraj"),
            ("2024-02-10", "Tahun Baru Cina"),
            ("2024-02-23", "Hari Kebangsaan"),
            ("2024-02-24", "Hari Kebangsaan (diperhatikan)"),
            ("2024-03-12", "Hari Pertama Berpuasa"),
            ("2024-03-28", "Hari Nuzul Al-Quran"),
            ("2024-04-10", "Hari Raya Aidil Fitri"),
            ("2024-04-11", "Hari Raya Aidil Fitri"),
            ("2024-04-12", "Hari Raya Aidil Fitri"),
            ("2024-04-13", "Hari Raya Aidil Fitri (diperhatikan)"),
            ("2024-05-31", "Hari Angkatan Bersenjata Diraja Brunei"),
            ("2024-06-01", "Hari Angkatan Bersenjata Diraja Brunei (diperhatikan)"),
            ("2024-06-17", "Hari Raya Aidil Adha"),
            ("2024-07-07", "Awal Tahun Hijrah"),
            ("2024-07-08", "Awal Tahun Hijrah (diperhatikan)"),
            ("2024-07-15", "Hari Keputeraan KDYMM Sultan Brunei"),
            ("2024-09-16", "Maulidur Rasul"),
            ("2024-12-25", "Hari Natal"),
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Awal Tahun Masihi"),
            ("2025-01-27", "Israk dan Mikraj"),
            ("2025-01-29", "Tahun Baru Cina"),
            ("2025-02-23", "Hari Kebangsaan"),
            ("2025-02-24", "Hari Kebangsaan (diperhatikan)"),
            ("2025-03-02", "Hari Pertama Berpuasa"),
            ("2025-03-03", "Hari Pertama Berpuasa (diperhatikan)"),
            ("2025-03-18", "Hari Nuzul Al-Quran"),
            ("2025-03-31", "Hari Raya Aidil Fitri"),
            ("2025-04-01", "Hari Raya Aidil Fitri"),
            ("2025-04-02", "Hari Raya Aidil Fitri"),
            ("2025-05-31", "Hari Angkatan Bersenjata Diraja Brunei"),
            ("2025-06-07", "Hari Raya Aidil Adha"),
            ("2025-06-27", "Awal Tahun Hijrah"),
            ("2025-06-28", "Awal Tahun Hijrah (diperhatikan)"),
            ("2025-07-15", "Hari Keputeraan KDYMM Sultan Brunei"),
            ("2025-09-05", "Maulidur Rasul"),
            ("2025-09-06", "Maulidur Rasul (diperhatikan)"),
            ("2025-12-25", "Hari Natal"),
        )

    def test_new_years_day(self):
        name = "Awal Tahun Masihi"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2012-01-02",
            "2016-01-02",
            "2017-01-02",
            "2021-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (diperhatikan)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_lunar_new_day(self):
        name = "Tahun Baru Cina"
        self.assertHolidayName(
            name,
            "2020-01-25",
            "2021-02-12",
            "2022-02-01",
            "2023-01-22",
            "2024-02-10",
            "2025-01-29",
        )
        self.assertHolidayName(name, self.full_range)
        obs_dts = (
            "2013-02-11",
            "2014-02-01",
            "2018-02-17",
            "2021-02-13",
            "2023-01-23",
        )
        self.assertHolidayName(f"{name} (diperhatikan)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_national_day(self):
        name = "Hari Kebangsaan"
        self.assertHolidayName(name, (f"{year}-02-23" for year in self.full_range))
        obs_dts = (
            "2001-02-24",
            "2003-02-24",
            "2007-02-24",
            "2014-02-24",
            "2018-02-24",
            "2020-02-24",
            "2024-02-24",
            "2025-02-24",
        )
        self.assertHolidayName(f"{name} (diperhatikan)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_armed_forces_day(self):
        name = "Hari Angkatan Bersenjata Diraja Brunei"
        self.assertHolidayName(name, (f"{year}-05-31" for year in self.full_range))
        obs_dts = (
            "2002-06-01",
            "2009-06-01",
            "2013-06-01",
            "2015-06-01",
            "2019-06-01",
            "2020-06-01",
            "2024-06-01",
        )
        self.assertHolidayName(f"{name} (diperhatikan)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_sultan_hassanal_bolkiah_birthday(self):
        name = "Hari Keputeraan KDYMM Sultan Brunei"
        self.assertHolidayName(name, (f"{year}-07-15" for year in self.full_range))
        obs_dts = (
            "2001-07-16",
            "2005-07-16",
            "2007-07-16",
            "2011-07-16",
            "2012-07-16",
            "2016-07-16",
            "2018-07-16",
            "2022-07-16",
        )
        self.assertHolidayName(f"{name} (diperhatikan)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        name = "Hari Natal"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2011-12-26",
            "2015-12-26",
            "2016-12-26",
            "2020-12-26",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (diperhatikan)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_isra_and_miraj(self):
        name = "Israk dan Mikraj"
        self.assertHolidayName(
            name,
            "2020-03-22",
            "2021-03-11",
            "2022-02-28",
            "2023-02-18",
            "2024-02-08",
            "2025-01-27",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2002-10-05",
            "2004-09-13",
            "2012-06-18",
            "2020-03-23",
        )
        self.assertHolidayName(f"{name} (diperhatikan)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_first_day_of_ramadan(self):
        name = "Hari Pertama Berpuasa"
        self.assertHolidayName(
            name,
            "2020-04-24",
            "2021-04-13",
            "2022-04-03",
            "2023-03-23",
            "2024-03-12",
            "2025-03-02",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2014-06-30",
            "2020-04-25",
            "2022-04-04",
            "2025-03-03",
        )
        self.assertHolidayName(f"{name} (diperhatikan)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_anniversary_of_the_relevation_of_the_quran(self):
        name = "Hari Nuzul Al-Quran"
        self.assertHolidayName(
            name,
            "2020-05-10",
            "2021-04-29",
            "2022-04-19",
            "2023-04-08",
            "2024-03-28",
            "2025-03-18",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2010-08-28",
            "2013-07-27",
            "2014-07-16",
            "2020-05-11",
        )
        self.assertHolidayName(f"{name} (diperhatikan)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_fitr(self):
        name = "Hari Raya Aidil Fitri"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2023-04-22",
            "2023-04-23",
            "2023-04-24",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2025-03-31",
            "2025-04-01",
            "2025-04-02",
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 2, range(self.start_year, 2012))
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 3, range(2012, 2033), range(2034, self.end_year)
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 6, 2033)
        obs_dts = (
            "2020-05-27",
            "2021-05-17",
            "2023-04-25",
            "2024-04-13",
        )
        self.assertHolidayName(f"{name} (diperhatikan)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_adha(self):
        name = "Hari Raya Aidil Adha"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-29",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2014-10-06",
            "2017-09-02",
            "2019-08-12",
            "2020-08-01",
        )
        self.assertHolidayName(f"{name} (diperhatikan)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_islamic_new_year(self):
        name = "Awal Tahun Hijrah"
        self.assertHolidayName(
            name,
            "2020-08-20",
            "2021-08-10",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-27",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2017-09-23",
            "2019-09-02",
            "2024-07-08",
            "2025-06-28",
        )
        self.assertHolidayName(f"{name} (diperhatikan)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_prophets_birthday(self):
        name = "Maulidur Rasul"
        self.assertHolidayName(
            name,
            "2020-10-29",
            "2021-10-19",
            "2022-10-08",
            "2023-09-28",
            "2024-09-16",
            "2025-09-05",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2010-02-27",
            "2012-02-06",
            "2017-12-02",
            "2025-09-06",
        )
        self.assertHolidayName(f"{name} (diperhatikan)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

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
