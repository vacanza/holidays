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

from holidays.calendars.gregorian import DEC
from holidays.constants import PUBLIC
from holidays.countries.indonesia import Indonesia
from holidays.helpers import tr


class IndonesiaStockExchange(Indonesia):
    """Indonesia Stock Exchange (IDX) holidays.

    IDX is closed on Indonesia public holidays and joint holidays (Cuti Bersama), and
    on December 31 for the year-end exchange holiday (Libur Bursa).

    References:
        * [2022 Holiday Calendar](https://investasi.kontan.co.id/news/tahun-depan-ada-250-hari-bursa-catat-tanggal-liburnya)
        * [2022 Eid al-Fitr changes](https://market.bisnis.com/read/20220428/7/1528502/besok-bursa-efek-indonesia-bei-libur-lebaran-buka-lagi-9-mei)
        * [2023 Holiday Calendar](https://www.cnbcindonesia.com/market/20221227082159-17-400351/simak-ada-242-hari-transaksi-ini-kalender-bursa-tahun-depan)
        * [2023 Eid al-Fitr changes](https://market.bisnis.com/read/20230330/7/1642150/update-jadwal-bursa-terkait-cuti-bersama-lebaran-cek-detailnya)
        * [2023 Eid al-Adha changes](https://economy.okezone.com/read/2023/06/27/278/2837678/perdagangan-bei-dan-layanan-bank-indonesia-besok-libur-berikut-jadwal-lengkapnya)
        * [2024 Election Day](https://www.kompas.tv/ekonomi/483031/bei-tetapkan-hari-pencoblosan-pemilu-14-februari-sebagai-libur-perdagangan-bursa)
        * [2024 Local Election Day](https://market.bisnis.com/read/20241127/7/1819336/pilkada-serentak-hari-ini-perdagangan-bursa-efek-indonesia-diliburkan)
        * [2025 Holiday Calendar](https://www.cnbcindonesia.com/market/20241017113149-17-580475/investor-wajib-tahu-ini-jadwal-libur-bursa-tahun-2025)
        * [2025 Independence Day Joint Holiday](https://market.bisnis.com/read/20250818/7/1903258/bei-tutup-perdagangan-18-agustus-2025-libur-cuti-bersama-kemerdekaan-ri)
        * [2026 Holiday Calendar](https://market.bisnis.com/read/20250923/7/1913812/catat-bei-umumkan-kalender-libur-bursa-pada-2026)
        * [2027 Holiday Calendar](https://www.idxchannel.com/market-news/dear-investor-ini-kalender-libur-bursa-efek-indonesia-2027/all)
    """

    country = None  # type: ignore[assignment]
    market = "XIDX"
    parent_entity = Indonesia
    supported_categories: tuple[str, ...] = (PUBLIC,)  # type: ignore[assignment]
    start_year = 2022

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        # Joint Holidays.
        self._add_special_holidays(("special_government_holidays",))

        if self._is_weekday(DEC, 31):
            # Exchange Holiday.
            self._add_holiday_dec_31(tr("Libur Bursa"))


class XIDX(IndonesiaStockExchange):
    pass


class IDX(IndonesiaStockExchange):
    pass
