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

from holidays.countries.tonga import Tonga
from tests.common import CommonCountryTests


class TestTonga(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Tonga)

    def test_special_holidays(self):
        self.assertHoliday(
            "2017-11-29",
            "2019-09-19",
            "2019-11-15",
        )
        self.assertNoNonObservedHoliday(
            # 2021 Boxing Day
            "2021-12-27",
        )

    def test_new_years_day(self):
        name = "ʻUluaki ʻAho ʻo e Taʻu Foʻou"
        name_observed = f"{name} (fakatokangaʻi)"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "1995-01-02",
            "2006-01-02",
            "2012-01-02",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHolidayName(name_observed, range(2017, self.end_year))

    def test_birthday_of_the_reigning_sovereign_of_tonga(self):
        name = "ʻAho ʻAloʻi ʻo ʻEne ʻAfio ko e Tuʻi ʻo Tonga ʻoku lolotonga Pule"
        self.assertHolidayName(
            name,
            (
                f"{year}-07-04"
                for year in (*range(self.start_year, 2007), *range(2013, self.end_year))
            ),
            (f"{year}-05-04" for year in range(2007, 2011)),
        )
        self.assertNoHolidayName(name, 2012)

        self.assertNoNonObservedHoliday(
            # Topou IV.
            "1993-07-05",
            "1999-07-05",
            "2004-07-05",
            # Topou V.
            "2008-05-05",
            # Topou V (Act 10 of 2010).
            "2011-05-02",
            # Topou VI.
            "2021-07-05",
            "2027-07-05",
        )
        self.assertNonObservedHoliday(
            # Topou V (Act 10 of 2010).
            "2011-05-04",
        )

    def test_birthday_of_the_heir_to_the_crown_of_tonga(self):
        name = "ʻAho ʻAloʻi ʻo e ʻEa ki he Kalauni ʻo Tonga"
        self.assertHolidayName(
            name,
            (f"{year}-05-04" for year in range(self.start_year, 2007)),
            (f"{year}-07-12" for year in range(2007, 2011)),
            (f"{year}-09-17" for year in range(2012, self.end_year)),
        )

        self.assertNoNonObservedHoliday(
            # Topou IV's Heir: Topou V.
            "1997-05-05",
            "2003-05-05",
            # Topou V's Heir: Topou VI.
            "2009-07-13",
            # Topou V's Heir: Topou VI (Act 10 of 2010).
            "2011-07-11",
            # Topou VI's Heir: Tupoutoʻa ʻUlukalala.
            "2017-09-18",
            "2023-09-18",
            "2028-09-18",
        )
        self.assertNonObservedHoliday(
            # Topou V's Heir: Topou VI (Act 10 of 2010).
            "2011-07-12",
        )

    def test_good_friday(self):
        name = "Falaite Lelei"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Monite ʻo e Toetuʻu"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_anzac_day(self):
        name = "ʻAho Anzac"
        name_observed = f"{name} (fakatokangaʻi)"
        self.assertHolidayName(name, (f"{year}-04-25" for year in self.full_range))
        obs_dts = (
            "1999-04-26",
            "2004-04-26",
            "2010-04-26",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHolidayName(name_observed, range(2017, self.end_year))

    def test_emancipation_day(self):
        name = "ʻAho Tauʻataina"
        self.assertHolidayName(name, (f"{year}-06-04" for year in range(self.start_year, 2010)))
        self.assertHoliday(
            "2020-06-08",
            "2021-06-07",
            "2022-06-06",
            "2023-06-05",
            "2024-06-03",
            "2025-06-02",
        )
        self.assertNonObservedHolidayName(name, range(2010, self.end_year))

        obs_dts = (
            "1995-06-05",
            "2000-06-05",
            "2006-06-05",
        )
        self.assertHolidayName(f"{name} (fakatokangaʻi)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_anniversary_of_the_coronation_day_of_the_reigning_sovereign_of_tonga(self):
        name = (
            "Fakamanatu ʻo e ʻAho Hilifaki Kalauni ʻo ʻEne ʻAfio ko e Tuʻi ʻo Tonga "
            "ʻa ia ʻoku lolotonga Pule"
        )
        self.assertHolidayName(name, (f"{year}-08-01" for year in {2008, 2009, 2011}))
        self.assertNoHolidayName(name, range(self.start_year, 2008), range(2012, self.end_year))

        self.assertNoNonObservedHoliday(
            # Topou V (Act 10 of 2010).
            "2010-08-02",
        )
        self.assertNonObservedHoliday(
            # Topou V (Act 10 of 2010).
            "2010-08-01",
        )

    def test_constitution_day(self):
        name = "ʻAho Konisitutone"
        self.assertHolidayName(name, (f"{year}-11-04" for year in range(self.start_year, 2010)))
        self.assertHoliday(
            "2020-11-02",
            "2021-11-08",
            "2022-11-07",
            "2023-11-06",
            "2024-11-04",
            "2025-11-03",
        )
        self.assertNonObservedHolidayName(name, range(2010, self.end_year))

        obs_dts = (
            "1990-11-05",
            "2001-11-05",
            "2007-11-05",
        )
        self.assertHolidayName(f"{name} (fakatokangaʻi)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_anniversary_of_the_coronation_of_hm_king_george_tupou_i(self):
        name = "ʻAho Fakamanatu ʻo e Hilifaki Kalauni ʻo ʻEne ʻAfio ko Siaosi Tupou I"
        self.assertHolidayName(name, (f"{year}-12-04" for year in range(self.start_year, 2010)))
        self.assertHoliday(
            "2020-12-07",
            "2021-12-06",
            "2022-12-05",
            "2023-12-04",
            "2024-12-02",
            "2025-12-08",
        )
        self.assertNonObservedHolidayName(name, range(2010, self.end_year))

        obs_dts = (
            "1994-12-05",
            "2005-12-05",
        )
        self.assertHolidayName(f"{name} (fakatokangaʻi)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        self.assertHolidayName("ʻAho Kilisimasi", (f"{year}-12-25" for year in self.full_range))

    def test_boxing_day(self):
        name = "ʻAho 2 ʻo e Kilisimasi"
        name_observed = f"{name} (fakatokangaʻi)"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        obs_dts = (
            "1994-12-27",
            "2005-12-27",
            "2021-12-27",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHolidayName(name_observed, range(2009, 2021), range(2022, self.end_year))

    def test_2017(self):
        # https://www.officeholidays.com/countries/tonga/2017
        self.assertHolidaysInYear(
            2017,
            ("2017-01-01", "ʻUluaki ʻAho ʻo e Taʻu Foʻou"),
            ("2017-04-14", "Falaite Lelei"),
            ("2017-04-17", "Monite ʻo e Toetuʻu"),
            ("2017-04-25", "ʻAho Anzac"),
            ("2017-06-05", "ʻAho Tauʻataina (fakatokangaʻi)"),
            ("2017-07-04", "ʻAho ʻAloʻi ʻo ʻEne ʻAfio ko e Tuʻi ʻo Tonga ʻoku lolotonga Pule"),
            ("2017-09-17", "ʻAho ʻAloʻi ʻo e ʻEa ki he Kalauni ʻo Tonga"),
            ("2017-09-18", "ʻAho ʻAloʻi ʻo e ʻEa ki he Kalauni ʻo Tonga (fakatokangaʻi)"),
            ("2017-11-06", "ʻAho Konisitutone (fakatokangaʻi)"),
            ("2017-11-29", "ʻAho malolo ʻakapulu ʻa Tonga"),
            (
                "2017-12-04",
                "ʻAho Fakamanatu ʻo e Hilifaki Kalauni ʻo ʻEne ʻAfio ko Siaosi Tupou I",
            ),
            ("2017-12-25", "ʻAho Kilisimasi"),
            ("2017-12-26", "ʻAho 2 ʻo e Kilisimasi"),
        )

    def test_2018(self):
        # https://www.gov.to/press-release/tonga-public-holidays-for-2018/
        self.assertHolidaysInYear(
            2018,
            ("2018-01-01", "ʻUluaki ʻAho ʻo e Taʻu Foʻou"),
            ("2018-03-30", "Falaite Lelei"),
            ("2018-04-02", "Monite ʻo e Toetuʻu"),
            ("2018-04-25", "ʻAho Anzac"),
            ("2018-06-04", "ʻAho Tauʻataina"),
            ("2018-07-04", "ʻAho ʻAloʻi ʻo ʻEne ʻAfio ko e Tuʻi ʻo Tonga ʻoku lolotonga Pule"),
            ("2018-09-17", "ʻAho ʻAloʻi ʻo e ʻEa ki he Kalauni ʻo Tonga"),
            ("2018-11-05", "ʻAho Konisitutone (fakatokangaʻi)"),
            (
                "2018-12-03",
                "ʻAho Fakamanatu ʻo e Hilifaki Kalauni ʻo ʻEne ʻAfio ko "
                "Siaosi Tupou I (fakatokangaʻi)",
            ),
            ("2018-12-25", "ʻAho Kilisimasi"),
            ("2018-12-26", "ʻAho 2 ʻo e Kilisimasi"),
        )

    def test_2019(self):
        # https://www.gov.to/press-release/tonga-public-holidays-for-2019-2/
        self.assertHolidaysInYear(
            2019,
            ("2019-01-01", "ʻUluaki ʻAho ʻo e Taʻu Foʻou"),
            ("2019-04-19", "Falaite Lelei"),
            ("2019-04-22", "Monite ʻo e Toetuʻu"),
            ("2019-04-25", "ʻAho Anzac"),
            ("2019-06-03", "ʻAho Tauʻataina (fakatokangaʻi)"),
            ("2019-07-04", "ʻAho ʻAloʻi ʻo ʻEne ʻAfio ko e Tuʻi ʻo Tonga ʻoku lolotonga Pule"),
            ("2019-09-17", "ʻAho ʻAloʻi ʻo e ʻEa ki he Kalauni ʻo Tonga"),
            ("2019-09-19", "Meʻafakaʻeiki ʻo e Siteiti ʻAkilisi Pōhiva"),
            ("2019-11-04", "ʻAho Konisitutone"),
            ("2019-11-15", "ʻAho malolo ʻakapulu ʻa Tonga"),
            (
                "2019-12-02",
                "ʻAho Fakamanatu ʻo e Hilifaki Kalauni ʻo ʻEne ʻAfio ko "
                "Siaosi Tupou I (fakatokangaʻi)",
            ),
            ("2019-12-25", "ʻAho Kilisimasi"),
            ("2019-12-26", "ʻAho 2 ʻo e Kilisimasi"),
        )

    def test_2020(self):
        # https://www.gov.to/press-release/tonga-public-holidays-for-2020/
        self.assertHolidaysInYear(
            2020,
            ("2020-01-01", "ʻUluaki ʻAho ʻo e Taʻu Foʻou"),
            ("2020-04-10", "Falaite Lelei"),
            ("2020-04-13", "Monite ʻo e Toetuʻu"),
            ("2020-04-25", "ʻAho Anzac"),
            ("2020-06-08", "ʻAho Tauʻataina (fakatokangaʻi)"),
            ("2020-07-04", "ʻAho ʻAloʻi ʻo ʻEne ʻAfio ko e Tuʻi ʻo Tonga ʻoku lolotonga Pule"),
            ("2020-09-17", "ʻAho ʻAloʻi ʻo e ʻEa ki he Kalauni ʻo Tonga"),
            ("2020-11-02", "ʻAho Konisitutone (fakatokangaʻi)"),
            (
                "2020-12-07",
                "ʻAho Fakamanatu ʻo e Hilifaki Kalauni ʻo ʻEne ʻAfio ko "
                "Siaosi Tupou I (fakatokangaʻi)",
            ),
            ("2020-12-25", "ʻAho Kilisimasi"),
            ("2020-12-26", "ʻAho 2 ʻo e Kilisimasi"),
        )

    def test_2021(self):
        # https://www.gov.to/press-release/tonga-public-holidays-for-2021/
        self.assertHolidaysInYear(
            2021,
            ("2021-01-01", "ʻUluaki ʻAho ʻo e Taʻu Foʻou"),
            ("2021-04-02", "Falaite Lelei"),
            ("2021-04-05", "Monite ʻo e Toetuʻu"),
            ("2021-04-25", "ʻAho Anzac"),
            ("2021-06-07", "ʻAho Tauʻataina (fakatokangaʻi)"),
            ("2021-07-04", "ʻAho ʻAloʻi ʻo ʻEne ʻAfio ko e Tuʻi ʻo Tonga ʻoku lolotonga Pule"),
            (
                "2021-07-05",
                "ʻAho ʻAloʻi ʻo ʻEne ʻAfio ko e Tuʻi ʻo Tonga ʻoku lolotonga Pule (fakatokangaʻi)",
            ),
            ("2021-09-17", "ʻAho ʻAloʻi ʻo e ʻEa ki he Kalauni ʻo Tonga"),
            ("2021-11-08", "ʻAho Konisitutone (fakatokangaʻi)"),
            (
                "2021-12-06",
                "ʻAho Fakamanatu ʻo e Hilifaki Kalauni ʻo ʻEne ʻAfio ko "
                "Siaosi Tupou I (fakatokangaʻi)",
            ),
            ("2021-12-25", "ʻAho Kilisimasi"),
            ("2021-12-26", "ʻAho 2 ʻo e Kilisimasi"),
            ("2021-12-27", "ʻAho 2 ʻo e Kilisimasi (fakatokangaʻi)"),  # ???
        )

    def test_2022(self):
        # https://www.gov.to/press-release/tonga-public-holidays-for-2022/
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "ʻUluaki ʻAho ʻo e Taʻu Foʻou"),
            ("2022-04-15", "Falaite Lelei"),
            ("2022-04-18", "Monite ʻo e Toetuʻu"),
            ("2022-04-25", "ʻAho Anzac"),
            ("2022-06-06", "ʻAho Tauʻataina (fakatokangaʻi)"),
            ("2022-07-04", "ʻAho ʻAloʻi ʻo ʻEne ʻAfio ko e Tuʻi ʻo Tonga ʻoku lolotonga Pule"),
            ("2022-09-17", "ʻAho ʻAloʻi ʻo e ʻEa ki he Kalauni ʻo Tonga"),
            ("2022-11-07", "ʻAho Konisitutone (fakatokangaʻi)"),
            (
                "2022-12-05",
                "ʻAho Fakamanatu ʻo e Hilifaki Kalauni ʻo ʻEne ʻAfio ko "
                "Siaosi Tupou I (fakatokangaʻi)",
            ),
            ("2022-12-25", "ʻAho Kilisimasi"),
            ("2022-12-26", "ʻAho 2 ʻo e Kilisimasi"),
        )

    def test_2024(self):
        # https://www.gov.to/press-release/tonga-public-holidays-for-2024/
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "ʻUluaki ʻAho ʻo e Taʻu Foʻou"),
            ("2024-03-29", "Falaite Lelei"),
            ("2024-04-01", "Monite ʻo e Toetuʻu"),
            ("2024-04-25", "ʻAho Anzac"),
            ("2024-06-03", "ʻAho Tauʻataina (fakatokangaʻi)"),
            ("2024-07-04", "ʻAho ʻAloʻi ʻo ʻEne ʻAfio ko e Tuʻi ʻo Tonga ʻoku lolotonga Pule"),
            ("2024-09-17", "ʻAho ʻAloʻi ʻo e ʻEa ki he Kalauni ʻo Tonga"),
            ("2024-11-04", "ʻAho Konisitutone"),
            (
                "2024-12-02",
                "ʻAho Fakamanatu ʻo e Hilifaki Kalauni ʻo ʻEne ʻAfio ko "
                "Siaosi Tupou I (fakatokangaʻi)",
            ),
            ("2024-12-25", "ʻAho Kilisimasi"),
            ("2024-12-26", "ʻAho 2 ʻo e Kilisimasi"),
        )

    def test_l10n_default(self):
        # https://www.gov.to/press-release/tonga-public-holidays-for-2023/
        self.assertLocalizedHolidays(
            ("2023-01-01", "ʻUluaki ʻAho ʻo e Taʻu Foʻou"),
            ("2023-04-07", "Falaite Lelei"),
            ("2023-04-10", "Monite ʻo e Toetuʻu"),
            ("2023-04-25", "ʻAho Anzac"),
            ("2023-06-05", "ʻAho Tauʻataina (fakatokangaʻi)"),
            ("2023-07-04", "ʻAho ʻAloʻi ʻo ʻEne ʻAfio ko e Tuʻi ʻo Tonga ʻoku lolotonga Pule"),
            ("2023-09-17", "ʻAho ʻAloʻi ʻo e ʻEa ki he Kalauni ʻo Tonga"),
            ("2023-09-18", "ʻAho ʻAloʻi ʻo e ʻEa ki he Kalauni ʻo Tonga (fakatokangaʻi)"),
            ("2023-11-06", "ʻAho Konisitutone (fakatokangaʻi)"),
            (
                "2023-12-04",
                "ʻAho Fakamanatu ʻo e Hilifaki Kalauni ʻo ʻEne ʻAfio ko Siaosi Tupou I",
            ),
            ("2023-12-25", "ʻAho Kilisimasi"),
            ("2023-12-26", "ʻAho 2 ʻo e Kilisimasi"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-25", "Anzac Day"),
            ("2023-06-05", "Emancipation Day (observed)"),
            ("2023-07-04", "Birthday of the Reigning Sovereign of Tonga"),
            ("2023-09-17", "Birthday of the Heir to the Crown of Tonga"),
            ("2023-09-18", "Birthday of the Heir to the Crown of Tonga (observed)"),
            ("2023-11-06", "Constitution Day (observed)"),
            ("2023-12-04", "Anniversary of the Coronation of HM King George Tupou I"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )
