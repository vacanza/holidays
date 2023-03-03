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

from datetime import date

from holidays.calendars import _get_nth_weekday_of_month
from holidays.constants import JAN, FEB, MAR, MAY, SEP, NOV, DEC, MON
from holidays.holiday_base import HolidayBase


class Mexico(HolidayBase):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Mexico
    - https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_festivos_en_M%C3%A9xico
    - https://www.gob.mx/cms/uploads/attachment/file/156203/1044_Ley_Federal_del_Trabajo.pdf  # noqa: E501
    - http://www.diputados.gob.mx/LeyesBiblio/ref/lft/LFT_orig_01abr70_ima.pdf
    """

    country = "MX"
    default_language = "es"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self[date(year, JAN, 1)] = self.tr("Año Nuevo")

        if year >= 1917:
            self[
                _get_nth_weekday_of_month(1, MON, FEB, year)
                if year >= 2006
                else date(year, FEB, 5)
                # Constitution Day.
            ] = self.tr("Día de la Constitución")

        if year >= 1917:
            self[
                _get_nth_weekday_of_month(3, MON, MAR, year)
                # no 2006 due to celebration of the 200th anniversary
                # of Benito Juárez in 2006
                if year >= 2007
                else date(year, MAR, 21)
                # Benito Juárez's birthday.
            ] = self.tr("Natalicio de Benito Juárez")

        if year >= 1923:
            # Labour Day.
            self[date(year, MAY, 1)] = self.tr("Día del Trabajo")

        # Independence Day.
        self[date(year, SEP, 16)] = self.tr("Día de la Independencia")

        if year >= 1917:
            self[
                _get_nth_weekday_of_month(3, MON, NOV, year)
                if year >= 2006
                else date(year, NOV, 20)
                # Revolution Day.
            ] = self.tr("Día de la Revolución")

        if year >= 1970 and (year - 1970) % 6 == 0:
            # Change of Federal Government.
            self[date(year, DEC, 1)] = self.tr(
                "Transmisión del Poder Ejecutivo Federal"
            )

        # Christmas Day.
        self[date(year, DEC, 25)] = self.tr("Navidad")


class MX(Mexico):
    pass


class MEX(Mexico):
    pass
