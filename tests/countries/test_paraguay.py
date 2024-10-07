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

from holidays.constants import GOVERNMENT
from holidays.countries.paraguay import Paraguay, PY, PRY
from tests.common import CommonCountryTests


class TestParaguay(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Paraguay, years=range(1990, 2050), years_non_observed=range(2000, 2025))

    def test_country_aliases(self):
        self.assertAliases(Paraguay, PY, PRY)

    def test_new_years_day(self):
        self.assertHolidayName("Año Nuevo", (f"{year}-01-01" for year in range(1990, 2050)))
        self.assertNoNonObservedHoliday(
            "2005-01-01",
            "2006-01-01",
            "2011-01-01",
            "2012-01-01",
            "2017-01-01",
            "2022-01-01",
            "2023-01-01",
        )

    def test_patriots_day(self):
        name = "Día de los Héroes de la Patria"
        years_excluded = {2013, 2016, 2018, 2022}
        self.assertHolidayName(
            name, (f"{year}-03-01" for year in set(range(1990, 2050)).difference(years_excluded))
        )
        self.assertNoHolidayName(name, (f"{year}-03-01" for year in years_excluded))
        self.assertHolidayName(
            name,
            "2013-03-04",
            "2016-02-29",
            "2018-02-26",
            "2022-02-28",
        )

    def test_easter(self):
        self.assertHolidayName(
            "Jueves Santo",
            "2019-04-18",
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
        )

        self.assertHolidayName(
            "Viernes Santo",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )

        dt = (
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
        )
        self.assertHolidayName("Domingo de Resurrección", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_labor_day(self):
        self.assertHolidayName(
            "Día del Trabajador", (f"{year}-05-01" for year in range(1990, 2050))
        )
        self.assertNoNonObservedHoliday(
            "2004-05-01",
            "2005-05-01",
            "2010-05-01",
            "2011-05-01",
            "2016-05-01",
            "2021-05-01",
            "2022-05-01",
        )

    def test_independence_day(self):
        name = "Día de la Independencia Nacional"
        self.assertHolidayName(name, (f"{year}-05-15" for year in range(1990, 2050)))
        self.assertHolidayName(name, (f"{year}-05-14" for year in range(2012, 2050)))
        self.assertNoHolidayName(name, (f"{year}-05-14" for year in range(1990, 2012)))
        self.assertNoNonObservedHoliday(
            "2004-05-15",
            "2005-05-15",
            "2010-05-15",
            "2011-05-15",
            "2016-05-14",
            "2016-05-15",
            "2017-05-14",
            "2022-05-14",
            "2022-05-15",
            "2023-05-14",
        )

    def test_chaco_armistice_day(self):
        name = "Día de la Paz del Chaco"
        years_excluded = {2014, 2018}
        self.assertHolidayName(
            name, (f"{year}-06-12" for year in set(range(1990, 2050)).difference(years_excluded))
        )
        self.assertNoHolidayName(name, (f"{year}-06-12" for year in years_excluded))
        self.assertHolidayName(
            name,
            "2014-06-16",
            "2018-06-11",
        )
        self.assertNoNonObservedHoliday(
            "2004-06-12",
            "2005-06-12",
            "2010-06-12",
            "2011-06-12",
            "2016-06-12",
            "2021-06-12",
            "2022-06-12",
        )

    def test_asuncion_foundations_day(self):
        self.assertHolidayName(
            "Día de la Fundación de Asunción", (f"{year}-08-15" for year in range(1990, 2050))
        )
        self.assertNoNonObservedHoliday(
            "2004-08-15",
            "2009-08-15",
            "2010-08-15",
            "2015-08-15",
            "2020-08-15",
            "2021-08-15",
        )

    def test_boqueron_battle_day(self):
        name = "Día de la Batalla de Boquerón"
        years_excluded = {2015, 2016, 2017, 2021, 2022}
        self.assertHolidayName(
            name, (f"{year}-09-29" for year in set(range(2000, 2050)).difference(years_excluded))
        )
        self.assertNoHolidayName(name, (f"{year}-09-29" for year in years_excluded))
        self.assertNoHolidayName(name, (f"{year}-09-29" for year in range(1990, 2000)))
        self.assertHolidayName(
            name,
            "2015-09-28",
            "2016-10-03",
            "2017-10-02",
            "2021-09-27",
            "2022-10-03",
        )
        self.assertNoNonObservedHoliday(
            "2001-09-29",
            "2002-09-29",
            "2007-09-29",
            "2012-09-29",
            "2013-09-29",
            "2018-09-29",
            "2019-09-29",
            "2024-09-29",
        )

    def test_caacupe_virgin_day(self):
        self.assertHolidayName(
            "Día de la Virgen de Caacupé", (f"{year}-12-08" for year in range(1990, 2050))
        )
        self.assertNoNonObservedHoliday(
            "2001-12-08",
            "2002-12-08",
            "2007-12-08",
            "2012-12-08",
            "2013-12-08",
            "2018-12-08",
            "2019-12-08",
            "2024-12-08",
        )

    def test_special_public_holidays(self):
        self.assertHoliday(
            "2007-01-29",
            "2009-09-10",
            "2010-06-14",
            "2011-04-19",
            "2011-05-14",
            "2011-05-16",
            "2013-08-14",
            "2015-07-10",
        )

    def test_special_government_holidays(self):
        self.assertHoliday(
            Paraguay(categories=GOVERNMENT, years=range(2010, 2023)),
            "2010-12-24",
            "2010-12-31",
            "2011-04-20",
            "2011-12-23",
            "2011-12-30",
            "2012-04-04",
            "2012-12-24",
            "2012-12-31",
            "2013-03-27",
            "2014-04-16",
            "2014-12-24",
            "2014-12-31",
            "2015-04-01",
            "2015-12-24",
            "2015-12-31",
            "2016-03-23",
            "2017-03-28",
            "2018-12-24",
            "2018-12-31",
            "2019-04-17",
            "2019-12-24",
            "2019-12-31",
            "2020-04-08",
            "2021-12-24",
            "2021-12-31",
            "2022-04-13",
            "2022-05-02",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-02-28", "Día de los Héroes de la Patria"),
            ("2022-04-13", "Asueto de la Administración Pública"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-04-17", "Domingo de Resurrección"),
            ("2022-05-01", "Día del Trabajador"),
            ("2022-05-02", "Asueto de la Administración Pública"),
            ("2022-05-14", "Día de la Independencia Nacional"),
            ("2022-05-15", "Día de la Independencia Nacional"),
            ("2022-06-12", "Día de la Paz del Chaco"),
            ("2022-08-15", "Día de la Fundación de Asunción"),
            ("2022-10-03", "Día de la Batalla de Boquerón"),
            ("2022-12-08", "Día de la Virgen de Caacupé"),
            ("2022-12-25", "Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-02-28", "Patriots Day"),
            ("2022-04-13", "Public sector holiday"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Public sector holiday"),
            ("2022-05-14", "Independence Day"),
            ("2022-05-15", "Independence Day"),
            ("2022-06-12", "Chaco Armistice Day"),
            ("2022-08-15", "Asuncion Foundation's Day"),
            ("2022-10-03", "Boqueron Battle Day"),
            ("2022-12-08", "Caacupe Virgin Day"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-02-28", "День національних героїв"),
            ("2022-04-13", "Вихідний державних установ"),
            ("2022-04-14", "Великий четвер"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-05-01", "День трудящих"),
            ("2022-05-02", "Вихідний державних установ"),
            ("2022-05-14", "День незалежності"),
            ("2022-05-15", "День незалежності"),
            ("2022-06-12", "День мирного договору в Чако"),
            ("2022-08-15", "День заснування Асунсьйона"),
            ("2022-10-03", "День битви за Бокерон"),
            ("2022-12-08", "Успіння Пресвятої Богородиці"),
            ("2022-12-25", "Різдво Христове"),
        )
