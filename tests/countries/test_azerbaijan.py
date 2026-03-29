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

from holidays.constants import WORKDAY
from holidays.countries.azerbaijan import Azerbaijan
from tests.common import CommonCountryTests, WorkingDayTests


class TestAzerbaijan(CommonCountryTests, WorkingDayTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(1990, 2073)
        super().setUpClass(Azerbaijan)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(Azerbaijan(categories=WORKDAY, years=range(self.start_year, 1992)))

    def test_special_holidays(self):
        self.assertHoliday(
            "2007-01-03",
            "2018-04-11",
            "2019-12-27",
            "2024-02-07",
            "2025-01-29",
            "2025-03-27",
            "2025-03-28",
            "2072-01-05",
        )

    def test_substituted_holidays(self):
        self.assertHoliday(
            "2011-08-29",
            "2013-01-03",
            "2013-01-04",
            "2014-01-03",
            "2014-01-06",
            "2020-01-03",
            "2020-01-06",
            "2020-03-27",
            "2020-05-27",
            "2021-05-11",
            "2021-05-12",
            "2021-07-19",
            "2022-03-07",
            "2022-11-07",
            "2023-06-27",
            "2023-06-30",
            "2023-11-10",
            "2024-01-04",
            "2024-01-05",
            "2024-04-12",
            "2024-11-12",
            "2024-11-13",
            "2024-12-30",
            "2025-01-03",
            "2025-06-27",
        )

    def test_workdays(self):
        self.assertWorkingDay(
            "2011-08-27",
            "2012-12-29",
            "2012-12-30",
            "2013-12-28",
            "2013-12-29",
            "2019-12-28",
            "2019-12-29",
            "2020-03-29",
            "2020-05-30",
            "2021-05-08",
            "2021-05-16",
            "2021-07-17",
            "2022-03-05",
            "2022-11-05",
            "2023-06-24",
            "2023-06-25",
            "2023-11-04",
            "2023-12-30",
            "2024-01-07",
            "2024-04-06",
            "2024-11-16",
            "2024-11-23",
            "2024-12-28",
            "2024-12-29",
            "2025-06-21",
        )

        for year, dts in {
            2012: (
                "2012-12-29",
                "2012-12-30",
            ),
            2013: (
                "2013-12-28",
                "2013-12-29",
            ),
            2019: (
                "2019-12-28",
                "2019-12-29",
            ),
            2023: ("2023-12-30",),
            2024: ("2024-12-29",),
        }.items():
            self.assertWorkingDay(Azerbaijan(years=year), dts)

    def test_new_years_day(self):
        name = "Yeni il bayramı"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        self.assertHolidayName(name, (f"{year}-01-02" for year in range(2006, self.end_year)))
        self.assertNoHolidayName(name, (f"{year}-01-02" for year in range(self.start_year, 2006)))
        obs_dts = (
            "2021-01-04",
            "2022-01-03",
            "2022-01-04",
            "2023-01-04",
        )
        self.assertHolidayName(f"{name} (müşahidə olunur)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_martyrs_day(self):
        name = "Ümumxalq hüzn günü"
        self.assertHolidayName(name, (f"{year}-01-20" for year in range(2000, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2000))

    def test_womens_day(self):
        name = "Qadınlar günü"
        self.assertHolidayName(name, (f"{year}-03-08" for year in self.full_range))
        obs_dts = (
            "2014-03-10",
            "2015-03-09",
            "2020-03-09",
        )
        self.assertHolidayName(f"{name} (müşahidə olunur)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_spring_festival(self):
        name = "Novruz bayramı"
        self.assertHolidayName(name, (f"{year}-03-20" for year in self.full_range))
        self.assertHolidayName(name, (f"{year}-03-21" for year in self.full_range))
        self.assertHolidayName(name, (f"{year}-03-22" for year in range(2007, self.end_year)))
        self.assertHolidayName(name, (f"{year}-03-23" for year in range(2007, self.end_year)))
        self.assertHolidayName(name, (f"{year}-03-24" for year in range(2007, self.end_year)))
        obs_dts = (
            "2024-03-25",
            "2024-03-26",
            "2025-03-25",
            "2025-03-26",
        )
        self.assertHolidayName(f"{name} (müşahidə olunur)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_victory_over_fascism_day(self):
        name = "Faşizm üzərində qələbə günü"
        self.assertHolidayName(name, (f"{year}-05-09" for year in self.full_range))
        obs_dts = (
            "2010-05-10",
            "2015-05-11",
            "2020-05-11",
            "2021-05-10",
        )
        self.assertHolidayName(f"{name} (müşahidə olunur)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_republic_day(self):
        name_1992 = "Respublika Günü"
        name_2021 = "Müstəqillik Günü"
        self.assertHolidayName(name_1992, (f"{year}-05-28" for year in range(1992, 2021)))
        self.assertHolidayName(name_2021, (f"{year}-05-28" for year in range(2021, self.end_year)))
        self.assertNoHolidayName(
            name_1992, range(self.start_year, 1992), range(2021, self.end_year)
        )
        self.assertNoHolidayName(name_2021, range(self.start_year, 2021))
        obs_dts_1992 = (
            "2006-05-29",
            "2011-05-30",
            "2016-05-30",
            "2017-05-29",
        )
        self.assertHolidayName(f"{name_1992} (müşahidə olunur)", obs_dts_1992)
        obs_dts_2021 = (
            "2022-05-30",
            "2023-05-29",
        )
        self.assertHolidayName(f"{name_2021} (müşahidə olunur)", obs_dts_2021)
        self.assertNoNonObservedHoliday(obs_dts_1992, obs_dts_2021)

    def test_national_liberation_day(self):
        name = "Azərbaycan xalqının milli qurtuluş günü"
        self.assertHolidayName(name, (f"{year}-06-15" for year in range(1997, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1997))
        obs_dts = (
            "2013-06-17",
            "2014-06-16",
            "2019-06-17",
            "2024-06-18",
        )
        self.assertHolidayName(f"{name} (müşahidə olunur)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_armed_forces_day(self):
        name = "Azərbaycan Respublikasının Silahlı Qüvvələri günü"
        self.assertHolidayName(name, (f"{year}-10-09" for year in range(1992, 1998)))
        self.assertHolidayName(name, (f"{year}-06-26" for year in range(1998, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1992))
        obs_dts = (
            "2011-06-27",
            "2016-06-27",
            "2021-06-28",
            "2022-06-27",
        )
        self.assertHolidayName(f"{name} (müşahidə olunur)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_memorial_day(self):
        name = "Anım Günü"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name, (f"{year}-09-27" for year in range(2021, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2021))

    def test_independence_restoration_day(self):
        name_1992 = "Milli Müstəqillik Günü"
        name_2021 = "Müstəqilliyin Bərpası Günü"
        self.assertHolidayName(
            name_1992, (f"{year}-10-18" for year in range(self.start_year, 2006))
        )
        self.assertNoHolidayName(name_1992, range(2006, self.end_year))

        self.assertWorkdayHolidayName(name_1992, (f"{year}-10-18" for year in range(2006, 2021)))
        self.assertWorkdayHolidayName(
            name_2021, (f"{year}-10-18" for year in range(2021, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name_1992, range(2021, self.end_year))
        self.assertNoWorkdayHolidayName(name_2021, range(self.start_year, 2021))

    def test_victory_day(self):
        name = "Zəfər Günü"
        self.assertHolidayName(name, (f"{year}-11-08" for year in range(2021, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2021))
        obs_dts = ("2025-11-10",)
        self.assertHolidayName(f"{name} (müşahidə olunur)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_national_flag_day(self):
        name = "Azərbaycan Respublikasının Dövlət bayrağı günü"
        self.assertHolidayName(name, (f"{year}-11-09" for year in range(2010, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2010))
        obs_dts = (
            "2014-11-10",
            "2019-11-11",
            "2024-11-11",
            "2025-11-11",
        )
        self.assertHolidayName(f"{name} (müşahidə olunur)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_constitution_day(self):
        name = "Konstitusiya Günü"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name, (f"{year}-11-12" for year in range(1996, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 1996))

    def test_revival_day(self):
        name = "Milli Dirçəliş Günü"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name, (f"{year}-11-17" for year in range(1992, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 1992))

    def test_international_azerbaijanis_solidarity_day(self):
        name = "Dünya azərbaycanlılarının həmrəyliyi günü"
        self.assertHolidayName(name, (f"{year}-12-31" for year in range(1993, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1993))
        obs_dts = (
            "2017-01-03",
            "2018-01-03",
            "2023-01-03",
            "2024-01-03",
        )
        self.assertHolidayName(f"{name} (müşahidə olunur)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_fitr(self):
        name = "Ramazan bayrami"
        self.assertHolidayName(
            name,
            "2005-11-03",
            "2006-10-23",
            "2006-10-24",
            "2020-05-24",
            "2020-05-25",
            "2021-05-13",
            "2021-05-14",
            "2022-05-02",
            "2022-05-03",
            "2023-04-21",
            "2023-04-22",
        )
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 1, range(1993, 2000), range(2001, 2006)
        )
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 2, 2000, range(2006, 2033), range(2034, 2065), range(2066, self.end_year)
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 4, 2033, 2065)
        self.assertNoIslamicNoEstimatedHolidayName(name, range(self.start_year, 1993))
        obs_dts = (
            "2018-06-18",
            "2018-06-19",
            "2020-05-26",
            "2023-04-24",
        )
        self.assertHolidayName(f"{name} (müşahidə olunur)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_adha(self):
        name = "Qurban bayrami"
        self.assertHolidayName(
            name,
            "2006-01-10",
            "2006-12-31",
            "2020-07-31",
            "2020-08-01",
            "2021-07-20",
            "2021-07-21",
            "2022-07-09",
            "2022-07-10",
            "2023-06-28",
            "2023-06-29",
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 1, range(1993, 2006))
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 2, 2006, range(2008, 2039), range(2040, 2071)
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 3, 2007, range(2071, self.end_year))
        self.assertIslamicNoEstimatedHolidayNameCount(name, 4, 2039)
        self.assertNoIslamicNoEstimatedHolidayName(name, range(self.start_year, 1993))
        obs_dts = (
            "2022-07-11",
            "2022-07-12",
            "2024-06-19",
            "2025-06-09",
            # Special Cases.
            "2007-01-03",
            "2072-01-05",
        )
        self.assertIslamicNoEstimatedHolidayName(f"{name} (müşahidə olunur)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2021(self):
        self.assertHolidayDatesInYear(
            2021,
            "2021-01-01",
            "2021-01-02",
            "2021-01-04",
            "2021-01-20",
            "2021-03-08",
            "2021-03-20",
            "2021-03-21",
            "2021-03-22",
            "2021-03-23",
            "2021-03-24",
            "2021-03-25",
            "2021-03-26",
            "2021-05-09",
            "2021-05-10",
            "2021-05-11",
            "2021-05-12",
            "2021-05-13",
            "2021-05-14",
            "2021-05-28",
            "2021-06-15",
            "2021-06-26",
            "2021-06-28",
            "2021-07-19",
            "2021-07-20",
            "2021-07-21",
            "2021-11-08",
            "2021-11-09",
            "2021-12-31",
        )

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Yeni il bayramı"),
            ("2022-01-02", "Yeni il bayramı"),
            ("2022-01-03", "Yeni il bayramı (müşahidə olunur)"),
            ("2022-01-04", "Yeni il bayramı (müşahidə olunur)"),
            ("2022-01-20", "Ümumxalq hüzn günü"),
            ("2022-03-07", "İstirahət günü (05.03.2022 ilə əvəz edilmişdir)"),
            ("2022-03-08", "Qadınlar günü"),
            ("2022-03-20", "Novruz bayramı"),
            ("2022-03-21", "Novruz bayramı"),
            ("2022-03-22", "Novruz bayramı"),
            ("2022-03-23", "Novruz bayramı"),
            ("2022-03-24", "Novruz bayramı"),
            ("2022-03-25", "Novruz bayramı (müşahidə olunur)"),
            ("2022-05-02", "Ramazan bayrami"),
            ("2022-05-03", "Ramazan bayrami"),
            ("2022-05-09", "Faşizm üzərində qələbə günü"),
            ("2022-05-28", "Müstəqillik Günü"),
            ("2022-05-30", "Müstəqillik Günü (müşahidə olunur)"),
            ("2022-06-15", "Azərbaycan xalqının milli qurtuluş günü"),
            ("2022-06-26", "Azərbaycan Respublikasının Silahlı Qüvvələri günü"),
            ("2022-06-27", "Azərbaycan Respublikasının Silahlı Qüvvələri günü (müşahidə olunur)"),
            ("2022-07-09", "Qurban bayrami"),
            ("2022-07-10", "Qurban bayrami"),
            ("2022-07-11", "Qurban bayrami (müşahidə olunur)"),
            ("2022-07-12", "Qurban bayrami (müşahidə olunur)"),
            ("2022-11-07", "İstirahət günü (05.11.2022 ilə əvəz edilmişdir)"),
            ("2022-11-08", "Zəfər Günü"),
            ("2022-11-09", "Azərbaycan Respublikasının Dövlət bayrağı günü"),
            ("2022-12-31", "Dünya azərbaycanlılarının həmrəyliyi günü"),
        )

    def test_2022_workday(self):
        self.assertWorkdayHolidaysInYear(
            2022,
            ("2022-09-27", "Anım Günü"),
            ("2022-10-18", "Müstəqilliyin Bərpası Günü"),
            ("2022-11-12", "Konstitusiya Günü"),
            ("2022-11-17", "Milli Dirçəliş Günü"),
        )

    def test_l10n_default(self):
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

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day"),
            ("2023-01-03", "International Azerbaijanis Solidarity Day (observed)"),
            ("2023-01-04", "New Year's Day (observed)"),
            ("2023-01-20", "Martyrs' Day"),
            ("2023-03-08", "Women's Day"),
            ("2023-03-20", "Spring Festival"),
            ("2023-03-21", "Spring Festival"),
            ("2023-03-22", "Spring Festival"),
            ("2023-03-23", "Spring Festival"),
            ("2023-03-24", "Spring Festival"),
            ("2023-04-21", "Eid al-Fitr"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-24", "Eid al-Fitr (observed)"),
            ("2023-05-09", "Victory over Fascism Day"),
            ("2023-05-28", "Independence Day"),
            ("2023-05-29", "Independence Day (observed)"),
            ("2023-06-15", "National Liberation Day"),
            ("2023-06-26", "Armed Forces Day"),
            ("2023-06-27", "Day off (substituted from 06/24/2023)"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-06-30", "Day off (substituted from 06/25/2023)"),
            ("2023-09-27", "Memorial Day"),
            ("2023-10-18", "Independence Restoration Day"),
            ("2023-11-08", "Victory Day"),
            ("2023-11-09", "National Flag Day"),
            ("2023-11-10", "Day off (substituted from 11/04/2023)"),
            ("2023-11-12", "Constitution Day"),
            ("2023-11-17", "National Revival Day"),
            ("2023-12-31", "International Azerbaijanis Solidarity Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2023-01-01", "Новий рік"),
            ("2023-01-02", "Новий рік"),
            ("2023-01-03", "Всесвітній день солідарності азербайджанців (вихідний)"),
            ("2023-01-04", "Новий рік (вихідний)"),
            ("2023-01-20", "День національної скорботи"),
            ("2023-03-08", "Жіночий день"),
            ("2023-03-20", "Свято Новруз"),
            ("2023-03-21", "Свято Новруз"),
            ("2023-03-22", "Свято Новруз"),
            ("2023-03-23", "Свято Новруз"),
            ("2023-03-24", "Свято Новруз"),
            ("2023-04-21", "Рамазан-байрам"),
            ("2023-04-22", "Рамазан-байрам"),
            ("2023-04-24", "Рамазан-байрам (вихідний)"),
            ("2023-05-09", "День перемоги над фашизмом"),
            ("2023-05-28", "День Незалежності"),
            ("2023-05-29", "День Незалежності (вихідний)"),
            ("2023-06-15", "День національного визволення азербайджанського народу"),
            ("2023-06-26", "День Збройних Сил"),
            ("2023-06-27", "Вихідний день (перенесено з 24.06.2023)"),
            ("2023-06-28", "Курбан-байрам"),
            ("2023-06-29", "Курбан-байрам"),
            ("2023-06-30", "Вихідний день (перенесено з 25.06.2023)"),
            ("2023-09-27", "День памʼяті"),
            ("2023-10-18", "День відновлення незалежності"),
            ("2023-11-08", "День Перемоги"),
            ("2023-11-09", "День державного прапора"),
            ("2023-11-10", "Вихідний день (перенесено з 04.11.2023)"),
            ("2023-11-12", "День Конституції"),
            ("2023-11-17", "День національного відродження"),
            ("2023-12-31", "Всесвітній день солідарності азербайджанців"),
        )
