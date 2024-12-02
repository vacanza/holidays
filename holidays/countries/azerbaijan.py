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

from datetime import date
from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.constants import PUBLIC, WORKDAY
from holidays.groups import InternationalHolidays, IslamicHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    WORKDAY_TO_NEXT_WORKDAY,
    SAT_SUN_TO_NEXT_WORKDAY,
)


class Azerbaijan(ObservedHolidayBase, InternationalHolidays, IslamicHolidays, StaticHolidays):
    """
    References:
        - https://en.wikipedia.org/wiki/Public_holidays_in_Azerbaijan
        - https://az.wikipedia.org/wiki/Az%C9%99rbaycan%C4%B1n_d%C3%B6vl%C9%99t_bayramlar%C4%B1_v%C9%99_x%C3%BCsusi_g%C3%BCnl%C9%99ri
        - https://www.sosial.gov.az/en/prod-calendar
    """

    country = "AZ"
    default_language = "az"
    # %s (estimated).
    estimated_label = tr("%s (təxmini)")
    # %s (observed).
    observed_label = tr("%s (müşahidə olunur)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (müşahidə olunur, təxmini)")
    supported_categories = (PUBLIC, WORKDAY)
    supported_languages = ("az", "en_US", "uk")
    start_year = 1990

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, AzerbaijanIslamicHolidays)
        StaticHolidays.__init__(self, AzerbaijanStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        kwargs.setdefault("observed_since", 2006)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        dts_observed = set()
        dts_non_observed = set()
        dts_bairami = set()

        # New Year's Day.
        name = tr("Yeni il bayramı")
        dts_observed.add(self._add_new_years_day(name))
        if self._year >= 2006:
            dts_observed.add(self._add_new_years_day_two(name))

        if self._year >= 2000:
            # Martyrs' Day.
            dts_non_observed.add(self._add_holiday_jan_20(tr("Ümumxalq hüzn günü")))

        # Women's Day.
        dts_observed.add(self._add_womens_day(tr("Qadınlar günü")))

        # Spring Festival.
        name = tr("Novruz bayramı")
        dts_observed.add(self._add_holiday_mar_20(name))
        dts_observed.add(self._add_holiday_mar_21(name))
        if self._year >= 2007:
            dts_observed.add(self._add_holiday_mar_22(name))
            dts_observed.add(self._add_holiday_mar_23(name))
            dts_observed.add(self._add_holiday_mar_24(name))

        dts_observed.add(
            self._add_world_war_two_victory_day(
                # Victory over Fascism Day.
                tr("Faşizm üzərində qələbə günü"),
                is_western=False,
            )
        )

        if self._year >= 1992:
            dts_observed.add(
                self._add_holiday_may_28(
                    # Independence Day.
                    tr("Müstəqillik Günü")
                    if self._year >= 2021
                    # Republic Day.
                    else tr("Respublika Günü")
                )
            )

        if self._year >= 1997:
            dts_observed.add(
                # National Liberation Day.
                self._add_holiday_jun_15(tr("Azərbaycan xalqının milli qurtuluş günü"))
            )

        if self._year >= 1992:
            # Armed Forces Day.
            name = tr("Azərbaycan Respublikasının Silahlı Qüvvələri günü")
            if self._year <= 1997:
                self._add_holiday_oct_9(name)
            else:
                dts_observed.add(self._add_holiday_jun_26(name))

        if self._year <= 2005:
            # Independence Day.
            self._add_holiday_oct_18(tr("Milli Müstəqillik Günü"))

        if self._year >= 2021:
            # Victory Day.
            dts_observed.add(self._add_holiday_nov_8(tr("Zəfər Günü")))

        if self._year >= 2010:
            dts_observed.add(
                # National Flag Day.
                self._add_holiday_nov_9(tr("Azərbaycan Respublikasının Dövlət bayrağı günü"))
            )

        if self._year >= 1993:
            # International Azerbaijanis Solidarity Day.
            name = tr("Dünya azərbaycanlılarının həmrəyliyi günü")
            self._add_new_years_eve(name)
            self._add_observed(date(self._year - 1, DEC, 31), name)

        if self._year >= 1993:
            # Eid al-Fitr.
            name = tr("Ramazan bayrami")
            dts_bairami.update(self._add_eid_al_fitr_day(name))
            if self._year >= 2006:
                dts_bairami.update(self._add_eid_al_fitr_day_two(name))

            # Eid al-Adha.
            name = tr("Qurban bayrami")
            dts_bairami.update(self._add_eid_al_adha_day(name))
            if self._year >= 2007:
                dts_bairami.update(self._add_eid_al_adha_day_two(name))

        # Article 105 of the Labor Code of the Republic of Azerbaijan states:
        # 5. If interweekly rest days and holidays that are not considered working days overlap,
        # that rest day is immediately transferred to the next working day.
        if self.observed and self._year >= 2006:
            self._populate_observed(dts_observed.union(dts_bairami))

            bayrami_names = {self.tr("Ramazan bayrami"), self.tr("Qurban bayrami")}
            # 6. If the holidays of Qurban and Ramadan coincide with another holiday
            # that is not considered a working day, the next working day is considered a rest day.
            for dt_observed in sorted(dts_bairami.difference(dts_non_observed)):
                if len(dt_holidays := self.get_list(dt_observed)) == 1:
                    continue
                for name in dt_holidays:
                    if name in bayrami_names:
                        self._add_observed(dt_observed, name, WORKDAY_TO_NEXT_WORKDAY)

    def _populate_workday_holidays(self):
        if self._year >= 2021:
            # Memorial Day.
            self._add_holiday_sep_27(tr("Anım Günü"))

        if self._year >= 2006:
            self._add_holiday_oct_18(
                # Independence Restoration Day.
                tr("Müstəqilliyin Bərpası Günü")
                if self._year >= 2021
                # Independence Day.
                else tr("Milli Müstəqillik Günü")
            )

        if self._year >= 1996:
            # Constitution Day.
            self._add_holiday_nov_12(tr("Konstitusiya Günü"))

        if self._year >= 1992:
            # National Revival Day.
            self._add_holiday_nov_17(tr("Milli Dirçəliş Günü"))


class AZ(Azerbaijan):
    pass


class AZE(Azerbaijan):
    pass


class AzerbaijanIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2002: (FEB, 21),
        2003: (FEB, 11),
        2004: (FEB, 1),
        2005: (JAN, 22),
        2006: ((JAN, 10), (DEC, 31)),
        2007: (DEC, 20),
        2008: (DEC, 8),
        2009: (NOV, 27),
        2010: (NOV, 16),
        2011: (NOV, 6),
        2012: (OCT, 25),
        2013: (OCT, 15),
        2014: (OCT, 4),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 1),
        2018: (AUG, 22),
        2019: (AUG, 12),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 16),
    }

    EID_AL_FITR_DATES = {
        2002: (DEC, 4),
        2003: (NOV, 25),
        2004: (NOV, 14),
        2005: (NOV, 3),
        2006: (OCT, 23),
        2007: (OCT, 12),
        2008: (SEP, 30),
        2009: (SEP, 20),
        2010: (SEP, 9),
        2011: (AUG, 30),
        2012: (AUG, 19),
        2013: (AUG, 8),
        2014: (JUL, 28),
        2015: (JUL, 17),
        2016: (JUL, 6),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 21),
        2024: (APR, 10),
    }


class AzerbaijanStaticHolidays:
    """
    Substituted holidays references:
        - https://nk.gov.az/az/senedler/qerarlar/is-va-istirahat-gunlarinin-yerlarinin-dayisdirilmasi-haqqinda-5423
        - https://nk.gov.az/az/senedler/qerarlar/is-va-istirahat-gunlarinin-yerlarinin--dayisdirilmasi-haqqinda-5982
        - https://nk.gov.az/az/senedler/qerarlar/is-va-istirahat-gunlarinin-yerlarinin-dayisdirilmasi-haqqinda-6488
        - https://nk.gov.az/az/senedler/qerarlar/is-ve-istirahet-gunlerinin-yerlerinin-deyisdirilme-7047
        - https://nk.gov.az/az/senedler/qerarlar/is-ve-istirahet-gunlerinin-yerlerinin-deyisdirilme-7466
        - https://nk.gov.az/az/senedler/qerarlar/is-ve-istirahet-gunlerinin-yerlerinin-deyisdirilme-7576
        - https://nk.gov.az/az/senedler/qerarlar/is-ve-istirahet-gunlerinin-yerlerinin-deyisdirilme-7843
        - https://nk.gov.az/az/senedler/qerarlar/is-ve-istirahet-gunlerinin-yerlerinin-deyisdirilme-8332
        - https://nk.gov.az/az/senedler/qerarlar/is-ve-istirahet-gunlerinin-yerlerinin-deyisdirilme-8449
    Special holidays references:
        - https://www.msk.gov.az/en/elections/pages/municipal-elections/belediyye-29-01-2025
    """

    eid_al_adha = tr("Qurban bayrami")
    # Substituted date format.
    substituted_date_format = tr("%d.%m.%Y")
    # Day off (substituted from %s).
    substituted_label = tr("İstirahət günü (%s ilə əvəz edilmişdir)")

    # Presidential elections.
    presidential_elections = tr("Prezidenti seçkiləri")

    # Municipal elections.
    municipal_elections = tr("Bələdiyyə seçkiləri")

    special_public_holidays = {
        2011: (AUG, 29, AUG, 27),
        2013: (
            (JAN, 3, DEC, 29, 2012),
            (JAN, 4, DEC, 30, 2012),
        ),
        2014: (
            (JAN, 3, DEC, 28, 2013),
            (JAN, 6, DEC, 29, 2013),
        ),
        2018: (APR, 11, presidential_elections),
        2019: (DEC, 27, municipal_elections),
        2020: (
            (MAR, 27, MAR, 29),
            (MAY, 27, MAY, 30),
            (JAN, 3, DEC, 28, 2019),
            (JAN, 6, DEC, 29, 2019),
        ),
        2021: (
            (MAY, 11, MAY, 8),
            (MAY, 12, MAY, 16),
            (JUL, 19, JUL, 17),
        ),
        2022: (
            (MAR, 7, MAR, 5),
            (NOV, 7, NOV, 5),
        ),
        2023: (
            (JUN, 27, JUN, 24),
            (JUN, 30, JUN, 25),
            (NOV, 10, NOV, 4),
        ),
        2024: (
            (JAN, 4, DEC, 30, 2023),
            (JAN, 5, JAN, 7),
            (FEB, 7, presidential_elections),
            (APR, 12, APR, 6),
            (NOV, 12, NOV, 16),
            (NOV, 13, NOV, 23),
            (DEC, 30, DEC, 28),
        ),
        2025: (
            (JAN, 3, DEC, 29, 2024),
            (JAN, 29, municipal_elections),
        ),
    }

    special_public_holidays_observed = {
        2007: (JAN, 3, eid_al_adha),
        2072: (JAN, 5, eid_al_adha),
    }
