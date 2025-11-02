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

from holidays.countries.micronesia import Micronesia
from tests.common import CommonCountryTests


class TestMicronesia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1987, 2050)
        super().setUpClass(Micronesia, years=years, years_non_observed=years)
        cls.subdiv_holidays = {
            subdiv: Micronesia(subdiv=subdiv, years=years) for subdiv in Micronesia.subdivisions
        }
        cls.subdiv_holidays_non_observed = {
            subdiv: Micronesia(subdiv=subdiv, years=years, observed=False)
            for subdiv in Micronesia.subdivisions
        }

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1987, 2050)))
        dt = (
            "2010-12-31",
            "2012-01-02",
            "2017-01-02",
            "2021-12-31",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_micronesian_culture_and_tradition_day(self):
        name = "Micronesian Culture and Tradition Day"
        self.assertHolidayName(name, (f"{year}-03-31" for year in range(2011, 2050)))
        self.assertNoHolidayName(name, range(1987, 2011))
        dt = (
            "2012-03-30",
            "2013-04-01",
            "2018-03-30",
            "2019-04-01",
            "2024-04-01",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_federated_states_of_micronesia_day(self):
        name = "Federated States of Micronesia Day"
        self.assertHolidayName(name, (f"{year}-05-10" for year in range(1987, 2050)))
        dt = (
            "2003-05-09",
            "2008-05-09",
            "2009-05-11",
            "2014-05-09",
            "2015-05-11",
            "2020-05-11",
            "2025-05-09",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_united_nations_day(self):
        name = "United Nations Day"
        self.assertHolidayName(name, (f"{year}-10-24" for year in range(1991, 2050)))
        self.assertNoHolidayName(name, range(1987, 1991))
        dt = (
            "2004-10-25",
            "2009-10-23",
            "2010-10-25",
            "2015-10-23",
            "2020-10-23",
            "2021-10-25",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-11-03" for year in range(1987, 2050)))
        dt = (
            "2001-11-02",
            "2002-11-04",
            "2007-11-02",
            "2012-11-02",
            "2013-11-04",
            "2018-11-02",
            "2019-11-04",
            "2024-11-04",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_fsm_veterans_of_foreign_wars_day(self):
        name = "FSM Veterans of Foreign Wars Day"
        self.assertHolidayName(name, (f"{year}-11-11" for year in range(2004, 2050)))
        self.assertNoHolidayName(name, range(1987, 2004))
        dt = (
            "2006-11-10",
            "2007-11-12",
            "2012-11-12",
            "2017-11-10",
            "2018-11-12",
            "2023-11-10",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_presidents_day(self):
        name = "Presidents Day"
        self.assertHolidayName(name, (f"{year}-11-23" for year in range(2021, 2050)))
        self.assertNoHolidayName(name, range(1987, 2021))
        dt = (
            "2024-11-22",
            "2025-11-24",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1987, 2050)))
        dt = (
            "2004-12-24",
            "2005-12-26",
            "2010-12-24",
            "2011-12-26",
            "2016-12-26",
            "2021-12-24",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_state_charter_day(self):
        name = "State Charter Day"
        self.assertNoHolidayName(name)
        dt = (
            "2004-09-27",
            "2009-09-25",
            "2010-09-27",
            "2015-09-25",
            "2020-09-25",
            "2021-09-27",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TRK":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-26" for year in range(1987, 2050))
                )
                self.assertHolidayName(f"{name} (observed)", holidays, dt)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_chuuk_state_constitution_day(self):
        name = "Chuuk State Constitution Day"
        self.assertNoHolidayName(name)
        dt = (
            "2000-10-02",
            "2005-09-30",
            "2006-10-02",
            "2011-09-30",
            "2016-09-30",
            "2017-10-02",
            "2022-09-30",
            "2023-10-02",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TRK":
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-01" for year in range(1990, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(1987, 1990))
                self.assertHolidayName(f"{name} (observed)", holidays, dt)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_kosrae_state_constitution_day(self):
        name = "Kosrae State Constitution Day"
        self.assertNoHolidayName(name)
        dt = (
            "2003-01-10",
            "2004-01-12",
            "2009-01-12",
            "2014-01-10",
            "2015-01-12",
            "2020-01-10",
            "2025-01-10",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "KSA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-11" for year in range(1991, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(1987, 1991))
                self.assertHolidayName(f"{name} (observed)", holidays, dt)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertNoHolidayName(name)
        dt = (
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "KSA":
                self.assertHolidayName(name, holidays, dt)
                self.assertHolidayName(name, holidays, range(2000, 2050))
                self.assertNoHolidayName(name, holidays, range(1987, 2000))
            elif subdiv == "PNI":
                self.assertHolidayName(name, holidays, dt)
                self.assertHolidayName(name, holidays, range(1987, 2050))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_gospel_day(self):
        name = "Gospel Day"
        self.assertNoHolidayName(name)
        dt = (
            "2004-08-20",
            "2005-08-22",
            "2010-08-20",
            "2011-08-22",
            "2016-08-22",
            "2021-08-20",
            "2022-08-22",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "KSA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-21" for year in range(2000, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(1987, 2000))
                self.assertHolidayName(f"{name} (observed)", holidays, dt)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_kosrae_liberation_day(self):
        name = "Kosrae Liberation Day"
        self.assertNoHolidayName(name)
        dt = (
            "2001-09-07",
            "2002-09-09",
            "2007-09-07",
            "2012-09-07",
            "2013-09-09",
            "2018-09-07",
            "2019-09-09",
            "2024-09-09",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "KSA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-08" for year in range(1991, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(1987, 1991))
                self.assertHolidayName(f"{name} (observed)", holidays, dt)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_self_government_day(self):
        name = "Self Government Day"
        self.assertNoHolidayName(name)
        dt = (
            "2001-11-02",
            "2002-11-04",
            "2007-11-02",
            "2012-11-02",
            "2013-11-04",
            "2018-11-02",
            "2019-11-04",
            "2024-11-04",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "KSA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-03" for year in range(1987, 2050))
                )
                self.assertHolidayName(f"{name} (observed)", holidays, dt)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_thanksgiving_day(self):
        name = "Thanksgiving Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "KSA":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-11-26",
                    "2021-11-25",
                    "2022-11-24",
                    "2023-11-23",
                    "2024-11-28",
                    "2025-11-27",
                )
                self.assertHolidayName(name, holidays, range(2011, 2050))
                self.assertNoHolidayName(name, holidays, range(1987, 2011))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_kosrae_disability_day(self):
        name = "Kosrae Disability Day"
        self.assertNoHolidayName(name)
        dt = (
            "2028-12-04",
            "2033-12-02",
            "2034-12-04",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "KSA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-03" for year in range(2024, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(1987, 2024))
                self.assertHolidayName(f"{name} (observed)", holidays, dt)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_womens_day(self):
        name = "Women's Day"
        self.assertNoHolidayName(name)
        dt = ("2025-03-07",)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PNI":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-08" for year in range(2022, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(1987, 2022))
                self.assertHolidayName(f"{name} (observed)", holidays, dt)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_pohnpei_cultural_day(self):
        name = "Pohnpei Cultural Day"
        self.assertNoHolidayName(name)
        dt = (
            "2001-03-30",
            "2002-04-01",
            "2007-03-30",
            "2012-03-30",
            "2013-04-01",
            "2019-04-01",
            "2024-04-01",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PNI":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-31" for year in range(1987, 2050))
                )
                self.assertHolidayName(f"{name} (observed)", holidays, dt)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_liberation_day(self):
        name = "Liberation Day"
        self.assertNoHolidayName(name)
        dt = (
            "2004-09-10",
            "2005-09-12",
            "2010-09-10",
            "2011-09-12",
            "2016-09-12",
            "2021-09-10",
            "2022-09-12",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PNI":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-11" for year in range(1987, 2050))
                )
                self.assertHolidayName(f"{name} (observed)", holidays, dt)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_pohnpei_constitution_day(self):
        name = "Pohnpei Constitution Day"
        self.assertNoHolidayName(name)
        dt = (
            "2003-11-07",
            "2008-11-07",
            "2009-11-09",
            "2014-11-07",
            "2015-11-09",
            "2020-11-09",
            "2025-11-07",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PNI":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-08" for year in range(1987, 2050))
                )
                self.assertHolidayName(f"{name} (observed)", holidays, dt)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_yap_day(self):
        name = "Yap Day"
        self.assertNoHolidayName(name)
        dt = (
            "2003-02-28",
            "2008-02-29",
            "2009-03-02",
            "2014-02-28",
            "2015-03-02",
            "2020-03-02",
            "2025-02-28",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "YAP":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-01" for year in range(1987, 2050))
                )
                self.assertHolidayName(f"{name} (observed)", holidays, dt)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_yap_state_constitution_day(self):
        name = "Yap State Constitution Day"
        self.assertNoHolidayName(name)
        dt = (
            "2000-12-25",
            "2005-12-23",
            "2006-12-25",
            "2011-12-23",
            "2016-12-23",
            "2017-12-25",
            "2022-12-23",
            "2023-12-25",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "YAP":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-24" for year in range(1987, 2050))
                )
                self.assertHolidayName(f"{name} (observed)", holidays, dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_2024(self):
        # https://www.timeanddate.com/holidays/micronesia/2024?hol=1
        self.assertHolidays(
            Micronesia(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-03-31", "Micronesian Culture and Tradition Day"),
            ("2024-04-01", "Micronesian Culture and Tradition Day (observed)"),
            ("2024-05-10", "Federated States of Micronesia Day"),
            ("2024-10-24", "United Nations Day"),
            ("2024-11-03", "Independence Day"),
            ("2024-11-04", "Independence Day (observed)"),
            ("2024-11-11", "FSM Veterans of Foreign Wars Day"),
            ("2024-11-22", "Presidents Day (observed)"),
            ("2024-11-23", "Presidents Day"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-01-10", "Kosrae State Constitution Day (observed)"),
            ("2025-01-11", "Kosrae State Constitution Day"),
            ("2025-02-28", "Yap Day (observed)"),
            ("2025-03-01", "Yap Day"),
            ("2025-03-07", "Women's Day (observed)"),
            ("2025-03-08", "Women's Day"),
            ("2025-03-31", "Micronesian Culture and Tradition Day; Pohnpei Cultural Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-09", "Federated States of Micronesia Day (observed)"),
            ("2025-05-10", "Federated States of Micronesia Day"),
            ("2025-08-21", "Gospel Day"),
            ("2025-09-08", "Kosrae Liberation Day"),
            ("2025-09-11", "Liberation Day"),
            ("2025-09-26", "State Charter Day"),
            ("2025-10-01", "Chuuk State Constitution Day"),
            ("2025-10-24", "United Nations Day"),
            ("2025-11-03", "Independence Day; Self Government Day"),
            ("2025-11-07", "Pohnpei Constitution Day (observed)"),
            ("2025-11-08", "Pohnpei Constitution Day"),
            ("2025-11-11", "FSM Veterans of Foreign Wars Day"),
            ("2025-11-23", "Presidents Day"),
            ("2025-11-24", "Presidents Day (observed)"),
            ("2025-11-27", "Thanksgiving Day"),
            ("2025-12-03", "Kosrae Disability Day"),
            ("2025-12-24", "Yap State Constitution Day"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-10", "Kosrae State Constitution Day (observed)"),
            ("2025-01-11", "Kosrae State Constitution Day"),
            ("2025-02-28", "Yap Day (observed)"),
            ("2025-03-01", "Yap Day"),
            ("2025-03-07", "Women's Day (observed)"),
            ("2025-03-08", "Women's Day"),
            ("2025-03-31", "Micronesian Culture and Tradition Day; Pohnpei Cultural Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-09", "Federated States of Micronesia Day (observed)"),
            ("2025-05-10", "Federated States of Micronesia Day"),
            ("2025-08-21", "Gospel Day"),
            ("2025-09-08", "Kosrae Liberation Day"),
            ("2025-09-11", "Liberation Day"),
            ("2025-09-26", "State Charter Day"),
            ("2025-10-01", "Chuuk State Constitution Day"),
            ("2025-10-24", "United Nations Day"),
            ("2025-11-03", "Independence Day; Self Government Day"),
            ("2025-11-07", "Pohnpei Constitution Day (observed)"),
            ("2025-11-08", "Pohnpei Constitution Day"),
            ("2025-11-11", "FSM Veterans of Foreign Wars Day"),
            ("2025-11-23", "Presidents Day"),
            ("2025-11-24", "Presidents Day (observed)"),
            ("2025-11-27", "Thanksgiving Day"),
            ("2025-12-03", "Kosrae Disability Day"),
            ("2025-12-24", "Yap State Constitution Day"),
            ("2025-12-25", "Christmas Day"),
        )
