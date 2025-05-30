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

from holidays.countries.niger import Niger, NE, NER
from tests.common import CommonCountryTests


class TestNiger(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1959, 2050)
        super().setUpClass(Niger, years=years, years_non_observed=years)
        cls.no_estimated_holidays = Niger(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Niger, NE, NER)

    def test_no_holidays(self):
        self.assertNoHolidays(Niger(years=1958))

    def test_new_years_day(self):
        name = "Ranar Sabuwar Shekara"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1998, 2050)))
        obs_dt = (
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (lura)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNoHolidayName(f"{name} (lura)", range(1959, 1998))

    def test_easter_monday(self):
        name = "Easter Litinin"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(1959, 2050))

    def test_concord_day(self):
        name = "Ranar Concord"
        self.assertHolidayName(name, (f"{year}-04-24" for year in range(1995, 2050)))
        self.assertNoHolidayName(name, range(1959, 1995))
        obs_dt = (
            "2011-04-25",
            "2016-04-25",
            "2022-04-25",
        )
        self.assertHolidayName(f"{name} (lura)", obs_dt)
        self.assertNoNonObservedHolidayName(name, obs_dt)
        self.assertNoHolidayName(f"{name} (lura)", range(1959, 1998))

    def test_international_labor_day(self):
        name = "Ranar Kwadago ta Duniya"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1959, 2050)))
        obs_dt = (
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (lura)", obs_dt)
        self.assertNoNonObservedHolidayName(name, obs_dt)
        self.assertNoHolidayName(f"{name} (lura)", range(1959, 1998))

    def test_ascension_thursday(self):
        name = "Hawan Yesu zuwa sama Alhamis"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, range(1959, 2050))

    def test_whit_sunday(self):
        name = "Fentikos"
        self.assertHolidayName(
            name,
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
        )
        self.assertHolidayName(name, range(1959, 2050))
        self.assertNoHolidayName(f"{name} (lura)", range(1959, 1998))

    def test_cnsp_coup_anniversary(self):
        name = "Bikin bukin juyin mulkin CNSP"
        self.assertHolidayName(
            name,
            "2024-07-26",
            "2025-07-26",
        )
        self.assertHolidayName(name, (f"{year}-07-26" for year in range(2024, 2050)))
        self.assertNoHolidayName(name, range(1959, 2024))

    def test_independence_day(self):
        name = "Bikin cikar shelar 'yancin kai"
        self.assertHolidayName(
            name,
            "2020-08-03",
            "2021-08-03",
            "2022-08-03",
            "2023-08-03",
            "2024-08-03",
            "2025-08-03",
        )
        self.assertHolidayName(name, (f"{year}-08-03" for year in range(1960, 2050)))
        self.assertNoHolidayName(name, 1959)
        obs_dt = (
            "2008-08-04",
            "2014-08-04",
            "2025-08-04",
        )
        self.assertHolidayName(f"{name} (lura)", obs_dt)
        self.assertNoNonObservedHolidayName(name, obs_dt)
        self.assertNoHolidayName(f"{name} (lura)", range(1959, 1998))

    def test_assumption_of_mary(self):
        name = "Zaton Maryama"
        self.assertHolidayName(
            name,
            "2020-08-15",
            "2021-08-15",
            "2022-08-15",
            "2023-08-15",
            "2024-08-15",
            "2025-08-15",
        )
        self.assertHolidayName(name, (f"{year}-08-15" for year in range(1959, 2050)))
        obs_dt = (
            "2010-08-16",
            "2021-08-16",
        )
        self.assertHolidayName(f"{name} (lura)", obs_dt)
        self.assertNoNonObservedHolidayName(name, obs_dt)
        self.assertNoHolidayName(f"{name} (lura)", range(1959, 1998))

    def test_all_saints_day(self):
        name = "Rana Duka Saints"
        self.assertHolidayName(
            name,
            "2020-11-01",
            "2021-11-01",
            "2022-11-01",
            "2023-11-01",
            "2024-11-01",
            "2025-11-01",
        )
        self.assertHolidayName(name, (f"{year}-11-01" for year in range(1959, 2050)))
        obs_dt = (
            "2009-11-02",
            "2015-11-02",
            "2020-11-02",
        )
        self.assertHolidayName(f"{name} (lura)", obs_dt)
        self.assertNoNonObservedHolidayName(name, obs_dt)
        self.assertNoHolidayName(f"{name} (lura)", range(1959, 1998))

    def test_republic_day(self):
        name = "Ranar Jamhuriya"
        self.assertHolidayName(
            name,
            "2020-12-18",
            "2021-12-18",
            "2022-12-18",
            "2023-12-18",
            "2024-12-18",
            "2025-12-18",
        )
        self.assertHolidayName(name, (f"{year}-12-18" for year in range(1959, 2050)))
        obs_dt = (
            "2011-12-19",
            "2016-12-19",
            "2022-12-19",
        )
        self.assertHolidayName(f"{name} (lura)", obs_dt)
        self.assertNoNonObservedHolidayName(name, obs_dt)
        self.assertNoHolidayName(f"{name} (lura)", range(1959, 1998))

    def test_christmas_day(self):
        name = "Ranar Kirsimeti"
        self.assertHolidayName(
            name,
            "2020-12-25",
            "2021-12-25",
            "2022-12-25",
            "2023-12-25",
            "2024-12-25",
            "2025-12-25",
        )
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1959, 2050)))
        obs_dt = (
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (lura)", obs_dt)
        self.assertNoNonObservedHolidayName(name, obs_dt)
        self.assertNoHolidayName(f"{name} (lura)", range(1959, 1998))

    def test_islamic_new_year(self):
        name = "Sabuwar Shekarar Musulunci"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-08-21",
            "2021-08-10",
            "2022-07-30",
            "2023-07-19",
            "2024-07-06",
            "2025-06-27",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1998, 2050))
        obs_dt = (
            "2004-02-23",
            "2011-11-28",
        )
        self.assertHolidayName(f"{name} (lura)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHolidayName(name, obs_dt)
        self.assertNoHolidayName(f"{name} (lura)", range(1959, 1998))

    def test_prophets_birthday(self):
        name = "Maulidin Annabi"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-16",
            "2025-09-05",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1998, 2050))
        obs_dt = (
            "2004-05-03",
            "2012-02-06",
            "2019-11-11",
        )
        self.assertHolidayName(f"{name} (lura)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHolidayName(name, obs_dt)

    def test_laylat_al_qadr(self):
        name = "Lailatul Kadri"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-05-20",
            "2021-05-09",
            "2022-04-28",
            "2023-04-18",
            "2024-04-06",
            "2025-03-27",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1998, 2050))
        obs_dt = (
            "2000-12-25",
            "2008-09-29",
            "2013-08-05",
            "2021-05-10",
        )
        self.assertHolidayName(f"{name} (lura)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHolidayName(name, obs_dt)

    def test_eid_al_fitr(self):
        name = "Eid al-Fitr"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-05-23",
            "2021-05-12",
            "2022-05-01",
            "2023-04-21",
            "2024-04-09",
            "2025-03-30",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1998, 2050))
        obs_dt = (
            "2004-11-15",
            "2012-08-20",
            "2022-05-02",
            "2025-03-31",
        )
        self.assertHolidayName(f"{name} (lura)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHolidayName(name, obs_dt)

    def test_eid_al_adha(self):
        name = "Eid al-Adha"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-07-31",
            "2021-07-20",
            "2022-07-10",
            "2023-06-28",
            "2024-06-16",
            "2025-06-07",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1998, 2050))
        obs_dt = (
            # "1985-07-01",
            "2014-10-06",
        )
        self.assertHolidayName(f"{name} (lura)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHolidayName(name, obs_dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Ranar Sabuwar Shekara"),
            ("2025-03-27", "Lailatul Kadri"),
            ("2025-03-30", "Eid al-Fitr"),
            ("2025-03-31", "Eid al-Fitr (lura)"),
            ("2025-04-21", "Easter Litinin"),
            ("2025-04-24", "Ranar Concord"),
            ("2025-05-01", "Ranar Kwadago ta Duniya"),
            ("2025-05-29", "Hawan Yesu zuwa sama Alhamis"),
            ("2025-06-07", "Eid al-Adha"),
            ("2025-06-08", "Fentikos; Hutun Eid al-Adha"),
            ("2025-06-09", "Fentikos (lura); Hutun Eid al-Adha (lura)"),
            ("2025-06-27", "Sabuwar Shekarar Musulunci"),
            ("2025-07-26", "Bikin bukin juyin mulkin CNSP"),
            ("2025-08-03", "Bikin cikar shelar 'yancin kai"),
            ("2025-08-04", "Bikin cikar shelar 'yancin kai (lura)"),
            ("2025-08-15", "Zaton Maryama"),
            ("2025-09-05", "Maulidin Annabi"),
            ("2025-11-01", "Rana Duka Saints"),
            ("2025-12-18", "Ranar Jamhuriya"),
            ("2025-12-25", "Ranar Kirsimeti"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-03-27", "Laylat al-Qadr"),
            ("2025-03-30", "Eid al-Fitr"),
            ("2025-03-31", "Eid al-Fitr (observed)"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-24", "Concord Day"),
            ("2025-05-01", "International Labor Day"),
            ("2025-05-29", "Ascension Thursday"),
            ("2025-06-07", "Eid al-Adha"),
            ("2025-06-08", "Eid al-Adha Holiday; Pentecost"),
            ("2025-06-09", "Eid al-Adha Holiday (observed); Pentecost (observed)"),
            ("2025-06-27", "Islamic New Year"),
            ("2025-07-26", "Anniversary of the CNSP Coup"),
            ("2025-08-03", "Anniversary of the Proclamation of Independence"),
            ("2025-08-04", "Anniversary of the Proclamation of Independence (observed)"),
            ("2025-08-15", "Assumption of Mary"),
            ("2025-09-05", "Prophet's Birthday"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-12-18", "Republic Day"),
            ("2025-12-25", "Christmas Day"),
        )
