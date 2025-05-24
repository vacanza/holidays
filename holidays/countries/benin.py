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

from holidays.calendars.gregorian import MAY
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase


class Benin(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Benin holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Benin>

        * [2022 All Saints' Day] (https://web.archive.org/web/20241010101230/https://travail.gouv.bj/page/communiques/la-journee-du-mardi-1er-novembre-2022-declaree-feriee-chomee-et-payee)
        * [2022 Christmas Day] (https://web.archive.org/web/20240814200022/https://travail.gouv.bj/page/communiques/la-journee-du-dimanche-25-decembre-2022-declaree-feriee-chomee-et-payee-a-loccasion-de-la-celebration-de-la-fete-de-noel-lire-le-communique-du-ministre-du-travail-et-de-la-fonction-publique)

        * [2023 New Year's Day] (https://web.archive.org/web/20240724084416/https://travail.gouv.bj/page/communiques/la-journee-du-dimanche-1er-janvier-2023-declaree-feriee-chomee-et-payee-a-loccasion-de-la-celebration-de-la-fete-du-nouvel-an)
        * [2023 Vodoun Festival] (https://web.archive.org/web/20240724084406/https://travail.gouv.bj/page/communiques/la-journee-du-mardi-10-janvier-2023-est-declaree-feriee-chomee-et-payee-a-loccasion-de-la-celebration-de-la-fete-annuelle-des-religions-traditionnelles-2301071350-956)
        * [2023 Eid al-Fitr] (https://web.archive.org/web/20240723004550/https://travail.gouv.bj/page/communiques/celebration-le-vendredi-21-avril-2023-de-la-fete-du-ramadan)
        * [2023 Easter Monday] (https://web.archive.org/web/20241010103541/https://travail.gouv.bj/page/communiques/la-journee-du-lundi-10-avril-2023-est-declaree-feriee-chomee-et-payee-en-raison-de-la-fete-de-paques)
        * [2023 Whit Monday](https://web.archive.org/web/20240911163554/https://travail.gouv.bj/page/communiques/la-fete-de-pentecote)
        * [2023 Labor Day] (https://web.archive.org/web/20240814205702/https://travail.gouv.bj/page/communiques/la-journee-du-lundi-1er-mai-2023-declaree-feriee-chomee-et-payee-sur-toute-letendue-du-territoire-national-a-loccasion-de-la-celebration-de-la-fete-du-travail)
        * [2023 Assumption Day] (https://web.archive.org/web/20241214182235/https://travail.gouv.bj/page/communiques/la-journee-du-mardi-15-aout-2023-declaree-feriee-chomee-et-payee-en-raison-de-la-fete-de-lassomption)
        * [2023 Independence Day] (https://web.archive.org/web/20240723004533/https://travail.gouv.bj/page/communiques/la-journee-du-mardi-1er-aout-2023-declaree-feriee-chomee-et-payee-a-l-occasion-de-la-fete-nationale)
        * [2023 Eid al-Adha] (https://web.archive.org/web/20250422035008/https://travail.gouv.bj/page/communiques/communique-du-ministere-du-travail-et-de-la-fonction-publique-2306262022-744)

        * [2024] (https://web.archive.org/web/20250317151037/http://beninconsulate.co.ke/index.php/news-events)
        * [2024 Vodoun Festival] (https://web.archive.org/web/20240723004435/https://travail.gouv.bj/page/communiques/la-journee-du-mercredi-10-janvier-2024-est-feriee-chomee-et-payee-sur-toute-letendue-du-territoire-national)
        * [2024 Eid al-Fitr] (https://web.archive.org/web/20241010114534/https://travail.gouv.bj/page/communiques/la-journee-du-mercredi-10-avril-2024-jour-du-ramadan-est-declaree-feriee-chomee-et-payee-sur-toute-letendue-du-territoire-national)
        * [2024 Easter Monday] (https://web.archive.org/web/20241106004344/https://travail.gouv.bj/page/communiques/la-journee-du-lundi-1er-avril-2024-lundi-de-paques-est-chomee)
        * [2024 Assumption Day] (https://web.archive.org/web/20250215044724/https://travail.gouv.bj/page/communiques/la-journee-du-dimanche-15-aout-jour-de-lassomption-est-feriee-chomee-et-payee-sur-toute-letendue-du-territoire-national)
        * [2024 Eid al-Adha] (https://web.archive.org/web/20241214200230/https://travail.gouv.bj/page/communiques/jour-de-la-tabaski)
        * [2024 Labor Day] (https://web.archive.org/web/20250418224409/https://www.travail.gouv.bj/page/communiques/la-journee-du-mercredi-1er-mai-2024-journee-de-la-fete-du-travail-est-feriee-chomee-et-payee-sur-toute-letendue-du-territoire-national)
        * [2024 Ascension Day] (https://web.archive.org/web/20241214204011/https://travail.gouv.bj/page/communiques/le-jeudi-09-mai-2024-jour-de-lascension-est-feriee-chomee-et-payee-sur-toute-letendue-du-territoire-national)
        * [2024 Whit Monday] (https://web.archive.org/web/20241010113401/https://travail.gouv.bj/page/communiques/le-lundi-20-mai-2024-lundi-de-pentecote-est-ferie-chome-et-paye-sur-toute-letendue-du-territoire-national)
        * [2024 Prophet's Birthday] (https://web.archive.org/web/20250215034616/https://travail.gouv.bj/page/communiques/la-journee-du-dimanche-15-septembre-2024-jour-de-maoloud-est-feriee-chomee-et-payee-sur-toute-letendue-du-territoire-national)
        * [2024 Christmas Day] (https://web.archive.org/web/20250122081816/https://travail.gouv.bj/page/communiques/la-journee-du-mercredi-25-decembre-2024-est-feriee-chomee-et-payee-sur-toute-letendue-du-territoire-national)

        * [2025] (https://web.archive.org/web/20250317141957/https://beninconsulate.co.ke/index.php/news-events?start=1)
        * [2025 New Year's Day] (https://web.archive.org/web/20250422023225/https://travail.gouv.bj/page/communiques/la-journee-du-mercredi-1er-janvier-2025-fete-du-nouvel-an-est-feriee-chomee-et-payee-sur-toute-letendue-du-territoire-national)
        * [2025 Vodoun Festival] (https://web.archive.org/web/20250422034718/https://travail.gouv.bj/page/communiques/les-journees-du-jeudi-9-janvier-2024-et-vendredi-10-janvier-2024-sont-feriees-chomees-et-payees-sur-toute-letendue-du-territoire-national)
    """

    country = "BJ"
    default_language = "fr_BJ"
    # %s (observé).
    observed_label = tr("%s (observé)")
    # %s (estimé).
    estimated_label = tr("%s (estimé)")
    # %s (observé, estimé).
    observed_estimated_label = tr("%s (observé, estimé)")
    supported_languages = ("en_US", "fr_BJ")
    start_year = 1960

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, show_estimated=islamic_show_estimated)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Jour de l'An"))

        # Vodoun Festival.
        name = tr("Journée Vaudoun")
        if self._year == 2024:
            self._add_holiday_jan_10(name)
            self._add_holiday_jan_9(f"{name} (observé)")
        else:
            self._add_holiday_jan_10(name)

        # Easter Monday.
        self._add_easter_monday(tr("Lundi de Pâques"))

        # Labour Day.
        self._add_labor_day(tr("Fête du Travail"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Jour de l'Ascension"))

        whit_monday_dates = {
            2023: (MAY, 29),
        }
        # Whit Monday.
        name = tr("Lundi de Pentecôte")
        if self._year in whit_monday_dates:
            self._add_holiday(name, whit_monday_dates[self._year])
        else:
            self._add_whit_monday(name)

        # Independence Day.
        self._add_holiday_aug_1(tr("Jour de l'indépendance"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Jour de l'Assomption"))

        # All Saints' Day.
        self._add_all_saints_day(tr("La Toussaint"))

        # Christmas Day.
        self._add_christmas_day(tr("Jour de Noël"))

        # Islamic holidays.

        # Prophet's Birthday.
        self._add_mawlid_day(tr("Maouloud"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Korité"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Tabaski"))


class BJ(Benin):
    pass


class BEN(Benin):
    pass
