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

from holidays.countries.afghanistan import Afghanistan, AF, AFG
from tests.common import CommonCountryTests


class TestAfghanistan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Afghanistan)

    def test_country_aliases(self):
        self.assertAliases(Afghanistan, AF, AFG)

    def test_2022(self):
        self.assertHoliday(
            "2022-02-15",  # Liberation Day
            "2022-03-20",  # March Equinox
            "2022-04-28",  # Defeat of Mujahideen Day
            "2022-05-01",  # International Workers' Day
            "2022-08-19",  # Independence Day
            "2022-09-09",  # Martyrs' Day
        )

    def test_independence_day(self):
        self.assertHoliday(
            "1919-08-19",
            "1920-08-19",
        )

    def test_labour_day(self):
        self.assertNoHoliday(
            "2021-05-02",
            "2022-05-04",
            "2023-05-02",
        )
        self.assertHoliday(
            "2021-05-01",
            "2022-05-01",
            "2023-05-01",
        )

    def test_islamic_holidays(self):
        # Eid al-Fitr - Feast Festive
        self.assertNoHoliday("2023-04-20")
        self.assertHoliday(
            "2023-04-21",
        )

        # Eid al-Adha - Scarfice Festive
        self.assertNoHoliday(
            "2023-07-02",
            "2024-07-15",
            "2024-07-19",
        )
        self.assertHoliday(
            "2023-06-28",
            "2024-06-16",
        )

        # Ashura
        self.assertNoHoliday("2023-07-29")
        self.assertHoliday("2023-07-28")

        # Mawlid / Prophet's Birthday
        self.assertNoHoliday(
            "2021-10-19",
            "2023-09-28",
        )
        self.assertHoliday(
            "2021-10-18",
            "2023-09-27",
        )

    def test_l10_default(self):
        self.assertLocalizedHolidays(
            ("2022-02-15", "روز آزادی"),  # Liberation Day
            ("2022-02-28", "میلاد پیامبر (estimated)"),  # Prophet's Birthday (estimated)
            ("2022-03-20", "اعتدال مارس"),  # March Equinox
            ("2022-03-21", "نوروز"),  # Nowruz (New Year)
            ("2022-04-02", "اول رمضان (estimated)"),  # First Ramadan (estimated)
            ("2022-04-28", "روز پیروزی افغان‌ها"),  # Victory Day of Afghans
            ("2022-05-01", "روز جهانی کارگر"),  # International Workers' Day
            ("2022-05-02", "عید فطر (estimated)"),  # Eid al-Fitr (estimated)
            ("2022-07-08", "روز عرفه (estimated)"),  # Day of Arafah (estimated)
            ("2022-07-09", "عید قربانی (estimated)"),  # Eid al-Adha (estimated)
            ("2022-08-08", "عاشورا (estimated)"),  # Ashura (estimated)
            ("2022-08-19", "روز استقلال"),  # Independence Day
            ("2022-09-09", "روز شهیدان"),  # Martyrs' Day
            ("2022-10-08", "میلاد پیامبر (estimated)"),  # Prophet's Birthday (estimated)
        )

    def test_l10n_ps(self):
        self.assertLocalizedHolidays(
            ("2022-02-15", "روز آزادی"),  # Liberation Day
            ("2022-02-28", "میلاد پیامبر (estimated)"),  # Prophet's Birthday (estimated)
            ("2022-03-20", "اعتدال مارس"),  # March Equinox
            ("2022-03-21", "نوروز"),  # Nowruz (New Year)
            ("2022-04-02", "اول رمضان (estimated)"),  # First Ramadan (estimated)
            ("2022-04-28", "روز پیروزی افغان‌ها"),  # Victory Day of Afghans
            ("2022-05-01", "روز جهانی کارگر"),  # International Workers' Day
            ("2022-05-02", "عید فطر (estimated)"),  # Eid al-Fitr (estimated)
            ("2022-07-08", "روز عرفه (estimated)"),  # Day of Arafah (estimated)
            ("2022-07-09", "عید قربانی (estimated)"),  # Eid al-Adha (estimated)
            ("2022-08-08", "عاشورا (estimated)"),  # Ashura (estimated)
            ("2022-08-19", "روز استقلال"),  # Independence Day
            ("2022-09-09", "روز شهیدان"),  # Martyrs' Day
            ("2022-10-08", "میلاد پیامبر (estimated)"),  # Prophet's Birthday (estimated)
        )
