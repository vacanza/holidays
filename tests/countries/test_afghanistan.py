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

from holidays.countries.afghanistan import Afghanistan, AF, AFG
from tests.common import CommonCountryTests


class TestAfghanistan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Afghanistan)

    def test_country_aliases(self):
        self.assertAliases(Afghanistan, AF, AFG)

    def test_no_holidays(self):
        self.assertNoHolidays(Afghanistan(years=self.start_year - 1))

    def test_liberation_day(self):
        name = "روز آزادی"
        self.assertHolidayName(name, (f"{year}-02-15" for year in range(1989, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1989))

    def test_nowruz(self):
        name = "نوروز"
        self.assertHolidayName(
            name,
            "2011-03-21",
            "2012-03-20",
            "2013-03-21",
            "2014-03-21",
            "2015-03-21",
            "2016-03-20",
            "2017-03-21",
            "2018-03-21",
            "2019-03-21",
            "2020-03-20",
        )
        self.assertHolidayName(name, range(self.start_year, 1997), range(2001, 2021))
        self.assertNoHolidayName(name, range(1997, 2001), range(2021, self.end_year))

    def test_victory_of_mujahideen_day(self):
        name = "روز پیروزی مجاهدین"
        self.assertHolidayName(name, (f"{year}-04-28" for year in range(1992, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1992))

    def test_international_workers_day(self):
        name = "روز جهانی کارگر"
        self.assertHolidayName(
            name, (f"{year}-05-01" for year in (*range(1974, 1997), *range(2002, 2022)))
        )
        self.assertNoHolidayName(name, range(1997, 2002), range(2022, self.end_year))

    def test_soviet_victory_day(self):
        name = "روز پیروزی شوروی"
        self.assertHolidayName(name, (f"{year}-05-09" for year in range(1978, 1989)))
        self.assertNoHolidayName(name, range(self.start_year, 1978), range(1989, self.end_year))

    def test_islamic_emirat_victory_day(self):
        name = "روز پیروزی امارت اسلامی"
        self.assertHolidayName(
            name,
            "2022-08-15",
            "2023-08-15",
            "2024-08-14",
        )
        self.assertHolidayName(name, range(2022, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2022))

    def test_american_withdrawal_day(self):
        name = "روز خروج آمریکایی ها"
        self.assertHolidayName(name, (f"{year}-08-31" for year in range(2022, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2022))

    def test_independence_day(self):
        self.assertHolidayName(
            "روز استقلال افغانستان", (f"{year}-08-19" for year in self.full_range)
        )

    def test_martyrs_day(self):
        name = "روز شهیدان"
        self.assertHolidayName(name, (f"{year}-09-09" for year in range(2012, 2021)))
        self.assertNoHolidayName(name, range(self.start_year, 2012), range(2021, self.end_year))

    def test_ashura(self):
        name = "عاشورا"
        self.assertHolidayName(
            name,
            "2014-11-03",
            "2015-10-24",
            "2016-10-12",
            "2017-10-01",
            "2018-09-21",
            "2019-09-10",
            "2020-08-30",
            "2021-08-19",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(1924, 2022))
        self.assertNoIslamicNoEstimatedHolidayName(
            name, range(self.start_year, 1924), range(2022, self.end_year)
        )

    def test_prophets_birthday(self):
        name = "میلاد پیامبر"
        self.assertHolidayName(
            name,
            "2014-01-14",
            "2015-01-03",
            "2015-12-24",
            "2016-12-12",
            "2017-12-01",
            "2018-11-21",
            "2019-11-10",
            "2020-10-29",
            "2021-10-19",
            "2022-10-08",
            "2023-09-27",
            "2024-09-16",
            "2025-09-05",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(1924, self.end_year))
        self.assertNoIslamicNoEstimatedHolidayName(name, range(self.start_year, 1924))

    def test_first_day_of_ramadan(self):
        name = "اول رمضان"
        self.assertHolidayName(
            name,
            "2014-06-29",
            "2015-06-18",
            "2016-06-07",
            "2017-05-27",
            "2018-05-16",
            "2019-05-06",
            "2020-04-24",
            "2021-04-13",
            "2022-04-02",
            "2023-03-23",
            "2024-03-11",
            "2025-03-01",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(1925, self.end_year))
        self.assertNoIslamicNoEstimatedHolidayName(name, range(self.start_year, 1925))

    def test_eid_al_fitr(self):
        name = "عید فطر"
        self.assertHolidayName(
            name,
            "2014-07-29",
            "2014-07-30",
            "2014-07-31",
            "2015-07-18",
            "2015-07-19",
            "2015-07-20",
            "2016-07-07",
            "2016-07-08",
            "2016-07-09",
            "2017-06-26",
            "2017-06-27",
            "2017-06-28",
            "2018-06-15",
            "2018-06-16",
            "2018-06-17",
            "2019-06-04",
            "2019-06-05",
            "2019-06-06",
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2022-05-01",
            "2022-05-02",
            "2022-05-03",
            "2023-04-22",
            "2023-04-23",
            "2023-04-24",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2025-03-30",
            "2025-03-31",
            "2025-04-01",
        )
        years_eid_al_fitr_twice_all = {1935, 1968, 2000, 2033}
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 3, set(range(1925, self.end_year)) - years_eid_al_fitr_twice_all
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 6, years_eid_al_fitr_twice_all)

    def test_arafah_day(self):
        name = "روز عرفه"
        self.assertHolidayName(
            name,
            "2014-10-04",
            "2015-09-22",
            "2016-09-12",
            "2017-09-01",
            "2018-08-21",
            "2019-08-10",
            "2020-07-30",
            "2021-07-19",
            "2022-07-08",
            "2023-06-27",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(1925, self.end_year))
        self.assertNoIslamicNoEstimatedHolidayName(name, range(self.start_year, 1925))

    def test_eid_al_adha(self):
        name = "عید قربانی"
        self.assertHolidayName(
            name,
            "2014-10-05",
            "2014-10-06",
            "2014-10-07",
            "2015-09-23",
            "2015-09-24",
            "2015-09-25",
            "2016-09-13",
            "2016-09-14",
            "2016-09-15",
            "2017-09-02",
            "2017-09-03",
            "2017-09-04",
            "2018-08-22",
            "2018-08-23",
            "2018-08-24",
            "2019-08-11",
            "2019-08-12",
            "2019-08-13",
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2024-06-17",
            "2024-06-18",
            "2024-06-19",
            "2025-06-07",
            "2025-06-08",
            "2025-06-09",
        )
        years_eid_al_adha_twice_all = {1941, 1974, 2039}
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 3, set(range(1925, self.end_year)) - years_eid_al_adha_twice_all - {2006, 2007}
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 4, 2006)
        self.assertIslamicNoEstimatedHolidayNameCount(name, 5, 2007)
        self.assertIslamicNoEstimatedHolidayNameCount(name, 6, years_eid_al_adha_twice_all)
        self.assertNoIslamicNoEstimatedHolidayName(name, range(self.start_year, 1925))

    def test_2021(self):
        self.assertHolidays(
            Afghanistan(years=2021),
            ("2021-02-15", "روز آزادی"),
            ("2021-04-13", "اول رمضان"),
            ("2021-04-28", "روز پیروزی مجاهدین"),
            ("2021-05-01", "روز جهانی کارگر"),
            ("2021-05-13", "عید فطر"),
            ("2021-05-14", "عید فطر"),
            ("2021-05-15", "عید فطر"),
            ("2021-07-19", "روز عرفه"),
            ("2021-07-20", "عید قربانی"),
            ("2021-07-21", "عید قربانی"),
            ("2021-07-22", "عید قربانی"),
            ("2021-08-19", "روز استقلال افغانستان; عاشورا"),
            ("2021-10-19", "میلاد پیامبر"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-02-15", "روز آزادی"),
            ("2022-04-02", "اول رمضان"),
            ("2022-04-28", "روز پیروزی مجاهدین"),
            ("2022-05-01", "عید فطر"),
            ("2022-05-02", "عید فطر"),
            ("2022-05-03", "عید فطر"),
            ("2022-07-08", "روز عرفه"),
            ("2022-07-09", "عید قربانی"),
            ("2022-07-10", "عید قربانی"),
            ("2022-07-11", "عید قربانی"),
            ("2022-08-15", "روز پیروزی امارت اسلامی"),
            ("2022-08-19", "روز استقلال افغانستان"),
            ("2022-08-31", "روز خروج آمریکایی ها"),
            ("2022-10-08", "میلاد پیامبر"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-02-15", "Liberation Day"),
            ("2022-04-02", "First Day of Ramadan"),
            ("2022-04-28", "Mojahedin's Victory Day"),
            ("2022-05-01", "Eid al-Fitr"),
            ("2022-05-02", "Eid al-Fitr"),
            ("2022-05-03", "Eid al-Fitr"),
            ("2022-07-08", "Day of Arafah"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-07-10", "Eid al-Adha"),
            ("2022-07-11", "Eid al-Adha"),
            ("2022-08-15", "Islamic Emirate Victory Day"),
            ("2022-08-19", "Afghanistan Independence Day"),
            ("2022-08-31", "American Withdrawal Day"),
            ("2022-10-08", "Prophet's Birthday"),
        )

    def test_l10n_ps_af(self):
        self.assertLocalizedHolidays(
            "ps_AF",
            ("2022-02-15", "د ازادۍ ورځ"),
            ("2022-04-02", "د روژې لومړۍ نیټه"),
            ("2022-04-28", "مجاهدو د بریا ورځ"),
            ("2022-05-01", "عید فطر"),
            ("2022-05-02", "عید فطر"),
            ("2022-05-03", "عید فطر"),
            ("2022-07-08", "د عرفه ورځ"),
            ("2022-07-09", "عید قربانی"),
            ("2022-07-10", "عید قربانی"),
            ("2022-07-11", "عید قربانی"),
            ("2022-08-15", "د اسلامي امارت د بریا ورځ"),
            ("2022-08-19", "د افغانستان د استقلال ورځ"),
            ("2022-08-31", "د امریکا د وتلو ورځ"),
            ("2022-10-08", "د پیغمبر الله صلی الله علیه وسلم د میلاد ورځ"),
        )
