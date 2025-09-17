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

from holidays.countries.paraguay import Paraguay, PY, PRY
from tests.common import CommonCountryTests


class TestParaguay(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Paraguay, years_government=range(2010, 2026))

    def test_country_aliases(self):
        self.assertAliases(Paraguay, PY, PRY)

    def test_no_holidays(self):
        self.assertNoHolidays(
            Paraguay(categories=Paraguay.supported_categories, years=self.start_year - 1)
        )

    def test_new_years_day(self):
        self.assertHolidayName("Año Nuevo", (f"{year}-01-01" for year in self.full_range))

    def test_patriots_day(self):
        self.assertHolidayName(
            "Día de los Héroes de la Patria",
            (
                f"{year}-03-01"
                for year in self.full_range
                if year not in {2013, 2016, 2017, 2018, 2019, 2022, 2023, 2025}
            ),
            "2013-03-04",
            "2016-02-29",
            "2017-02-27",
            "2018-02-26",
            "2019-03-04",
            "2022-02-28",
            "2023-02-27",
            "2025-03-03",
        )

    def test_maundy_thursday(self):
        name = "Jueves Santo"
        self.assertHolidayName(
            name,
            "2019-04-18",
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
        )
        self.assertHolidayName(name, self.full_range)

    def test_good_friday(self):
        name = "Viernes Santo"
        self.assertHolidayName(
            name,
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_sunday(self):
        name = "Domingo de Resurrección"
        self.assertHolidayName(
            name,
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        self.assertHolidayName(
            "Día de los Trabajadores", (f"{year}-05-01" for year in self.full_range)
        )

    def test_national_holiday(self):
        name = "Feriado Nacional"
        self.assertHolidayName(name, (f"{year}-05-14" for year in range(2012, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2012))

    def test_independence_day(self):
        self.assertHolidayName(
            "Día de la Independencia Nacional", (f"{year}-05-15" for year in self.full_range)
        )

    def test_chaco_armistice_day(self):
        self.assertHolidayName(
            "Día de la Paz del Chaco",
            (
                f"{year}-06-12"
                for year in self.full_range
                if year not in {2013, 2014, 2018, 2019, 2024, 2025}
            ),
            "2013-06-10",
            "2014-06-16",
            "2018-06-11",
            "2019-06-17",
            "2024-06-10",
            "2025-06-16",
        )

    def test_asuncion_foundations_day(self):
        self.assertHolidayName(
            "Día de la Fundación de Asunción",
            (
                f"{year}-08-15"
                for year in (*range(self.start_year, 2017), *range(2018, self.end_year))
            ),
            "2017-08-14",
        )

    def test_boqueron_battle_day(self):
        name = "Día de la Batalla de Boquerón"
        self.assertHolidayName(
            name,
            (
                f"{year}-09-29"
                for year in range(1995, self.end_year)
                if year not in {2015, 2016, 2017, 2021, 2022, 2024}
            ),
            "2015-09-28",
            "2016-10-03",
            "2017-10-02",
            "2021-09-27",
            "2022-10-03",
            "2024-09-30",
        )
        self.assertNoHolidayName(name, range(self.start_year, 1995))

    def test_caacupe_virgin_day(self):
        self.assertHolidayName(
            "Día de la Virgen de Caacupé", (f"{year}-12-08" for year in self.full_range)
        )

    def test_special_public_holidays(self):
        self.assertHolidayName(
            "Asueto adicional",
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
        self.assertGovernmentHolidayName(
            "Asueto de la Administración Pública",
            "2010-12-24",
            "2010-12-31",
            "2011-04-20",
            "2011-12-23",
            "2011-12-30",
            "2012-04-04",
            "2012-12-24",
            "2012-12-31",
            "2013-03-27",
            "2013-12-24",
            "2013-12-31",
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
            "2022-12-23",
            "2022-12-30",
            "2023-04-05",
            "2023-12-07",
            "2024-03-27",
            "2024-12-24",
            "2024-12-31",
            "2025-04-16",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-02-28", "Día de los Héroes de la Patria"),
            ("2022-04-13", "Asueto de la Administración Pública"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-04-17", "Domingo de Resurrección"),
            ("2022-05-01", "Día de los Trabajadores"),
            ("2022-05-02", "Asueto de la Administración Pública"),
            ("2022-05-14", "Feriado Nacional"),
            ("2022-05-15", "Día de la Independencia Nacional"),
            ("2022-06-12", "Día de la Paz del Chaco"),
            ("2022-08-15", "Día de la Fundación de Asunción"),
            ("2022-10-03", "Día de la Batalla de Boquerón"),
            ("2022-12-08", "Día de la Virgen de Caacupé"),
            ("2022-12-23", "Asueto de la Administración Pública"),
            ("2022-12-25", "Día de la Navidad"),
            ("2022-12-30", "Asueto de la Administración Pública"),
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
            ("2022-05-01", "Workers' Day"),
            ("2022-05-02", "Public sector holiday"),
            ("2022-05-14", "National Holiday"),
            ("2022-05-15", "Independence Day"),
            ("2022-06-12", "Chaco Armistice Day"),
            ("2022-08-15", "Asuncion Foundation's Day"),
            ("2022-10-03", "Boqueron Battle Day"),
            ("2022-12-08", "Caacupe Virgin Day"),
            ("2022-12-23", "Public sector holiday"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-30", "Public sector holiday"),
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
            ("2022-05-14", "Національне свято"),
            ("2022-05-15", "День незалежності"),
            ("2022-06-12", "День мирного договору в Чако"),
            ("2022-08-15", "День заснування Асунсьйона"),
            ("2022-10-03", "День битви за Бокерон"),
            ("2022-12-08", "День Богоматері Каакупе"),
            ("2022-12-23", "Вихідний державних установ"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-30", "Вихідний державних установ"),
        )
