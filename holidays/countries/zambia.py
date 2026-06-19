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

from holidays.calendars.gregorian import JAN, MAR, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class Zambia(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Zambia holidays.

    While Easter Sunday and Easter Monday are not explicitly listed in The Public Holidays Act,
    they're included annually via Section 3 (Power to declare additional public holidays).

    According to the The Constitution of Zambia (Amendment) Act, 2016 (Act No. 2 of 2016):
        Art. 56. (1) A general election shall be held, every five years after
                     the last general election, on the second Thursday of August.
                 (2) The day on which a general election is held shall be a public holiday.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Zambia>
        * <https://web.archive.org/web/20251231114231/https://diggers.news/local/2025/03/20/govt-shifts-dates-for-heroes-unity-day-celebrations/>
        * [Public Holidays (Amendment) Act, 1983](https://web.archive.org/web/20260619052920/https://media.zambialii.org/media/legislation/32576/source_file/a486a2d17b169913/zm-act-1983-12-publication-document.pdf)
        * [Public Holidays (Amendment) Act, 1987](https://web.archive.org/web/20260619052723/https://media.zambialii.org/media/legislation/34567/source_file/24d5d4308fa254b8/zm-act-1987-23-publication-document.pdf)
        * [The Public Holidays Act, 1964 (December 31st, 1996 Consolidated Version)](https://web.archive.org/web/20231208015918/https://www.parliament.gov.zm/sites/default/files/documents/acts/Public%20Holidays%20Act.pdf)
        * [The Public Holiday (Declaration) Notice, 2007](https://web.archive.org/web/20260618090525/https://media.zambialii.org/media/legislation/40206/source_file/4ae8f8a36bdf2102/zm-act-si-2007-33-publication-document.pdf)
        * [The Public Holiday (Declaration), Notice, 2015](https://web.archive.org/web/20260619040408/https://media.zambialii.org/media/legislation/41471/source_file/c067d60ca47e5b94/zm-act-si-2015-78-publication-document.pdf)
        * [The Constitution of Zambia (Amendment) Act, 2016 (Act No. 2 of 2016)](https://web.archive.org/web/20260619050424/https://www.wipo.int/wipolex/en/legislation/details/18212)
        * [The Public Holidays (Declaration) Notice, 2021](https://web.archive.org/web/20260618085320/https://media.zambialii.org/media/legislation/20557/source_file/a522bf833eba3759/zm-act-si-2021-72-publication-document.pdf)
        * [Gazette Notice No. 1169 of 2025](http://archive.today/2026.06.19-063418/https://www.scribd.com/embeds/1014654689/content)
    """

    country = "ZM"
    observed_label = "%s (observed)"
    # Public Holidays (Amendment) Act, 1983 came into effect on April 8th, 1983.
    start_year = 1984

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, ZambiaStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # The Public Holiday (Declaration) Notice, 2007.
        if self._year >= 2008:
            # International Women's Day.
            self._add_observed(self._add_womens_day("International Women's Day"))

        # Youth Day.
        name = "Youth Day"
        if self._year >= 1988:
            self._add_observed(self._add_holiday_mar_12(name))
        else:
            self._add_holiday_3rd_sat_of_mar(name)

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Holy Saturday.
        self._add_holy_saturday("Holy Saturday")

        # Easter Sunday.
        self._add_easter_sunday("Easter Sunday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # The Public Holidays (Declaration) Notice, 2021.
        if self._year >= 2022:
            # Kenneth Kaunda Day.
            self._add_observed(self._add_holiday_apr_28("Kenneth Kaunda Day"))

        # Labor Day.
        self._add_observed(self._add_labor_day("Labour Day"))

        # Africa Freedom Day.
        self._add_observed(self._add_africa_day("Africa Freedom Day"))

        # Heroes' Day.
        self._add_holiday_1st_mon_of_jul("Heroes' Day")

        # Unity Day.
        self._add_holiday_1_day_past_1st_mon_of_jul("Unity Day")

        # Farmers' Day.
        self._add_holiday_1st_mon_of_aug("Farmers' Day")

        # The Public Holiday (Declaration), Notice, 2015.
        if self._year >= 2016:
            # National Prayer Day.
            self._add_observed(self._add_holiday_oct_18("National Prayer Day"))

            # The Constitution of Zambia (Amendment) Act, 2016 (Act No. 2 of 2016).
            if self._year % 5 == 1:
                # General Election Day.
                self._add_holiday_2nd_thu_of_aug("General Election Day")

        # Independence Day.
        self._add_observed(self._add_holiday_oct_24("Independence Day"))

        # Christmas Day.
        self._add_observed(self._add_christmas_day("Christmas Day"))


class ZM(Zambia):
    pass


class ZMB(Zambia):
    pass


class ZambiaStaticHolidays:
    """Zambia special holidays.

    References:
       * [The Public Holiday (Declaration) Notice, 2014](https://web.archive.org/web/20260619024137/https://media.zambialii.org/media/legislation/41389/source_file/4c0627188f528494/zm-act-si-2014-61-publication-document.pdf)
       * [The Public Holidays (Declaration) Notice, 2014](https://web.archive.org/web/20260619035400/https://media.zambialii.org/media/legislation/41393/source_file/448987a69ee8f357/zm-act-si-2014-66-publication-document.pdf)
       * [The Public Holidays (Declaration) Notice, 2015](https://web.archive.org/web/20260619040014/https://media.zambialii.org/media/legislation/41397/source_file/285b30277071303f/zm-act-si-2015-1-publication-document.pdf)
       * [The Public Holidays (Declaration) Notice 2016](https://web.archive.org/web/20260619040813/https://media.zambialii.org/media/legislation/41587/source_file/1287ab93099c38bc/zm-act-si-2016-66-publication-document.pdf)
       * [The Public Holidays (Declaration) Notice, 2018](https://web.archive.org/web/20260619042036/https://media.zambialii.org/media/legislation/42023/source_file/db3fb6a9f874f9cf/zm-act-si-2018-15-publication-document.pdf)
       * [The Public Holidays (Declaration) (No. 2) Notice, 2018](https://web.archive.org/web/20260619041704/https://media.zambialii.org/media/legislation/41988/source_file/0d665b642b92af1d/zm-act-si-2018-55-publication-document.pdf)
       * [The Public Holidays (Declaration) Notice, 2019](https://web.archive.org/web/20260619041859/https://media.zambialii.org/media/legislation/41889/source_file/296795324217f09a/zm-act-si-2019-71-publication-document.pdf)
       * [The Public Holidays (Declaration) Notice, 2021](https://web.archive.org/web/20260618090004/https://media.zambialii.org/media/legislation/20656/source_file/0a71ea33a669b4c7/zm-act-si-2021-69-publication-document.pdf)
       * [The Public Holidays (Declaration) (No. 2) Notice, 2021](https://web.archive.org/web/20260618090354/https://media.zambialii.org/media/legislation/20849/source_file/208ddaf910039a7b/zm-act-si-2021-71-publication-document.pdf)
       * [The Public Holidays (Declaration) (No. 4) Notice, 2021](https://media.zambialii.org/media/legislation/20635/source_file/a028171d09918fdf/zm-act-si-2021-73-publication-document.pdf)
       * [The Public Holidays (Declaration) Notice, 2022](https://web.archive.org/web/20260618090121/https://media.zambialii.org/media/legislation/20676/source_file/01907c24e7d34f3e/zm-act-si-2022-20-publication-document.pdf)
    """

    # Bridge Public Holiday.
    name_bridge_public_holiday = "Bridge Public Holiday"

    # Inauguration Ceremony of President-elect and Vice-President-elect.
    name_inauguration_ceremony = (
        "Inauguration Ceremony of President-elect and Vice-President-elect"
    )

    special_public_holidays = {
        2014: (
            # State Funeral of Michael Chilufya Sata.
            (NOV, 11, "State Funeral of Michael Chilufya Sata"),
            (DEC, 26, name_bridge_public_holiday),
        ),
        2015: (
            (JAN, 2, name_bridge_public_holiday),
            # Presidential Election.
            (JAN, 20, "Presidential Election"),
        ),
        2016: ((SEP, 13, name_inauguration_ceremony),),
        2018: (
            (MAR, 9, name_bridge_public_holiday),
            # Mayoral and Ward By-elections.
            (JUL, 26, "Mayoral and Ward By-elections"),
        ),
        2019: (OCT, 25, name_bridge_public_holiday),
        2021: (
            # Memorial Service for Kenneth Kaunda.
            (JUL, 2, "Memorial Service for Kenneth Kaunda"),
            # State Funeral of Kenneth Kaunda.
            (JUL, 7, "State Funeral of Kenneth Kaunda"),
            (AUG, 13, name_bridge_public_holiday),
            (AUG, 24, name_inauguration_ceremony),
        ),
        # State Funeral of Rupiah Banda.
        2022: (MAR, 18, "State Funeral of Rupiah Banda"),
    }
