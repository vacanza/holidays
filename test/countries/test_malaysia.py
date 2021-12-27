# -*- coding: utf-8 -*-

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
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
)


class TestMalaysia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Malaysia()

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
        }

        for col, state in enumerate(columns):
            my_holidays = holidays.Malaysia(years=2021, state=state)
            # check if all holidays are in here
            tot_holidays = 0
            for hol_date, is_holiday in rows.items():
                if is_holiday[col]:
                    self.assertIn(hol_date, my_holidays)
                    tot_holidays += 1
            # check that there are no extra ones
            assert len(my_holidays) == tot_holidays

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

    def test_JHR_holidays(self):
        Johor_holidays = holidays.MY(years=2015, state="JHR")
        # Birthday of the Sultan of Johor
        self.assertIn(date(2015, 3, 23), Johor_holidays)
        self.assertIn(date(2016, 3, 23), Johor_holidays)
        self.assertIn(date(2020, 3, 23), Johor_holidays)
        self.assertIn(date(2022, 3, 23), Johor_holidays)
        self.assertNotIn(date(2001, 3, 23), Johor_holidays)
        self.assertNotIn(date(1990, 3, 23), Johor_holidays)

    def test_KDH_holidays(self):
        Kedah_holidays = holidays.MY(
            years=[2018, 2019, 2020, 2021, 2022], state="KDH"
        )
        self.assertIn(date(2018, 8, 22), Kedah_holidays)
        self.assertIn(date(2019, 8, 11), Kedah_holidays)
        self.assertIn(date(2020, 7, 31), Kedah_holidays)
        self.assertIn(date(2021, 7, 20), Kedah_holidays)
        self.assertIn(date(2022, 7, 9), Kedah_holidays)

    def test_KTN_holidays(self):
        Kelantan_holidays = holidays.MY(
            years=[2018, 2019, 2020, 2021, 2022], state="KTN"
        )
        self.assertIn(date(2018, 11, 11), Kelantan_holidays)
        self.assertIn(date(2019, 11, 12), Kelantan_holidays)
        self.assertIn(date(2020, 11, 11), Kelantan_holidays)
        self.assertIn(date(2029, 11, 12), Kelantan_holidays)

    def test_NSN_holidays(self):
        Negeri_Sembilan_holidays = holidays.MY(
            years=[2018, 2019, 2020, 2021, 2022], state="NSN"
        )
        self.assertIn(date(2018, 1, 14), Negeri_Sembilan_holidays)
        self.assertIn(date(2023, 1, 14), Negeri_Sembilan_holidays)
        self.assertNotIn(date(2020, 11, 11), Negeri_Sembilan_holidays)
        self.assertNotIn(date(2029, 11, 12), Negeri_Sembilan_holidays)

    def test_PNG_holidays(self):
        Penang_holidays = holidays.MY(
            years=[2023, 2024, 2019, 2020, 2021, 2022], state="PNG"
        )
        self.assertIn(date(2020, 7, 7), Penang_holidays)
        self.assertIn(date(2020, 7, 11), Penang_holidays)
        self.assertIn(date(2019, 7, 13), Penang_holidays)
        self.assertIn(date(2017, 7, 8), Penang_holidays)
        self.assertIn(date(2024, 7, 13), Penang_holidays)
        self.assertIn(date(2023, 7, 8), Penang_holidays)

    def test_PRK_holidays(self):
        Perak_holidays = holidays.MY(
            years=[2013, 2018, 2019, 2020, 2021, 2022], state="PRK"
        )
        self.assertIn(date(2018, 11, 2), Perak_holidays)
        self.assertIn(date(2019, 11, 1), Perak_holidays)
        self.assertIn(date(2020, 11, 6), Perak_holidays)
        self.assertIn(date(2021, 11, 5), Perak_holidays)
        self.assertIn(date(2022, 11, 4), Perak_holidays)
        self.assertNotIn(date(2023, 11, 27), Perak_holidays)
        self.assertIn(date(2013, 11, 27), Perak_holidays)

    def test_SBH_holidays(self):
        Sabah_holidays = holidays.MY(
            years=[2017, 2018, 2019, 2020, 2021, 2022], state="SBH"
        )
        self.assertIn(date(2018, 5, 30), Sabah_holidays)
        self.assertIn(date(2018, 5, 31), Sabah_holidays)
        self.assertIn(date(2020, 5, 31), Sabah_holidays)
        self.assertIn(date(2020, 5, 30), Sabah_holidays)
        self.assertIn(date(2017, 10, 7), Sabah_holidays)
        self.assertIn(date(2018, 10, 6), Sabah_holidays)
        self.assertIn(date(2019, 10, 5), Sabah_holidays)
        self.assertIn(date(2020, 10, 3), Sabah_holidays)
        self.assertIn(date(2020, 12, 24), Sabah_holidays)
        self.assertNotIn(date(2010, 12, 24), Sabah_holidays)

    def test_SWK_holidays(self):
        Sarawakholidays = holidays.MY(
            years=[2018, 2019, 2020, 2021, 2022], state="SWK"
        )
        # Gawai Dayak
        self.assertIn(date(2018, 6, 1), Sarawakholidays)
        self.assertIn(date(2018, 6, 2), Sarawakholidays)
        self.assertIn(date(2020, 6, 2), Sarawakholidays)
        self.assertIn(date(2020, 6, 2), Sarawakholidays)
        # Birthday of the Governor of Sarawak
        self.assertIn(date(2018, 10, 13), Sarawakholidays)
        self.assertIn(date(2019, 10, 12), Sarawakholidays)
        self.assertIn(date(2020, 10, 10), Sarawakholidays)
        self.assertIn(date(2021, 10, 9), Sarawakholidays)
        self.assertIn(date(2022, 10, 8), Sarawakholidays)
        # Sarawak Day
        self.assertIn(date(2022, 7, 22), Sarawakholidays)
        self.assertNotIn(date(2014, 7, 22), Sarawakholidays)

    def test_SGR_holidays(self):
        Selangor_holidays = holidays.MY(
            years=[2018, 2019, 2020, 2021, 2022], state="SGR"
        )
        # Birthday of The Sultan of Selangor
        self.assertIn(date(2018, 12, 11), Selangor_holidays)
        self.assertIn(date(2019, 12, 11), Selangor_holidays)
        # Thaipusam
        self.assertIn(date(2021, 1, 28), Selangor_holidays)
        self.assertIn(date(2022, 1, 18), Selangor_holidays)

    def test_TRG_holidays(self):
        Terengganu_holidays = holidays.MY(
            years=[2018, 2019, 2020, 2021, 2022], state="TRG"
        )
        # Anniversary of the Installation of the Sultan of Terengganu
        self.assertIn(date(2018, 3, 4), Terengganu_holidays)
        self.assertIn(date(2019, 3, 4), Terengganu_holidays)
        # Birthday of the Sultan of Terengganu
        self.assertIn(date(2020, 4, 26), Terengganu_holidays)
        self.assertIn(date(2029, 4, 26), Terengganu_holidays)
        # The Arafat Day is one day before Eid al-Adha
        self.assertIn(date(2021, 7, 20), Terengganu_holidays)
        self.assertIn(date(2022, 7, 9), Terengganu_holidays)

    def test_KUL_holidays(self):
        Kuala_Lumpur_holidays = holidays.MY(
            years=[1970, 2018, 2019, 2020, 2021, 2022], state="KUL"
        )
        # Federal Territory Day
        self.assertIn(date(2018, 2, 1), Kuala_Lumpur_holidays)
        self.assertIn(date(2019, 2, 1), Kuala_Lumpur_holidays)
        self.assertNotIn(date(1970, 2, 1), Kuala_Lumpur_holidays)

    def test_MLK_holidays(self):
        Malacca_holidays = holidays.MY(
            years=[2018, 2019, 2020, 2021, 2022], state="MLK"
        )
        # Declaration of Malacca as a Historical City in Melaka
        self.assertIn(date(2018, 4, 15), Malacca_holidays)
        self.assertIn(date(2019, 4, 15), Malacca_holidays)
        # Birthday of the Governor of MelakaMelaka

    #        self.assertIn(date(2018, 10, 12), Malacca_holidays)
    #        self.assertIn(date(2019, 10, 11), Malacca_holidays)
    #        self.assertIn(date(2020, 10, 9), Malacca_holidays)
    #        self.assertIn(date(2021, 10, 8), Malacca_holidays)

    def test_LBN_holidays(self):
        Labuan_holidays = holidays.MY(
            years=[1972, 2018, 2019, 2020, 2021, 2022], state="LBN"
        )
        # Pesta Kaamatan
        self.assertIn(date(2018, 5, 30), Labuan_holidays)
        self.assertIn(date(2019, 5, 31), Labuan_holidays)
        # Federal Territory Day
        self.assertIn(date(2020, 2, 1), Labuan_holidays)
        self.assertIn(date(2022, 2, 1), Labuan_holidays)
        self.assertNotIn(date(1972, 2, 1), Labuan_holidays)

    def test_PJY_holidays(self):
        Putrajaya_holidays = holidays.MY(
            years=[2018, 2019, 2020, 2021, 2022], state="PJY"
        )
        # Federal Territory Day
        self.assertIn(date(2020, 2, 1), Putrajaya_holidays)
        self.assertIn(date(2022, 2, 1), Putrajaya_holidays)
        self.assertNotIn(date(1972, 2, 1), Putrajaya_holidays)
        self.assertIn(date(2022, 1, 18), Putrajaya_holidays)
