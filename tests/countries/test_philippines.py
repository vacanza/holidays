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

from holidays.constants import WORKDAY
from holidays.countries.philippines import Philippines, PH, PHL
from tests.common import CommonCountryTests


class TestPhilippines(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Philippines, years=range(1988, 2050))

    def test_country_aliases(self):
        self.assertAliases(Philippines, PH, PHL)

    def test_no_holidays(self):
        self.assertNoHolidays(Philippines(years=1987))
        self.assertNoHolidays(Philippines(years=2008, categories=WORKDAY))

    def test_special_holidays(self):
        self.assertHoliday(
            # Additional special (non-working) day.
            "2008-12-26",
            "2008-12-29",
            "2009-11-02",
            "2009-12-24",
            "2010-12-24",
            "2012-11-02",
            "2013-11-02",
            "2013-12-24",
            "2014-12-24",
            "2014-12-26",
            "2015-01-02",
            "2015-12-24",
            "2016-01-02",
            "2016-10-31",
            "2016-12-24",
            "2017-01-02",
            "2017-10-31",
            "2018-05-14",
            "2018-11-02",
            "2018-12-24",
            "2019-05-13",
            "2019-11-02",
            "2019-12-24",
            "2020-11-02",
            "2020-12-24",
            "2022-05-09",
            "2022-10-31",
            "2023-01-02",
            "2023-10-30",
            "2023-11-02",
            "2023-12-26",
            "2024-02-09",
            "2024-11-02",
            "2024-12-24",
            "2025-07-27",
            "2025-10-31",
            "2025-12-24",
        )

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1988, 2050)))

    def test_chinese_new_year(self):
        name = "Chinese New Year"
        self.assertHolidayName(
            name,
            "2012-01-23",
            "2013-02-10",
            "2014-01-31",
            "2015-02-19",
            "2016-02-08",
            "2017-01-28",
            "2018-02-16",
            "2019-02-05",
            "2020-01-25",
            "2021-02-12",
            "2022-02-01",
            "2024-02-10",
        )
        self.assertNoHolidayName(name, range(1988, 2012), 2023)

    def test_edsa_revolution(self):
        name = "EDSA People Power Revolution Anniversary"
        self.assertHolidayName(
            name,
            (f"{year}-02-25" for year in range(2018, 2023)),
            "2016-02-25",
            "2023-02-24",
        )
        self.assertHolidayName(
            name,
            Philippines(categories=WORKDAY, years=range(2025, 2050)),
            (f"{year}-02-25" for year in range(2025, 2050)),
        )
        self.assertNoHolidayName(name, range(1988, 2016), 2017, range(2024, 2050))

    def test_maundy_thursday(self):
        name = "Maundy Thursday"
        self.assertHolidayName(
            name,
            "2016-03-24",
            "2017-04-13",
            "2018-03-29",
            "2019-04-18",
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
        )
        self.assertHolidayName(name, range(1988, 2050))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2016-03-25",
            "2017-04-14",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
        )
        self.assertHolidayName(name, range(1988, 2050))

    def test_black_saturday(self):
        name = "Black Saturday"
        self.assertHolidayName(
            name,
            "2016-03-26",
            "2017-04-15",
            "2018-03-31",
            "2019-04-20",
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            "2023-04-08",
            "2024-03-30",
        )
        self.assertHolidayName(name, range(2013, 2050))
        self.assertNoHolidayName(name, range(1988, 2013))

    def test_day_of_valor(self):
        name = "Araw ng Kagitingan"
        years_non_apr_9 = {2008, 2009, 2023}
        self.assertHolidayName(
            name,
            (f"{year}-04-09" for year in set(range(1988, 2050)) - years_non_apr_9),
            "2008-04-07",
            "2009-04-06",
            "2023-04-10",
        )

    def test_labor_day(self):
        self.assertHolidayName("Labor Day", (f"{year}-05-01" for year in range(1988, 2050)))

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(
            name,
            (f"{year}-06-12" for year in (*range(1988, 2007), *range(2011, 2050))),
            "2007-06-11",
            "2008-06-09",
            "2009-06-12",
            "2010-06-14",
        )

    def test_iglesia_ni_cristo(self):
        # 2025 special non-working day is marked as an additional entry for now,
        # not part of this test case.
        name = "Founding Anniversary of Iglesia ni Cristo"
        self.assertHolidayName(
            name,
            Philippines(categories=WORKDAY, years=range(2009, 2050)),
            (f"{year}-07-27" for year in (*range(2009, 2025), *range(2026, 2050))),
        )
        self.assertNoHolidayName(name, range(1988, 2050))

    def test_ninoy_aquino_day(self):
        name = "Ninoy Aquino Day"
        years_non_aug_21 = {2007, 2008, 2010, 2024}
        self.assertHolidayName(
            name,
            (f"{year}-08-21" for year in set(range(2004, 2050)) - years_non_aug_21),
            "2007-08-20",
            "2008-08-18",
            "2010-08-23",
            "2024-08-23",
        )
        self.assertNoHolidayName(name, range(1988, 2004))

    def test_national_heroes_day(self):
        name = "National Heroes Day"
        self.assertHolidayName(
            name,
            "2004-08-29",
            "2005-08-28",
            "2006-08-27",
            "2007-08-27",
            "2008-08-25",
            "2016-08-29",
            "2017-08-28",
            "2018-08-27",
            "2019-08-26",
            "2020-08-31",
            "2021-08-30",
            "2022-08-29",
            "2023-08-28",
            "2024-08-26",
        )
        self.assertHolidayName(name, range(1988, 2050))

    def test_all_saints_day(self):
        self.assertHolidayName("All Saints' Day", (f"{year}-11-01" for year in range(1988, 2050)))

    def test_bonifacio_day(self):
        name = "Bonifacio Day"
        self.assertHolidayName(
            name,
            (f"{year}-11-30" for year in (*range(1988, 2008), *range(2011, 2050))),
            "2008-12-01",
            "2009-11-30",
            "2010-11-29",
        )

    def test_immaculate_conception_day(self):
        name = "Feast of the Immaculate Conception of Mary"
        self.assertHolidayName(name, (f"{year}-12-08" for year in range(2019, 2050)))
        self.assertNoHolidayName(name, range(1988, 2019))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1988, 2050)))

    def test_rizal_day(self):
        name = "Rizal Day"
        self.assertHolidayName(
            name,
            (f"{year}-12-30" for year in (*range(1988, 2010), *range(2011, 2050))),
            "2010-12-27",
        )

    def test_last_day_of_year(self):
        name = "Last Day of the Year"
        self.assertHolidayName(
            name, (f"{year}-12-31" for year in (*range(1988, 2021), *range(2023, 2050)))
        )
        self.assertNoHolidayName(name, 2021, 2022)

    def test_eid_al_fitr(self):
        name = "Eid'l Fitr"
        self.assertHolidayName(
            name,
            "2016-07-07",
            "2017-06-26",
            "2018-06-15",
            "2019-06-05",
            "2020-05-25",
            "2021-05-13",
            "2022-05-03",
            "2023-04-21",
            "2024-04-10",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(set(range(2002, 2050)).issubset(years_found))
        self.assertFalse(set(range(1988, 2002)).intersection(years_found))

    def test_eid_al_adha(self):
        name = "Eid'l Adha"
        self.assertHolidayName(
            name,
            "2016-09-10",
            "2017-09-02",
            "2018-08-21",
            "2019-08-12",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-17",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(set(range(2010, 2050)).issubset(years_found))
        self.assertFalse(set(range(1988, 2010)).intersection(years_found))

    def test_2018(self):
        self.assertHolidays(
            Philippines(years=2018),
            ("2018-01-01", "New Year's Day"),
            ("2018-02-16", "Chinese New Year"),
            ("2018-02-25", "EDSA People Power Revolution Anniversary"),
            ("2018-03-29", "Maundy Thursday"),
            ("2018-03-30", "Good Friday"),
            ("2018-03-31", "Black Saturday"),
            ("2018-04-09", "Araw ng Kagitingan"),
            ("2018-05-01", "Labor Day"),
            ("2018-05-14", "Elections special (non-working) day"),
            ("2018-06-12", "Independence Day"),
            ("2018-06-15", "Eid'l Fitr"),
            ("2018-08-21", "Eid'l Adha; Ninoy Aquino Day"),
            ("2018-08-27", "National Heroes Day"),
            ("2018-11-01", "All Saints' Day"),
            ("2018-11-02", "Additional special (non-working) day"),
            ("2018-11-30", "Bonifacio Day"),
            ("2018-12-24", "Additional special (non-working) day"),
            ("2018-12-25", "Christmas Day"),
            ("2018-12-30", "Rizal Day"),
            ("2018-12-31", "Last Day of the Year"),
        )

    def test_2019(self):
        self.assertHolidays(
            Philippines(years=2019),
            ("2019-01-01", "New Year's Day"),
            ("2019-02-05", "Chinese New Year"),
            ("2019-02-25", "EDSA People Power Revolution Anniversary"),
            ("2019-04-09", "Araw ng Kagitingan"),
            ("2019-04-18", "Maundy Thursday"),
            ("2019-04-19", "Good Friday"),
            ("2019-04-20", "Black Saturday"),
            ("2019-05-01", "Labor Day"),
            ("2019-05-13", "Elections special (non-working) day"),
            ("2019-06-05", "Eid'l Fitr"),
            ("2019-06-12", "Independence Day"),
            ("2019-08-12", "Eid'l Adha"),
            ("2019-08-21", "Ninoy Aquino Day"),
            ("2019-08-26", "National Heroes Day"),
            ("2019-11-01", "All Saints' Day"),
            ("2019-11-02", "Additional special (non-working) day"),
            ("2019-11-30", "Bonifacio Day"),
            ("2019-12-08", "Feast of the Immaculate Conception of Mary"),
            ("2019-12-24", "Additional special (non-working) day"),
            ("2019-12-25", "Christmas Day"),
            ("2019-12-30", "Rizal Day"),
            ("2019-12-31", "Last Day of the Year"),
        )

    def test_2020(self):
        self.assertHolidays(
            Philippines(years=2020),
            ("2020-01-01", "New Year's Day"),
            ("2020-01-25", "Chinese New Year"),
            ("2020-02-25", "EDSA People Power Revolution Anniversary"),
            ("2020-04-09", "Araw ng Kagitingan; Maundy Thursday"),
            ("2020-04-10", "Good Friday"),
            ("2020-04-11", "Black Saturday"),
            ("2020-05-01", "Labor Day"),
            ("2020-05-25", "Eid'l Fitr"),
            ("2020-06-12", "Independence Day"),
            ("2020-07-31", "Eid'l Adha"),
            ("2020-08-21", "Ninoy Aquino Day"),
            ("2020-08-31", "National Heroes Day"),
            ("2020-11-01", "All Saints' Day"),
            ("2020-11-02", "Additional special (non-working) day"),
            ("2020-11-30", "Bonifacio Day"),
            ("2020-12-08", "Feast of the Immaculate Conception of Mary"),
            ("2020-12-24", "Additional special (non-working) day"),
            ("2020-12-25", "Christmas Day"),
            ("2020-12-30", "Rizal Day"),
            ("2020-12-31", "Last Day of the Year"),
        )

    def test_2021(self):
        self.assertHolidays(
            Philippines(years=2021),
            ("2021-01-01", "New Year's Day"),
            ("2021-02-12", "Chinese New Year"),
            ("2021-02-25", "EDSA People Power Revolution Anniversary"),
            ("2021-04-01", "Maundy Thursday"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-03", "Black Saturday"),
            ("2021-04-09", "Araw ng Kagitingan"),
            ("2021-05-01", "Labor Day"),
            ("2021-05-13", "Eid'l Fitr"),
            ("2021-06-12", "Independence Day"),
            ("2021-07-20", "Eid'l Adha"),
            ("2021-08-21", "Ninoy Aquino Day"),
            ("2021-08-30", "National Heroes Day"),
            ("2021-11-01", "All Saints' Day"),
            ("2021-11-30", "Bonifacio Day"),
            ("2021-12-08", "Feast of the Immaculate Conception of Mary"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-30", "Rizal Day"),
        )

    def test_2022(self):
        self.assertHolidays(
            Philippines(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-02-01", "Chinese New Year"),
            ("2022-02-25", "EDSA People Power Revolution Anniversary"),
            ("2022-04-09", "Araw ng Kagitingan"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Black Saturday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-03", "Eid'l Fitr"),
            ("2022-05-09", "Elections special (non-working) day"),
            ("2022-06-12", "Independence Day"),
            ("2022-07-09", "Eid'l Adha"),
            ("2022-08-21", "Ninoy Aquino Day"),
            ("2022-08-29", "National Heroes Day"),
            ("2022-10-31", "Additional special (non-working) day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-30", "Bonifacio Day"),
            ("2022-12-08", "Feast of the Immaculate Conception of Mary"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-30", "Rizal Day"),
        )

    def test_2023(self):
        self.assertHolidays(
            Philippines(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "Additional special (non-working) day"),
            ("2023-02-24", "EDSA People Power Revolution Anniversary"),
            ("2023-04-06", "Maundy Thursday"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-08", "Black Saturday"),
            ("2023-04-10", "Araw ng Kagitingan"),
            ("2023-04-21", "Eid'l Fitr"),
            ("2023-05-01", "Labor Day"),
            ("2023-06-12", "Independence Day"),
            ("2023-06-28", "Eid'l Adha"),
            ("2023-08-21", "Ninoy Aquino Day"),
            ("2023-08-28", "National Heroes Day"),
            ("2023-10-30", "Elections special (non-working) day"),
            ("2023-11-01", "All Saints' Day"),
            ("2023-11-02", "Additional special (non-working) day"),
            ("2023-11-30", "Bonifacio Day"),
            ("2023-12-08", "Feast of the Immaculate Conception of Mary"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Additional special (non-working) day"),
            ("2023-12-30", "Rizal Day"),
            ("2023-12-31", "Last Day of the Year"),
        )

    def test_2025(self):
        self.assertHolidays(
            Philippines(years=2025),
            ("2025-01-01", "New Year's Day"),
            ("2025-01-29", "Chinese New Year"),
            ("2025-03-30", "Eid'l Fitr (estimated)"),
            ("2025-04-09", "Araw ng Kagitingan"),
            ("2025-04-17", "Maundy Thursday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-19", "Black Saturday"),
            ("2025-05-01", "Labor Day"),
            ("2025-06-06", "Eid'l Adha (estimated)"),
            ("2025-06-12", "Independence Day"),
            ("2025-07-27", "Additional special (non-working) day"),
            ("2025-08-21", "Ninoy Aquino Day"),
            ("2025-08-25", "National Heroes Day"),
            ("2025-10-31", "All Saints' Day Eve"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-11-30", "Bonifacio Day"),
            ("2025-12-08", "Feast of the Immaculate Conception of Mary"),
            ("2025-12-24", "Christmas Eve"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-30", "Rizal Day"),
            ("2025-12-31", "Last Day of the Year"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-02-09", "Additional special (non-working) day"),
            ("2024-02-10", "Chinese New Year"),
            ("2024-03-28", "Maundy Thursday"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Black Saturday"),
            ("2024-04-09", "Araw ng Kagitingan"),
            ("2024-04-10", "Eid'l Fitr"),
            ("2024-05-01", "Labor Day"),
            ("2024-06-12", "Independence Day"),
            ("2024-06-17", "Eid'l Adha"),
            ("2024-07-27", "Founding Anniversary of Iglesia ni Cristo"),
            ("2024-08-23", "Ninoy Aquino Day"),
            ("2024-08-26", "National Heroes Day"),
            ("2024-11-01", "All Saints' Day"),
            ("2024-11-02", "Additional special (non-working) day"),
            ("2024-11-30", "Bonifacio Day"),
            ("2024-12-08", "Feast of the Immaculate Conception of Mary"),
            ("2024-12-24", "Additional special (non-working) day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-30", "Rizal Day"),
            ("2024-12-31", "Last Day of the Year"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-02-09", "Additional special (non-working) day"),
            ("2024-02-10", "Chinese New Year"),
            ("2024-03-28", "Maundy Thursday"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Black Saturday"),
            ("2024-04-09", "Day of Valor"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-05-01", "Labor Day"),
            ("2024-06-12", "Independence Day"),
            ("2024-06-17", "Eid al-Adha"),
            ("2024-07-27", "Founding Anniversary of Iglesia ni Cristo"),
            ("2024-08-23", "Ninoy Aquino Day"),
            ("2024-08-26", "National Heroes Day"),
            ("2024-11-01", "All Saints' Day"),
            ("2024-11-02", "Additional special (non-working) day"),
            ("2024-11-30", "Bonifacio Day"),
            ("2024-12-08", "Immaculate Conception"),
            ("2024-12-24", "Additional special (non-working) day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-30", "Rizal Day"),
            ("2024-12-31", "New Year's Eve"),
        )

    def test_l10n_fil(self):
        self.assertLocalizedHolidays(
            "fil",
            ("2024-01-01", "Bagong Taon"),
            ("2024-02-09", "Karagdagang Espesyal na Araw (Walang Trabajo)"),
            ("2024-02-10", "Bagong Taon ng mga Tsino"),
            ("2024-03-28", "Huwebes Santo"),
            ("2024-03-29", "Biyernes Santo"),
            ("2024-03-30", "Sabado de Gloria"),
            ("2024-04-09", "Araw ng Kagitingan"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-05-01", "Araw ng Paggawa"),
            ("2024-06-12", "Araw ng Kalayaan"),
            ("2024-06-17", "Eid al-Adha"),
            ("2024-07-27", "Anibersaryo ng Pagkatatag ng Iglesia ni Cristo"),
            ("2024-08-23", "Araw ng Kabayanihan ni Ninoy Aquino"),
            ("2024-08-26", "Araw ng mga Bayani"),
            ("2024-11-01", "Araw ng mga Santo"),
            ("2024-11-02", "Karagdagang Espesyal na Araw (Walang Trabajo)"),
            ("2024-11-30", "Araw ng Kabayanihan ni Bonifacio"),
            (
                "2024-12-08",
                "Dakilang Kapistahan ng Kalinis-linisang Paglilihi sa Mahal na Birheng Maria",
            ),
            ("2024-12-24", "Karagdagang Espesyal na Araw (Walang Trabajo)"),
            ("2024-12-25", "Pasko"),
            ("2024-12-30", "Araw ng Kabayanihan ni Rizal"),
            ("2024-12-31", "Bisperas ng Bagong Taon"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2024-01-01", "วันขึ้นปีใหม่"),
            ("2024-02-09", "วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2024-02-10", "วันตรุษจีน"),
            ("2024-03-28", "วันพฤหัสบดีศักดิ์สิทธิ์"),
            ("2024-03-29", "วันศุกร์ประเสริฐ"),
            ("2024-03-30", "วันเสาร์ศักดิ์สิทธิ์"),
            ("2024-04-09", "วันแห่งความกล้าหาญ"),
            ("2024-04-10", "วันอีฎิ้ลฟิตริ"),
            ("2024-05-01", "วันแรงงาน"),
            ("2024-06-12", "วันประกาศเอกราชสาธารณรัฐฟิลิปปินส์"),
            ("2024-06-17", "วันอีดิ้ลอัฎฮา"),
            ("2024-07-27", "วันครบรอบการสถาปนานิกายคริสตจักรของพระคริสต์"),
            ("2024-08-23", "วันนินอย อากีโน"),
            ("2024-08-26", "วันวีรบุรุษแห่งชาติ"),
            ("2024-11-01", "วันสมโภชนักบุญทั้งหลาย"),
            ("2024-11-02", "วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2024-11-30", "วันโบนีฟาซีโอ"),
            ("2024-12-08", "วันสมโภชแม่พระผู้ปฏิสนธินิรมล"),
            ("2024-12-24", "วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2024-12-25", "วันคริสต์มาส"),
            ("2024-12-30", "วันรีซัล"),
            ("2024-12-31", "วันสิ้นปี"),
        )
