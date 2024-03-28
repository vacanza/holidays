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

from holidays.countries.tonga import Tonga, TO, TON
from tests.common import CommonCountryTests


class TestTonga(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Tonga, years=range(1989, 2050), years_non_observed=range(1989, 2050))

    def test_country_aliases(self):
        self.assertAliases(Tonga, TO, TON)

    def test_no_holidays(self):
        self.assertNoHolidays(Tonga(years=1988))

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

    def test_government_actual_date_observance(self):
        self.assertNonObservedHoliday(
            # Emancipation Day.
            "2017-06-04",
            "2019-06-04",
            "2020-06-04",
            "2021-06-04",
            "2022-06-04",
            "2023-06-04",
            "2024-06-04",
            # Constitution Day.
            "2017-11-04",
            "2018-11-04",
            "2020-11-04",
            "2021-11-04",
            "2022-11-04",
            "2023-11-04",
            # HM King Topou I's Coronation Day.
            "2018-12-04",
            "2019-12-04",
            "2021-12-04",
            "2022-12-04",
            "2024-12-04",
        )

    def test_birthday_of_the_reigning_sovereign(self):
        name = "'Aho 'Alo'i 'o 'Ene 'Afio ko e Tu'i 'o Tonga 'oku lolotonga Pule"
        self.assertHolidayName(name, (f"{year}-07-04" for year in range(1989, 2007)))
        self.assertHolidayName(name, (f"{year}-05-04" for year in range(2007, 2011)))
        self.assertNoHolidayName(name, 2012)
        self.assertHolidayName(name, (f"{year}-07-04" for year in range(2013, 2050)))

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

    def test_birthday_of_the_heir_to_the_crown(self):
        name = "'Aho 'Alo'i 'o e 'Ea ki he Kalauni 'o Tonga"
        self.assertHolidayName(name, (f"{year}-05-04" for year in range(1989, 2007)))
        self.assertHolidayName(name, (f"{year}-07-12" for year in range(2007, 2011)))
        self.assertHolidayName(name, (f"{year}-09-17" for year in range(2012, 2050)))

        self.assertNoNonObservedHoliday(
            # Topou IV's Heir: Topou V.
            "1997-05-05",
            "2003-05-05",
            # Topou V's Heir: Topou VI.
            "2009-07-13",
            # Topou V's Heir: Topou VI (Act 10 of 2010).
            "2011-07-11",
            # Topou VI's Heir: Tupouto'a 'Ulukalala.
            "2017-09-18",
            "2023-09-18",
            "2028-09-18",
        )
        self.assertNonObservedHoliday(
            # Topou V's Heir: Topou VI (Act 10 of 2010).
            "2011-07-12",
        )

    def test_coronation_day_anniversary(self):
        name = (
            "Fakamanatu 'o e 'Aho Hilifaki Kalauni 'o 'Ene 'Afio ko e Tu'i 'o Tonga "
            "'a ia 'oku lolotonga Pule"
        )
        self.assertNoHolidayName(name, range(1989, 2008))
        self.assertHolidayName(name, (f"{year}-08-01" for year in {2008, 2009, 2011}))
        self.assertNoHolidayName(name, range(2012, 2050))

        self.assertNoNonObservedHoliday(
            # Topou V (Act 10 of 2010).
            "2010-08-02",
        )
        self.assertNonObservedHoliday(
            # Topou V (Act 10 of 2010).
            "2010-08-01",
        )

    def test_2017(self):
        # https://www.officeholidays.com/countries/tonga/2017
        self.assertHolidays(
            Tonga(years=2017),
            ("2017-01-01", "'Uluaki 'Aho 'o e Ta'u Fo'ou"),
            ("2017-04-14", "Falaite Lelei"),
            ("2017-04-17", "Monite 'o e Toetu'u"),
            ("2017-04-25", "'Aho Anzac"),
            ("2017-06-05", "'Aho Tau'ataina (fakatokanga'i)"),
            ("2017-07-04", "'Aho 'Alo'i 'o 'Ene 'Afio ko e Tu'i 'o Tonga 'oku lolotonga Pule"),
            ("2017-09-17", "'Aho 'Alo'i 'o e 'Ea ki he Kalauni 'o Tonga"),
            ("2017-09-18", "'Aho 'Alo'i 'o e 'Ea ki he Kalauni 'o Tonga (fakatokanga'i)"),
            ("2017-11-06", "'Aho Konisitutone (fakatokanga'i)"),
            ("2017-11-29", "'Aho malolo 'akapulu 'a Tonga"),
            (
                "2017-12-04",
                "'Aho Fakamanatu 'o e Hilifaki Kalauni 'o 'Ene 'Afio ko Siaosi Tupou I",
            ),
            ("2017-12-25", "'Aho Kilisimasi"),
            ("2017-12-26", "'Aho 2 'o e Kilisimasi"),
        )

    def test_2018(self):
        # https://www.gov.to/press-release/tonga-public-holidays-for-2018/
        self.assertHolidays(
            Tonga(years=2018),
            ("2018-01-01", "'Uluaki 'Aho 'o e Ta'u Fo'ou"),
            ("2018-03-30", "Falaite Lelei"),
            ("2018-04-02", "Monite 'o e Toetu'u"),
            ("2018-04-25", "'Aho Anzac"),
            ("2018-06-04", "'Aho Tau'ataina"),
            ("2018-07-04", "'Aho 'Alo'i 'o 'Ene 'Afio ko e Tu'i 'o Tonga 'oku lolotonga Pule"),
            ("2018-09-17", "'Aho 'Alo'i 'o e 'Ea ki he Kalauni 'o Tonga"),
            ("2018-11-05", "'Aho Konisitutone (fakatokanga'i)"),
            (
                "2018-12-03",
                (
                    "'Aho Fakamanatu 'o e Hilifaki Kalauni 'o 'Ene 'Afio ko "
                    "Siaosi Tupou I (fakatokanga'i)"
                ),
            ),
            ("2018-12-25", "'Aho Kilisimasi"),
            ("2018-12-26", "'Aho 2 'o e Kilisimasi"),
        )

    def test_2019(self):
        # https://www.gov.to/press-release/tonga-public-holidays-for-2019-2/
        self.assertHolidays(
            Tonga(years=2019),
            ("2019-01-01", "'Uluaki 'Aho 'o e Ta'u Fo'ou"),
            ("2019-04-19", "Falaite Lelei"),
            ("2019-04-22", "Monite 'o e Toetu'u"),
            ("2019-04-25", "'Aho Anzac"),
            ("2019-06-03", "'Aho Tau'ataina (fakatokanga'i)"),
            ("2019-07-04", "'Aho 'Alo'i 'o 'Ene 'Afio ko e Tu'i 'o Tonga 'oku lolotonga Pule"),
            ("2019-09-17", "'Aho 'Alo'i 'o e 'Ea ki he Kalauni 'o Tonga"),
            ("2019-09-19", "Me'afaka'eiki 'o e Siteiti 'Akilisi Pohiva"),
            ("2019-11-04", "'Aho Konisitutone"),
            ("2019-11-15", "'Aho malolo 'akapulu 'a Tonga"),
            (
                "2019-12-02",
                (
                    "'Aho Fakamanatu 'o e Hilifaki Kalauni 'o 'Ene 'Afio ko "
                    "Siaosi Tupou I (fakatokanga'i)"
                ),
            ),
            ("2019-12-25", "'Aho Kilisimasi"),
            ("2019-12-26", "'Aho 2 'o e Kilisimasi"),
        )

    def test_2020(self):
        # https://www.gov.to/press-release/tonga-public-holidays-for-2020/
        self.assertHolidays(
            Tonga(years=2020),
            ("2020-01-01", "'Uluaki 'Aho 'o e Ta'u Fo'ou"),
            ("2020-04-10", "Falaite Lelei"),
            ("2020-04-13", "Monite 'o e Toetu'u"),
            ("2020-04-25", "'Aho Anzac"),
            ("2020-06-08", "'Aho Tau'ataina (fakatokanga'i)"),
            ("2020-07-04", "'Aho 'Alo'i 'o 'Ene 'Afio ko e Tu'i 'o Tonga 'oku lolotonga Pule"),
            ("2020-09-17", "'Aho 'Alo'i 'o e 'Ea ki he Kalauni 'o Tonga"),
            ("2020-11-02", "'Aho Konisitutone (fakatokanga'i)"),
            (
                "2020-12-07",
                (
                    "'Aho Fakamanatu 'o e Hilifaki Kalauni 'o 'Ene 'Afio ko "
                    "Siaosi Tupou I (fakatokanga'i)"
                ),
            ),
            ("2020-12-25", "'Aho Kilisimasi"),
            ("2020-12-26", "'Aho 2 'o e Kilisimasi"),
        )

    def test_2021(self):
        # https://www.gov.to/press-release/tonga-public-holidays-for-2021/
        self.assertHolidays(
            Tonga(years=2021),
            ("2021-01-01", "'Uluaki 'Aho 'o e Ta'u Fo'ou"),
            ("2021-04-02", "Falaite Lelei"),
            ("2021-04-05", "Monite 'o e Toetu'u"),
            ("2021-04-25", "'Aho Anzac"),
            ("2021-06-07", "'Aho Tau'ataina (fakatokanga'i)"),
            ("2021-07-04", "'Aho 'Alo'i 'o 'Ene 'Afio ko e Tu'i 'o Tonga 'oku lolotonga Pule"),
            (
                "2021-07-05",
                (
                    "'Aho 'Alo'i 'o 'Ene 'Afio ko e Tu'i 'o Tonga 'oku "
                    "lolotonga Pule (fakatokanga'i)"
                ),
            ),
            ("2021-09-17", "'Aho 'Alo'i 'o e 'Ea ki he Kalauni 'o Tonga"),
            ("2021-11-08", "'Aho Konisitutone (fakatokanga'i)"),
            (
                "2021-12-06",
                (
                    "'Aho Fakamanatu 'o e Hilifaki Kalauni 'o 'Ene 'Afio ko "
                    "Siaosi Tupou I (fakatokanga'i)"
                ),
            ),
            ("2021-12-25", "'Aho Kilisimasi"),
            ("2021-12-26", "'Aho 2 'o e Kilisimasi"),
            ("2021-12-27", "'Aho 2 'o e Kilisimasi (fakatokanga'i)"),  # ???
        )

    def test_2022(self):
        # https://www.gov.to/press-release/tonga-public-holidays-for-2022/
        self.assertHolidays(
            Tonga(years=2022),
            ("2022-01-01", "'Uluaki 'Aho 'o e Ta'u Fo'ou"),
            ("2022-04-15", "Falaite Lelei"),
            ("2022-04-18", "Monite 'o e Toetu'u"),
            ("2022-04-25", "'Aho Anzac"),
            ("2022-06-06", "'Aho Tau'ataina (fakatokanga'i)"),
            ("2022-07-04", "'Aho 'Alo'i 'o 'Ene 'Afio ko e Tu'i 'o Tonga 'oku lolotonga Pule"),
            ("2022-09-17", "'Aho 'Alo'i 'o e 'Ea ki he Kalauni 'o Tonga"),
            ("2022-11-07", "'Aho Konisitutone (fakatokanga'i)"),
            (
                "2022-12-05",
                (
                    "'Aho Fakamanatu 'o e Hilifaki Kalauni 'o 'Ene 'Afio ko "
                    "Siaosi Tupou I (fakatokanga'i)"
                ),
            ),
            ("2022-12-25", "'Aho Kilisimasi"),
            ("2022-12-26", "'Aho 2 'o e Kilisimasi"),
        )

    def test_2024(self):
        # https://www.gov.to/press-release/tonga-public-holidays-for-2024/
        self.assertHolidays(
            Tonga(years=2024),
            ("2024-01-01", "'Uluaki 'Aho 'o e Ta'u Fo'ou"),
            ("2024-03-29", "Falaite Lelei"),
            ("2024-04-01", "Monite 'o e Toetu'u"),
            ("2024-04-25", "'Aho Anzac"),
            ("2024-06-03", "'Aho Tau'ataina (fakatokanga'i)"),
            ("2024-07-04", "'Aho 'Alo'i 'o 'Ene 'Afio ko e Tu'i 'o Tonga 'oku lolotonga Pule"),
            ("2024-09-17", "'Aho 'Alo'i 'o e 'Ea ki he Kalauni 'o Tonga"),
            ("2024-11-04", "'Aho Konisitutone"),
            (
                "2024-12-02",
                (
                    "'Aho Fakamanatu 'o e Hilifaki Kalauni 'o 'Ene 'Afio ko "
                    "Siaosi Tupou I (fakatokanga'i)"
                ),
            ),
            ("2024-12-25", "'Aho Kilisimasi"),
            ("2024-12-26", "'Aho 2 'o e Kilisimasi"),
        )

    def test_l10n_default(self):
        # https://www.gov.to/press-release/tonga-public-holidays-for-2023/
        self.assertLocalizedHolidays(
            ("2023-01-01", "'Uluaki 'Aho 'o e Ta'u Fo'ou"),
            ("2023-04-07", "Falaite Lelei"),
            ("2023-04-10", "Monite 'o e Toetu'u"),
            ("2023-04-25", "'Aho Anzac"),
            ("2023-06-05", "'Aho Tau'ataina (fakatokanga'i)"),
            ("2023-07-04", "'Aho 'Alo'i 'o 'Ene 'Afio ko e Tu'i 'o Tonga 'oku lolotonga Pule"),
            ("2023-09-17", "'Aho 'Alo'i 'o e 'Ea ki he Kalauni 'o Tonga"),
            ("2023-09-18", "'Aho 'Alo'i 'o e 'Ea ki he Kalauni 'o Tonga (fakatokanga'i)"),
            ("2023-11-06", "'Aho Konisitutone (fakatokanga'i)"),
            (
                "2023-12-04",
                "'Aho Fakamanatu 'o e Hilifaki Kalauni 'o 'Ene 'Afio ko Siaosi Tupou I",
            ),
            ("2023-12-25", "'Aho Kilisimasi"),
            ("2023-12-26", "'Aho 2 'o e Kilisimasi"),
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
