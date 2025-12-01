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

from holidays.constants import WORKDAY
from holidays.countries.libya import Libya
from tests.common import CommonCountryTests


class TestLibya(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1988, 2050)
        super().setUpClass(Libya, years=years)
        cls.workday_holidays = Libya(years=years, categories=WORKDAY, islamic_show_estimated=False)
        cls.no_estimated_holidays = Libya(years=years, islamic_show_estimated=False)

    def test_special_holidays(self):
        self.assertHolidayName("عطلة رسمية", "2023-12-10")

    def test_peoples_authority_day(self):
        name = "عید إعلان سلطة الشعب"
        self.assertHolidayName(name, (f"{year}-03-02" for year in range(1988, 2012)))
        self.assertNoHolidayName(name, range(2012, 2050))

    def test_american_forces_evacuation_day(self):
        name = "عيد إجلاء القوات الأمريكية"
        self.assertHolidayName(name, (f"{year}-06-11" for year in range(1988, 2012)))
        self.assertNoHolidayName(name, range(2012, 2050))

    def test_glorious_july_revolution_day(self):
        name = "عيد ثورة يوليو المجيدة"
        self.assertHolidayName(name, (f"{year}-07-23" for year in range(1988, 2012)))
        self.assertNoHolidayName(name, range(2012, 2050))

    def test_great_al_fateh_day(self):
        name = "عيد الفاتح العظيم"
        self.assertHolidayName(name, (f"{year}-09-01" for year in range(1988, 2012)))
        self.assertNoHolidayName(name, range(2012, 2050))

    def test_anniversary_of_the_february_17_revolution(self):
        name = "ثورة 17 فبراير"
        self.assertHolidayName(name, (f"{year}-02-17" for year in range(2012, 2050)))
        self.assertNoHolidayName(name, range(1988, 2012))

    def test_labor_day(self):
        name = "عيد العمال"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(2012, 2050)))
        self.assertNoHolidayName(name, range(1988, 2012))

    def test_national_environmental_sanitation_day(self):
        name = "يوم وطني للإصحاح البيئي"
        self.assertHolidayName(name, (f"{year}-08-14" for year in range(2022, 2050)))
        self.assertNoHolidayName(name, range(1988, 2022))

    def test_martyrs_day(self):
        name = "يوم الشهيد"
        self.assertHolidayName(name, (f"{year}-09-16" for year in range(2012, 2050)))
        self.assertNoHolidayName(name, range(1988, 2012))

    def test_liberation_day(self):
        name = "يوم التحرير"
        self.assertHolidayName(name, (f"{year}-10-23" for year in range(2012, 2050)))
        self.assertNoHolidayName(name, range(1988, 2012))

    def test_independence_day(self):
        name = "عيد الاستقلال"
        self.assertHolidayName(name, (f"{year}-12-24" for year in range(2012, 2050)))
        self.assertNoHolidayName(name, range(1988, 2012))

    def test_islamic_new_year(self):
        name = "عيد رأس السنة الهجرية"
        self.assertHolidayName(
            name,
            "2021-08-10",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2012, 2050))
        self.assertNoHolidayName(name, self.no_estimated_holidays, range(1988, 2012))
        self.assertHolidayName(name, self.workday_holidays, range(1988, 2012))
        self.assertNoHolidayName(name, self.workday_holidays, range(2012, 2050))

    def test_prophets_birthday(self):
        name = "ذكرى المولد النبوي الشريف"
        self.assertHolidayName(
            name,
            "2020-10-29",
            "2021-10-19",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1988, 2050))

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        self.assertHolidayName(
            name,
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2025-03-31",
            "2025-04-01",
            "2025-04-02",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1988, 2050))

    def test_day_of_arafah(self):
        name = "يوم عرفة"
        self.assertHolidayName(
            name,
            "2020-07-30",
            "2021-07-19",
            "2022-07-08",
            "2023-06-27",
            "2024-06-15",
            "2025-06-05",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1988, 2050))

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        self.assertHolidayName(
            name,
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2024-06-16",
            "2024-06-17",
            "2024-06-18",
            "2025-06-06",
            "2025-06-07",
            "2025-06-08",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1988, 2050))

    def test_syrian_revolution_day(self):
        name = "عيد ثورة سوريا"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-03-08" for year in range(1988, 2012))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(2012, 2050))

    def test_anniversary_of_arab_league(self):
        name = "ذكرى إنشاء الجامعة العربية"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-03-22" for year in range(1988, 2012))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(2012, 2050))

    def test_british_forces_evacuation_day(self):
        name = "عيد إجلاء القوات البريطانية"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-03-28" for year in range(1988, 2012))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(2012, 2050))

    def test_italian_forces_evacuation_day(self):
        name = "عيد إجلاء الطليان"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-10-07" for year in range(1988, 2012))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(2012, 2050))

    def test_ashura_day(self):
        name = "عاشوراء"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.workday_holidays,
            "1988-08-22",
            "1989-08-11",
            "1990-08-01",
            "2010-12-16",
            "2011-12-05",
        )
        self.assertHolidayName(name, self.workday_holidays, range(1988, 2012))
        self.assertNoHolidayName(name, self.workday_holidays, range(2012, 2050))

    def test_isra_and_miraj_day(self):
        name = "ذكرى الإسراء والمعراج"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.workday_holidays,
            "1988-03-15",
            "1989-03-05",
            "1990-02-22",
            "2010-07-09",
            "2011-06-29",
        )
        self.assertHolidayName(name, self.workday_holidays, range(1988, 2012))
        self.assertNoHolidayName(name, self.workday_holidays, range(2012, 2050))

    def test_night_of_forgiveness(self):
        name = "ليلة النصف من شعبان"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.workday_holidays,
            "1988-04-02",
            "1989-03-22",
            "1990-03-12",
            "2010-07-27",
            "2011-07-16",
        )
        self.assertHolidayName(name, self.workday_holidays, range(1988, 2012))
        self.assertNoHolidayName(name, self.workday_holidays, range(2012, 2050))

    def test_2024(self):
        self.assertHolidays(
            Libya(years=2024),
            ("2024-02-17", "ثورة 17 فبراير"),
            ("2024-04-10", "عيد الفطر"),
            ("2024-04-11", "عيد الفطر"),
            ("2024-04-12", "عيد الفطر"),
            ("2024-05-01", "عيد العمال"),
            ("2024-06-15", "يوم عرفة"),
            ("2024-06-16", "عيد الأضحى"),
            ("2024-06-17", "عيد الأضحى"),
            ("2024-06-18", "عيد الأضحى"),
            ("2024-07-07", "عيد رأس السنة الهجرية"),
            ("2024-08-14", "يوم وطني للإصحاح البيئي"),
            ("2024-09-15", "ذكرى المولد النبوي الشريف"),
            ("2024-09-16", "يوم الشهيد"),
            ("2024-10-23", "يوم التحرير"),
            ("2024-12-24", "عيد الاستقلال"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-02-17", "ثورة 17 فبراير"),
            ("2025-03-31", "عيد الفطر"),
            ("2025-04-01", "عيد الفطر"),
            ("2025-04-02", "عيد الفطر"),
            ("2025-05-01", "عيد العمال"),
            ("2025-06-05", "يوم عرفة"),
            ("2025-06-06", "عيد الأضحى"),
            ("2025-06-07", "عيد الأضحى"),
            ("2025-06-08", "عيد الأضحى"),
            ("2025-06-26", "عيد رأس السنة الهجرية"),
            ("2025-08-14", "يوم وطني للإصحاح البيئي"),
            ("2025-09-04", "ذكرى المولد النبوي الشريف (المقدرة)"),
            ("2025-09-16", "يوم الشهيد"),
            ("2025-10-23", "يوم التحرير"),
            ("2025-12-24", "عيد الاستقلال"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-02-17", "Anniversary of the February 17 Revolution"),
            ("2025-03-31", "Eid al-Fitr"),
            ("2025-04-01", "Eid al-Fitr"),
            ("2025-04-02", "Eid al-Fitr"),
            ("2025-05-01", "Labor Day"),
            ("2025-06-05", "Day of Arafah"),
            ("2025-06-06", "Eid al-Adha"),
            ("2025-06-07", "Eid al-Adha"),
            ("2025-06-08", "Eid al-Adha"),
            ("2025-06-26", "Islamic New Year"),
            ("2025-08-14", "National Environmental Sanitation Day"),
            ("2025-09-04", "Prophet's Birthday (estimated)"),
            ("2025-09-16", "Martyrs' Day"),
            ("2025-10-23", "Liberation Day"),
            ("2025-12-24", "Independence Day"),
        )
