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

from gettext import gettext as tr

from holidays.calendars.gregorian import JAN
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class Monaco(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Monaco holidays.

    References:
        * [Law No. 798 of Feb 18, 1966](https://web.archive.org/web/20260418044949/https://legimonaco.mc/tnc/loi/1966/02-18-798/)
        * [Circular No. 2019-2](https://web.archive.org/web/20260415115315/https://journaldemonaco.gouv.mc/Journaux/2019/Journal-8427/Circulaire-n-2019-2-Modification-de-la-circulaire-n-79-93-du-13-novembre-1979-parue-au-Journal-de-Monaco-du-23-novembre-1979-concernant-l-application-de-la-loi-n-1.020-du-5-juillet-1979-modifiant-la-loi-n-800-du-18-fevrier-1966-regissant-la-remunera)
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Monaco>
        * <https://web.archive.org/web/20220729194021/https://en.service-public-entreprises.gouv.mc/Employment-and-social-affairs/Employment-regulations/Leave/Public-Holidays>

    Checked with:
        * [2016](https://web.archive.org/web/20260122031654/https://journaldemonaco.gouv.mc/Journaux/2015/Journal-8248/Communique-n-2015-12-du-15-octobre-2015-relatif-a-la-liste-des-jours-chomes-et-payes-pour-l-annee-2016)
        * [2017](https://web.archive.org/web/20220830085850/https://journaldemonaco.gouv.mc/Journaux/2016/Journal-8300/Circulaire-n-2016-09-du-10-octobre-2016-relative-a-la-liste-des-jours-chomes-et-payes-pour-l-annee-2017)
        * [2018](https://web.archive.org/web/20260417161343/https://journaldemonaco.gouv.mc/Journaux/2017/Journal-8353/Circulaire-n-2017-9-du-18-octobre-2017-relative-a-la-liste-des-jours-chomes-et-payes-pour-l-annee-2018)
        * [2019](https://web.archive.org/web/20260413120235/https://journaldemonaco.gouv.mc/Journaux/2018/Journal-8402/Circulaire-n-2018-12-du-24-septembre-2018-relative-a-la-liste-des-jours-chomes-et-payes-pour-l-annee-2019)
        * [2019 Immaculate Conception](https://web.archive.org/web/20260416082709/https://journaldemonaco.gouv.mc/Journaux/2019/Journal-8427/Circulaire-n-2019-1-Modification-de-la-circulaire-n-2018-12-du-24-septembre-2018-parue-au-Journal-de-Monaco-du-5-octobre-2018-relative-a-la-liste-des-jours-chomes-et-payes-pour-l-annee-2019)
        * [2020](https://web.archive.org/web/20250909040043/https://journaldemonaco.gouv.mc/Journaux/2019/Journal-8459/Circulaire-n-2019-12-du-22-octobre-2019-relative-a-la-liste-des-jours-chomes-et-payes-pour-l-annee-2020)
        * [2021](https://web.archive.org/web/20241004075126/https://journaldemonaco.gouv.mc/Journaux/2020/Journal-8505/Circulaire-n-2020-7-du-14-septembre-2020-relative-a-la-liste-des-jours-chomes-et-payes-pour-l-annee-2021)
        * [2022](https://web.archive.org/web/20260210124905/https://journaldemonaco.gouv.mc/Journaux/2021/Journal-8560/Circulaire-n-2021-8-du-27-septembre-2021-relative-a-la-liste-des-jours-chomes-et-payes-pour-l-annee-2022.)
        * [2023](https://web.archive.org/web/20251208004325/https://journaldemonaco.gouv.mc/Journaux/2022/Journal-8612/Circulaire-n-2022-14-du-5-octobre-2022-relative-a-la-liste-des-jours-chomes-et-payes-pour-l-annee-2023)
        * [2024](https://web.archive.org/web/20250906203823/https://journaldemonaco.gouv.mc/Journaux/2023/Journal-8664/Circulaire-n-2023-14-du-2-octobre-2023-relative-a-la-liste-des-jours-chomes-et-payes-pour-l-annee-2024.)
        * [2025](https://web.archive.org/web/20251006035703/https://journaldemonaco.gouv.mc/Journaux/2024/Journal-8716/Circulaire-n-2024-7-du-1er-octobre-2024-relative-a-la-liste-des-jours-chomes-et-payes-pour-l-annee-2025.)
        * [2026](https://web.archive.org/web/20260217063816/https://journaldemonaco.gouv.mc/Journaux/2025/Journal-8768/Circulaire-n-2025-8-du-1er-octobre-2025-relative-a-la-liste-des-jours-chomes-et-payes-pour-l-annee-2026)
    """

    country = "MC"
    default_language = "fr_MC"
    # %s (observed).
    observed_label = tr("%s (reporté)")
    # Law No. 798 of Feb 18, 1966.
    start_year = 1967
    supported_languages = ("en_US", "fr_MC", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, MonacoStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("Le jour de l'An")))

        # Saint Devote's Day.
        self._add_holiday_jan_27(tr("Le jour de la Sainte-Dévote"))

        # Easter Monday.
        self._add_easter_monday(tr("Le Lundi de Pâques"))

        # Labor Day.
        self._add_observed(self._add_labor_day(tr("Le jour de la Fête du Travail")))

        # Ascension Day.
        self._add_ascension_thursday(tr("Le jour de l'Ascension"))

        # Pentecost Monday.
        self._add_pentecost_monday(tr("Le Lundi de Pentecôte"))

        # Corpus Christi.
        self._add_corpus_christi_day(tr("Le jour de la Fête Dieu"))

        # Assumption Day.
        self._add_observed(self._add_assumption_of_mary_day(tr("Le jour de l'Assomption")))

        # All Saints' Day.
        self._add_observed(self._add_all_saints_day(tr("Le jour de la Toussaint")))

        self._add_observed(
            # Prince's Day.
            self._add_holiday_nov_19(tr("Le jour de la Fête de S.A.S. le Prince Souverain"))
        )

        # Immaculate Conception.
        dt = self._add_immaculate_conception_day(tr("Le jour de l'Immaculée Conception"))
        # Circular No. 2019-2.
        if self._year >= 2019:
            self._add_observed(dt)

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Le jour de Noël")))


class MC(Monaco):
    pass


class MCO(Monaco):
    pass


class MonacoStaticHolidays:
    """Monaco special holidays.

    References:
        * [Law No. 1.413 of Dec 19, 2014](https://web.archive.org/web/20251215053349/https://journaldemonaco.gouv.mc/Journaux/2014/Journal-8205/Loi-n-1.413-du-19-decembre-2014-declarant-jour-ferie-legal-le-7-janvier-2015)
    """

    special_public_holidays = {
        # Public holiday.
        2015: (JAN, 7, tr("Jour férié")),
    }
