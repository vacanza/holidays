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
        super().setUpClass(
            Afghanistan, years=range(1919, 2050), years_non_observed=range(1919, 2050)
        )

    def test_country_aliases(self):
        self.assertAliases(Afghanistan, AF, AFG)

    def test_no_holidays(self):
        self.assertNoHolidays(Afghanistan(years=1918))

    def test_2021(self):
        self.assertHolidays(
            Afghanistan(years=2021),
            ("2021-02-15", "روز آزادی"),
            ("2021-04-13", "اول رمضان (برآورد شده)"),
            ("2021-04-28", "روز پیروزی مجاهدین"),
            ("2021-05-01", "روز جهانی کارگر"),
            ("2021-05-13", "عید فطر (برآورد شده)"),
            ("2021-05-14", "عید فطر (برآورد شده)"),
            ("2021-05-15", "عید فطر (برآورد شده)"),
            ("2021-07-19", "روز عرفه (برآورد شده)"),
            ("2021-07-20", "عید قربانی (برآورد شده)"),
            ("2021-07-21", "عید قربانی (برآورد شده)"),
            ("2021-07-22", "عید قربانی (برآورد شده)"),
            ("2021-08-18", "عاشورا (برآورد شده)"),
            ("2021-08-19", "روز استقلال افغانستان"),
            ("2021-09-09", "روز شهیدان"),
            ("2021-10-18", "میلاد پیامبر (برآورد شده)"),
        )

    def test_liberation_day(self):
        name = "روز آزادی"
        self.assertHolidayName(name, (f"{year}-02-15" for year in range(1989, 2050)))
        self.assertNoHolidayName(name, range(1919, 1989))

    def test_nowruz(self):
        name = "نوروز"
        self.assertHolidayName(
            name, (f"{year}-03-21" for year in (*range(1919, 1997), *range(2001, 2021)))
        )
        self.assertNoHolidayName(name, range(1997, 2001), range(2021, 2050))

    def test_victory_of_mujahideen_day(self):
        name = "روز پیروزی مجاهدین"
        self.assertHolidayName(name, (f"{year}-04-28" for year in range(1992, 2050)))
        self.assertNoHolidayName(name, range(1919, 1992))

    def test_international_workers_day(self):
        name = "روز جهانی کارگر"
        self.assertHolidayName(
            name, (f"{year}-05-01" for year in (*range(1974, 1997), *range(2002, 2022)))
        )
        self.assertNoHolidayName(name, range(1997, 2002), range(2022, 2050))

    def test_soviet_victory_day(self):
        name = "روز پیروزی شوروی"
        self.assertHolidayName(name, (f"{year}-05-09" for year in range(1978, 1989)))
        self.assertNoHolidayName(name, range(1919, 1978), (1989, 2050))

    def test_american_withdrawal_day(self):
        name = "روز خروج آمریکایی ها"
        self.assertHolidayName(name, (f"{year}-08-31" for year in range(2022, 2050)))
        self.assertNoHolidayName(name, range(1919, 2022))

    def test_independence_day(self):
        name = "روز استقلال افغانستان"
        self.assertHolidayName(name, (f"{year}-08-19" for year in range(1919, 2050)))

    def test_martyrs_day(self):
        name = "روز شهیدان"
        self.assertHolidayName(name, (f"{year}-09-09" for year in range(2012, 2050)))
        self.assertNoHolidayName(name, range(1919, 2012))

    def test_eid_al_fitr(self):
        self.assertNoHolidayName("روز اول عید فطر", range(1919, 2001))
        self.assertNoHolidayName("روز دوم عید فطر", range(1919, 2001))
        self.assertNoHolidayName("سومین روز عید فطر", range(1919, 2001))

    def test_l10_default(self):
        self.assertLocalizedHolidays(
            ("2022-02-15", "روز آزادی"),
            ("2022-04-02", "اول رمضان (برآورد شده)"),
            ("2022-04-28", "روز پیروزی مجاهدین"),
            ("2022-05-02", "عید فطر (برآورد شده)"),
            ("2022-05-03", "عید فطر (برآورد شده)"),
            ("2022-05-04", "عید فطر (برآورد شده)"),
            ("2022-07-08", "روز عرفه (برآورد شده)"),
            ("2022-07-09", "عید قربانی (برآورد شده)"),
            ("2022-07-10", "عید قربانی (برآورد شده)"),
            ("2022-07-11", "عید قربانی (برآورد شده)"),
            ("2022-08-08", "عاشورا (برآورد شده)"),
            ("2022-08-19", "روز استقلال افغانستان"),
            ("2022-08-31", "روز خروج آمریکایی ها"),
            ("2022-09-09", "روز شهیدان"),
            ("2022-10-08", "میلاد پیامبر (برآورد شده)"),
        )

    def test_l10n_ps_af(self):
        self.assertLocalizedHolidays(
            "ps_AF",
            ("2022-02-15", "د ازادۍ ورځ"),
            ("2022-04-02", "د روژې لومړۍ نیټه (اټکل)"),
            ("2022-04-28", "مجاهدو د بریا ورځ"),
            ("2022-05-02", "عید فطر (اټکل)"),
            ("2022-05-03", "عید فطر (اټکل)"),
            ("2022-05-04", "عید فطر (اټکل)"),
            ("2022-07-08", "د عرفه ورځ (اټکل)"),
            ("2022-07-09", "عید قربانی (اټکل)"),
            ("2022-07-10", "عید قربانی (اټکل)"),
            ("2022-07-11", "عید قربانی (اټکل)"),
            ("2022-08-08", "عاشورا (اټکل)"),
            ("2022-08-19", "د افغانستان د استقلال ورځ"),
            ("2022-08-31", "د امریکا د وتلو ورځ"),
            ("2022-09-09", "د شهیدانو ورځ"),
            ("2022-10-08", "د پیغمبر الله صلی الله علیه وسلم د میلاد ورځ (اټکل)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-02-15", "Liberation Day"),
            ("2022-04-02", "First Day of Ramadan (estimated)"),
            ("2022-04-28", "Mojahedin's Victory Day"),
            ("2022-05-02", "Eid al-Fitr (estimated)"),
            ("2022-05-03", "Eid al-Fitr (estimated)"),
            ("2022-05-04", "Eid al-Fitr (estimated)"),
            ("2022-07-08", "Day of Arafah (estimated)"),
            ("2022-07-09", "Eid al-Adha (estimated)"),
            ("2022-07-10", "Eid al-Adha (estimated)"),
            ("2022-07-11", "Eid al-Adha (estimated)"),
            ("2022-08-08", "Ashura (estimated)"),
            ("2022-08-19", "Afghanistan Independence Day"),
            ("2022-08-31", "The Day of America's Withdrawal"),
            ("2022-09-09", "Martyrs' Day"),
            ("2022-10-08", "Prophet's Birthday (estimated)"),
        )
