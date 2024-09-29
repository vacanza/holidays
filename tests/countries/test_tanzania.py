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

from holidays.constants import BANK, PUBLIC
from holidays.countries.tanzania import Tanzania, TZ, TZA
from tests.common import CommonCountryTests


class TestTanzania(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Tanzania, years=range(1994, 2077))

    def test_country_aliases(self):
        self.assertAliases(Tanzania, TZ, TZA)

    def test_no_holidays(self):
        self.assertNoHolidays(Tanzania(years=1993))
        self.assertNoHolidays(Tanzania(years=1993, categories=BANK))

    def test_special_holidays(self):
        self.assertHoliday(
            "2002-08-25",
            "2015-11-05",
            "2020-10-28",
            "2021-03-22",
            "2021-03-25",
            "2022-08-23",
        )

    def test_2018_all(self):
        self.assertHolidays(
            Tanzania(categories=(BANK, PUBLIC), years=2018),
            ("2018-01-01", "Mwaka Mpya"),
            ("2018-01-12", "Mapinduzi ya Zanzibar"),
            ("2018-03-30", "Ijumaa Kuu"),
            ("2018-04-01", "Sikukuu ya Pasaka"),
            ("2018-04-02", "Jumatatu ya Pasaka"),
            (
                "2018-04-07",
                (
                    "Siku ya kumbukumbu ya Rais wa Kwanza wa Serikali ya Mapinduzi Zanzibar "
                    "Sheikh Abeid Amani Karume"
                ),
            ),
            ("2018-04-26", "Muungano wa Tanganyika na Zanzibar"),
            ("2018-05-01", "Sikukuu ya Wafanyakazi"),
            ("2018-06-15", "Eid El-Fitry"),
            ("2018-07-07", "Sabasaba"),
            ("2018-08-08", "Siku ya Wakulima"),
            ("2018-08-22", "Eid El-Hajj"),
            ("2018-10-14", "Kumbukumbu ya Mwalimu Nyerere"),
            ("2018-11-21", "Maulidi"),
            ("2018-12-09", "Uhuru na Jamhuri"),
            ("2018-12-25", "Kuzaliwa Kristo"),
            ("2018-12-26", "Siku ya Kupeana Zawadi"),
        )

    def test_2020_all(self):
        self.assertHolidays(
            Tanzania(categories=(BANK, PUBLIC), years=2020),
            ("2020-01-01", "Mwaka Mpya"),
            ("2020-01-12", "Mapinduzi ya Zanzibar"),
            (
                "2020-04-07",
                (
                    "Siku ya kumbukumbu ya Rais wa Kwanza wa Serikali ya Mapinduzi Zanzibar "
                    "Sheikh Abeid Amani Karume"
                ),
            ),
            ("2020-04-10", "Ijumaa Kuu"),
            ("2020-04-12", "Sikukuu ya Pasaka"),
            ("2020-04-13", "Jumatatu ya Pasaka"),
            ("2020-04-26", "Muungano wa Tanganyika na Zanzibar"),
            ("2020-05-01", "Sikukuu ya Wafanyakazi"),
            ("2020-05-24", "Eid El-Fitry"),
            ("2020-07-07", "Sabasaba"),
            ("2020-07-31", "Eid El-Hajj"),
            ("2020-08-08", "Siku ya Wakulima"),
            ("2020-10-14", "Kumbukumbu ya Mwalimu Nyerere"),
            ("2020-10-28", "Sikukuu ya Uchaguzi Mkuu wa Tanzania"),
            ("2020-10-29", "Maulidi"),
            ("2020-12-09", "Uhuru na Jamhuri"),
            ("2020-12-25", "Kuzaliwa Kristo"),
            ("2020-12-26", "Siku ya Kupeana Zawadi"),
        )

    def test_2021_all(self):
        self.assertHolidays(
            Tanzania(categories=(BANK, PUBLIC), years=2021),
            ("2021-01-01", "Mwaka Mpya"),
            ("2021-01-12", "Mapinduzi ya Zanzibar"),
            ("2021-03-22", "Mazishi cha John Pombe Magufuli"),
            ("2021-03-25", "Mazishi cha John Pombe Magufuli"),
            ("2021-04-02", "Ijumaa Kuu"),
            ("2021-04-04", "Sikukuu ya Pasaka"),
            ("2021-04-05", "Jumatatu ya Pasaka"),
            (
                "2021-04-07",
                (
                    "Siku ya kumbukumbu ya Rais wa Kwanza wa Serikali ya Mapinduzi Zanzibar "
                    "Sheikh Abeid Amani Karume"
                ),
            ),
            ("2021-04-26", "Muungano wa Tanganyika na Zanzibar"),
            ("2021-05-01", "Sikukuu ya Wafanyakazi"),
            ("2021-05-14", "Eid El-Fitry"),
            ("2021-07-07", "Sabasaba"),
            ("2021-07-21", "Eid El-Hajj"),
            ("2021-08-08", "Siku ya Wakulima"),
            ("2021-10-14", "Kumbukumbu ya Mwalimu Nyerere"),
            ("2021-10-19", "Maulidi"),
            ("2021-12-09", "Uhuru na Jamhuri"),
            ("2021-12-25", "Kuzaliwa Kristo"),
            ("2021-12-26", "Siku ya Kupeana Zawadi"),
        )

    def test_2022_all(self):
        self.assertHolidays(
            Tanzania(categories=(BANK, PUBLIC), years=2022),
            ("2022-01-01", "Mwaka Mpya"),
            ("2022-01-12", "Mapinduzi ya Zanzibar"),
            (
                "2022-04-07",
                (
                    "Siku ya kumbukumbu ya Rais wa Kwanza wa Serikali ya Mapinduzi Zanzibar "
                    "Sheikh Abeid Amani Karume"
                ),
            ),
            ("2022-04-15", "Ijumaa Kuu"),
            ("2022-04-17", "Sikukuu ya Pasaka"),
            ("2022-04-18", "Jumatatu ya Pasaka"),
            ("2022-04-26", "Muungano wa Tanganyika na Zanzibar"),
            ("2022-05-01", "Sikukuu ya Wafanyakazi"),
            ("2022-05-03", "Eid El-Fitry"),
            ("2022-07-07", "Sabasaba"),
            ("2022-07-10", "Eid El-Hajj"),
            ("2022-08-08", "Siku ya Wakulima"),
            ("2022-08-23", "Siku ya Sensa ya Kitaifa ya Watu na Makazi"),
            ("2022-10-09", "Maulidi"),
            ("2022-10-14", "Kumbukumbu ya Mwalimu Nyerere"),
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
                    "Ijumaa Kuu; Siku ya kumbukumbu ya Rais wa Kwanza wa Serikali "
                    "ya Mapinduzi Zanzibar Sheikh Abeid Amani Karume"
                ),
            ),
            ("2023-04-09", "Sikukuu ya Pasaka"),
            ("2023-04-10", "Jumatatu ya Pasaka"),
            ("2023-04-22", "Eid El-Fitry"),
            ("2023-04-26", "Muungano wa Tanganyika na Zanzibar"),
            ("2023-05-01", "Sikukuu ya Wafanyakazi"),
            ("2023-06-29", "Eid El-Hajj"),
            ("2023-07-07", "Sabasaba"),
            ("2023-08-08", "Siku ya Wakulima"),
            ("2023-09-28", "Maulidi"),
            ("2023-10-14", "Kumbukumbu ya Mwalimu Nyerere"),
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
            ("2023-04-26", "Union Celebrations"),
            ("2023-05-01", "Worker's Day"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-07-07", "International Trade Fair"),
            ("2023-08-08", "Peasants Day"),
            ("2023-09-28", "Prophet's Birthday"),
            ("2023-10-14", "The Mwalimu Nyerere Day"),
            ("2023-12-09", "Independence and Republic Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )
