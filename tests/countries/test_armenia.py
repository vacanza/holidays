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

from holidays.countries.armenia import Armenia
from tests.common import CommonCountryTests, WorkingDayTests


class TestArmenia(CommonCountryTests, WorkingDayTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Armenia)

    def test_new_years_day(self):
        name = "Նոր տարվա օր"
        self.assertHolidayName(
            name,
            (f"{year}-01-01" for year in self.full_range),
            (f"{year}-01-02" for year in self.full_range),
        )

    def test_christmas_and_epiphany_day(self):
        self.assertHolidayName(
            "Սուրբ Ծնունդ եւ Հայտնություն", (f"{year}-01-06" for year in self.full_range)
        )

    def test_christmas_holidays(self):
        name = "նախածննդյան տոներ"
        self.assertHolidayName(
            name,
            (f"{year}-01-03" for year in range(2010, 2022)),
            (f"{year}-01-04" for year in range(2010, 2022)),
            (f"{year}-01-05" for year in range(2010, 2022)),
        )
        self.assertNoHolidayName(name, range(self.start_year, 2010), range(2022, self.end_year))

    def test_day_of_remembrance_of_the_dead(self):
        name = "Մեռելոց հիշատակի օր"
        self.assertHolidayName(name, (f"{year}-01-07" for year in range(2010, 2022)))
        self.assertNoHolidayName(name, range(self.start_year, 2010), range(2022, self.end_year))

    def test_remembrance_for_fallen_defenders(self):
        name = "Հայրենիքի պաշտպանության համար զոհվածների հիշատակի օր"
        self.assertHolidayName(name, (f"{year}-01-27" for year in range(2026, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2026))

    def test_army_day(self):
        name = "Բանակի օր"
        self.assertHolidayName(name, (f"{year}-01-28" for year in range(2003, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2003))

        self.assertWorkdayHolidayName(name, "2002-01-28")
        self.assertNoWorkdayHolidayName(
            name, range(self.start_year, 2002), range(2003, self.end_year)
        )

    def test_womens_day(self):
        name_2001 = "Կանանց միջազգային օր"
        name_2002 = "Կանանց տոն"
        self.assertHolidayName(name_2001, "2001-03-08")
        self.assertHolidayName(name_2002, (f"{year}-03-08" for year in range(2002, self.end_year)))
        self.assertNoHolidayName(
            name_2001, range(self.start_year, 2001), range(2002, self.end_year)
        )
        self.assertNoHolidayName(name_2002, range(self.start_year, 2002))

    def test_motherhood_and_beauty_day(self):
        name_1994_2003 = "Մայրության և գեղեցկության տոն"
        name_2002 = "Մայրության, գեղեցկության եւ սիրո տոն"
        self.assertHolidayName(name_1994_2003, (f"{year}-04-07" for year in range(1994, 2002)))
        self.assertNoHolidayName(
            name_1994_2003, range(self.start_year, 1994), range(2002, self.end_year)
        )
        self.assertNoHolidayName(name_2002)

        self.assertWorkdayHolidayName(name_2002, "2002-04-07")
        self.assertWorkdayHolidayName(
            name_1994_2003, (f"{year}-04-07" for year in range(2003, self.end_year))
        )
        self.assertNoWorkdayHolidayName(
            name_2002, range(self.start_year, 2002), range(2003, self.end_year)
        )
        self.assertNoWorkdayHolidayName(name_1994_2003, range(self.start_year, 2003))

    def test_armenian_genocide_remembrance_day(self):
        name_1992 = "Ցեղասպանության զոհերի հիշատակի օր"
        name_2015 = "Հայոց ցեղասպանության զոհերի հիշատակի օր"
        self.assertHolidayName(
            name_1992, (f"{year}-04-24" for year in range(self.start_year, 2015))
        )
        self.assertHolidayName(name_2015, (f"{year}-04-24" for year in range(2015, self.end_year)))
        self.assertNoHolidayName(name_1992, range(2015, self.end_year))
        self.assertNoHolidayName(name_2015, range(self.start_year, 2015))

    def test_labor_day(self):
        name_2001 = "Աշխատավորների համերաշխության միջազգային օր"
        name_2002 = "Աշխատանքի օր"
        self.assertHolidayName(name_2001, "2001-05-01")
        self.assertHolidayName(name_2002, (f"{year}-05-01" for year in range(2002, self.end_year)))
        self.assertNoHolidayName(
            name_2001, range(self.start_year, 2001), range(2002, self.end_year)
        )
        self.assertNoHolidayName(name_2002, range(self.start_year, 2002))

    def test_victory_and_peace_day(self):
        name = "Հաղթանակի և Խաղաղության տոն"
        self.assertHolidayName(name, (f"{year}-05-09" for year in range(1995, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1995))

    def test_republic_day(self):
        self.assertHolidayName("Հանրապետության օր", (f"{year}-05-28" for year in self.full_range))

    def test_constitution_day(self):
        name = "Սահմանադրության օր"
        self.assertHolidayName(name, (f"{year}-07-05" for year in range(1996, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1996))

    def test_independence_day(self):
        name = "Անկախության օր"
        self.assertHolidayName(name, (f"{year}-09-21" for year in range(1992, self.end_year)))
        self.assertNoHolidayName(name, 1991)

    def test_new_years_eve(self):
        self.assertHolidayName("Նոր տարվա գիշեր", (f"{year}-12-31" for year in self.full_range))

    def test_mother_language_day(self):
        name = "Մայրենի լեզվի օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name, (f"{year}-02-21" for year in range(2006, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2006))

    def test_saint_vardanants_day(self):
        name = "Սուրբ Վարդանանց տոն"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name,
            "2020-02-27",
            "2021-03-11",
            "2022-03-03",
            "2023-02-23",
            "2024-03-14",
            "2025-02-27",
        )
        self.assertWorkdayHolidayName(name, range(2002, self.end_year))
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2002))

    def test_remembrance_of_victims_of_massacres_day(self):
        name = (
            "Ադրբեջանական ԽՍՀ-ում կազմակերպված ջարդերի զոհերի հիշատակի եւ "
            "բռնագաղթված հայ բնակչության իրավունքների պաշտպանության օր"
        )
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name, (f"{year}-02-28" for year in range(2006, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2006))

    def test_armenian_cinema_day(self):
        name = "Հայ կինոյի օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name, (f"{year}-04-16" for year in range(2020, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2020))

    def test_taxpayer_day(self):
        name = "Հարկ վճարողի օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name, (f"{year}-04-18" for year in range(2022, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2022))

    def test_citizen_of_republic_of_armenia_day(self):
        name = "Հայաստանի Հանրապետության քաղաքացու օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name,
            "2020-04-25",
            "2021-04-25",
            "2022-04-30",
            "2023-04-29",
            "2024-04-27",
            "2025-04-26",
        )
        self.assertWorkdayHolidayName(name, range(2019, self.end_year))
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2019))

    def test_defenders_day(self):
        name = "Երկրապահի օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name, (f"{year}-05-08" for year in range(2002, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2002))

    def test_family_day(self):
        name = "Ընտանիքի օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name, (f"{year}-05-15" for year in range(2012, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2012))

    def test_students_and_youth_day(self):
        name = "Ուսանողների եւ երիտասարդների օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name, (f"{year}-05-16" for year in range(2016, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2016))

    def test_childrens_rights_protection_day(self):
        name = "Երեխաների իրավունքների պաշտպանության օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name, (f"{year}-06-01" for year in range(2002, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2002))

    def test_remembrance_of_repressed_day(self):
        name = "Բռնադատվածների հիշատակի օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name, (f"{year}-06-14" for year in range(2007, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2007))

    def test_fathers_day(self):
        name = "Հայրերի օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name, (f"{year}-06-17" for year in range(2025, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2025))

    def test_feast_of_holy_etchmiadzin(self):
        name = "Սուրբ Էջմիածնի տոն"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name,
            "2020-06-21",
            "2021-07-04",
            "2022-06-26",
            "2023-06-18",
            "2024-07-07",
            "2025-06-22",
        )
        self.assertWorkdayHolidayName(name, range(2002, self.end_year))
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2002))

    def test_state_symbols_day(self):
        name = "Պետական խորհրդանիշների օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name, (f"{year}-07-05" for year in range(2017, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2017))

    def test_remembrance_of_victims_of_sinjar_yazidi_genocide_day(self):
        name = "2014 թվականի՝ Սինջարի եզդիների ցեղասպանության զոհերի հիշատակի օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name, (f"{year}-08-03" for year in range(2024, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2024))

    def test_knowledge_and_literacy_day(self):
        name_2001 = "Գիտելիքի, գրի եւ դպրության օր"
        name_2005 = "Գիտելիքի եւ դպրության օր"
        self.assertNoHolidayName(name_2001)
        self.assertNoHolidayName(name_2005)

        self.assertWorkdayHolidayName(name_2001, (f"{year}-09-01" for year in range(2001, 2005)))
        self.assertWorkdayHolidayName(
            name_2005, (f"{year}-09-01" for year in range(2005, self.end_year))
        )
        self.assertNoWorkdayHolidayName(
            name_2001, range(self.start_year, 2001), range(2005, self.end_year)
        )
        self.assertNoWorkdayHolidayName(name_2005, range(self.start_year, 2005))

    def test_national_minorities_day(self):
        name = "Հայաստանի Հանրապետության ազգային փոքրամասնությունների օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name,
            "2021-10-03",
            "2022-10-02",
            "2023-10-01",
            "2024-10-06",
            "2025-10-05",
        )
        self.assertWorkdayHolidayName(name, range(2021, self.end_year))
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2021))

    def test_teachers_day(self):
        name = "Ուսուցչի օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name, (f"{year}-10-05" for year in range(2011, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2011))

    def test_translators_day(self):
        name = "Թարգմանչաց տոն"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name,
            "2020-10-10",
            "2021-10-09",
            "2022-10-08",
            "2023-10-14",
            "2024-10-12",
            "2025-10-11",
        )
        self.assertWorkdayHolidayName(name, range(2001, self.end_year))
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2001))

    def test_local_self_government_day(self):
        name = "Տեղական ինքնակառավարման օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name, (f"{year}-11-10" for year in range(2011, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2011))

    def test_earthquake_victims_remembrance_day(self):
        name_2001 = "Երկրաշարժի զոհերի հիշատակի օր"
        name_2020 = "Երկրաշարժի զոհերի հիշատակի եւ աղետներին դիմակայունության օր"
        self.assertNoHolidayName(name_2001)
        self.assertNoHolidayName(name_2020)

        self.assertWorkdayHolidayName(name_2001, (f"{year}-12-07" for year in range(2001, 2020)))
        self.assertWorkdayHolidayName(
            name_2020, (f"{year}-12-07" for year in range(2020, self.end_year))
        )
        self.assertNoWorkdayHolidayName(
            name_2001, range(self.start_year, 2001), range(2020, self.end_year)
        )
        self.assertNoWorkdayHolidayName(name_2020, range(self.start_year, 2020))

    def test_condemnation_and_prevention_of_genocides_day(self):
        name = "Ցեղասպանությունների դատապարտման եւ կանխարգելման օր"
        self.assertNoHolidayName(name)

        self.assertWorkdayHolidayName(
            name, (f"{year}-12-09" for year in range(2015, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2015))

    def test_substituted_holidays(self):
        self.assertHoliday(
            "1998-12-07",
            "2000-05-08",
            "2003-01-03",
            "2005-01-03",
            "2005-03-07",
            "2005-07-04",
            "2006-01-03",
            "2006-05-08",
            "2007-01-03",
            "2007-01-04",
            "2007-04-30",
            "2008-01-03",
            "2008-01-04",
            "2008-05-02",
            "2008-06-30",
            "2008-08-18",
            "2008-09-15",
            "2009-01-05",
            "2009-01-07",
            "2009-04-13",
            "2009-07-20",
            "2009-08-17",
            "2009-09-14",
            "2010-01-08",
            "2010-04-05",
            "2010-07-12",
            "2010-08-16",
            "2010-09-13",
            "2010-09-20",
            "2011-03-07",
            "2011-04-25",
            "2011-07-04",
            "2011-08-01",
            "2011-08-15",
            "2011-09-12",
            "2012-03-09",
            "2012-04-09",
            "2012-04-30",
            "2012-07-06",
            "2012-07-16",
            "2012-08-13",
            "2012-09-17",
            "2013-04-01",
            "2013-05-10",
            "2013-05-27",
            "2013-07-08",
            "2013-08-19",
            "2013-09-16",
            "2013-12-30",
            "2014-01-27",
            "2014-04-21",
            "2014-05-02",
            "2014-07-28",
            "2014-08-18",
            "2014-09-15",
            "2015-01-08",
            "2015-01-09",
            "2015-04-06",
            "2015-04-23",
            "2015-07-13",
            "2015-09-14",
            "2016-03-07",
            "2016-03-28",
            "2016-09-12",
            "2017-04-17",
            "2017-05-08",
            "2017-09-18",
            "2018-03-09",
            "2018-04-02",
            "2018-04-30",
            "2018-10-11",
            "2018-10-12",
            "2020-01-27",
            "2020-05-29",
            "2021-09-20",
        )
        self.assertSubdivLoHoliday("2018-12-07")
        self.assertSubdivShHoliday("2018-12-07")

    def test_workdays(self):
        self.assertWorkingDay(
            "1998-12-12",
            "2000-05-06",
            "2002-12-29",
            "2005-01-08",
            "2005-03-05",
            "2005-07-02",
            "2006-01-08",
            "2006-05-06",
            "2006-12-30",
            "2007-01-07",
            "2007-04-28",
            "2007-12-29",
            "2008-01-12",
            "2008-05-04",
            "2008-06-28",
            "2008-08-16",
            "2008-09-13",
            "2008-12-27",
            "2009-01-10",
            "2009-04-18",
            "2009-07-18",
            "2009-08-15",
            "2009-09-12",
            "2009-12-26",
            "2010-04-10",
            "2010-07-17",
            "2010-08-21",
            "2010-09-11",
            "2010-09-18",
            "2011-03-12",
            "2011-04-30",
            "2011-07-09",
            "2011-08-06",
            "2011-08-20",
            "2011-09-17",
            "2012-03-24",
            "2012-04-14",
            "2012-04-28",
            "2012-07-14",
            "2012-07-21",
            "2012-08-18",
            "2012-09-29",
            "2013-04-13",
            "2013-05-18",
            "2013-06-01",
            "2013-07-13",
            "2013-08-24",
            "2013-09-28",
            "2013-12-28",
            "2014-02-01",
            "2014-04-26",
            "2014-05-31",
            "2014-08-02",
            "2014-08-23",
            "2014-09-27",
            "2014-12-20",
            "2014-12-27",
            "2015-04-11",
            "2015-04-18",
            "2015-07-18",
            "2015-09-19",
            "2016-03-12",
            "2016-04-02",
            "2016-09-24",
            "2017-05-06",
            "2017-05-20",
            "2017-09-23",
            "2018-03-17",
            "2018-04-07",
            "2018-05-05",
            "2018-10-27",
            "2018-11-03",
            "2020-02-01",
            "2020-05-23",
            "2021-09-25",
        )

        for year, dts in {
            2002: ("2002-12-29",),
            2006: (
                "2006-01-08",
                "2006-05-06",
                "2006-12-30",
            ),
            2007: (
                "2007-01-07",
                "2007-04-28",
                "2007-12-29",
            ),
            2008: (
                "2008-01-12",
                "2008-05-04",
                "2008-06-28",
                "2008-08-16",
                "2008-09-13",
                "2008-12-27",
            ),
            2009: (
                "2009-01-10",
                "2009-04-18",
                "2009-07-18",
                "2009-08-15",
                "2009-09-12",
                "2009-12-26",
            ),
            2014: (
                "2014-02-01",
                "2014-04-26",
                "2014-05-31",
                "2014-08-02",
                "2014-08-23",
                "2014-09-27",
                "2014-12-20",
                "2014-12-27",
            ),
        }.items():
            self.assertWorkingDay(Armenia(years=year), dts)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Նոր տարվա օր"),
            ("2025-01-02", "Նոր տարվա օր"),
            ("2025-01-06", "Սուրբ Ծնունդ եւ Հայտնություն"),
            ("2025-01-28", "Բանակի օր"),
            ("2025-02-21", "Մայրենի լեզվի օր"),
            ("2025-02-27", "Սուրբ Վարդանանց տոն"),
            (
                "2025-02-28",
                "Ադրբեջանական ԽՍՀ-ում կազմակերպված ջարդերի զոհերի հիշատակի եւ բռնագաղթված հայ "
                "բնակչության իրավունքների պաշտպանության օր",
            ),
            ("2025-03-08", "Կանանց տոն"),
            ("2025-04-07", "Մայրության և գեղեցկության տոն"),
            ("2025-04-16", "Հայ կինոյի օր"),
            ("2025-04-18", "Հարկ վճարողի օր"),
            ("2025-04-24", "Հայոց ցեղասպանության զոհերի հիշատակի օր"),
            ("2025-04-26", "Հայաստանի Հանրապետության քաղաքացու օր"),
            ("2025-05-01", "Աշխատանքի օր"),
            ("2025-05-08", "Երկրապահի օր"),
            ("2025-05-09", "Հաղթանակի և Խաղաղության տոն"),
            ("2025-05-15", "Ընտանիքի օր"),
            ("2025-05-16", "Ուսանողների եւ երիտասարդների օր"),
            ("2025-05-28", "Հանրապետության օր"),
            ("2025-06-01", "Երեխաների իրավունքների պաշտպանության օր"),
            ("2025-06-14", "Բռնադատվածների հիշատակի օր"),
            ("2025-06-17", "Հայրերի օր"),
            ("2025-06-22", "Սուրբ Էջմիածնի տոն"),
            ("2025-07-05", "Պետական խորհրդանիշների օր; Սահմանադրության օր"),
            ("2025-08-03", "2014 թվականի՝ Սինջարի եզդիների ցեղասպանության զոհերի հիշատակի օր"),
            ("2025-09-01", "Գիտելիքի եւ դպրության օր"),
            ("2025-09-21", "Անկախության օր"),
            (
                "2025-10-05",
                "Հայաստանի Հանրապետության ազգային փոքրամասնությունների օր; Ուսուցչի օր",
            ),
            ("2025-10-11", "Թարգմանչաց տոն"),
            ("2025-11-10", "Տեղական ինքնակառավարման օր"),
            ("2025-12-07", "Երկրաշարժի զոհերի հիշատակի եւ աղետներին դիմակայունության օր"),
            ("2025-12-09", "Ցեղասպանությունների դատապարտման եւ կանխարգելման օր"),
            ("2025-12-31", "Նոր տարվա գիշեր"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-02", "New Year's Day"),
            ("2025-01-06", "Christmas and Epiphany"),
            ("2025-01-28", "Army Day"),
            ("2025-02-21", "Mother Language Day"),
            ("2025-02-27", "Saint Vardanants' Day"),
            (
                "2025-02-28",
                "Day of Remembrance of the Victims of the Massacres Organized in the Azerbaijan "
                "SSR and the Protection of the Rights of the Deported Armenian Population",
            ),
            ("2025-03-08", "Women's Day"),
            ("2025-04-07", "Motherhood and Beauty Day"),
            ("2025-04-16", "Armenian Cinema Day"),
            ("2025-04-18", "Taxpayer Day"),
            ("2025-04-24", "Day of Remembrance of the Victims of Armenian Genocide"),
            ("2025-04-26", "Citizen of the Republic of Armenia Day"),
            ("2025-05-01", "Labor Day"),
            ("2025-05-08", "Defender's Day"),
            ("2025-05-09", "Victory and Peace Day"),
            ("2025-05-15", "Family Day"),
            ("2025-05-16", "Students and Youth Day"),
            ("2025-05-28", "Republic Day"),
            ("2025-06-01", "Children's Rights Protection Day"),
            ("2025-06-14", "Day of Remembrance of the Repressed"),
            ("2025-06-17", "Father's Day"),
            ("2025-06-22", "Feast of Holy Etchmiadzin"),
            ("2025-07-05", "Constitution Day; State Symbols' Day"),
            (
                "2025-08-03",
                "Day of Remembrance of the Victims of the Sinjar Yazidi Genocide of 2014",
            ),
            ("2025-09-01", "Knowledge and Literacy Day"),
            ("2025-09-21", "Independence Day"),
            ("2025-10-05", "Day of National Minorities of the Republic of Armenia; Teacher's Day"),
            ("2025-10-11", "Translators' Day"),
            ("2025-11-10", "Local Self-Government Day"),
            ("2025-12-07", "Earthquake Victims Remembrance Day and Disaster Resilience Day"),
            ("2025-12-09", "Day of the Condemnation and Prevention of Genocides"),
            ("2025-12-31", "New Year's Eve"),
        )
