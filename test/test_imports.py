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


class TestHolidayslImports:
    def test_constants(self):
        from holidays import MON, TUE, WED, THU, FRI, SAT, SUN

    def test_holidays_base(self):
        from holidays import DateLike, HolidayBase, HolidaySum

    def test_utils(self):
        from holidays import CountryHoliday, country_holidays
        from holidays import financial_holidays, list_supported_countries
        from holidays import list_supported_financial
