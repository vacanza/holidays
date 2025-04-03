#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.

#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import _timedelta
from holidays.countries.qatar import Qatar, QA, QAT
from tests.common import CommonCountryTests


class TestQatar(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Qatar, years=range(1971, 2050))
        cls.no_estimated_holidays = Qatar(years=range(2000, 2024), islamic_show_estimated=False)

        def test_country_aliases(self):
            self.assertAliases(Qatar, QA, QAT)

        def test_no_holidays(self):
            self.assertNoHolidays(Qatar(years=1971))

        def test_sports_day(self):
            name = "اليوم الوطني للرياضة"
            self.assertHolidayName(name, range(2012, 2050))
            self.assertNoHolidayName(name, range(1971, 2012))
            dts = (
                "2012-02-14",
                "2013-02-12",
                "2014-02-11",
                "2015-02-10",
                "2016-02-09",
                "2017-02-14",
                "2018-02-13",
                "2019-02-12",
                "2020-02-11",
                "2021-02-09",
                "2022-02-08",
                "2023-02-14",
                "2024-02-13",
                "2025-02-11",
                "2026-02-10",
                "2027-02-09",
                "2028-02-08",
                "2029-02-13",
                "2030-02-12",
            )
            self.assertHolidayName(name, dts)

        def test_national_day(self):
            name = "اليوم الوطني لقطر"
            self.assertHolidayName(name, (f"{year}-12-18" for year in range(2007, 2050)))
            self.assertNoHolidayName(name, range(1971, 2007))

        def test_eid_al_fitr(self):
            name = "عيد الفطر"
            for dt in (
                date(2005, 11, 4),
                date(2006, 10, 24),
                date(2007, 10, 13),
                date(2008, 10, 2),
                date(2009, 9, 21),
                date(2010, 9, 10),
                date(2011, 8, 31),
                date(2012, 8, 19),
                date(2013, 8, 8),
                date(2014, 7, 28),
                date(2015, 7, 18),
                date(2016, 7, 6),
                date(2017, 6, 25),
                date(2018, 6, 15),
                date(2019, 6, 4),
                date(2020, 5, 24),
                date(2021, 5, 13),
                date(2022, 5, 2),
                date(2023, 4, 21),
                date(2024, 4, 10),
                date(2025, 3, 30),
            ):
                self.assertHolidayName(
                    name, self.no_estimated_holidays, dt, _timedelta(dt, +1), _timedelta(dt, +2)
                )

        def test_eid_al_adha(self):
            name = "عيد الأضحى"
            for dt in (
                date(2005, 1, 21),
                date(2006, 1, 10),
                date(2006, 12, 31),
                date(2007, 12, 20),
                date(2008, 12, 9),
                date(2009, 11, 28),
                date(2010, 11, 15),
                date(2011, 11, 6),
                date(2012, 10, 26),
                date(2013, 10, 15),
                date(2014, 10, 4),
                date(2015, 9, 23),
                date(2016, 9, 10),
                date(2017, 8, 31),
                date(2018, 8, 22),
                date(2019, 8, 11),
                date(2020, 7, 31),
                date(2021, 7, 20),
                date(2022, 7, 9),
                date(2023, 6, 28),
                date(2024, 6, 16),
            ):
                self.assertHolidayName(
                    name, self.no_estimated_holidays, dt, _timedelta(dt, +1), _timedelta(dt, +2)
                )

        def test_march_bank_holiday(self):
            name = "عطلة البنك"
            self.assertHolidayName(name, range(2010, 2050))
            self.assertNoHolidayName(name, range(1971, 2010))
            dts = (
                "2010-03-07",
                "2011-03-06",
                "2012-03-04",
                "2013-03-03",
                "2014-03-02",
                "2015-03-01",
                "2016-03-06",
                "2017-03-05",
                "2018-03-04",
                "2019-03-03",
                "2020-03-01",
                "2021-03-07",
                "2022-03-06",
                "2023-03-05",
                "2024-03-03",
                "2025-03-02",
            )
            self.assertHolidayName(name, dts)

        def test_2011(self):
            self.assertHolidays(
                Qatar(years=2011),
                ("2011-01-01", "رأس السنة الميلادية"),
                ("2011-03-06", "عطلة البنك"),
                ("2011-08-31", "عيد الفطر"),
                ("2011-09-01", "عيد الفطر"),
                ("2011-09-02", "عيد الفطر"),
                ("2011-11-06", "عيد الأضحى"),
                ("2011-11-07", "عيد الأضحى"),
                ("2011-11-08", "عيد الأضحى"),
                ("2011-12-18", "اليوم الوطني لقطر"),
            )

        def test_l10n_default(self):
            self.assertLocalizedHolidays(
                ("2012-01-01", "رأس السنة الميلادية"),
                ("2012-02-14", "اليوم الوطني للرياضة"),
                ("2012-03-04", "عطلة البنك"),
                ("2012-08-19", "عيد الفطر"),
                ("2012-08-20", "عيد الفطر"),
                ("2012-08-21", "عيد الفطر"),
                ("2012-10-26", "عيد الأضحى"),
                ("2012-10-27", "عيد الأضحى"),
                ("2012-10-28", "عيد الأضحى"),
                ("2012-12-18", "اليوم الوطني لقطر"),
            )

        def test_l10n_en_us(self):
            self.assertLocalizedHolidays(
                "en_US",
                ("2012-01-01", "New Year's Day"),
                ("2012-02-14", "National Sports Day"),
                ("2012-03-04", "March Bank Holiday"),
                ("2012-08-19", "Eid al-Fitr"),
                ("2012-08-20", "Eid al-Fitr"),
                ("2012-08-21", "Eid al-Fitr"),
                ("2012-10-26", "Eid al-Adha"),
                ("2012-10-27", "Eid al-Adha"),
                ("2012-10-28", "Eid al-Adha"),
                ("2012-12-18", "Qatar National Day"),
            )
