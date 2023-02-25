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
#  Copyright: Kateryna Golovanova <kate@kgthreads.com>, 2022

from datetime import date
from datetime import timedelta as td

from dateutil.easter import EASTER_ORTHODOX, easter

from holidays.calendars import _islamic_to_gre
from holidays.constants import JAN, MAR, MAY, NOV, DEC
from holidays.holiday_base import HolidayBase


class BosniaAndHerzegovina(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Bosnia_and_Herzegovina
    https://www.paragraf.ba/neradni-dani-fbih.html
    https://www.paragraf.ba/neradni-dani-republike-srpske.html
    https://www.paragraf.ba/neradni-dani-brcko.html
    """

    country = "BA"
    subdivisions = [
        "BD",
        "FBiH",
        "RS",
    ]

    def _populate(self, year):
        def _add_holiday(hol_date: date, hol_name: str) -> None:
            if hol_date.year == year:
                self[hol_date] = hol_name

        # New Year's Day
        new_year = date(year, JAN, 1)
        self[new_year] = "Nova Godina"
        self[new_year + td(days=+1)] = "Drugi dan Nove Godine"

        if (
            self.subdiv in {"FBiH", "BD"}
            and self.observed
            and self._is_sunday(new_year)
        ):
            self[new_year + td(days=+2)] = "Treći dan Nove Godine"

        # Orthodox Christmas Eve
        if self.subdiv in {"FBiH", "RS"}:
            self[date(year, JAN, 6)] = "Pravoslavno Badnje veče"

        # Orthodox Christmas
        self[date(year, JAN, 7)] = "Božić (Божић)"

        # Orthodox New Year
        if self.subdiv == "RS":
            self[date(year, JAN, 14)] = "Pravoslavna Nova Godina"

        # Independence Day
        if self.subdiv == "FBiH":
            self[date(year, MAR, 1)] = "Dan nezavisnosti"

        # Day of establishment of Brčko District
        if self.subdiv == "BD":
            self[date(year, MAR, 8)] = "Dan uspostavljanja Brčko distrikta"

        easter_date_catholic = easter(year)
        easter_date_orthodox = easter(year, method=EASTER_ORTHODOX)
        if self.subdiv in {"FBiH", "RS"}:
            # Catholic Good Friday
            self[
                easter_date_catholic + td(days=-2)
            ] = "Veliki Petak (Katolički)"

            # Catholic Easter
            self[easter_date_catholic] = "Uskrs (Katolički)"

            # Orthodox Easter
            self[easter_date_orthodox] = "Vaskrs (Pravoslavni)"

            # Orthodox Easter Monday
            self[
                easter_date_orthodox + td(days=+1)
            ] = "Uskrsni ponedjeljak (Pravoslavni)"

        # Catholic Easter Monday
        self[
            easter_date_catholic + td(days=+1)
        ] = "Uskrsni ponedjeljak (Katolički)"

        # Orthodox Good Friday
        self[easter_date_orthodox + td(days=-2)] = "Veliki Petak (Pravoslavni)"

        # Labor Day
        may_1 = date(year, MAY, 1)
        self[may_1] = "Dan rada"
        self[may_1 + td(days=+1)] = "Drugi dan Dana rada"

        if self.observed and self._is_sunday(may_1):
            self[may_1 + td(days=+2)] = "Treći dan Dana rada"

        # Victory Day
        if self.subdiv in {"FBiH", "RS"}:
            self[date(year, MAY, 9)] = "Dan pobjede nad fašizmom"

        for yr in (year - 1, year):
            # Eid al-Fitr
            # Date of observance is announced yearly, this is an estimate
            for dt in _islamic_to_gre(yr, 10, 1):
                _add_holiday(dt, "Ramazanski Bajram")
                if self.subdiv in {"FBiH", "RS"}:
                    _add_holiday(
                        dt + td(days=+1), "Drugi Dan Ramazanski Bajram"
                    )
            # Eid ul-Adha
            # Date of observance is announced yearly, this is an estimate
            for dt in _islamic_to_gre(yr, 12, 10):
                _add_holiday(dt, "Kurban Bajram")
                if self.subdiv in {"FBiH", "RS"}:
                    _add_holiday(dt + td(days=+1), "Drugi Dan Kurban Bajram")

        # Dayton Agreement Day
        if self.subdiv == "RS":
            self[date(year, NOV, 21)] = (
                "Dan uspostave Opšteg okvirnog sporazuma za mir u "
                "Bosni i Hercegovini"
            )

        # Statehood Day
        if self.subdiv == "FBiH":
            self[date(year, NOV, 25)] = "Dan državnosti"

        # Catholic Christmas Eve
        if self.subdiv in {"FBiH", "RS"}:
            self[date(year, DEC, 24)] = "Badnji dan (Katolički)"

        # Catholic Christmas
        self[date(year, DEC, 25)] = "Božić (Katolički)"


class BA(BosniaAndHerzegovina):
    pass


class BIH(BosniaAndHerzegovina):
    pass
