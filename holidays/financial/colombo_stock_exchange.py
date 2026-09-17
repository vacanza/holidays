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

from holidays.countries.sri_lanka import SriLanka
from holidays.groups import StaticHolidays


class ColomboStockExchange(SriLanka, StaticHolidays):
    """Colombo Stock Exchange (CSE) holiday calendar."""

    market = "XCOL"
    supported_categories = ("public", "half_day")  # type: ignore[assignment]

    # References:
    # 2026- https://cdn.cse.lk/cmt/upload_report_file/DXSvedMKDI9Qdp0J_20Apr2026114930GMT_1776685770276.pdf
    # 2025- https://cdn.cse.lk/cmt/upload_report_file/Yc55Y9aEiyhAB71R_18Nov2024081707GMT_1731917827859.pdf
    # 2024- https://cdn.cse.lk/cmt/upload_report_file/zM646FN086F69pB1_12Oct2023034430GMT_1697082270635.pdf
    # 2023- https://cdn.cse.lk/cmt/report/HPtW1TbUWfysYSiH_28Sep2022105732GMT_1664362652950.pdf
    # 2022- https://cdn.cse.lk/cmt/upload_cse_report_file/circulars_487_30-09-2021.pdf
    # 2021- https://cdn.cse.lk/cmt/upload_cse_report_file/circulars_759_07-09-2020.pdf
    # 2020- https://cdn.cse.lk/cmt/upload_cse_report_file/circulars_75_16-10-2019.pdf
    # 2019- https://cdn.cse.lk/cmt/upload_cse_announcements/9501540465936_.pdf
    # 2018- https://stockmarket-holidays.com/colombo-stock-exchange-holidays/133/
    def __init__(self, *args, **kwargs):
        self.static_holidays = {
            # 2026 Ad-Hoc Closures
            "2026-01-01": "CSE Customary Holiday",
            # 2025 Ad-Hoc Closures
            "2025-01-01": "Customary Holiday",
            "2025-04-15": "Special Bank Holiday",
            # 2024 Ad-Hoc Closures
            "2024-01-01": "CSE Customary Holiday",
            "2024-02-05": "Additional holiday in lieu of Independence Day falling on Sunday",
            # 2023 Ad-Hoc Closures
            "2023-01-16": "Additional holiday in lieu of Tamil Thai Pongal Day falling on Sunday",
            # 2022 Ad-Hoc Closures
            "2022-05-02": "Additional holiday in lieu of May Day falling on Sunday",
            "2022-10-10": "Additional holiday in lieu of Milad-Un-Nabi "
            "(Holy Prophet's Birthday) falling on Sunday",
            "2022-12-26": "Additional holiday in lieu of Christmas Day falling on Sunday",
            # 2021 Ad-Hoc Closures
            "2021-01-01": "CSE Customary Holiday",
            # 2020 Planned Ad-Hoc Closures
            "2020-01-01": "CSE Customary Holiday",
            "2020-04-14": "Special Bank Holiday on account of the Day "
            "prior to Sinhala & Tamil New Year Day "
            "falling on a Sunday",
            "2020-03-20": "Market closure due to COVID-19",
            # 2019 Ad-Hoc Closures
            "2019-01-01": "CSE Customary Holiday",
            "2019-04-15": "Special Bank Holiday on account of "
            "Sinhala & Tamil New Year Day "
            "falling on a Sunday",
            "2019-05-20": "Special Bank Holiday on account of Day "
            "Following Vesak Full Moon Poya Day "
            "falling on a Sunday",
            "2019-11-11": "Special Bank Holiday on account of "
            "Holy Prophet's Birthday falling on a Sunday",
            # 2018 Ad-Hoc Closures
            "2018-02-05": "National Day Holiday",
            "2018-04-30": "Vesak Holiday",
        }

        self.static_half_days = {
            # 2024 Half-Days
            "2024-04-10": "Additional half holiday in lieu of Sinhala "
            "& Tamil New Year Day falling on Saturday",
            # 2023 Half-Days
            "2023-02-03": "Additional half holiday in lieu of the "
            "Independence Day falling on Saturday",
            "2023-05-04": "Additional half holiday in lieu of Day Following Vesak "
            "Full Moon Poya Day falling on Saturday",
            # 2021 Half-Days
            "2021-04-30": "Additional half-holiday on account of the "
            "May Day falling on a Saturday",
            "2021-12-24": "Additional half-holiday on account of the Christmas "
            "Day falling on a Saturday",
            # 2019 Half-Days
            "2019-04-12": "Special Bank Half-holiday on account of Day prior "
            "to Sinhala & Tamil New Year Day "
            "falling on a Saturday",
            # 2018 Half-Days
            "2018-04-13": "Day prior to Sinhala & Tamil New Year day",
        }

        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        for dt_str, name in self.static_holidays.items():
            year, month, day = (int(x) for x in dt_str.split("-"))

            if year == self._year:
                self._add_holiday(name, month, day)

    def _populate_half_day_holidays(self):
        for dt_str, name in self.static_half_days.items():
            year, month, day = (int(x) for x in dt_str.split("-"))

            if year == self._year:
                self._add_holiday(name, month, day)


class XCOL(ColomboStockExchange):
    pass
