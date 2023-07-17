#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.morocco import Morocco, MA, MOR
from tests.common import TestCase


class TestMorocco(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Morocco)

    def test_country_aliases(self):
        self.assertCountryAliases(Morocco, MA, MOR)

    def test_2019(self):
        self.assertHolidayDates(
            "2019-01-01",
            "2019-01-11",
            "2019-05-01",
            "2019-06-04",
            "2019-06-05",
            "2019-07-30",
            "2019-08-11",
            "2019-08-12",
            "2019-08-14",
            "2019-08-20",
            "2019-08-21",
            "2019-08-31",
            "2019-11-06",
            "2019-11-09",
            "2019-11-10",
            "2019-11-18",
        )

    def test_1999(self):
        self.assertHolidayDates(
            "1999-01-01",
            "1999-01-11",
            "1999-01-18",
            "1999-01-19",
            "1999-03-03",
            "1999-03-27",
            "1999-03-28",
            "1999-04-17",
            "1999-05-01",
            "1999-06-26",
            "1999-06-27",
            "1999-07-09",
            "1999-08-14",
            "1999-08-20",
            "1999-11-06",
            "1999-11-18",
        )

    def test_amazigh_new_year(self):
        self.assertHoliday("2024-01-13")
        self.assertNoHoliday("2023-01-13")

    def test_independence_manifesto_day(self):
        self.assertHoliday("1945-01-11")
        self.assertNoHoliday("1944-01-11")

    def test_independence_day(self):
        self.assertHolidayName("عيد الإستقلال", "1957-11-18")
        self.assertHolidayName("عيد العرش", "1956-11-18", "1957-11-18")

    def test_hijri_based(self):
        self.assertHoliday(
            # Eid al-Fitr
            "2021-05-13",
            "2021-05-14",
            # Eid al-Adha
            "2006-01-10",
            "2006-12-31",
            "2021-07-20",
            "2021-07-21",
            # Islamic New Year
            "2008-01-10",
            "2008-12-29",
            "2021-08-09",
            # Prophet Muhammad's Birthday
            "2021-10-18",
            "2021-10-19",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "رأس السنة الميلادية"),
            ("2023-01-11", "ذكرى تقديم وثيقة الاستقلال"),
            ("2023-04-21", "(تقدير*) *عيد الفطر"),
            ("2023-04-22", "(تقدير*) *عيد الفطر"),
            ("2023-05-01", "عيد العمال"),
            ("2023-06-28", "(تقدير*) *عيد الأضحى"),
            ("2023-06-29", "(تقدير*) *عيد الأضحى"),
            ("2023-07-19", "(تقدير*) *رأس السنة الهجرية"),
            ("2023-07-30", "عيد العرش"),
            ("2023-08-14", "ذكرى استرجاع إقليم وادي الذهب"),
            ("2023-08-20", "ذكرى ثورة الملك و الشعب"),
            ("2023-08-21", "عيد الشباب"),
            ("2023-09-27", "(تقدير*) *عيد المولد النبوي"),
            ("2023-09-28", "(تقدير*) *عيد المولد النبوي"),
            ("2023-11-06", "ذكرى المسيرة الخضراء"),
            ("2023-11-18", "عيد الإستقلال"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-01-11", "Proclamation of Independence Day"),
            ("2023-04-21", "Eid al-Fitr* (*estimated)"),
            ("2023-04-22", "Eid al-Fitr* (*estimated)"),
            ("2023-05-01", "Labor Day"),
            ("2023-06-28", "Eid al-Adha* (*estimated)"),
            ("2023-06-29", "Eid al-Adha* (*estimated)"),
            ("2023-07-19", "Islamic New Year* (*estimated)"),
            ("2023-07-30", "Throne Day"),
            ("2023-08-14", "Oued Ed-Dahab Day"),
            ("2023-08-20", "Revolution Day"),
            ("2023-08-21", "Youth Day"),
            ("2023-09-27", "Prophet's Birthday* (*estimated)"),
            ("2023-09-28", "Prophet's Birthday* (*estimated)"),
            ("2023-11-06", "Green March"),
            ("2023-11-18", "Independence Day"),
        )
