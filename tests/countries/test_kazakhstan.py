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

from holidays.countries.kazakhstan import Kazakhstan, KZ, KAZ
from tests.common import CommonCountryTests


class TestKazakhstan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Kazakhstan, years=range(1991, 2050))

    def test_country_aliases(self):
        self.assertAliases(Kazakhstan, KZ, KAZ)

    def test_no_holidays(self):
        self.assertNoHolidays(Kazakhstan(years=1990))

    def test_new_year(self):
        name = "Жаңа жыл"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1991, 2050)))
        self.assertHolidayName(name, (f"{year}-01-02" for year in range(1991, 2050)))

    def test_christmas(self):
        name = "Православиелік Рождество"
        self.assertHolidayName(name, (f"{year}-01-07" for year in range(2006, 2050)))
        self.assertNoHoliday(f"{year}-01-07" for year in range(1991, 2006))
        self.assertNoHolidayName(name, range(1991, 2006))

    def test_womens_day(self):
        self.assertHolidayName(
            "Халықаралық әйелдер күні", (f"{year}-03-08" for year in range(1991, 2050))
        )

    def test_nauryz(self):
        name = "Наурыз мейрамы"
        for year in range(2010, 2050):
            self.assertHolidayName(name, f"{year}-03-21", f"{year}-03-22", f"{year}-03-23")
        self.assertNoHolidayName(name, range(1991, 2002))
        for year in set(range(2002, 2010)) - {2005, 2007}:
            self.assertNoNonObservedHoliday(
                Kazakhstan(observed=False, years=year),
                f"{year}-03-21",
                f"{year}-03-23",
            )

    def test_solidarity_day(self):
        self.assertHolidayName(
            "Қазақстан халқының бірлігі мерекесі", (f"{year}-05-01" for year in range(1991, 2050))
        )

    def test_defenders_day(self):
        name = "Отан Қорғаушы күні"
        self.assertHolidayName(name, (f"{year}-05-07" for year in range(2013, 2050)))
        self.assertNoHoliday(f"{year}-05-07" for year in range(1991, 2013))
        self.assertNoHolidayName(name, range(1991, 2013))

    def test_victory_day(self):
        self.assertHolidayName("Жеңіс күні", (f"{year}-05-09" for year in range(1991, 2050)))

    def test_capital_day(self):
        name = "Астана күні"
        self.assertHolidayName(name, (f"{year}-07-06" for year in range(2009, 2050)))
        self.assertNoHoliday(f"{year}-07-06" for year in range(1991, 2009))
        self.assertNoHolidayName(name, range(1991, 2009))

    def test_constitution_day(self):
        name = "Қазақстан Республикасының Конституциясы күні"
        self.assertHolidayName(name, (f"{year}-08-30" for year in range(1996, 2050)))
        self.assertNoHoliday(f"{year}-08-30" for year in range(1991, 1996))
        self.assertNoHolidayName(name, range(1991, 1996))

    def test_republic_day(self):
        name = "Республика күні"
        self.assertHolidayName(name, (f"{year}-10-25" for year in range(1994, 2009)))
        self.assertHolidayName(name, (f"{year}-10-25" for year in range(2022, 2050)))
        self.assertNoHoliday(f"{year}-10-25" for year in range(1991, 1994))
        self.assertNoHoliday(f"{year}-10-25" for year in range(2009, 2022))
        self.assertNoHolidayName(name, range(1991, 1994), range(2009, 2022))

    def test_first_president_day(self):
        name = "Қазақстан Республикасының Тұңғыш Президенті күні"
        self.assertHolidayName(name, (f"{year}-12-01" for year in range(2012, 2022)))
        self.assertNoHoliday(f"{year}-12-01" for year in range(1991, 2012))
        self.assertNoHoliday(f"{year}-12-01" for year in range(2022, 2050))
        self.assertNoHolidayName(name, range(1991, 2012), range(2022, 2050))

    def test_independence_day(self):
        name = "Тəуелсіздік күні"
        self.assertHolidayName(name, (f"{year}-12-16" for year in range(1991, 2050)))
        self.assertHolidayName(name, (f"{year}-12-17" for year in range(2002, 2022)))
        self.assertNoHoliday(f"{year}-12-17" for year in range(1991, 2002))
        self.assertNoNonObservedHoliday(
            Kazakhstan(observed=False, years=range(2022, 2050)),
            (f"{year}-12-17" for year in range(2022, 2050)),
        )

    def test_kurban_ait(self):
        name = "Құрбан айт"
        self.assertHolidayName(
            name,
            "2006-01-10",
            "2007-12-20",
            "2008-12-08",
            "2009-11-27",
            "2010-11-16",
            "2011-11-06",
            "2012-10-26",
            "2013-10-15",
            "2014-10-04",
            "2015-09-24",
            "2016-09-12",
            "2017-09-01",
            "2018-08-21",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
        )

    def test_observed(self):
        observed_holidays = (
            "2012-01-03",
            "2012-12-18",
            "2013-03-25",
            "2013-07-08",
            "2013-12-02",
            "2014-03-10",
            "2014-03-24",
            "2014-03-25",
            "2014-07-07",
            "2014-09-01",
            "2015-03-09",
            "2015-03-24",
            "2015-03-25",
            "2015-05-11",
            "2015-08-31",
            "2016-01-04",
            "2016-05-02",
            "2016-05-10",
            "2016-12-19",
            "2017-01-03",
            "2017-05-08",
            "2017-12-18",
            "2017-12-19",
            "2018-12-03",
            "2018-12-18",
            "2019-03-25",
            "2019-07-08",
            "2019-12-02",
            "2020-03-09",
            "2020-03-24",
            "2020-03-25",
            "2020-08-31",
            "2021-01-04",
            "2021-03-24",
            "2021-05-03",
            "2021-05-10",
            "2022-01-04",
            "2022-05-02",
            "2022-05-10",
            "2023-01-03",
            "2023-05-08",
            "2023-12-18",
            "2024-03-25",
            "2024-07-08",
        )
        self.assertHoliday(observed_holidays)
        self.assertNoNonObservedHoliday(observed_holidays)

    def test_substituted_holidays(self):
        self.assertHoliday(
            "2000-05-08",
            "2001-03-09",
            "2001-03-23",
            "2001-04-30",
            "2001-12-31",
            "2002-05-10",
            "2003-05-02",
            "2003-12-15",
            "2005-03-07",
            "2005-03-21",
            "2005-08-29",
            "2005-10-24",
            "2006-01-11",
            "2006-05-08",
            "2007-03-09",
            "2007-03-23",
            "2007-08-31",
            "2007-10-26",
            "2007-12-31",
            "2008-05-02",
            "2009-12-18",
            "2010-01-08",
            "2010-07-05",
            "2011-03-07",
            "2011-08-29",
            "2012-03-09",
            "2012-04-30",
            "2012-12-31",
            "2013-05-10",
            "2013-10-14",
            "2014-01-03",
            "2014-05-02",
            "2014-05-08",
            "2016-03-07",
            "2017-03-20",
            "2017-07-07",
            "2018-03-09",
            "2018-04-30",
            "2018-05-08",
            "2018-08-31",
            "2018-12-31",
            "2019-05-10",
            "2020-01-03",
            "2020-05-08",
            "2020-12-18",
            "2021-07-05",
            "2022-03-07",
            "2022-08-29",
            "2022-10-24",
            "2023-07-07",
            "2024-05-08",
        )

    def test2022(self):
        self.assertHolidays(
            Kazakhstan(years=2022),
            ("2022-01-01", "Жаңа жыл"),
            ("2022-01-02", "Жаңа жыл"),
            ("2022-01-03", "Жаңа жыл (қайта белгіленген демалыс)"),
            ("2022-01-04", "Жаңа жыл (қайта белгіленген демалыс)"),
            ("2022-01-07", "Православиелік Рождество"),
            ("2022-03-07", "Демалыс күні (05.03.2022 бастап ауыстырылды)"),
            ("2022-03-08", "Халықаралық әйелдер күні"),
            ("2022-03-21", "Наурыз мейрамы"),
            ("2022-03-22", "Наурыз мейрамы"),
            ("2022-03-23", "Наурыз мейрамы"),
            ("2022-05-01", "Қазақстан халқының бірлігі мерекесі"),
            ("2022-05-02", "Қазақстан халқының бірлігі мерекесі (қайта белгіленген демалыс)"),
            ("2022-05-07", "Отан Қорғаушы күні"),
            ("2022-05-09", "Жеңіс күні"),
            ("2022-05-10", "Отан Қорғаушы күні (қайта белгіленген демалыс)"),
            ("2022-07-06", "Астана күні"),
            ("2022-07-09", "Құрбан айт"),
            ("2022-08-29", "Демалыс күні (27.08.2022 бастап ауыстырылды)"),
            ("2022-08-30", "Қазақстан Республикасының Конституциясы күні"),
            ("2022-10-24", "Демалыс күні (22.10.2022 бастап ауыстырылды)"),
            ("2022-10-25", "Республика күні"),
            ("2022-12-16", "Тəуелсіздік күні"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Жаңа жыл"),
            ("2024-01-02", "Жаңа жыл"),
            ("2024-01-07", "Православиелік Рождество"),
            ("2024-03-08", "Халықаралық әйелдер күні"),
            ("2024-03-21", "Наурыз мейрамы"),
            ("2024-03-22", "Наурыз мейрамы"),
            ("2024-03-23", "Наурыз мейрамы"),
            ("2024-03-25", "Наурыз мейрамы (қайта белгіленген демалыс)"),
            ("2024-05-01", "Қазақстан халқының бірлігі мерекесі"),
            ("2024-05-07", "Отан Қорғаушы күні"),
            ("2024-05-08", "Демалыс күні (04.05.2024 бастап ауыстырылды)"),
            ("2024-05-09", "Жеңіс күні"),
            ("2024-06-16", "Құрбан айт"),
            ("2024-07-06", "Астана күні"),
            ("2024-07-08", "Астана күні (қайта белгіленген демалыс)"),
            ("2024-08-30", "Қазақстан Республикасының Конституциясы күні"),
            ("2024-10-25", "Республика күні"),
            ("2024-12-16", "Тəуелсіздік күні"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "New Year's Day"),
            ("2024-01-07", "Orthodox Christmas"),
            ("2024-03-08", "International Women's Day"),
            ("2024-03-21", "Nowruz holiday"),
            ("2024-03-22", "Nowruz holiday"),
            ("2024-03-23", "Nowruz holiday"),
            ("2024-03-25", "Nowruz holiday (observed)"),
            ("2024-05-01", "Kazakhstan's People Solidarity Holiday"),
            ("2024-05-07", "Defender of the Fatherland Day"),
            ("2024-05-08", "Day off (substituted from 05/04/2024)"),
            ("2024-05-09", "Victory Day"),
            ("2024-06-16", "Eid al-Adha"),
            ("2024-07-06", "Capital Day"),
            ("2024-07-08", "Capital Day (observed)"),
            ("2024-08-30", "Constitution Day"),
            ("2024-10-25", "Republic Day"),
            ("2024-12-16", "Independence Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2024-01-01", "Новий рік"),
            ("2024-01-02", "Новий рік"),
            ("2024-01-07", "Православне Різдво"),
            ("2024-03-08", "Міжнародний жіночий день"),
            ("2024-03-21", "Свято Новруз"),
            ("2024-03-22", "Свято Новруз"),
            ("2024-03-23", "Свято Новруз"),
            ("2024-03-25", "Свято Новруз (вихідний)"),
            ("2024-05-01", "Свято єдності народу Казахстану"),
            ("2024-05-07", "День захисника Вітчизни"),
            ("2024-05-08", "Вихідний день (перенесено з 04.05.2024)"),
            ("2024-05-09", "День Перемоги"),
            ("2024-06-16", "Курбан-байрам"),
            ("2024-07-06", "День Столиці"),
            ("2024-07-08", "День Столиці (вихідний)"),
            ("2024-08-30", "День Конституції Республіки Казахстан"),
            ("2024-10-25", "День Республіки"),
            ("2024-12-16", "День незалежності"),
        )
