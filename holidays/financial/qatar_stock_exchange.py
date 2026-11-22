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

from holidays.calendars.gregorian import MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, DEC
from holidays.constants import PUBLIC
from holidays.countries.qatar import Qatar
from holidays.groups import StaticHolidays
from holidays.helpers import tr


class QatarStockExchange(Qatar):
    """Qatar Stock Exchange (QSE) holidays.

    QSE follows the Qatar public and bank holidays and trades from Sunday to Thursday.
    The Eid closures are set every year by the Qatar Financial Markets Authority and
    usually run longer than the Eid days themselves.

    References:
        * [Calendar of Business Days 2011](https://web.archive.org/web/20211025231733/https://www.qe.com.qa/documents/20181/664307/QE+Market+Notice+029+-+2010+12+09+Calendar+of+Business+days+2011.pdf/28a9204b-7a52-0ee7-6127-b49f0fe1ed39)
        * [Bank Holiday 2011](https://web.archive.org/web/20211025230355/https://www.qe.com.qa/documents/20181/663726/QE+Market+Notice+013-+2011+03+02+Bank+Holiday+on+Sunday+6+March+2011.pdf/6bdacfe7-c174-5b0f-6c49-8de88d3dcd0e)
        * [New Year's Day 2012](https://web.archive.org/web/20211023003630/https://www.qe.com.qa/documents/20181/663726/QE+Market+Notice+042+-+2011+12+28+official+holiday.pdf/3034bbc7-10cc-521b-d0f6-181644e28b6b)
        * [National Sport Day 2012](https://web.archive.org/web/20211023021841/https://www.qe.com.qa/documents/20181/663279/QE+Market+Notice+02-+2012+02+09+National+sports+day+on+Tuesday+14+February+2012.pdf/fe8c878f-f26c-9e36-1700-7840e8e8f792)
    """

    country = None  # type: ignore[assignment]
    market = "DSMD"
    parent_entity = Qatar
    supported_categories = (PUBLIC,)  # type: ignore[assignment]
    start_year = 2011

    def __init__(self, *args, **kwargs):
        StaticHolidays.__init__(self, QatarStockExchangeStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        super()._populate_public_holidays()
        super()._populate_bank_holidays()

        for dt in tuple(self.keys()):
            if self._is_weekend(dt):
                self.pop(dt)


class DSMD(QatarStockExchange):
    pass


class QSE(QatarStockExchange):
    pass


class QatarStockExchangeStaticHolidays:
    """Qatar Stock Exchange (QSE) special holidays.

    References:
        * 2011:
            * [Eid al-Fitr](https://web.archive.org/web/20211026001619/https://www.qe.com.qa/documents/20181/663726/QE_Market_Notice_31_-_2011_08_25_Eid_AL_fitr_Holiday%5B1%5D.pdf/6a814c4f-a7c2-812d-c45c-9f46470cddc8)
        * 2012:
            * [Eid al-Adha](https://web.archive.org/web/20211023020155/https://www.qe.com.qa/documents/20181/663279/QE+Market+Notice+027+-+2012+10+22+Eid+Al-Adha+Holiday.pdf/a4a826bd-d8c1-c475-0fca-279c278d76bf)
        * 2013:
            * [Public Holiday](https://web.archive.org/web/20211023012136/https://www.qe.com.qa/documents/20181/662727/QE+Market+Notice+018-+2013+06+24+Officially+holiday.pdf/6f6b61fa-ad16-cf1d-6d45-12ed9fd32fe0)
            * [Eid al-Fitr](https://web.archive.org/web/20211023022006/https://www.qe.com.qa/documents/20181/662727/QE+Market+Notice+026+-+2013+08+06+Eid+AL+fitr+Holiday.pdf/06cd30bc-63f5-7341-23d0-0eed85147670)
            * [Eid al-Adha](https://web.archive.org/web/20211016191403/https://www.qe.com.qa/documents/20181/662727/QE+Market+Notice+036+-+2013+10+08+Eid+Al-Adha+Holiday.pdf/a9765ffd-0cc6-3c85-8715-cc6270c02df7)
            * [National Day](https://web.archive.org/web/20211025225044/https://www.qe.com.qa/documents/20181/662727/QE+Market+Notice+041+-+2013+12+17+National+Day+Holiday+%282%29.pdf/eb637af3-163b-4b7b-8f04-90502c94d750)
        * 2014:
            * [Eid al-Fitr](https://web.archive.org/web/20211016180327/https://www.qe.com.qa/documents/20181/658970/QE+Market+Notice+020-+2014+07+24+Eid+AL+fitr+Holiday.pdf/d34e3ae5-ff5e-d470-8f3d-ad41cb85ed2a)
            * [Eid al-Adha](https://web.archive.org/web/20240602175209/https://www.qe.com.qa/documents/20181/658970/QE+MARKET+NOTICE+025+-01102014-Eid+Al-Adha+Holiday.pdf/f2b64d79-c466-a870-cd1d-a27c526d4c3c)
        * 2015:
            * [Eid al-Fitr](https://web.archive.org/web/20261108105726/https://mondovisione.com/news/eid-al-fiter-holiday-for-qatar-exchange-1-2015715/)
            * [Eid al-Adha](https://web.archive.org/web/20261108105812/https://mondovisione.com/media-and-resources/news/eid-al-al-ad-ha-holiday-for-qatar-exchange-2015921)
            * [National Day](https://web.archive.org/web/20261108105943/https://mondovisione.com/news/qatar-stock-exchange-national-day-holiday-20151218/)
        * 2016:
            * [Eid al-Fitr](https://web.archive.org/web/20261108110104/https://mondovisione.com/news/qatar-stock-exchange-reminder-of-eid-al-fitr-holiday-201675)
            * [Eid al-Adha](https://web.archive.org/web/20261108110340/https://mondovisione.com/news/eid-al-adha-holiday-for-qatar-stock-exchange-201696)
        * 2017:
            * [Eid al-Fitr](https://web.archive.org/web/20211023022133/https://www.qe.com.qa/documents/20181/656479/QSE+Market+Notice+017-2017+06+22+Eid+Al-Fitr+Holidays+-+%D8%B9%D8%B7%D9%84%D8%A9+%D8%B9%D9%8A%D8%AF+%D8%A7%D9%84%D9%81%D8%B7%D8%B1+%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%83+%D9%84%D8%B9%D8%A7%D9%85+2017.pdf/7ea33eef-5b71-09c9-c5fe-5ab3cc13bf8f)
            * [Eid al-Adha](https://web.archive.org/web/20211026002056/https://www.qe.com.qa/documents/20181/656479/QSE+MARKET+NOTICE+022+-29082017-Eid+Al-Adha+Holiday/33d8f89f-ffbb-4893-c968-a2efe6fcb0ec)
            * [National Day](https://web.archive.org/web/20211025223216/https://www.qe.com.qa/documents/20181/656479/QSE+Market+Notice+029-2017-12-16+National+Day+Holiday+-+%D8%A5%D8%AC%D8%A7%D8%B2%D8%A9+%D8%A7%D9%84%D9%8A%D9%88%D9%85+%D8%A7%D9%84%D9%88%D8%B7%D9%86%D9%8A.pdf/18e6a585-9895-ae2f-2418-260afaf52a81)
        * 2018:
            * [Eid al-Fitr](https://web.archive.org/web/20211026001339/https://www.qe.com.qa/documents/20181/792789/QSE+Market+Notice+017-2018-06-12+Eid+Al-Fitr+Holidays+-++%D8%B9%D8%B7%D9%84%D8%A9+%D8%B9%D9%8A%D8%AF+%D8%A7%D9%84%D9%81%D8%B7%D8%B1+%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%83+%D9%84%D8%B9%D8%A7%D9%85+2018....pdf/9c7eeac2-90ba-4150-3abb-d9de9ec9648c)
            * [Eid al-Adha](https://web.archive.org/web/20261108110451/https://mondovisione.com/news/eid-al-adha-holiday-for-qatar-stock-exchange-1-2018816)
        * 2019:
            * [National Day](https://web.archive.org/web/20211025234825/https://www.qe.com.qa/documents/20181/883269/QSE+Market+Notice+034-2019-12-17+National+Day+Holiday+-+%D8%A5%D8%AC%D8%A7%D8%B2%D8%A9+%D8%A7%D9%84%D9%8A%D9%88%D9%85+%D8%A7%D9%84%D9%88%D8%B7%D9%86%D9%8A/74229a6f-426b-c431-ea53-bf96db9c3589)
        * 2020:
            * [Eid al-Fitr](https://web.archive.org/web/20261108110541/https://mondovisione.com/news/qatar-stock-exchange-announces-eid-al-fiter-holiday-for-2020-2020519)
            * [Eid al-Adha](https://web.archive.org/web/20261108110737/https://mondovisione.com/news/qatar-stock-exchange-announces-eid-al-adha-holiday-for-2020-2020728)
            * [National Day](https://web.archive.org/web/20261108110825/https://mondovisione.com/news/an-official-holiday-at-qatar-stock-exchange-on-thursday-on-the-occasion-of-qatar-20201215)
        * 2021:
            * [Eid al-Fitr](https://web.archive.org/web/20261108110900/https://mondovisione.com/news/qatar-stock-exchange-eid-al-fitr-holiday-2021510)
            * [Eid al-Adha](https://web.archive.org/web/20261108110945/https://mondovisione.com/media-and-resources/news/qatar-stock-exchange-eid-al-adha-holiday-for-2021-2021715)
            * [National Day](https://web.archive.org/web/20261108111151/https://mondovisione.com/media-and-resources/news/an-official-holiday-at-qatar-stock-exchange-on-sunday-on-the-occasion-of-qatar-n-20211216)
        * 2022:
            * [Eid al-Fitr](https://web.archive.org/web/20261108111216/https://mondovisione.com/news/qatar-stock-exchange-eid-al-fitr-holiday-1-2022428)
            * [Eid al-Adha](https://web.archive.org/web/20261108111309/https://mondovisione.com/media-and-resources/news/eid-al-adha-holiday-for-2022-at-qatar-stock-exchange-202276)
        * 2023:
            * [Eid al-Fitr](https://web.archive.org/web/20261108111350/https://mondovisione.com/news/qatar-stock-exchange-eid-al-fitr-holiday-2-2023418)
            * [Eid al-Adha](https://web.archive.org/web/20261108111448/https://mondovisione.com/media-and-resources/news/qatar-stock-exchange-eid-al-adha-holiday-for-2023-2023625)
            * [National Day](https://web.archive.org/web/20261108111532/https://mondovisione.com/news/an-official-holiday-for-the-qatar-stock-exchange-on-the-occasion-of-the-nationa-20231214)
        * 2024:
            * [Eid al-Fitr](https://web.archive.org/web/20261108111615/https://mondovisione.com/news/qatar-stock-exchange-eid-al-fitr-holiday-3-202448)
            * [National Day](https://web.archive.org/web/20261108111700/https://mondovisione.com/news/an-official-holiday-for-the-qatar-stock-exchange-on-the-occasion-of-the-nationa-1-20241216)
        * 2025:
            * [Eid al-Fitr](https://web.archive.org/web/20261108111814/https://mondovisione.com/news/qatar-stock-exchange-eid-al-fitr-holiday-2025326)
            * [Eid al-Adha](https://web.archive.org/web/20261108111915/https://mondovisione.com/news/qatar-stock-exchange-announces-eid-al-adha-holiday-202563)
        * 2026:
            * [Eid al-Fitr](https://web.archive.org/web/20261108111954/https://mondovisione.com/news/qatar-stock-exchange-announces-eid-al-fitr-holiday-2026318/)
            * [Eid al-Adha](https://web.archive.org/web/20261108112046/https://mondovisione.com/media-and-resources/news/qatar-stock-exchange-announces-eid-al-adha-holiday-2026524/)
            * [Official Mourning](https://web.archive.org/web/20261108112134/https://mondovisione.com/news/qatar-stock-exchange-official-mourning-holiday-in-the-state-of-qatar-2026712/)
    """

    # Eid al-Fitr Holiday.
    eid_al_fitr_holiday = tr("عطلة عيد الفطر")

    # Eid al-Adha Holiday.
    eid_al_adha_holiday = tr("عطلة عيد الأضحى")

    # Qatar National Day.
    national_day = tr("اليوم الوطني لقطر")

    # Official Mourning.
    official_mourning = tr("حداد رسمي")

    special_public_holidays = {
        2011: (AUG, 30, eid_al_fitr_holiday),
        2012: (
            (OCT, 25, eid_al_adha_holiday),
            (OCT, 29, eid_al_adha_holiday),
        ),
        2013: (
            # Public Holiday.
            (JUN, 25, tr("عطلة رسمية")),
            (AUG, 11, eid_al_fitr_holiday),
            (AUG, 12, eid_al_fitr_holiday),
            (OCT, 13, eid_al_adha_holiday),
            (OCT, 14, eid_al_adha_holiday),
            (DEC, 19, national_day),
        ),
        2014: (
            (JUL, 31, eid_al_fitr_holiday),
            (OCT, 7, eid_al_adha_holiday),
            (OCT, 8, eid_al_adha_holiday),
            (OCT, 9, eid_al_adha_holiday),
        ),
        2015: (
            (JUL, 21, eid_al_fitr_holiday),
            (SEP, 27, eid_al_adha_holiday),
            (SEP, 28, eid_al_adha_holiday),
            (DEC, 20, national_day),
        ),
        2016: (
            (JUL, 10, eid_al_fitr_holiday),
            (SEP, 13, eid_al_adha_holiday),
            (SEP, 14, eid_al_adha_holiday),
            (SEP, 15, eid_al_adha_holiday),
        ),
        2017: (
            (JUN, 28, eid_al_fitr_holiday),
            (JUN, 29, eid_al_fitr_holiday),
            (SEP, 3, eid_al_adha_holiday),
            (SEP, 4, eid_al_adha_holiday),
            (SEP, 5, eid_al_adha_holiday),
            (DEC, 17, national_day),
        ),
        2018: (
            (JUN, 18, eid_al_fitr_holiday),
            (JUN, 19, eid_al_fitr_holiday),
            (AUG, 19, eid_al_adha_holiday),
            (AUG, 20, eid_al_adha_holiday),
            (AUG, 21, eid_al_adha_holiday),
        ),
        2019: (DEC, 19, national_day),
        2020: (
            (MAY, 27, eid_al_fitr_holiday),
            (MAY, 28, eid_al_fitr_holiday),
            (JUL, 30, eid_al_adha_holiday),
            (AUG, 3, eid_al_adha_holiday),
            (AUG, 4, eid_al_adha_holiday),
            (DEC, 17, national_day),
        ),
        2021: (
            (MAY, 12, eid_al_fitr_holiday),
            (MAY, 16, eid_al_fitr_holiday),
            (JUL, 18, eid_al_adha_holiday),
            (JUL, 19, eid_al_adha_holiday),
            (DEC, 19, national_day),
        ),
        2022: (
            (MAY, 1, eid_al_fitr_holiday),
            (MAY, 5, eid_al_fitr_holiday),
            (JUL, 12, eid_al_adha_holiday),
        ),
        2023: (
            (APR, 24, eid_al_fitr_holiday),
            (APR, 25, eid_al_fitr_holiday),
            (JUN, 27, eid_al_adha_holiday),
            (DEC, 17, national_day),
        ),
        2024: (
            (APR, 9, eid_al_fitr_holiday),
            (DEC, 19, national_day),
        ),
        2025: (
            (APR, 2, eid_al_fitr_holiday),
            (APR, 3, eid_al_fitr_holiday),
            (JUN, 5, eid_al_adha_holiday),
            (JUN, 9, eid_al_adha_holiday),
        ),
        2026: (
            (MAR, 19, eid_al_fitr_holiday),
            (MAR, 23, eid_al_fitr_holiday),
            (MAY, 26, eid_al_adha_holiday),
            (JUL, 13, official_mourning),
            (JUL, 14, official_mourning),
            (JUL, 15, official_mourning),
            (JUL, 16, official_mourning),
        ),
    }
