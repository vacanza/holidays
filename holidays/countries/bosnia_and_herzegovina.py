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
#  Copyright: Kateryna Golovanova <kate@kgthreads.com>, 2022

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import FR, MO
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import DEC, JAN, JUN, MAR, MAY, NOV, SUN
from holidays.holiday_base import HolidayBase
from holidays.utils import _islamic_to_gre


class BosniaAndHerzegovina(HolidayBase):
    """
    Bosnia and Herzegovina holidays.
    See https://en.wikipedia.org/wiki/Public_holidays_in_Bosnia_and_Herzegovina
    for details.
    """

    country = "BA"
    subdivisions = [
        "BD",
        "FBiH",
        "RS",
    ]

    def _populate(self, year):

        # New Year's Day.
        self[date(year, JAN, 1)] = "Nova Godina"
        self[date(year, JAN, 2)] = "Drugi dan Nove Godine"

        if self.observed and date(year, JAN, 1).weekday() == SUN:
            self[date(year, JAN, 1) + rd(days=+2)] = "Treći dan Nove Godine"

        # Labor Day.
        may_1 = date(year, MAY, 1)
        self[may_1] = "Dan rada"
        self[may_1 + rd(days=+1)] = "Drugi dan Dana rada"

        if self.observed and may_1.weekday() == SUN:
            self[may_1 + rd(days=+2)] = "Treći dan Dana rada"

        if self.subdiv == "FBiH":
            # Independence Day.
            self[date(year, MAR, 1)] = "Dan nezavisnosti"

            # Catholic Good Friday.
            self[
                easter(year) + rd(weekday=FR(-1))
            ] = "Veliki Petak (Katolički)"

            # Catholic Easter.
            self[easter(year)] = "Uskrs (Katolički)"
            self[
                easter(year) + rd(weekday=MO(+1))
            ] = "Uskrsni ponedjeljak (Katolički)"

            # Corpus Cristi.
            self[
                easter(year) + rd(days=+60)
            ] = "Tijelovo (Tijelo i Krv Kristova)"

            # Eid al-Fitr.
            # Date of observance is announced yearly, this is an estimate.
            for dt in _islamic_to_gre(year, 10, 1):
                self[dt] = "Ramazanski Bajram"
                self[dt + rd(days=+1)] = "Drugi Dan Ramazanski Bajram"

            # Eid ul-Adha.
            # Date of observance is announced yearly, this is an estimate.
            name = "Kurban Bajram"
            for dt in _islamic_to_gre(year, 12, 10):
                self[dt] = name
                for d in range(1, 4):
                    self[dt + rd(days=+d)] = name

            # Islamic New Year.
            for dt in _islamic_to_gre(year, 1, 1):
                self[dt] = "Muslimanska Nova Godina"

            # All Saints Day.
            self[date(year, 11, 1)] = "Svi Sveti"

            # All Souls Day.
            self[date(year, 11, 2)] = "Dušni dan"

            # Statehood Day.
            self[date(year, NOV, 25)] = "Dan državnosti"

            # Catholic Christmas.
            self[date(year, DEC, 25)] = "Božić (Katolički)"

            # St. Stephen's Day.
            self[date(year, DEC, 26)] = "Stipandan (Stjepandan)"

        elif self.subdiv == "RS":
            # Orthodox Christmas Eve.
            self[date(year, JAN, 6)] = "Pravoslavno Badnje veče"

            # Orthodox Christmas.
            self[date(year, JAN, 7)] = "Božić (Божић)"

            # Republic day.
            self[date(year, JAN, 9)] = "Dan Republike"

            # Orthodox New Year.
            self[date(year, JAN, 14)] = "Pravoslavna Nova Godina"

            # Orthodox Good Friday.
            self[
                easter(year, method=2) + rd(weekday=FR(-1))
            ] = "Veliki Petak (Pravoslavni)"

            # Orthodox Easter.
            self[easter(year, method=2)] = "Vaskrs (Pravoslavni)"
            self[
                easter(year, method=2) + rd(weekday=MO(+1))
            ] = "Uskrsni ponedjeljak (Pravoslavni)"

            # Victory Day.
            self[date(year, MAY, 9)] = "Dan pobjede"

            # St. Vitus Day.
            self[date(year, JUN, 28)] = "Vidovdan"

            # Dayton Agreement Day.
            self[date(year, NOV, 21)] = (
                "Dan uspostave Opšteg okvirnog sporazuma za mir u "
                "Bosni i Hercegovini"
            )


class BA(BosniaAndHerzegovina):
    pass


class BIH(BosniaAndHerzegovina):
    pass
