#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from collections.abc import Iterable
from datetime import date
from typing import Optional, Union

from holidays.calendars import _HebrewLunisolar
from holidays.calendars.gregorian import _timedelta
from holidays.calendars.hebrew import (
    HANUKKAH,
    INDEPENDENCE_DAY,
    LAG_BAOMER,
    PASSOVER,
    PURIM,
    ROSH_HASHANAH,
    SHAVUOT,
    SUKKOT,
    TISHA_BAV,
    YOM_KIPPUR,
)


class HebrewCalendarHolidays:
    """
    Hebrew lunisolar calendar holidays.
    """

    @property
    def _hanukkah_date(self) -> set[Optional[date]]:
        """
        Return Hanukkah date.
        In some Gregorian years, there may be two Hanukkah dates.

        Hanukkah is a Jewish festival commemorating the recovery of Jerusalem
        and subsequent rededication of the Second Temple.
        https://en.wikipedia.org/wiki/Hanukkah
        """
        return {
            _HebrewLunisolar._get_holiday(HANUKKAH, year) for year in (self._year - 1, self._year)
        }

    @property
    def _israel_independence_date(self) -> Optional[date]:
        """
        Return Israel Independence Day date.

        Yom Ha'atzmaut is Israel's national day, commemorating the Israeli Declaration
        of Independence on 14 May 1948.
        https://en.wikipedia.org/wiki/Independence_Day_(Israel)
        """
        return _HebrewLunisolar._get_holiday(INDEPENDENCE_DAY, self._year)

    @property
    def _lag_baomer_date(self) -> Optional[date]:
        """
        Return Lag BaOmer date.

        Lag BaOmer, also Lag B'Omer or Lag LaOmer, is a Jewish religious holiday celebrated
        on the 33rd day of the Counting of the Omer, which occurs on the 18th day of
        the Hebrew month of Iyar.
        https://en.wikipedia.org/wiki/Lag_BaOmer
        """
        return _HebrewLunisolar._get_holiday(LAG_BAOMER, self._year)

    @property
    def _passover_date(self) -> Optional[date]:
        """
        Return Passover date.

        Passover, also called Pesach, is a major Jewish holiday and one of the Three Pilgrimage
        Festivals. It celebrates the Exodus of the Israelites from slavery in Egypt.
        https://en.wikipedia.org/wiki/Passover
        """
        return _HebrewLunisolar._get_holiday(PASSOVER, self._year)

    @property
    def _purim_date(self) -> Optional[date]:
        """
        Return Purim date.

        Purim is a Jewish holiday that commemorates the saving of the Jewish people
        from annihilation at the hands of an official of the Achaemenid Empire named Haman,
        as it is recounted in the Book of Esther.
        https://en.wikipedia.org/wiki/Purim
        """
        return _HebrewLunisolar._get_holiday(PURIM, self._year)

    @property
    def _rosh_hashanah_date(self) -> Optional[date]:
        """
        Return Rosh Hashanah date.

        Rosh Hashanah is the New Year in Judaism.
        https://en.wikipedia.org/wiki/Rosh_Hashanah
        """
        return _HebrewLunisolar._get_holiday(ROSH_HASHANAH, self._year)

    @property
    def _shavuot_date(self) -> Optional[date]:
        """
        Return Shavuot date.

        Shavuot, or Shvues, is a Jewish holiday, one of the biblically ordained
        Three Pilgrimage Festivals. It occurs on the sixth day of the Hebrew month of Sivan.
        https://en.wikipedia.org/wiki/Shavuot
        """
        return _HebrewLunisolar._get_holiday(SHAVUOT, self._year)

    @property
    def _sukkot_date(self) -> Optional[date]:
        """
        Return Sukkot date.

        Sukkot, also known as the Feast of Tabernacles or Feast of Booths, is a Torah-commanded
        holiday celebrated for seven days, beginning on the 15th day of the month of Tishrei.
        https://en.wikipedia.org/wiki/Sukkot
        """
        return _HebrewLunisolar._get_holiday(SUKKOT, self._year)

    @property
    def _tisha_bav_date(self) -> Optional[date]:
        """
        Return Tisha B'Av date.

        Tisha B'Av is an annual fast day in Judaism.
        https://en.wikipedia.org/wiki/Tisha_B%27Av
        """
        return _HebrewLunisolar._get_holiday(TISHA_BAV, self._year)

    @property
    def _yom_kippur_date(self) -> Optional[date]:
        """
        Return Yom Kippur date.

        Yom Kippur (Day of Atonement) is the holiest day of the year in Judaism.
        It occurs annually on the 10th of Tishrei.
        https://en.wikipedia.org/wiki/Yom_Kippur
        """
        return _HebrewLunisolar._get_holiday(YOM_KIPPUR, self._year)

    def _add_hebrew_holiday(self, name: str, dt: date, days_delta: Union[int, Iterable[int]] = 0):
        if days_delta:
            for delta in (days_delta,) if isinstance(days_delta, int) else days_delta:
                self._add_holiday(name, _timedelta(dt, delta))
        else:
            self._add_holiday(name, dt)
