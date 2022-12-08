#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date

import holidays
from holidays.constants import (
    APR,
    AUG,
    DEC,
    FEB,
    JAN,
    JUL,
    JUN,
    MAR,
    MAY,
    NOV,
    OCT,
    SEP,
)


class TestMalaysia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Malaysia()
        years = (
            1970,
            1985,
            1990,
            2001,
            2010,
            2014,
            2015,
            2018,
            2019,
            2020,
            2021,
            2022,
            2023,
        )
        self.johor_holidays = holidays.Malaysia(years=years, subdiv="JHR")
        self.kedah_holidays = holidays.Malaysia(years=years, subdiv="KDH")
        self.kelantan_holidays = holidays.Malaysia(years=years, subdiv="KTN")
        self.malacca_holidays = holidays.Malaysia(years=years, subdiv="MLK")
        self.negeri_sembilan_holidays = holidays.Malaysia(
            years=years,
            subdiv="NSN",
        )
        self.pahang_holidays = holidays.Malaysia(years=years, subdiv="PHG")
        self.perak_holidays = holidays.Malaysia(years=years, subdiv="PRK")
        self.perlis_holidays = holidays.Malaysia(years=years, subdiv="PLS")
        self.penang_holidays = holidays.Malaysia(years=years, subdiv="PNG")
        self.sabah_holidays = holidays.Malaysia(years=years, subdiv="SBH")
        self.sarawak_holidays = holidays.Malaysia(years=years, subdiv="SWK")
        self.selangor_holidays = holidays.Malaysia(years=years, subdiv="SGR")
        self.terengganu_holidays = holidays.Malaysia(years=years, subdiv="TRG")
        self.kuala_lumpur_holidays = holidays.Malaysia(
            years=years, subdiv="KUL"
        )
        self.labuan_holidays = holidays.Malaysia(years=years, subdiv="LBN")
        self.putrajaya_holidays = holidays.Malaysia(years=years, subdiv="PJY")

    def test_Malaysia_Wikipedia(self):
        # reproduce table at
        # https://en.wikipedia.org/wiki/Public_holidays_in_Malaysia
        # as of 19-Sep-21
        columns = [
            "JHR",  # "Johor"
            "KDH",  # "Kedah"
            "KTN",  # "Kelantan"
            "KUL",  # "FT Kuala Lumpur"
            "LBN",  # "FT Labuan"
            "MLK",  # "Malacca"
            "NSN",  # "Negeri Sembilan"
            "PHG",  # "Pahang"
            "PNG",  # "Penang"
            "PRK",  # "Perak"
            "PLS",  # "Perlis"
            "PJY",  # "FT Putrajaya"
            "SBH",  # "Sabah"
            "SWK",  # "Sarawak"
            "SGR",  # "Selangor"
            "TRG",  # "Terengganu"
        ]
        rows = {
            date(2021, JAN, 1): [
                0,
                0,
                0,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                0,
                1,
                1,
                1,
                1,
                0,
            ],
            date(2021, JAN, 14): [
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, JAN, 28): [
                1,
                0,
                0,
                1,
                0,
                0,
                1,
                0,
                1,
                1,
                0,
                1,
                0,
                0,
                1,
                0,
            ],
            date(2021, FEB, 1): [
                0,
                0,
                0,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
            ],
            date(2021, FEB, 12): [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            date(2021, FEB, 13): [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            date(2021, FEB, 14): [
                1,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
            date(2021, MAR, 4): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
            date(2021, MAR, 11): [
                0,
                1,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                1,
            ],
            date(2021, MAR, 23): [
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, APR, 2): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                1,
                0,
                0,
            ],
            date(2021, APR, 13): [
                1,
                1,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, APR, 15): [
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, APR, 26): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
            date(2021, APR, 29): [
                0,
                0,
                1,
                1,
                1,
                0,
                0,
                1,
                1,
                1,
                1,
                1,
                0,
                0,
                1,
                1,
            ],
            date(2021, MAY, 1): [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            date(2021, MAY, 2): [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
            date(2021, MAY, 13): [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            date(2021, MAY, 14): [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            date(2021, MAY, 16): [
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, MAY, 22): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, MAY, 26): [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            date(2021, MAY, 30): [
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
            ],
            date(2021, MAY, 31): [
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
            ],
            date(2021, JUN, 1): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
            ],
            date(2021, JUN, 2): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
            ],
            date(2021, JUN, 7): [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            date(2021, JUN, 20): [
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, JUL, 7): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, JUL, 10): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, JUL, 17): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, JUL, 19): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
            date(2021, JUL, 20): [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            date(2021, JUL, 21): [
                0,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                1,
            ],
            date(2021, JUL, 22): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
            ],
            date(2021, JUL, 30): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, AUG, 10): [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            date(2021, AUG, 24): [
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, AUG, 31): [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            date(2021, SEP, 13): [
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, SEP, 16): [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            date(2021, OCT, 2): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
            ],
            date(2021, OCT, 9): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
            ],
            date(2021, OCT, 19): [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            date(2021, NOV, 4): [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                0,
                1,
                1,
            ],
            date(2021, NOV, 5): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, NOV, 11): [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, NOV, 12): [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            date(2021, DEC, 3): [
                0,
                0,
                0,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
            ],
            date(2021, DEC, 11): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
            ],
            date(2021, DEC, 24): [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
            ],
            date(2021, DEC, 25): [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            date(2021, DEC, 26): [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
        }

        for col, state in enumerate(columns):
            my_holidays = holidays.Malaysia(years=2021, subdiv=state)
            # check if all holidays are in here
            for hol_date, is_holiday in rows.items():
                if is_holiday[col]:
                    self.assertIn(hol_date, my_holidays)
                else:
                    self.assertNotIn(hol_date, my_holidays)

    def test_Malaysia(self):
        # Federal Public Holidays

        # https://www.timeanddate.com/holidays/malaysia/2001
        self.assertIn(date(2001, 1, 24), self.holidays)
        self.assertIn(date(2001, 1, 25), self.holidays)
        self.assertIn(date(2001, 3, 6), self.holidays)
        self.assertIn(date(2001, 3, 26), self.holidays)
        self.assertIn(date(2001, 5, 1), self.holidays)
        self.assertIn(date(2001, 5, 7), self.holidays)
        self.assertIn(date(2001, 6, 2), self.holidays)
        self.assertIn(date(2001, 6, 4), self.holidays)
        self.assertIn(date(2001, 8, 31), self.holidays)
        self.assertIn(date(2001, 11, 14), self.holidays)
        self.assertIn(date(2001, 12, 17), self.holidays)
        self.assertIn(date(2001, 12, 18), self.holidays)
        self.assertIn(date(2001, 12, 25), self.holidays)

    def test_special_holidays(self):
        self.assertIn(date(1999, 11, 29), self.holidays)
        self.assertIn(date(2018, 5, 9), self.holidays)
        self.assertIn(date(2019, 7, 30), self.holidays)

    def test_JHR_holidays(self):
        state_holidays = self.johor_holidays

        # Birthday of the Sultan of Johor
        self.assertIn(date(2015, 3, 23), state_holidays)
        self.assertIn(date(2018, 3, 23), state_holidays)
        self.assertIn(date(2020, 3, 23), state_holidays)
        self.assertIn(date(2022, 3, 23), state_holidays)
        self.assertNotIn(date(2014, 3, 23), state_holidays)
        # Hari Hol of Sultan Iskandar of Johor
        self.assertIn(date(2018, 10, 15), state_holidays)
        self.assertIn(date(2019, 10, 5), state_holidays)
        self.assertIn(date(2020, 9, 24), state_holidays)
        self.assertIn(date(2021, 9, 13), state_holidays)
        self.assertIn(date(2022, 9, 3), state_holidays)
        self.assertIn(date(2023, 8, 22), state_holidays)
        self.assertNotIn(date(2010, 1, 21), state_holidays)
        # Thaipusam
        self.assertIn(date(2018, 1, 31), state_holidays)
        self.assertIn(date(2019, 1, 21), state_holidays)
        self.assertIn(date(2020, 2, 8), state_holidays)
        self.assertIn(date(2021, 1, 28), state_holidays)
        self.assertIn(date(2022, 1, 18), state_holidays)
        self.assertIn(date(2023, 2, 5), state_holidays)
        # Beginning of Ramadan
        self.assertIn(date(2018, 5, 17), state_holidays)
        self.assertIn(date(2019, 5, 6), state_holidays)
        self.assertIn(date(2020, 4, 24), state_holidays)
        self.assertIn(date(2020, 4, 26), state_holidays)  # In lieu
        self.assertIn(date(2021, 4, 13), state_holidays)
        self.assertIn(date(2022, 4, 3), state_holidays)
        self.assertIn(date(2023, 3, 23), state_holidays)
        # Labour Day Holiday
        self.assertIn(date(2022, 5, 4), state_holidays)
        # Malaysia Day [In lieu]
        self.assertNotIn(date(2018, 9, 17), state_holidays)

    def test_KDH_holidays(self):
        state_holidays = self.kedah_holidays

        # Hari Raya Haji
        self.assertIn(date(2018, 8, 22), state_holidays)
        self.assertIn(date(2019, 8, 11), state_holidays)
        self.assertIn(date(2020, 7, 31), state_holidays)
        self.assertIn(date(2021, 7, 20), state_holidays)
        self.assertIn(date(2022, 7, 10), state_holidays)
        self.assertIn(date(2023, 6, 28), state_holidays)
        # Hari Raya Haji Holiday
        self.assertIn(date(2018, 8, 23), state_holidays)
        self.assertIn(date(2019, 8, 12), state_holidays)
        self.assertIn(date(2020, 8, 1), state_holidays)
        self.assertIn(date(2020, 8, 2), state_holidays)  # In lieu
        self.assertIn(date(2021, 7, 21), state_holidays)
        self.assertIn(date(2022, 7, 11), state_holidays)
        self.assertIn(date(2023, 6, 29), state_holidays)
        # Isra and Mi'raj
        self.assertIn(date(2018, 4, 14), state_holidays)
        self.assertIn(date(2019, 4, 3), state_holidays)
        self.assertIn(date(2020, 3, 22), state_holidays)
        self.assertIn(date(2021, 3, 11), state_holidays)
        self.assertIn(date(2022, 3, 1), state_holidays)
        self.assertIn(date(2023, 2, 18), state_holidays)
        # Beginning of Ramadan
        self.assertIn(date(2018, 5, 17), state_holidays)
        self.assertIn(date(2019, 5, 6), state_holidays)
        self.assertIn(date(2020, 4, 24), state_holidays)
        self.assertIn(date(2020, 4, 26), state_holidays)  # In lieu
        self.assertIn(date(2021, 4, 13), state_holidays)
        self.assertIn(date(2022, 4, 3), state_holidays)
        self.assertIn(date(2023, 3, 23), state_holidays)
        # Thaipusam in 2022
        self.assertIn(date(2022, 1, 18), state_holidays)
        # Malaysia Day [In lieu]
        self.assertNotIn(date(2018, 9, 17), state_holidays)

    def test_KTN_holidays(self):
        state_holidays = self.kelantan_holidays

        # Birthday of the Sultan of Kelantan
        self.assertIn(date(2018, 11, 11), state_holidays)
        self.assertIn(date(2019, 11, 12), state_holidays)
        self.assertIn(date(2020, 11, 11), state_holidays)
        self.assertNotIn(date(2001, 11, 11), state_holidays)
        # Hari Raya Haji
        self.assertIn(date(2018, 8, 22), state_holidays)
        self.assertIn(date(2019, 8, 11), state_holidays)
        self.assertIn(date(2020, 7, 31), state_holidays)
        self.assertIn(date(2021, 7, 20), state_holidays)
        self.assertIn(date(2022, 7, 10), state_holidays)
        self.assertIn(date(2023, 6, 28), state_holidays)
        # Hari Raya Haji Holiday
        self.assertIn(date(2018, 8, 23), state_holidays)
        self.assertIn(date(2019, 8, 12), state_holidays)
        self.assertIn(date(2020, 8, 1), state_holidays)
        self.assertIn(date(2020, 8, 2), state_holidays)  # In lieu
        self.assertIn(date(2021, 7, 21), state_holidays)
        self.assertIn(date(2022, 7, 11), state_holidays)
        self.assertIn(date(2023, 6, 29), state_holidays)
        # Nuzul Al-Quran Day
        self.assertIn(date(2018, 6, 2), state_holidays)
        self.assertIn(date(2018, 6, 3), state_holidays)  # In lieu
        self.assertIn(date(2019, 5, 22), state_holidays)
        self.assertIn(date(2020, 5, 10), state_holidays)
        self.assertIn(date(2021, 4, 29), state_holidays)
        self.assertIn(date(2022, 4, 19), state_holidays)
        self.assertIn(date(2023, 4, 8), state_holidays)
        self.assertIn(date(2023, 4, 9), state_holidays)  # In lieu
        # Labour Day Holiday
        self.assertIn(date(2022, 5, 4), state_holidays)
        # Malaysia Day [In lieu]
        self.assertNotIn(date(2018, 9, 17), state_holidays)

    def test_NSN_holidays(self):
        state_holidays = self.negeri_sembilan_holidays

        # New Year's Day
        self.assertIn(date(2018, 1, 1), state_holidays)
        self.assertIn(date(2020, 1, 1), state_holidays)
        self.assertIn(date(2022, 1, 1), state_holidays)
        self.assertIn(date(2023, 1, 2), state_holidays)  # In lieu
        # Isra and Mi'raj
        self.assertIn(date(2018, 4, 14), state_holidays)
        self.assertIn(date(2019, 4, 3), state_holidays)
        self.assertIn(date(2020, 3, 22), state_holidays)
        self.assertIn(date(2021, 3, 11), state_holidays)
        self.assertIn(date(2022, 3, 1), state_holidays)
        self.assertIn(date(2023, 2, 18), state_holidays)
        # Birthday of the Sultan of Negeri Sembilan
        self.assertIn(date(2018, 1, 14), state_holidays)
        self.assertIn(date(2023, 1, 14), state_holidays)
        self.assertNotIn(date(2008, 1, 14), state_holidays)
        # Thaipusam
        self.assertIn(date(2018, 1, 31), state_holidays)
        self.assertIn(date(2019, 1, 21), state_holidays)
        self.assertIn(date(2020, 2, 8), state_holidays)
        self.assertIn(date(2021, 1, 28), state_holidays)
        self.assertIn(date(2022, 1, 18), state_holidays)
        self.assertIn(date(2023, 2, 5), state_holidays)

    def test_PNG_holidays(self):
        state_holidays = self.penang_holidays

        # New Year's Day
        self.assertIn(date(2018, 1, 1), state_holidays)
        self.assertIn(date(2020, 1, 1), state_holidays)
        self.assertIn(date(2022, 1, 1), state_holidays)
        self.assertIn(date(2023, 1, 2), state_holidays)  # In lieu
        # Nuzul Al-Quran Day
        self.assertIn(date(2018, 6, 2), state_holidays)
        self.assertIn(date(2019, 5, 22), state_holidays)
        self.assertIn(date(2020, 5, 10), state_holidays)
        self.assertIn(date(2020, 5, 11), state_holidays)  # In lieu
        self.assertIn(date(2021, 4, 29), state_holidays)
        self.assertIn(date(2022, 4, 19), state_holidays)
        self.assertIn(date(2023, 4, 8), state_holidays)
        # Thaipusam
        self.assertIn(date(2018, 1, 31), state_holidays)
        self.assertIn(date(2019, 1, 21), state_holidays)
        self.assertIn(date(2020, 2, 8), state_holidays)
        self.assertIn(date(2021, 1, 28), state_holidays)
        self.assertIn(date(2022, 1, 18), state_holidays)
        self.assertIn(date(2023, 2, 5), state_holidays)
        self.assertIn(date(2023, 2, 6), state_holidays)  # In lieu
        # George Town Heritage Day
        self.assertIn(date(2009, 7, 7), state_holidays)
        self.assertIn(date(2020, 7, 7), state_holidays)
        self.assertNotIn(date(2008, 7, 7), state_holidays)
        # Birthday of the Governor of Penang
        self.assertIn(date(2017, 7, 8), state_holidays)
        self.assertIn(date(2019, 7, 13), state_holidays)
        self.assertIn(date(2020, 7, 11), state_holidays)
        self.assertIn(date(2022, 7, 9), state_holidays)
        self.assertIn(date(2023, 7, 8), state_holidays)

    def test_PRK_holidays(self):
        state_holidays = self.perak_holidays

        # New Year's Day
        self.assertIn(date(2018, 1, 1), state_holidays)
        self.assertIn(date(2020, 1, 1), state_holidays)
        self.assertIn(date(2022, 1, 1), state_holidays)
        self.assertIn(date(2023, 1, 2), state_holidays)  # In lieu
        # Nuzul Al-Quran Day
        self.assertIn(date(2018, 6, 2), state_holidays)
        self.assertIn(date(2019, 5, 22), state_holidays)
        self.assertIn(date(2020, 5, 10), state_holidays)
        self.assertIn(date(2020, 5, 11), state_holidays)  # In lieu
        self.assertIn(date(2021, 4, 29), state_holidays)
        self.assertIn(date(2022, 4, 19), state_holidays)
        self.assertIn(date(2023, 4, 8), state_holidays)
        # Thaipusam
        self.assertIn(date(2018, 1, 31), state_holidays)
        self.assertIn(date(2019, 1, 21), state_holidays)
        self.assertIn(date(2020, 2, 8), state_holidays)
        self.assertIn(date(2021, 1, 28), state_holidays)
        self.assertIn(date(2022, 1, 18), state_holidays)
        self.assertIn(date(2023, 2, 5), state_holidays)
        self.assertIn(date(2023, 2, 6), state_holidays)  # In lieu
        # Birthday of the Sultan of Perak
        self.assertIn(date(2009, 11, 27), state_holidays)
        self.assertIn(date(2017, 11, 27), state_holidays)
        self.assertIn(date(2018, 11, 2), state_holidays)
        self.assertIn(date(2019, 11, 1), state_holidays)
        self.assertIn(date(2020, 11, 6), state_holidays)
        self.assertIn(date(2021, 11, 5), state_holidays)
        self.assertIn(date(2022, 11, 4), state_holidays)
        self.assertNotIn(date(2018, 11, 27), state_holidays)

    def test_SBH_holidays(self):
        state_holidays = self.sabah_holidays

        # New Year's Day
        self.assertIn(date(2018, 1, 1), state_holidays)
        self.assertIn(date(2020, 1, 1), state_holidays)
        self.assertIn(date(2022, 1, 1), state_holidays)
        self.assertIn(date(2023, 1, 2), state_holidays)  # In lieu
        # Pesta Kaamatan
        self.assertIn(date(2018, 5, 30), state_holidays)
        self.assertIn(date(2019, 5, 31), state_holidays)
        # Good Friday
        self.assertIn(date(2018, 3, 30), state_holidays)
        self.assertIn(date(2020, 4, 10), state_holidays)
        self.assertIn(date(2021, 4, 2), state_holidays)
        self.assertIn(date(2022, 4, 15), state_holidays)
        self.assertIn(date(2023, 4, 7), state_holidays)
        # Birthday of the Governor of Sabah
        self.assertIn(date(2017, 10, 7), state_holidays)
        self.assertIn(date(2018, 10, 6), state_holidays)
        self.assertIn(date(2019, 10, 5), state_holidays)
        self.assertIn(date(2020, 10, 3), state_holidays)
        # Christmas Eve
        self.assertIn(date(2019, 12, 24), state_holidays)
        self.assertIn(date(2020, 12, 24), state_holidays)
        self.assertNotIn(date(2018, 12, 24), state_holidays)

    def test_SWK_holidays(self):
        state_holidays = self.sarawak_holidays

        # New Year's Day
        self.assertIn(date(2018, 1, 1), state_holidays)
        self.assertIn(date(2020, 1, 1), state_holidays)
        self.assertIn(date(2022, 1, 1), state_holidays)
        self.assertIn(date(2023, 1, 2), state_holidays)  # In lieu
        # Good Friday
        self.assertIn(date(2018, 3, 30), state_holidays)
        self.assertIn(date(2020, 4, 10), state_holidays)
        self.assertIn(date(2021, 4, 2), state_holidays)
        self.assertIn(date(2022, 4, 15), state_holidays)
        self.assertIn(date(2023, 4, 7), state_holidays)
        # Gawai Dayak
        self.assertIn(date(2018, 6, 1), state_holidays)
        self.assertIn(date(2018, 6, 2), state_holidays)
        self.assertIn(date(2020, 6, 2), state_holidays)
        self.assertIn(date(2020, 6, 2), state_holidays)
        # Birthday of the Governor of Sarawak
        self.assertIn(date(2018, 10, 13), state_holidays)
        self.assertIn(date(2019, 10, 12), state_holidays)
        self.assertIn(date(2020, 10, 10), state_holidays)
        self.assertIn(date(2021, 10, 9), state_holidays)
        self.assertIn(date(2022, 10, 8), state_holidays)
        # Sarawak Day
        self.assertIn(date(2017, 7, 22), state_holidays)
        self.assertIn(date(2018, 7, 22), state_holidays)
        self.assertIn(date(2018, 7, 23), state_holidays)  # In lieu
        self.assertIn(date(2022, 7, 22), state_holidays)
        self.assertNotIn(date(2014, 7, 22), state_holidays)
        # Deepavali
        self.assertNotIn(date(2018, 11, 6), state_holidays)
        self.assertNotIn(date(2022, 10, 24), state_holidays)

    def test_SGR_holidays(self):
        state_holidays = self.selangor_holidays

        # New Year's Day
        self.assertIn(date(2018, 1, 1), state_holidays)
        self.assertIn(date(2020, 1, 1), state_holidays)
        self.assertIn(date(2022, 1, 1), state_holidays)
        self.assertIn(date(2023, 1, 2), state_holidays)  # In lieu
        # Nuzul Al-Quran Day
        self.assertIn(date(2018, 6, 2), state_holidays)
        self.assertIn(date(2019, 5, 22), state_holidays)
        self.assertIn(date(2020, 5, 10), state_holidays)
        self.assertIn(date(2020, 5, 11), state_holidays)  # In lieu
        self.assertIn(date(2021, 4, 29), state_holidays)
        self.assertIn(date(2022, 4, 19), state_holidays)
        self.assertIn(date(2023, 4, 8), state_holidays)
        # Thaipusam
        self.assertIn(date(2018, 1, 31), state_holidays)
        self.assertIn(date(2019, 1, 21), state_holidays)
        self.assertIn(date(2020, 2, 8), state_holidays)
        self.assertIn(date(2021, 1, 28), state_holidays)
        self.assertIn(date(2022, 1, 18), state_holidays)
        self.assertIn(date(2023, 2, 5), state_holidays)
        self.assertIn(date(2023, 2, 6), state_holidays)  # In lieu
        # Birthday of The Sultan of Selangor
        self.assertIn(date(2018, 12, 11), state_holidays)
        self.assertIn(date(2019, 12, 11), state_holidays)

    def test_TRG_holidays(self):
        state_holidays = self.terengganu_holidays

        # Arafat Day
        self.assertIn(date(2018, 8, 21), state_holidays)
        self.assertIn(date(2019, 8, 10), state_holidays)
        self.assertIn(date(2019, 8, 13), state_holidays)  # In lieu
        self.assertIn(date(2020, 7, 30), state_holidays)
        self.assertIn(date(2021, 7, 19), state_holidays)
        self.assertIn(date(2022, 7, 9), state_holidays)
        self.assertIn(date(2022, 7, 12), state_holidays)  # In lieu
        self.assertIn(date(2023, 6, 27), state_holidays)
        # Hari Raya Haji
        self.assertIn(date(2018, 8, 22), state_holidays)
        self.assertIn(date(2019, 8, 11), state_holidays)
        self.assertIn(date(2020, 7, 31), state_holidays)
        self.assertIn(date(2021, 7, 20), state_holidays)
        self.assertIn(date(2022, 7, 10), state_holidays)
        self.assertIn(date(2023, 6, 28), state_holidays)
        # Hari Raya Haji Holiday
        self.assertIn(date(2018, 8, 23), state_holidays)
        self.assertIn(date(2019, 8, 12), state_holidays)
        self.assertIn(date(2020, 8, 1), state_holidays)
        self.assertIn(date(2020, 8, 2), state_holidays)  # In lieu
        self.assertIn(date(2021, 7, 21), state_holidays)
        self.assertIn(date(2022, 7, 11), state_holidays)
        self.assertIn(date(2023, 6, 29), state_holidays)
        # Isra and Mi'raj
        self.assertIn(date(2020, 3, 22), state_holidays)
        self.assertIn(date(2021, 3, 11), state_holidays)
        self.assertIn(date(2022, 3, 1), state_holidays)
        self.assertIn(date(2023, 2, 18), state_holidays)
        self.assertIn(date(2023, 2, 19), state_holidays)  # In lieu
        self.assertNotIn(date(2018, 4, 14), state_holidays)
        self.assertNotIn(date(2019, 4, 3), state_holidays)
        # Nuzul Al-Quran Day
        self.assertIn(date(2018, 6, 2), state_holidays)
        self.assertIn(date(2018, 6, 3), state_holidays)  # In lieu
        self.assertIn(date(2019, 5, 22), state_holidays)
        self.assertIn(date(2020, 5, 10), state_holidays)
        self.assertIn(date(2021, 4, 29), state_holidays)
        self.assertIn(date(2022, 4, 19), state_holidays)
        self.assertIn(date(2023, 4, 8), state_holidays)
        self.assertIn(date(2023, 4, 9), state_holidays)  # In lieu
        # Anniversary of the Installation of the Sultan of Terengganu
        self.assertIn(date(2000, 3, 4), state_holidays)
        self.assertIn(date(2018, 3, 4), state_holidays)
        self.assertIn(date(2019, 3, 4), state_holidays)
        self.assertNotIn(date(1999, 3, 4), state_holidays)
        # Birthday of the Sultan of Terengganu
        self.assertIn(date(2020, 4, 26), state_holidays)
        self.assertIn(date(2022, 4, 26), state_holidays)
        self.assertNotIn(date(1999, 4, 26), state_holidays)
        # Labour Day Holiday
        self.assertIn(date(2022, 5, 4), state_holidays)
        # Malaysia Day [In lieu]
        self.assertNotIn(date(2018, 9, 17), state_holidays)

    def test_KUL_holidays(self):
        state_holidays = self.kuala_lumpur_holidays

        # New Year's Day
        self.assertIn(date(2018, 1, 1), state_holidays)
        self.assertIn(date(2020, 1, 1), state_holidays)
        self.assertIn(date(2022, 1, 1), state_holidays)
        self.assertIn(date(2023, 1, 2), state_holidays)  # In lieu
        # Federal Territory Day
        self.assertIn(date(2018, 2, 1), state_holidays)
        self.assertIn(date(2019, 2, 1), state_holidays)
        self.assertNotIn(date(1970, 2, 1), state_holidays)
        # Thaipusam
        self.assertIn(date(2018, 1, 31), state_holidays)
        self.assertIn(date(2019, 1, 21), state_holidays)
        self.assertIn(date(2020, 2, 8), state_holidays)
        self.assertIn(date(2021, 1, 28), state_holidays)
        self.assertIn(date(2022, 1, 18), state_holidays)
        self.assertIn(date(2023, 2, 5), state_holidays)
        # Malaysia Cup Holiday
        self.assertIn(date(2021, 12, 3), state_holidays)

    def test_MLK_holidays(self):
        state_holidays = self.malacca_holidays

        # New Year's Day
        self.assertIn(date(2018, 1, 1), state_holidays)
        self.assertIn(date(2020, 1, 1), state_holidays)
        self.assertIn(date(2022, 1, 1), state_holidays)
        self.assertIn(date(2023, 1, 2), state_holidays)  # In lieu
        # Beginning of Ramadan
        self.assertIn(date(2018, 5, 17), state_holidays)
        self.assertIn(date(2019, 5, 6), state_holidays)
        self.assertIn(date(2020, 4, 24), state_holidays)
        self.assertIn(date(2021, 4, 13), state_holidays)
        self.assertIn(date(2022, 4, 3), state_holidays)
        self.assertIn(date(2022, 4, 4), state_holidays)  # In lieu
        self.assertIn(date(2023, 3, 23), state_holidays)
        # Declaration of Malacca as a Historical City
        self.assertIn(date(2018, 4, 15), state_holidays)
        self.assertIn(date(2019, 4, 15), state_holidays)
        self.assertNotIn(date(1985, 4, 15), state_holidays)
        # Birthday of the Governor of Malacca
        self.assertIn(date(2018, 10, 12), state_holidays)
        self.assertIn(date(2019, 10, 11), state_holidays)
        self.assertIn(date(2020, 8, 24), state_holidays)
        self.assertIn(date(2021, 8, 24), state_holidays)
        self.assertIn(date(2022, 8, 24), state_holidays)
        self.assertNotIn(date(2019, 8, 24), state_holidays)
        self.assertNotIn(date(2020, 10, 9), state_holidays)

    def test_LBN_holidays(self):
        state_holidays = self.labuan_holidays

        # New Year's Day
        self.assertIn(date(2018, 1, 1), state_holidays)
        self.assertIn(date(2020, 1, 1), state_holidays)
        self.assertIn(date(2022, 1, 1), state_holidays)
        self.assertIn(date(2023, 1, 2), state_holidays)  # In lieu
        # Federal Territory Day
        self.assertIn(date(2020, 2, 1), state_holidays)
        self.assertIn(date(2022, 2, 1), state_holidays)
        self.assertNotIn(date(1970, 2, 1), state_holidays)
        # Pesta Kaamatan
        self.assertIn(date(2018, 5, 30), state_holidays)
        self.assertIn(date(2019, 5, 31), state_holidays)
        # Nuzul Al-Quran Day
        self.assertIn(date(2018, 6, 2), state_holidays)
        self.assertIn(date(2019, 5, 22), state_holidays)
        self.assertIn(date(2020, 5, 10), state_holidays)
        self.assertIn(date(2020, 5, 11), state_holidays)  # In lieu
        self.assertIn(date(2021, 4, 29), state_holidays)
        self.assertIn(date(2022, 4, 19), state_holidays)
        self.assertIn(date(2023, 4, 8), state_holidays)
        # Malaysia Cup Holiday
        self.assertIn(date(2021, 12, 3), state_holidays)

    def test_PHG_holidays(self):
        state_holidays = self.pahang_holidays

        # New Year's Day
        self.assertIn(date(2018, 1, 1), state_holidays)
        self.assertIn(date(2020, 1, 1), state_holidays)
        self.assertIn(date(2022, 1, 1), state_holidays)
        self.assertIn(date(2023, 1, 2), state_holidays)  # In lieu
        # Nuzul Al-Quran Day
        self.assertIn(date(2018, 6, 2), state_holidays)
        self.assertIn(date(2019, 5, 22), state_holidays)
        self.assertIn(date(2020, 5, 10), state_holidays)
        self.assertIn(date(2020, 5, 11), state_holidays)  # In lieu
        self.assertIn(date(2021, 4, 29), state_holidays)
        self.assertIn(date(2022, 4, 19), state_holidays)
        self.assertIn(date(2023, 4, 8), state_holidays)
        # Hari Hol of Pahang
        self.assertIn(date(2001, 5, 7), state_holidays)
        self.assertIn(date(2018, 5, 7), state_holidays)
        self.assertIn(date(2019, 5, 7), state_holidays)
        self.assertIn(date(2020, 5, 22), state_holidays)
        self.assertIn(date(2021, 5, 22), state_holidays)
        self.assertIn(date(2022, 5, 22), state_holidays)
        self.assertNotIn(date(2010, 5, 22), state_holidays)
        self.assertNotIn(date(2021, 5, 7), state_holidays)
        self.assertNotEqual(
            state_holidays[date(2020, 5, 7)], "Hari Hol of Pahang"
        )

    def test_PLS_holidays(self):
        state_holidays = self.perlis_holidays

        # Hari Raya Haji
        self.assertIn(date(2018, 8, 22), state_holidays)
        self.assertIn(date(2019, 8, 11), state_holidays)
        self.assertIn(date(2020, 7, 31), state_holidays)
        self.assertIn(date(2021, 7, 20), state_holidays)
        self.assertIn(date(2022, 7, 10), state_holidays)
        self.assertIn(date(2023, 6, 28), state_holidays)
        # Hari Raya Haji Holiday
        self.assertIn(date(2018, 8, 23), state_holidays)
        self.assertIn(date(2019, 8, 12), state_holidays)
        self.assertIn(date(2019, 8, 13), state_holidays)  # In lieu
        self.assertIn(date(2020, 8, 1), state_holidays)
        self.assertIn(date(2021, 7, 21), state_holidays)
        self.assertIn(date(2022, 7, 11), state_holidays)
        self.assertIn(date(2022, 7, 12), state_holidays)  # In lieu
        self.assertIn(date(2023, 6, 29), state_holidays)
        # Isra and Mi'raj
        self.assertIn(date(2018, 4, 14), state_holidays)
        self.assertIn(date(2019, 4, 3), state_holidays)
        self.assertIn(date(2020, 3, 22), state_holidays)
        self.assertIn(date(2020, 3, 23), state_holidays)  # In lieu
        self.assertIn(date(2021, 3, 11), state_holidays)
        self.assertIn(date(2022, 3, 1), state_holidays)
        self.assertIn(date(2023, 2, 18), state_holidays)
        # Nuzul Al-Quran Day
        self.assertIn(date(2018, 6, 2), state_holidays)
        self.assertIn(date(2019, 5, 22), state_holidays)
        self.assertIn(date(2020, 5, 10), state_holidays)
        self.assertIn(date(2020, 5, 11), state_holidays)  # In lieu
        self.assertIn(date(2021, 4, 29), state_holidays)
        self.assertIn(date(2022, 4, 19), state_holidays)
        self.assertIn(date(2023, 4, 8), state_holidays)
        # Birthday of The Raja of Perlis
        self.assertIn(date(2000, 5, 17), state_holidays)
        self.assertIn(date(2010, 5, 17), state_holidays)
        self.assertIn(date(2017, 5, 17), state_holidays)
        self.assertIn(date(2018, 7, 17), state_holidays)
        self.assertIn(date(2022, 7, 17), state_holidays)
        self.assertNotIn(date(2017, 7, 17), state_holidays)
        self.assertNotIn(date(2018, 5, 17), state_holidays)

    def test_PJY_holidays(self):
        state_holidays = self.putrajaya_holidays

        # New Year's Day
        self.assertIn(date(2018, 1, 1), state_holidays)
        self.assertIn(date(2020, 1, 1), state_holidays)
        self.assertIn(date(2022, 1, 1), state_holidays)
        self.assertIn(date(2023, 1, 2), state_holidays)  # In lieu
        # Nuzul Al-Quran Day
        self.assertIn(date(2018, 6, 2), state_holidays)
        self.assertIn(date(2019, 5, 22), state_holidays)
        self.assertIn(date(2020, 5, 10), state_holidays)
        self.assertIn(date(2020, 5, 11), state_holidays)  # In lieu
        self.assertIn(date(2021, 4, 29), state_holidays)
        self.assertIn(date(2022, 4, 19), state_holidays)
        self.assertIn(date(2023, 4, 8), state_holidays)
        # Thaipusam
        self.assertIn(date(2018, 1, 31), state_holidays)
        self.assertIn(date(2019, 1, 21), state_holidays)
        self.assertIn(date(2020, 2, 8), state_holidays)
        self.assertIn(date(2021, 1, 28), state_holidays)
        self.assertIn(date(2022, 1, 18), state_holidays)
        self.assertIn(date(2023, 2, 5), state_holidays)
        self.assertIn(date(2023, 2, 6), state_holidays)  # In lieu
        # Federal Territory Day
        self.assertIn(date(2018, 2, 1), state_holidays)
        self.assertIn(date(2019, 2, 1), state_holidays)
        self.assertNotIn(date(1970, 2, 1), state_holidays)
        # Malaysia Cup Holiday
        self.assertIn(date(2021, 12, 3), state_holidays)

    def test_aliases(self):
        holidays1 = holidays.MY()
        holidays2 = holidays.MYS()
        self.assertEqual(list(holidays1), list(holidays2))
