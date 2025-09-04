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

from holidays.countries.belarus import Belarus, BY, BLR
from tests.common import CommonCountryTests, WorkingDayTests


class TestBelarus(CommonCountryTests, WorkingDayTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(BY.start_year, 2050)
        super().setUpClass(Belarus, years=cls.full_range)

    def test_country_aliases(self):
        self.assertAliases(Belarus, BY, BLR)

    def test_no_holidays(self):
        self.assertNoHolidays(
            Belarus(categories=Belarus.supported_categories, years=BY.start_year - 1)
        )

    def test_public_2018(self):
        # http://calendar.by/procal.php?year=2018
        # https://www.officeholidays.com/countries/belarus/index.php
        self.assertHolidays(
            Belarus(years=2018),
            ("2018-01-01", "Новы год"),
            ("2018-01-02", "Выходны (перанесены з 20.01.2018)"),
            ("2018-01-07", "Нараджэнне Хрыстова (праваслаўнае Раство)"),
            ("2018-03-08", "Дзень жанчын"),
            ("2018-03-09", "Выходны (перанесены з 03.03.2018)"),
            ("2018-04-01", "Каталiцкi Вялiкдзень"),
            ("2018-04-08", "Праваслаўны Вялiкдзень"),
            ("2018-04-16", "Выходны (перанесены з 14.04.2018)"),
            ("2018-04-17", "Радаўніца"),
            ("2018-04-30", "Выходны (перанесены з 28.04.2018)"),
            ("2018-05-01", "Свята працы"),
            ("2018-05-09", "Дзень Перамогі"),
            ("2018-07-02", "Выходны (перанесены з 07.07.2018)"),
            ("2018-07-03", "Дзень Незалежнасці Рэспублікі Беларусь (Дзень Рэспублікі)"),
            ("2018-11-07", "Дзень Кастрычніцкай рэвалюцыі"),
            ("2018-12-24", "Выходны (перанесены з 22.12.2018)"),
            ("2018-12-25", "Нараджэнне Хрыстова (каталіцкае Раство)"),
            ("2018-12-31", "Выходны (перанесены з 29.12.2018)"),
        )

    def test_constitution_day(self):
        name = "Дзень Канстытуцыі"

        self.assertWorkdayHolidayName(name, (f"{year}-03-15" for year in range(1999, 2050)))
        self.assertNoWorkdayHolidayName(name, range(BY.start_year, 1995))
        self.assertHolidayName(name, (f"{year}-03-15" for year in range(1995, 1999)))
        self.assertNoHolidayName(
            name,
            (f"{year}-03-15" for year in range(BY.start_year, 1995)),
            (f"{year}-03-15" for year in range(1999, 2050)),
        )

    def test_day_of_unity_of_the_peoples_of_belarus_and_russia(self):
        name = "Дзень яднання народаў Беларусі і Расіі"

        self.assertWorkdayHolidayName(name, (f"{year}-04-02" for year in range(1996, 2050)))
        self.assertNoWorkdayHolidayName(name, range(BY.start_year, 1996))
        self.assertNoHolidayName(name)

    def test_national_symbol_day(self):
        name = "Дзень Дзяржаўнага сцяга, Дзяржаўнага герба і Дзяржаўнага гімна Рэспублікі Беларусь"

        self.assertWorkdayHolidayName(
            name,
            "2012-05-13",
            "2013-05-12",
            "2014-05-11",
            "2015-05-10",
            "2016-05-08",
            "2017-05-14",
            "2018-05-13",
            "2019-05-12",
            "2020-05-10",
            "2021-05-09",
            "2022-05-08",
            "2023-05-14",
            "2024-05-12",
            "2025-05-11",
            "2026-05-10",
            "2027-05-09",
            "2028-05-14",
            "2029-05-13",
            "2030-05-12",
        )
        self.assertNoWorkdayHolidayName(name, range(BY.start_year, 1998))
        self.assertNoHolidayName(name)

    def test_day_of_the_republic(self):
        name = "Дзень Незалежнасці Рэспублікі Беларусь (Дзень Рэспублікі)"

        self.assertHolidayName(name, (f"{year}-07-27" for year in range(BY.start_year, 1997)))
        self.assertHolidayName(name, (f"{year}-07-03" for year in range(1997, 2050)))
        self.assertNoHolidayName(name, (f"{year}-07-27" for year in range(1997, 2050)))
        self.assertNoHolidayName(name, (f"{year}-07-03" for year in range(BY.start_year, 1997)))

    def test_day_of_peoples_unity(self):
        name = "Дзень народнага адзінства"

        self.assertWorkdayHolidayName(name, (f"{year}-09-17" for year in range(2021, 2050)))
        self.assertNoWorkdayHolidayName(name, range(BY.start_year, 2021))
        self.assertNoHolidayName(name)

    def test_new_years_day(self):
        name = "Новы год"

        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        self.assertHolidayName(name, (f"{year}-01-02" for year in range(2020, 2050)))
        self.assertNoHolidayName(name, (f"{year}-01-02" for year in range(BY.start_year, 2020)))

    def test_day_of_fatherland_defenders(self):
        name = "Дзень абаронцаў Айчыны і Узброеных Сіл Рэспублікі Беларусь"

        self.assertWorkdayHolidayName(name, (f"{year}-02-23" for year in self.full_range))
        self.assertNoHolidayName(name)

    def test_october_revolution_day(self):
        name = "Дзень Кастрычніцкай рэвалюцыі"

        self.assertHolidayName(name, (f"{year}-11-07" for year in range(1995, 2050)))
        self.assertNoHolidayName(name, range(BY.start_year, 1995))

    def test_catholic_easter(self):
        name = "Каталiцкi Вялiкдзень"

        # https://calendar.by/content.php?id=19
        dt = (
            "2012-04-08",
            "2013-03-31",
            "2014-04-20",
            "2015-04-05",
            "2016-03-27",
            "2017-04-16",
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
            "2026-04-05",
            "2027-03-28",
            "2028-04-16",
            "2029-04-01",
            "2030-04-21",
        )
        self.assertHolidayName(name, dt)
        self.assertNoHolidayName(name, BY.start_year)

    def test_orthodox_easter(self):
        name = "Праваслаўны Вялiкдзень"

        # https://calendar.by/content.php?id=19
        dt = (
            "2012-04-15",
            "2013-05-05",
            "2014-04-20",
            "2015-04-12",
            "2016-05-01",
            "2017-04-16",
            "2018-04-08",
            "2019-04-28",
            "2020-04-19",
            "2021-05-02",
            "2022-04-24",
            "2023-04-16",
            "2024-05-05",
            "2025-04-20",
            "2026-04-12",
            "2027-05-02",
            "2028-04-16",
            "2029-04-08",
            "2030-04-28",
        )
        self.assertHolidayName(name, dt)
        self.assertNoHolidayName(name, BY.start_year)

    def test_radunitsa(self):
        # https://calendar.by/content.php?id=20
        self.assertHolidayName(
            "Радаўніца",
            "2012-04-24",
            "2013-05-14",
            "2014-04-29",
            "2015-04-21",
            "2016-05-10",
            "2017-04-25",
            "2018-04-17",
            "2019-05-07",
            "2020-04-28",
            "2021-05-11",
            "2022-05-03",
            "2023-04-25",
            "2024-05-14",
            "2025-04-29",
            "2026-04-21",
            "2027-05-11",
            "2028-04-25",
            "2029-04-17",
            "2030-05-07",
        )

    def test_dzyady(self):
        name = "Дзень памяці"

        self.assertWorkdayHolidayName(name, (f"{year}-11-02" for year in range(1998, 2050)))
        self.assertNoWorkdayHolidayName(name, range(BY.start_year, 1998))
        self.assertHolidayName(name, (f"{year}-11-02" for year in range(1992, 1998)))
        self.assertNoHolidayName(name, BY.start_year, range(1998, 2050))

    def test_substituted_holidays(self):
        self.assertHoliday(
            "1998-01-02",
            "1998-04-27",
            "1999-01-08",
            "1999-04-19",
            "2000-05-08",
            "2000-11-06",
            "2001-01-02",
            "2001-03-09",
            "2001-04-23",
            "2001-04-30",
            "2001-07-02",
            "2001-12-24",
            "2001-12-31",
            "2002-01-02",
            "2002-05-10",
            "2002-11-08",
            "2003-01-06",
            "2003-05-05",
            "2004-01-02",
            "2004-01-05",
            "2004-01-06",
            "2004-04-19",
            "2005-03-07",
            "2006-01-02",
            "2006-05-08",
            "2006-11-06",
            "2007-01-02",
            "2007-03-09",
            "2007-04-16",
            "2007-04-30",
            "2007-07-02",
            "2007-12-24",
            "2007-12-31",
            "2008-01-02",
            "2008-05-05",
            "2008-07-04",
            "2008-12-26",
            "2009-01-02",
            "2009-04-27",
            "2010-01-08",
            "2010-04-12",
            "2010-05-10",
            "2011-03-07",
            "2011-05-02",
            "2012-03-09",
            "2012-04-23",
            "2012-07-02",
            "2012-12-24",
            "2012-12-31",
            "2013-01-02",
            "2013-05-10",
            "2014-01-02",
            "2014-01-06",
            "2014-04-30",
            "2014-07-04",
            "2014-12-26",
            "2015-01-02",
            "2015-04-20",
            "2016-01-08",
            "2016-03-07",
            "2017-01-02",
            "2017-04-24",
            "2017-05-08",
            "2017-11-06",
            "2018-01-02",
            "2018-03-09",
            "2018-04-16",
            "2018-04-30",
            "2018-07-02",
            "2018-12-24",
            "2018-12-31",
            "2019-05-06",
            "2019-05-08",
            "2019-11-08",
            "2020-01-06",
            "2020-04-27",
            "2021-01-08",
            "2021-05-10",
            "2022-03-07",
            "2022-05-02",
            "2023-04-24",
            "2023-05-08",
            "2023-11-06",
            "2024-05-13",
            "2024-11-08",
            "2025-01-06",
            "2025-04-28",
            "2025-07-04",
            "2025-12-26",
        )

    def test_workdays(self):
        self.assertWorkingDay(
            "1998-01-10",
            "1998-04-25",
            "1999-01-16",
            "1999-04-17",
            "2000-05-13",
            "2000-11-11",
            "2001-01-20",
            "2001-03-03",
            "2001-04-21",
            "2001-04-28",
            "2001-07-07",
            "2001-12-22",
            "2001-12-29",
            "2002-01-05",
            "2002-05-18",
            "2002-11-16",
            "2003-01-04",
            "2003-05-03",
            "2004-01-10",
            "2004-01-17",
            "2004-01-31",
            "2004-04-17",
            "2005-03-12",
            "2006-01-21",
            "2006-05-06",
            "2006-11-04",
            "2006-12-30",
            "2007-03-17",
            "2007-04-14",
            "2007-05-05",
            "2007-07-07",
            "2007-12-22",
            "2007-12-29",
            "2008-01-12",
            "2008-05-03",
            "2008-06-28",
            "2008-12-20",
            "2009-01-10",
            "2009-04-25",
            "2010-01-23",
            "2010-04-17",
            "2010-05-15",
            "2011-03-12",
            "2011-05-14",
            "2012-03-11",
            "2012-04-28",
            "2012-06-30",
            "2012-12-22",
            "2012-12-29",
            "2013-01-05",
            "2013-05-18",
            "2014-01-04",
            "2014-01-11",
            "2014-05-03",
            "2014-07-12",
            "2014-12-20",
            "2015-01-10",
            "2015-04-25",
            "2016-01-16",
            "2016-03-05",
            "2017-01-21",
            "2017-04-29",
            "2017-05-06",
            "2017-11-04",
            "2018-01-20",
            "2018-03-03",
            "2018-04-14",
            "2018-04-28",
            "2018-07-07",
            "2018-12-22",
            "2018-12-29",
            "2019-05-04",
            "2019-05-11",
            "2019-11-16",
            "2020-01-04",
            "2020-04-04",
            "2021-01-16",
            "2021-05-15",
            "2022-03-12",
            "2022-05-14",
            "2023-04-29",
            "2023-05-13",
            "2023-11-11",
            "2024-05-18",
            "2024-11-16",
            "2025-01-11",
            "2025-04-26",
            "2025-07-12",
            "2025-12-20",
        )

        for year, dts in {
            2006: (
                "2006-01-21",
                "2006-05-06",
                "2006-11-04",
                "2006-12-30",
            ),
        }.items():
            self.assertWorkingDay(Belarus(years=year), dts)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новы год"),
            ("2022-01-02", "Новы год"),
            ("2022-01-07", "Нараджэнне Хрыстова (праваслаўнае Раство)"),
            ("2022-02-23", "Дзень абаронцаў Айчыны і Узброеных Сіл Рэспублікі Беларусь"),
            ("2022-03-07", "Выходны (перанесены з 12.03.2022)"),
            ("2022-03-08", "Дзень жанчын"),
            ("2022-03-15", "Дзень Канстытуцыі"),
            ("2022-04-02", "Дзень яднання народаў Беларусі і Расіі"),
            ("2022-04-17", "Каталiцкi Вялiкдзень"),
            ("2022-04-24", "Праваслаўны Вялiкдзень"),
            ("2022-05-01", "Свята працы"),
            ("2022-05-02", "Выходны (перанесены з 14.05.2022)"),
            ("2022-05-03", "Радаўніца"),
            (
                "2022-05-08",
                (
                    "Дзень Дзяржаўнага сцяга, Дзяржаўнага герба і "
                    "Дзяржаўнага гімна Рэспублікі Беларусь"
                ),
            ),
            ("2022-05-09", "Дзень Перамогі"),
            ("2022-07-03", "Дзень Незалежнасці Рэспублікі Беларусь (Дзень Рэспублікі)"),
            ("2022-09-17", "Дзень народнага адзінства"),
            ("2022-11-02", "Дзень памяці"),
            ("2022-11-07", "Дзень Кастрычніцкай рэвалюцыі"),
            ("2022-12-25", "Нараджэнне Хрыстова (каталіцкае Раство)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-07", "Orthodox Christmas Day"),
            (
                "2022-02-23",
                (
                    "Day of the Fatherland's Defenders and "
                    "the Armed Forces of the Republic of Belarus"
                ),
            ),
            ("2022-03-07", "Day off (substituted from 03/12/2022)"),
            ("2022-03-08", "Women's Day"),
            ("2022-03-15", "Constitution Day"),
            ("2022-04-02", "Day of Unity of the Peoples of Belarus and Russia"),
            ("2022-04-17", "Catholic Easter"),
            ("2022-04-24", "Orthodox Easter"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Day off (substituted from 05/14/2022)"),
            ("2022-05-03", "Radunitsa (Day of Rejoicing)"),
            (
                "2022-05-08",
                (
                    "Day of the National Coat of Arms of the Republic of Belarus, "
                    "the National Flag of the Republic of Belarus and "
                    "the National Anthem of the Republic of Belarus"
                ),
            ),
            ("2022-05-09", "Victory Day"),
            ("2022-07-03", "Independence Day of the Republic of Belarus (Day of the Republic)"),
            ("2022-09-17", "Day of People's Unity"),
            ("2022-11-02", "Dzyady (All Souls' Day)"),
            ("2022-11-07", "October Revolution Day"),
            ("2022-12-25", "Catholic Christmas Day"),
        )

    def test_l10n_ru(self):
        self.assertLocalizedHolidays(
            "ru",
            ("2022-01-01", "Новый год"),
            ("2022-01-02", "Новый год"),
            ("2022-01-07", "Рождество Христово (православное Рождество)"),
            ("2022-02-23", "День защитников Отечества и Вооруженных Сил Республики Беларусь"),
            ("2022-03-07", "Выходной (перенесено с 12.03.2022)"),
            ("2022-03-08", "День женщин"),
            ("2022-03-15", "День Конституции"),
            ("2022-04-02", "День единения народов Беларуси и России"),
            ("2022-04-17", "Католическая Пасха"),
            ("2022-04-24", "Православная Пасха"),
            ("2022-05-01", "Праздник труда"),
            ("2022-05-02", "Выходной (перенесено с 14.05.2022)"),
            ("2022-05-03", "Радуница"),
            (
                "2022-05-08",
                (
                    "День Государственного флага, Государственного герба и "
                    "Государственного гимна Республики Беларусь"
                ),
            ),
            ("2022-05-09", "День Победы"),
            ("2022-07-03", "День Независимости Республики Беларусь (День Республики)"),
            ("2022-09-17", "День народного единства"),
            ("2022-11-02", "День памяти"),
            ("2022-11-07", "День Октябрьской революции"),
            ("2022-12-25", "Рождество Христово (католическое Рождество)"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-02", "วันขึ้นปีใหม่"),
            ("2022-01-07", "วันประสูติของพระคริสต์ (คริสต์มาสนิกายออร์โธดอกซ์)"),
            ("2022-02-23", "วันพิทักษ์ปิตุภูมิและกองทัพแห่งสาธารณรัฐเบลารุส"),
            ("2022-03-07", "วันหยุด (แทน 12/03/2022)"),
            ("2022-03-08", "วันสตรี"),
            ("2022-03-15", "วันรัฐธรรมนูญ"),
            ("2022-04-02", "วันแห่งความสามัคคีของประชาชนเบลารุสและรัสเซีย"),
            ("2022-04-17", "วันอีสเตอร์นิกายคาทอลิก"),
            ("2022-04-24", "วันอีสเตอร์นิกายออร์โธดอกซ์"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-02", "วันหยุด (แทน 14/05/2022)"),
            ("2022-05-03", "ราเดาว์นิตซา (วันแห่งความยินดี)"),
            ("2022-05-08", "วันธงชาติ ตราแผ่นดิน และเพลงชาติแห่งสาธารณรัฐเบลารุส"),
            ("2022-05-09", "วันแห่งชัยชนะ"),
            ("2022-07-03", "วันประกาศอิสรภาพแห่งสาธารณรัฐเบลารุส (วันสาธารณรัฐ)"),
            ("2022-09-17", "วันแห่งความสามัคคีของประชาชน"),
            ("2022-11-02", "ดียาดี (วันภาวนาอุทิศแด่ผู้ล่วงลับ)"),
            ("2022-11-07", "วันครบรอบการปฏิวัติเดือนตุลาคม"),
            ("2022-12-25", "วันประสูติของพระคริสต์ (คริสต์มาสนิกายคาทอลิก)"),
        )
