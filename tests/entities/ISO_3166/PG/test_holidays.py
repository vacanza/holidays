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

from holidays.entities.ISO_3166.PG import PgHolidays
from tests.common import CommonCountryTests


class TestPgHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            PgHolidays, years=range(1953, 2050), years_non_observed=range(1953, 2050)
        )

    def test_no_holidays(self):
        self.assertNoHolidays(PgHolidays(years=1952))

    def test_special_holidays(self):
        dt = (
            "2018-11-16",
            "2021-01-08",
            "2021-03-01",
            "2021-03-12",
            "2022-09-19",
            "2023-04-18",
        )
        dt_observed = (
            "2022-02-28",
            "2023-02-24",
            "2023-06-16",
            "2023-09-15",
        )
        self.assertHoliday(dt, dt_observed)
        self.assertNoNonObservedHoliday(dt_observed)

    def test_1953(self):
        # http://www.paclii.org/pg/legis/consol_act/pha1953163.pdf
        self.assertHolidays(
            PgHolidays(years=1953),
            ("1953-01-01", "New Year's Day"),
            ("1953-04-03", "Good Friday"),
            ("1953-04-04", "Easter Saturday"),
            ("1953-04-05", "Easter Sunday"),
            ("1953-04-06", "Easter Monday"),
            ("1953-06-08", "Queen's Birthday"),
            ("1953-07-23", "Papua New Guinea Remembrance Day"),
            ("1953-12-25", "Christmas Day"),
            ("1953-12-26", "Boxing Day"),
        )

    def test_2019(self):
        # https://www.scribd.com/document/465334129/PNG-2019-Gazetted-Public-Holidays-pdf
        # https://pngiportal.org/directory/national-gazette-g560-602-2018
        self.assertHolidays(
            PgHolidays(years=2019),
            ("2019-01-01", "New Year's Day"),
            ("2019-04-19", "Good Friday"),
            ("2019-04-20", "Easter Saturday"),
            ("2019-04-21", "Easter Sunday"),
            ("2019-04-22", "Easter Monday"),
            ("2019-06-10", "Queen's Birthday"),
            ("2019-07-23", "Papua New Guinea Remembrance Day"),
            ("2019-08-26", "National Repentance Day"),
            ("2019-09-16", "Independence Day"),
            ("2019-12-25", "Christmas Day"),
            ("2019-12-26", "Boxing Day"),
        )

    def test_2020(self):
        # https://publicholidays.asia/wp-content/uploads/2020/01/PNG_PublicHolidays_2020.png
        self.assertHolidays(
            PgHolidays(years=2020),
            ("2020-01-01", "New Year's Day"),
            ("2020-04-10", "Good Friday"),
            ("2020-04-11", "Easter Saturday"),
            ("2020-04-12", "Easter Sunday"),
            ("2020-04-13", "Easter Monday"),
            ("2020-06-08", "Queen's Birthday"),
            ("2020-07-23", "Papua New Guinea Remembrance Day"),
            ("2020-08-26", "National Repentance Day"),
            ("2020-09-16", "Independence Day"),
            ("2020-12-25", "Christmas Day"),
            ("2020-12-26", "Boxing Day"),
        )

    def test_2021(self):
        # https://publicholidays.asia/wp-content/uploads/2020/12/PNG_PublicHolidays_2021.pdf
        # https://www.efpng.org.pg/wp-content/uploads/2021/05/CIRCULAR-No.17-2021-AMENDMENTS-TO-2021-PUBLIC-HOLIDAY.pdf
        # Easter dates were later corrected as of https://web.archive.org/web/20210411125811/https://www.businessadvantagepng.com/papua-new-guinea-public-for-holidays/
        self.assertHolidays(
            PgHolidays(years=2021),
            ("2021-01-01", "New Year's Day"),
            ("2021-01-08", "State Funeral of Sir Mekere Morauta"),
            ("2021-03-01", "National Day of Mourning for Sir Michael Somare"),
            ("2021-03-12", "National Day of Mourning for Sir Michael Somare"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-03", "Easter Saturday"),
            ("2021-04-04", "Easter Sunday"),
            ("2021-04-05", "Easter Monday"),
            ("2021-06-14", "Queen's Birthday"),
            ("2021-07-23", "Papua New Guinea Remembrance Day"),
            ("2021-08-26", "National Repentance Day"),
            ("2021-09-16", "Independence Day"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-26", "Boxing Day"),
            ("2021-12-27", "Boxing Day (observed)"),
        )

    def test_2022(self):
        # https://publicholidays.asia/wp-content/uploads/2022/01/PNG_PublicHolidays_2022.pdf
        # Somare Day public holiday was observed on Feb 28 instead as of
        # https://web.archive.org/web/20220703204538/https://www.businessadvantagepng.com/papua-new-guinea-public-for-holidays/
        self.assertHolidays(
            PgHolidays(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-02-26", "Grand Chief Sir Michael Somare Remembrance Day"),
            ("2022-02-28", "Grand Chief Sir Michael Somare Remembrance Day (observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Easter Saturday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-06-13", "Queen's Birthday"),
            ("2022-07-23", "Papua New Guinea Remembrance Day"),
            ("2022-08-26", "National Repentance Day"),
            ("2022-09-16", "Independence Day"),
            ("2022-09-19", "State Funeral of Queen Elizabeth II"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_2023(self):
        # https://publicholidays.asia/wp-content/uploads/2022/12/PNG_PublicHolidays_2023.pdf
        # https://pnghausbung.com/kings-birthday-holiday-to-be-observed-on-16th-june/
        self.assertHolidays(
            PgHolidays(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-02-24", "Grand Chief Sir Michael Somare Remembrance Day (observed)"),
            ("2023-02-26", "Grand Chief Sir Michael Somare Remembrance Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-08", "Easter Saturday"),
            ("2023-04-09", "Easter Sunday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-18", "State Funeral of Sir Rabbie Namaliu"),
            ("2023-06-16", "King's Birthday (observed)"),
            ("2023-06-17", "King's Birthday"),
            ("2023-07-23", "Papua New Guinea Remembrance Day"),
            ("2023-07-24", "Papua New Guinea Remembrance Day (observed)"),
            ("2023-08-26", "National Repentance Day"),
            ("2023-09-15", "Independence Day (observed)"),
            ("2023-09-16", "Independence Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2024(self):
        # https://web.archive.org/web/20231221053513/https://www.businessadvantagepng.com/papua-new-guinea-public-for-holidays/
        self.assertHolidays(
            PgHolidays(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-02-26", "Grand Chief Sir Michael Somare Remembrance Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-31", "Easter Sunday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-06-17", "King's Birthday"),
            ("2024-07-23", "Papua New Guinea Remembrance Day"),
            ("2024-08-26", "National Repentance Day"),
            ("2024-09-16", "Independence Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )
