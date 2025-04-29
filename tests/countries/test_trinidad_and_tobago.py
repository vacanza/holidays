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

from holidays.constants import OPTIONAL
from holidays.countries.trinidad_and_tobago import TrinidadAndTobago, TT, TTO
from tests.common import CommonCountryTests


class TestTrinidadAndTobago(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1963, 2050)
        super().setUpClass(TrinidadAndTobago, years=years, years_non_observed=years)
        cls.no_estimated_holidays = TrinidadAndTobago(years=years, islamic_show_estimated=False)
        cls.optional_holidays = TrinidadAndTobago(categories=OPTIONAL, years=years)

    def test_country_aliases(self):
        self.assertAliases(TrinidadAndTobago, TT, TTO)

    def test_no_holidays(self):
        self.assertNoHolidays(TrinidadAndTobago(years=1962))
        self.assertNoHolidays(TrinidadAndTobago(categories=OPTIONAL, years=1962))

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1963, 2050)))
        dt = (
            "1967-01-02",
            "1968-01-02",
            "1978-01-02",
            "1984-01-02",
            "1989-01-02",
            "1995-01-02",
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
            "2034-01-02",
            "2040-01-02",
            "2045-01-02",
            "2051-01-02",
            "2062-01-02",
            "2068-01-02",
            "2073-01-02",
            "2079-01-02",
            "2090-01-02",
            "2096-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1963, 2050))
        dt = (
            "2018-04-03",
            "2029-04-03",
            "2040-04-03",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(1963, 2050))
        dt = (
            "2043-03-31",
            "2054-03-31",
            "2065-03-31",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_spiritual_baptist_liberation_day(self):
        name = "Spiritual Baptist Liberation Day"
        self.assertHolidayName(name, (f"{year}-03-30" for year in range(1996, 2050)))
        dt = (
            "1997-04-01",
            "2003-03-31",
            "2008-03-31",
            "2014-03-31",
            "2018-04-03",
            "2025-04-01",
            "2029-04-03",
            "2031-03-31",
            "2036-03-31",
            "2040-04-03",
            "2042-03-31",
            "2043-03-31",
            "2053-03-31",
            "2054-03-31",
            "2059-04-01",
            "2064-03-31",
            "2065-03-31",
            "2070-04-01",
            "2081-04-01",
            "2087-03-31",
            "2092-04-01",
            "2098-03-31",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNoHolidayName(name, range(1963, 1996))

    def test_indian_arrival_day(self):
        name = "Indian Arrival Day"
        self.assertHolidayName(name, (f"{year}-05-30" for year in range(1996, 2050)))
        dt = (
            "1999-05-31",
            "2002-05-31",
            "2004-05-31",
            "2010-05-31",
            "2013-05-31",
            "2021-05-31",
            "2024-05-31",
            "2027-05-31",
            "2032-05-31",
            "2038-05-31",
            "2049-05-31",
            "2055-05-31",
            "2060-05-31",
            "2066-05-31",
            "2077-05-31",
            "2083-05-31",
            "2086-05-31",
            "2088-05-31",
            "2094-05-31",
            "2097-05-31",
            "2100-05-31",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNoHolidayName(name, range(1963, 1996))

    def test_corpus_christi(self):
        name = "Corpus Christi"
        self.assertHolidayName(
            name,
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
            "2025-06-19",
        )
        self.assertHolidayName(name, range(1963, 2050))
        dt = (
            "2002-05-31",
            "2003-06-20",
            "2013-05-31",
            "2014-06-20",
            "2024-05-31",
            "2025-06-20",
            "2086-05-31",
            "2087-06-20",
            "2097-05-31",
            "2098-06-20",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_labor_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-06-19" for year in range(1973, 2050)))
        dt = (
            "1977-06-20",
            "1983-06-20",
            "1985-06-20",
            "1988-06-20",
            "1994-06-20",
            "2003-06-20",
            "2005-06-20",
            "2011-06-20",
            "2014-06-20",
            "2016-06-20",
            "2022-06-20",
            "2025-06-20",
            "2033-06-20",
            "2039-06-20",
            "2044-06-20",
            "2050-06-21",
            "2061-06-20",
            "2067-06-20",
            "2072-06-20",
            "2078-06-20",
            "2087-06-20",
            "2089-06-20",
            "2095-06-20",
            "2098-06-20",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNoHolidayName(name, range(1963, 1973))

    def test_african_emancipation_day(self):
        name = "African Emancipation Day"
        self.assertHolidayName(name, (f"{year}-08-01" for year in range(1985, 2050)))
        dt = (
            "1993-08-02",
            "1999-08-02",
            "2004-08-02",
            "2010-08-02",
            "2021-08-02",
            "2027-08-02",
            "2032-08-02",
            "2038-08-02",
            "2049-08-02",
            "2055-08-02",
            "2060-08-02",
            "2066-08-02",
            "2077-08-02",
            "2083-08-02",
            "2088-08-02",
            "2094-08-02",
            "2100-08-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNoHolidayName(name, range(1963, 1985))

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-08-31" for year in range(1963, 2050)))
        dt = (
            "1969-09-01",
            "1975-09-01",
            "1980-09-01",
            "1986-09-01",
            "1997-09-01",
            "2003-09-01",
            "2008-09-01",
            "2014-09-01",
            "2025-09-01",
            "2031-09-01",
            "2036-09-01",
            "2042-09-01",
            "2053-09-01",
            "2059-09-01",
            "2064-09-01",
            "2070-09-01",
            "2081-09-01",
            "2087-09-01",
            "2092-09-01",
            "2098-09-01",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_republic_day(self):
        name = "Republic Day"
        self.assertHolidayName(name, (f"{year}-09-24" for year in range(1976, 2050)))
        dt = (
            "1976-09-27",
            "1978-09-25",
            "1989-09-25",
            "1995-09-25",
            "2000-09-25",
            "2006-09-25",
            "2017-09-25",
            "2023-09-25",
            "2028-09-25",
            "2034-09-25",
            "2045-09-25",
            "2051-09-25",
            "2056-09-25",
            "2062-09-25",
            "2073-09-25",
            "2079-09-25",
            "2084-09-25",
            "2090-09-25",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNoHolidayName(name, range(1963, 1976))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1963, 2050)))
        dt = (
            "1966-12-27",
            "1977-12-27",
            "1983-12-27",
            "1988-12-27",
            "1994-12-27",
            "2005-12-27",
            "2011-12-27",
            "2016-12-27",
            "2022-12-27",
            "2033-12-27",
            "2039-12-27",
            "2044-12-27",
            "2050-12-27",
            "2061-12-27",
            "2067-12-27",
            "2072-12-27",
            "2078-12-27",
            "2089-12-27",
            "2095-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1963, 2050)))
        dt = (
            "1965-12-27",
            "1971-12-27",
            "1976-12-27",
            "1982-12-27",
            "1993-12-27",
            "1999-12-27",
            "2004-12-27",
            "2010-12-27",
            "2021-12-27",
            "2027-12-27",
            "2032-12-27",
            "2038-12-27",
            "2049-12-27",
            "2055-12-27",
            "2060-12-27",
            "2066-12-27",
            "2077-12-27",
            "2083-12-27",
            "2088-12-27",
            "2094-12-27",
            "2100-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_diwali(self):
        name = "Divali"
        self.assertHolidayName(
            name,
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-10-31",
            "2025-10-20",
        )
        self.assertHolidayName(name, range(1963, 2050))
        dt = (
            "1979-11-19",
            "1985-11-11",
            "2002-11-04",
            "2006-11-20",
            "2009-11-16",
            "2019-10-28",
            "2023-11-13",
            "2029-11-05",
            "2036-11-17",
            "2056-11-06",
            "2063-11-19",
            "2073-10-30",
            "2077-11-15",
            "2090-11-20",
            "2100-11-01",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_eid_al_fitr(self):
        name = "Eid-Ul-Fitr"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-22",
            "2024-04-10",
            "2025-03-31",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1963, 2050))
        dt = (
            "1963-02-25",
            "1968-01-02",
            "1976-09-27",
            "1978-09-04",
            "1985-06-20",
            "1986-06-09",
            "1994-03-14",
            "2001-12-17",
            "2004-11-15",
            "2009-09-21",
            "2012-08-20",
            "2020-05-25",
            "2033-01-03",
            "2037-11-09",
            "2040-10-08",
            "2048-07-13",
            "2056-04-17",
            "2064-01-21",
            "2076-09-01",
        )
        self.assertHolidayName(f"{name} (observed)", self.no_estimated_holidays, dt)
        self.assertNoNonObservedHoliday(dt)

    def test_carnival_monday(self):
        name = "Carnival Monday"
        self.assertHolidayName(
            name,
            self.optional_holidays,
            "2020-02-24",
            "2021-02-15",
            "2022-02-28",
            "2023-02-20",
            "2024-02-12",
            "2025-03-03",
        )
        self.assertHolidayName(name, self.optional_holidays, range(1963, 2050))
        self.assertNoHolidayName(name)

    def test_carnival_tuesday(self):
        name = "Carnival Tuesday"
        self.assertHolidayName(
            name,
            self.optional_holidays,
            "2020-02-25",
            "2021-02-16",
            "2022-03-01",
            "2023-02-21",
            "2024-02-13",
            "2025-03-04",
        )
        self.assertHolidayName(name, self.optional_holidays, range(1963, 2050))
        self.assertNoHolidayName(name)

    def test_optional_2025(self):
        self.assertHolidays(
            TrinidadAndTobago(categories=OPTIONAL, years=2025),
            ("2025-03-03", "Carnival Monday"),
            ("2025-03-04", "Carnival Tuesday"),
        )

    def test_2024(self):
        self.assertHolidays(
            TrinidadAndTobago(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Spiritual Baptist Liberation Day"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-10", "Eid-Ul-Fitr"),
            ("2024-05-30", "Corpus Christi; Indian Arrival Day"),
            ("2024-05-31", "Corpus Christi (observed); Indian Arrival Day (observed)"),
            ("2024-06-19", "Labour Day"),
            ("2024-08-01", "African Emancipation Day"),
            ("2024-08-31", "Independence Day"),
            ("2024-09-24", "Republic Day"),
            ("2024-10-31", "Divali"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_2025(self):
        self.assertHolidays(
            TrinidadAndTobago(years=2025),
            ("2025-01-01", "New Year's Day"),
            ("2025-03-30", "Spiritual Baptist Liberation Day"),
            ("2025-03-31", "Eid-Ul-Fitr"),
            ("2025-04-01", "Spiritual Baptist Liberation Day (observed)"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-30", "Indian Arrival Day"),
            ("2025-06-19", "Corpus Christi; Labour Day"),
            ("2025-06-20", "Corpus Christi (observed); Labour Day (observed)"),
            ("2025-08-01", "African Emancipation Day"),
            ("2025-08-31", "Independence Day"),
            ("2025-09-01", "Independence Day (observed)"),
            ("2025-09-24", "Republic Day"),
            ("2025-10-20", "Divali"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-03-03", "Carnival Monday"),
            ("2025-03-04", "Carnival Tuesday"),
            ("2025-03-30", "Spiritual Baptist Liberation Day"),
            ("2025-03-31", "Eid-Ul-Fitr"),
            ("2025-04-01", "Spiritual Baptist Liberation Day (observed)"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-30", "Indian Arrival Day"),
            ("2025-06-19", "Corpus Christi; Labour Day"),
            ("2025-06-20", "Corpus Christi (observed); Labour Day (observed)"),
            ("2025-08-01", "African Emancipation Day"),
            ("2025-08-31", "Independence Day"),
            ("2025-09-01", "Independence Day (observed)"),
            ("2025-09-24", "Republic Day"),
            ("2025-10-20", "Divali"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-03-03", "Carnival Monday"),
            ("2025-03-04", "Carnival Tuesday"),
            ("2025-03-30", "Spiritual Baptist Liberation Day"),
            ("2025-03-31", "Eid al-Fitr"),
            ("2025-04-01", "Spiritual Baptist Liberation Day (observed)"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-30", "Indian Arrival Day"),
            ("2025-06-19", "Corpus Christi; Labor Day"),
            ("2025-06-20", "Corpus Christi (observed); Labor Day (observed)"),
            ("2025-08-01", "African Emancipation Day"),
            ("2025-08-31", "Independence Day"),
            ("2025-09-01", "Independence Day (observed)"),
            ("2025-09-24", "Republic Day"),
            ("2025-10-20", "Diwali"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
