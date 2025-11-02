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

from holidays.constants import BANK, PUBLIC
from holidays.countries.tanzania import Tanzania
from tests.common import CommonCountryTests


class TestTanzania(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1965, 2050)
        super().setUpClass(Tanzania, years=years, years_non_observed=years)
        cls.bank_holidays = Tanzania(categories=BANK, years=years)
        cls.no_estimated_holidays = Tanzania(years=years, islamic_show_estimated=False)

    def test_special_holidays(self):
        self.assertHoliday(
            "1967-12-01",
            "2002-08-25",
            "2015-11-05",
            "2020-10-28",
            "2021-03-22",
            "2021-03-25",
            "2022-08-23",
        )

    def test_new_years_day(self):
        name = "Mwaka Mpya"
        self.assertHolidayName(
            name, (f"{year}-01-01" for year in (*range(1965, 1967), *range(1987, 2050)))
        )
        self.assertNoHolidayName(name, range(1967, 1987))
        obs_dt = (
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
        )
        self.assertHolidayName(f"Badala ya {name}", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_zanzibar_revolution_day(self):
        name = "Mapinduzi ya Zanzibar"
        self.assertHolidayName(name, (f"{year}-01-12" for year in range(1965, 2050)))
        obs_dt = (
            "2014-01-13",
            "2019-01-14",
            "2020-01-13",
        )
        self.assertHolidayName(f"Badala ya {name}", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_party_founding_day(self):
        name_asp = "Kuzaliwa kwa ASP"
        name_ccm = "Kuzaliwa kwa Chama cha Mapinduzi"
        self.assertHolidayName(name_asp, (f"{year}-02-05" for year in range(1973, 1977)))
        self.assertHolidayName(name_ccm, (f"{year}-02-05" for year in range(1977, 1994)))
        self.assertNoHolidayName(name_asp, range(1965, 1973), range(1977, 2050))
        self.assertNoHolidayName(name_ccm, range(1965, 1977), range(1994, 2050))

    def test_sheikh_abeid_amani_karume_day(self):
        name = (
            "Siku ya kumbukumbu ya Rais wa Kwanza wa Serikali ya "
            "Mapinduzi Zanzibar Sheikh Abeid Amani Karume"
        )
        self.assertHolidayName(name, (f"{year}-04-07" for year in range(2006, 2050)))
        self.assertNoHolidayName(name, range(1965, 2006))
        obs_dt = (
            "2012-04-10",
            "2013-04-08",
            "2018-04-09",
            "2019-04-08",
        )
        self.assertHolidayName(f"Badala ya {name}", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_good_friday(self):
        name = "Ijumaa Kuu"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1965, 2050))

    def test_easter_sunday(self):
        name = "Sikukuu ya Pasaka"
        self.assertHolidayName(
            name,
            self.bank_holidays,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, self.bank_holidays, range(1965, 2050))
        self.assertNoHolidayName(name, range(1965, 2050))

    def test_easter_monday(self):
        name = "Jumatatu ya Pasaka"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(1965, 2050))

    def test_union_celebrations(self):
        name_day = "Sikukuu ya Muungano"
        name_celebrations = "Muungano wa Tanzania"
        self.assertHolidayName(name_day, (f"{year}-04-26" for year in range(1965, 1991)))
        self.assertHolidayName(name_celebrations, (f"{year}-04-26" for year in range(1991, 2050)))
        self.assertNoHolidayName(name_day, range(1991, 2050))
        self.assertNoHolidayName(name_celebrations, range(1965, 1991))
        obs_dt = (
            "2008-04-28",
            "2009-04-27",
            "2014-04-28",
            "2015-04-27",
            "2020-04-27",
        )
        self.assertHolidayName(f"Badala ya {name_celebrations}", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_international_workers_day(self):
        name = "Sikukuu ya Wafanyakazi Ulimwenguni"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1965, 2050)))
        obs_dt = (
            "2010-05-03",
            "2011-05-02",
            "2016-05-02",
            "2021-05-03",
            "2022-05-02",
        )
        self.assertHolidayName(f"Badala ya {name}", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_international_trade_fair_and_peasants_day(self):
        name_1965 = "Saba Saba"
        name_1977 = "Sikukuu ya Wakulima"
        name_1994 = "Sabasaba"

        self.assertHolidayName(name_1965, (f"{year}-07-07" for year in range(1965, 1977)))
        self.assertHolidayName(
            name_1977,
            (f"{year}-07-07" for year in range(1977, 1994)),
            (f"{year}-08-08" for year in range(1995, 2050)),
        )
        self.assertHolidayName(name_1994, (f"{year}-07-07" for year in range(1994, 2050)))
        self.assertNoHolidayName(name_1965, range(1977, 2050))
        self.assertNoHolidayName(name_1977, range(1965, 1977), 1994)
        self.assertNoHolidayName(name_1994, range(1965, 1994))

        obs_dt_jul7 = (
            "2007-07-09",
            "2012-07-09",
            "2013-07-08",
            "2018-07-09",
            "2019-07-08",
        )
        self.assertHolidayName(f"Badala ya {name_1994}", obs_dt_jul7)

        obs_dt_aug8 = (
            "2009-08-10",
            "2010-08-09",
            "2015-08-10",
            "2020-08-10",
            "2021-08-09",
        )
        self.assertHolidayName(f"Badala ya {name_1977}", obs_dt_aug8)
        self.assertNoNonObservedHoliday(obs_dt_jul7, obs_dt_aug8)

    def test_the_mwalimu_nyerere_day_and_the_climax_of_the_uhuru_torch_race(self):
        name = "Kumbukumbu ya Mwalimu Nyerere na Kilele cha mbio za Mwenge"
        self.assertHolidayName(name, (f"{year}-10-14" for year in range(2002, 2050)))
        self.assertNoHolidayName(name, range(1965, 2002))
        obs_dt = (
            "2006-10-16",
            "2007-10-15",
            "2012-10-15",
            "2017-10-16",
            "2018-10-15",
        )
        self.assertHolidayName(f"Badala ya {name}", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_independence_and_republic_day(self):
        name = "Uhuru na Jamhuri"
        self.assertHolidayName(name, (f"{year}-12-09" for year in range(1965, 2050)))
        obs_dt = (
            "2006-12-11",
            "2007-12-10",
            "2012-12-10",
            "2017-12-11",
            "2018-12-10",
        )
        self.assertHolidayName(f"Badala ya {name}", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_christmas_day(self):
        name = "Kuzaliwa Kristo"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1965, 2050)))
        obs_dt = (
            "1994-12-27",
            "2005-12-27",
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
        )
        self.assertHolidayName(f"Badala ya {name}", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_boxing_day(self):
        name = "Siku ya Kupeana Zawadi"
        self.assertHolidayName(
            name, (f"{year}-12-26" for year in (*range(1965, 1966), *range(1993, 2050)))
        )
        self.assertNoHolidayName(name, range(1966, 1993))
        obs_dt = (
            "2009-12-28",
            "2010-12-27",
            "2015-12-28",
            "2020-12-28",
            "2021-12-27",
        )
        self.assertHolidayName(f"Badala ya {name}", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_eid_al_fitr(self):
        name = "Eid El-Fitri"
        self.assertHolidayName(
            name,
            "1965-02-03",
            "1965-02-04",
            "2020-05-24",
            "2020-05-25",
            "2021-05-14",
            "2021-05-15",
            "2022-05-03",
            "2022-05-04",
            "2023-04-22",
            "2023-04-23",
            "2024-04-10",
            "2024-04-11",
            "2025-03-31",
            "2025-04-01",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1965, 2050))
        obs_dt = (
            "2018-06-18",
            "2020-05-26",
            "2021-05-17",
        )
        self.assertHolidayName(f"Badala ya {name}", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_eid_al_adha(self):
        name = "Eid El Hajj"
        self.assertHolidayName(
            name,
            "1965-04-13",
            "1965-04-14",
            "2020-07-31",
            "2021-07-21",
            "2022-07-10",
            "2023-06-29",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1965, 2050))
        obs_dt = (
            "2014-10-06",
            "2017-09-04",
            "2022-07-11",
        )
        self.assertHolidayName(f"Badala ya {name}", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_prophets_birthday(self):
        name = "Maulidi"
        self.assertHolidayName(
            name,
            "1965-07-12",
            "2020-10-29",
            "2021-10-19",
            "2022-10-09",
            "2023-09-28",
            "2024-09-16",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1965, 2050))
        obs_dt = (
            "2015-01-05",
            "2019-11-11",
        )
        self.assertHolidayName(f"Badala ya {name}", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_2022_all(self):
        self.assertHolidays(
            Tanzania(categories=(BANK, PUBLIC), years=2022),
            ("2022-01-01", "Mwaka Mpya"),
            ("2022-01-03", "Badala ya Mwaka Mpya"),
            ("2022-01-12", "Mapinduzi ya Zanzibar"),
            (
                "2022-04-07",
                (
                    "Siku ya kumbukumbu ya Rais wa Kwanza wa Serikali ya "
                    "Mapinduzi Zanzibar Sheikh Abeid Amani Karume"
                ),
            ),
            ("2022-04-15", "Ijumaa Kuu"),
            ("2022-04-17", "Sikukuu ya Pasaka"),
            ("2022-04-18", "Jumatatu ya Pasaka"),
            ("2022-04-26", "Muungano wa Tanzania"),
            ("2022-05-01", "Sikukuu ya Wafanyakazi Ulimwenguni"),
            ("2022-05-02", "Badala ya Sikukuu ya Wafanyakazi Ulimwenguni"),
            ("2022-05-03", "Eid El-Fitri"),
            ("2022-05-04", "Eid El-Fitri"),
            ("2022-07-07", "Sabasaba"),
            ("2022-07-10", "Eid El Hajj"),
            ("2022-07-11", "Badala ya Eid El Hajj"),
            ("2022-08-08", "Sikukuu ya Wakulima"),
            ("2022-08-23", "Siku ya Sensa ya Kitaifa ya Watu na Makazi"),
            ("2022-10-09", "Maulidi"),
            ("2022-10-14", "Kumbukumbu ya Mwalimu Nyerere na Kilele cha mbio za Mwenge"),
            ("2022-12-09", "Uhuru na Jamhuri"),
            ("2022-12-25", "Kuzaliwa Kristo"),
            ("2022-12-26", "Siku ya Kupeana Zawadi"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Mwaka Mpya"),
            ("2023-01-12", "Mapinduzi ya Zanzibar"),
            (
                "2023-04-07",
                (
                    "Ijumaa Kuu; Siku ya kumbukumbu ya Rais wa Kwanza wa Serikali ya "
                    "Mapinduzi Zanzibar Sheikh Abeid Amani Karume"
                ),
            ),
            ("2023-04-09", "Sikukuu ya Pasaka"),
            ("2023-04-10", "Jumatatu ya Pasaka"),
            ("2023-04-22", "Eid El-Fitri"),
            ("2023-04-23", "Eid El-Fitri"),
            ("2023-04-26", "Muungano wa Tanzania"),
            ("2023-05-01", "Sikukuu ya Wafanyakazi Ulimwenguni"),
            ("2023-06-29", "Eid El Hajj"),
            ("2023-07-07", "Sabasaba"),
            ("2023-08-08", "Sikukuu ya Wakulima"),
            ("2023-09-28", "Maulidi"),
            ("2023-10-14", "Kumbukumbu ya Mwalimu Nyerere na Kilele cha mbio za Mwenge"),
            ("2023-12-09", "Uhuru na Jamhuri"),
            ("2023-12-25", "Kuzaliwa Kristo"),
            ("2023-12-26", "Siku ya Kupeana Zawadi"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-01-12", "Zanzibar Revolution Day"),
            ("2023-04-07", "Good Friday; The Sheikh Abeid Amani Karume Day"),
            ("2023-04-09", "Easter Sunday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-23", "Eid al-Fitr"),
            ("2023-04-26", "Union Celebrations"),
            ("2023-05-01", "International Workers' Day"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-07-07", "International Trade Fair"),
            ("2023-08-08", "Peasants' Day"),
            ("2023-09-28", "Prophet's Birthday"),
            ("2023-10-14", "The Mwalimu Nyerere Day and Climax of the Uhuru Torch Race"),
            ("2023-12-09", "Independence and Republic Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )
