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

# mypy: disable-error-code=attr-defined

import warnings
from unittest import TestCase

from holidays.countries.india import India
from tests.common import CommonCountryTests


class TestIndia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", category=UserWarning)
        cls.hindu_start_year = 2001
        cls.hindu_end_year = 2035
        cls.hindu_full_range = range(cls.hindu_start_year, cls.hindu_end_year + 1)
        super().setUpClass(India, with_subdiv_categories=True)

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")

    def test_deprecated(self):
        # Deprecated Code, Remapped Code.
        for subdiv1, subdiv2 in (
            ("DD", "DH"),
            ("OR", "OD"),
        ):
            self.assertEqual(
                India(subdiv=subdiv1, years=2023).keys(),
                India(subdiv=subdiv2, years=2023).keys(),
            )

    def test_hindu_calendar_out_of_range_warning(self):
        with warnings.catch_warnings():
            warnings.simplefilter("default", UserWarning)
            for year in (
                *range(self.start_year, self.hindu_start_year),
                *range(self.hindu_end_year + 1, self.end_year),
            ):
                with self.assertWarns(UserWarning):
                    India(years=year)

    def test_republic_day(self):
        name = "Republic Day"
        self.assertHolidayName(name, (f"{year}-01-26" for year in range(1950, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1950))

    def test_palm_sunday(self):
        name = "Palm Sunday"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2020-04-05",
            "2021-03-28",
            "2022-04-10",
            "2023-04-02",
            "2024-03-24",
            "2025-04-13",
        )
        self.assertOptionalHolidayName(name, self.full_range)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_sunday(self):
        name = "Easter Sunday"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertOptionalHolidayName(name, self.full_range)

    def test_labor_day(self):
        name = "Labour Day"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(name, (f"{year}-05-01" for year in self.full_range))

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-08-15" for year in self.full_range))

    def test_gandhi_jayanti(self):
        self.assertHolidayName("Gandhi Jayanti", (f"{year}-10-02" for year in self.full_range))

    def test_childrens_day(self):
        name = "Children's Day"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(name, (f"{year}-11-14" for year in self.full_range))

    def test_christmas(self):
        self.assertHolidayName("Christmas", (f"{year}-12-25" for year in self.full_range))

    def test_ashura(self):
        name = "Muharram"
        self.assertHolidayName(
            name,
            "2020-08-30",
            "2021-08-20",
            "2022-08-09",
            "2023-07-29",
            "2024-07-17",
            "2025-07-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_prophets_birthday(self):
        name = "Milad-un-Nabi"
        self.assertHolidayName(
            name,
            "2020-10-30",
            "2021-10-19",
            "2022-10-09",
            "2023-09-28",
            "2024-09-16",
            "2025-09-05",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_fitr(self):
        name = "Id-ul-Fitr"
        self.assertHolidayName(
            name,
            "2020-05-25",
            "2021-05-14",
            "2022-05-03",
            "2023-04-22",
            "2024-04-11",
            "2025-03-31",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_adha(self):
        name = "Bakrid"
        self.assertHolidayName(
            name,
            "2020-08-01",
            "2021-07-21",
            "2022-07-10",
            "2023-06-29",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def _assertHinduHolidayHelper(  # noqa: N802
        self,
        name: str,
        dts: tuple[str, ...],
        *,
        category_optional: bool = False,
        subdivs: set | None = None,
    ):
        """Once HinduHolidays properly supports full Hindu calendar range,
        update the following section in your code to the following format:

            name = "Holiday Name"
            self.assertHolidayName(
                name,
                "2020-XX-XX",
                "2021-XX-XX",
                "2022-XX-XX",
                "2023-XX-XX",
                "2024-XX-XX",
                "2025-XX-XX",
            )
            self.assertHolidayName(name, self.full_range)
        """
        if category_optional is False and subdivs is None:
            self.assertHolidayName(name, dts)
            self.assertHolidayName(name, self.hindu_full_range)
            self.assertNoHolidayName(
                name,
                range(self.start_year, self.hindu_start_year),
                range(self.hindu_end_year + 1, self.end_year),
            )
        # This assumes there's no subdiv-level optional holidays yet.
        elif category_optional is True:
            self.assertNoHolidayName(name)
            self.assertOptionalHolidayName(name, dts)
            self.assertOptionalHolidayName(name, self.hindu_full_range)
            self.assertNoOptionalHolidayName(
                name,
                range(self.start_year, self.hindu_start_year),
                range(self.hindu_end_year + 1, self.end_year),
            )
        elif subdivs is not None:
            self.assertNoHolidayName(name)
            for subdiv, holidays in self.subdiv_holidays.items():
                if subdiv in subdivs:
                    self.assertHolidayName(name, holidays, dts)
                    self.assertHolidayName(name, holidays, self.hindu_full_range)
                    self.assertNoHolidayName(
                        name,
                        holidays,
                        range(self.start_year, self.hindu_start_year),
                        range(self.hindu_end_year + 1, self.end_year),
                    )
                else:
                    self.assertNoHolidayName(name, holidays)

    def test_buddha_purnima(self):
        name = "Buddha Purnima"
        dts = (
            "2020-05-07",
            "2021-05-26",
            "2022-05-16",
            "2023-05-05",
            "2024-05-23",
            "2025-05-12",
        )
        self._assertHinduHolidayHelper(name, dts)

    def test_diwali(self):
        name = "Diwali"
        dts = (
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-10-31",
            "2025-10-20",
        )
        self._assertHinduHolidayHelper(name, dts)

    def test_dussehra(self):
        name = "Dussehra"
        dts = (
            "2020-10-25",
            "2021-10-15",
            "2022-10-05",
            "2023-10-24",
            "2024-10-12",
            "2025-10-02",
        )
        self._assertHinduHolidayHelper(name, dts)

    def test_janmashtami(self):
        name = "Janmashtami"
        dts = (
            "2020-08-12",
            "2021-08-30",
            "2022-08-19",
            "2023-09-07",
            "2024-08-26",
            "2025-08-16",
        )
        self._assertHinduHolidayHelper(name, dts)

    def test_mahavir_jayanti(self):
        name = "Mahavir Jayanti"
        dts = (
            "2020-04-06",
            "2021-04-25",
            "2022-04-14",
            "2023-04-04",
            "2024-04-21",
            "2025-04-10",
        )
        self._assertHinduHolidayHelper(name, dts)

    def test_maha_shivaratri(self):
        name = "Maha Shivaratri"
        dts = (
            "2020-02-21",
            "2021-03-11",
            "2022-03-01",
            "2023-02-18",
            "2024-03-08",
            "2025-02-26",
        )
        self._assertHinduHolidayHelper(name, dts)

    def test_guru_nanak_jayanti(self):
        name = "Guru Nanak Jayanti"
        dts = (
            "2020-11-30",
            "2021-11-19",
            "2022-11-08",
            "2023-11-27",
            "2024-11-15",
            "2025-11-05",
        )
        self._assertHinduHolidayHelper(name, dts)

    def test_holi(self):
        name = "Holi"
        dts = (
            "2020-03-10",
            "2021-03-29",
            "2022-03-18",
            "2023-03-08",
            "2024-03-25",
            "2025-03-14",
        )
        # OPTIONAL.
        self._assertHinduHolidayHelper(name, dts, category_optional=True)
        # MH.
        self.assertSubdivMhHolidayName(name, "2026-03-03")
        self.assertNoSubdivMhHolidayName(name, "2026-03-04")
        self.assertSubdivMhHolidayName(name, self.hindu_full_range)
        self.assertNoSubdivMhOptionalHolidayName(name)

    def test_ganesh_chaturthi(self):
        name = "Ganesh Chaturthi"
        dts = (
            "2020-08-22",
            "2021-09-10",
            "2022-08-31",
            "2023-09-19",
            "2024-09-07",
            "2025-08-27",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)

    def test_govardhan_puja(self):
        name = "Govardhan Puja"
        dts = (
            "2020-11-15",
            "2021-11-05",
            "2022-10-25",
            "2023-11-13",
            "2024-11-02",
            "2025-10-22",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)

    def test_maha_navami(self):
        name = "Maha Navami"
        dts = (
            "2020-10-24",
            "2021-10-14",
            "2022-10-04",
            "2023-10-23",
            "2024-10-11",
            "2025-10-01",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)

    def test_maharishi_valmiki_jayanti(self):
        name = "Maharishi Valmiki Jayanti"
        dts = (
            "2020-10-31",
            "2021-10-20",
            "2022-10-09",
            "2023-10-28",
            "2024-10-17",
            "2025-10-07",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)

    def test_makar_sankranti(self):
        name = "Makar Sankranti"
        name_as = "Magh Bihu"
        name_gj = "Uttarayan"
        dts = (
            "2020-01-15",
            "2021-01-14",
            "2022-01-14",
            "2023-01-14",
            "2024-01-14",
            "2025-01-14",
        )
        # OPTIONAL.
        self._assertHinduHolidayHelper(name, dts, category_optional=True)
        # SUBDIVS.
        self._assertHinduHolidayHelper(name_as, dts, subdivs={"AS"})
        self._assertHinduHolidayHelper(name_gj, dts, subdivs={"GJ"})

    def test_raksha_bandhan(self):
        name = "Raksha Bandhan"
        dts = (
            "2020-08-03",
            "2021-08-22",
            "2022-08-11",
            "2023-08-30",
            "2024-08-19",
            "2025-08-09",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)

    def test_ram_navami(self):
        name = "Ram Navami"
        dts = (
            "2020-04-02",
            "2021-04-21",
            "2022-04-10",
            "2023-03-30",
            "2024-04-17",
            "2025-04-06",
        )
        # OPTIONAL.
        self._assertHinduHolidayHelper(name, dts, category_optional=True)
        # SUBDIVS.
        self._assertHinduHolidayHelper(name, dts, subdivs={"AN"})

    def test_navratri_sharad_navratri(self):
        name = "Navratri / Sharad Navratri"
        dts = (
            "2020-10-17",
            "2021-10-07",
            "2022-09-26",
            "2023-10-15",
            "2024-10-03",
            "2025-09-22",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)

    def test_gudi_padwa(self):
        name_gudi_padwa = "Gudi Padwa"
        name_ugadi = "Ugadi"
        dts = (
            "2020-03-25",
            "2021-04-13",
            "2022-04-02",
            "2023-03-22",
            "2024-04-09",
            "2025-03-30",
        )
        self._assertHinduHolidayHelper(name_gudi_padwa, dts, subdivs={"MH"})
        self._assertHinduHolidayHelper(name_ugadi, dts, subdivs={"AP", "KA", "TS"})

    def test_chhath_puja(self):
        name = "Chhath Puja"
        dts = (
            "2020-11-20",
            "2021-11-10",
            "2022-10-30",
            "2023-11-19",
            "2024-11-07",
            "2025-10-28",
        )
        self._assertHinduHolidayHelper(name, dts, subdivs={"BR", "DL", "JH", "UP"})

    def test_parsi_new_year_shahenshahi(self):
        name = "Parsi New Year (Shahenshahi)"
        self.assertNoHolidayName(name)
        dts = (
            "1972-08-28",
            "2019-08-17",
            "2020-08-16",
            "2021-08-16",
            "2022-08-16",
            "2023-08-16",
            "2024-08-15",
            "2025-08-15",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"GJ", "MH"}:
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_onam(self):
        name = "Onam"
        dts = (
            "2020-08-31",
            "2021-08-21",
            "2022-09-08",
            "2023-08-29",
            "2024-09-15",
            "2025-09-05",
        )
        self._assertHinduHolidayHelper(name, dts, subdivs={"AN", "KL"})

    def test_guru_gobind_singh_jayanti(self):
        name = "Guru Gobind Singh Jayanti"
        dts = (
            "2020-01-02",
            "2021-01-20",
            "2022-01-09",
            "2022-12-29",
            "2024-01-17",
            "2025-01-06",
            "2025-12-27",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PB":
                self.assertHolidayName(name, holidays, dts)
                self.assertNoHolidayName(
                    name,
                    holidays,
                    range(self.start_year, self.hindu_start_year),
                    range(self.hindu_end_year + 1, self.end_year),
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_vaisakhi(self):
        name = "Vaisakhi"
        dts = (
            "2020-04-13",
            "2021-04-14",
            "2022-04-14",
            "2023-04-14",
            "2024-04-13",
            "2025-04-13",
        )
        self._assertHinduHolidayHelper(name, dts, subdivs={"PB"})

    def test_maharana_pratap_jayanti(self):
        name = "Maharana Pratap Jayanti"
        dts = (
            "2020-05-25",
            "2021-06-13",
            "2022-06-02",
            "2023-05-22",
            "2024-06-09",
            "2025-05-29",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "RJ":
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, range(2010, self.hindu_end_year + 1))
                self.assertNoHolidayName(
                    name,
                    holidays,
                    range(self.start_year, 2010),
                    range(self.hindu_end_year + 1, self.end_year),
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_pongal(self):
        name = "Pongal"
        dts = (
            "2020-01-15",
            "2021-01-14",
            "2022-01-14",
            "2023-01-15",
            "2024-01-15",
            "2025-01-14",
        )
        self._assertHinduHolidayHelper(name, dts, subdivs={"TN"})

    def test_thiruvalluvar_day_mattu_pongal(self):
        name = "Thiruvalluvar Day / Mattu Pongal"
        dts = (
            "2020-01-16",
            "2021-01-15",
            "2022-01-15",
            "2023-01-16",
            "2024-01-16",
            "2025-01-15",
        )
        self._assertHinduHolidayHelper(name, dts, subdivs={"TN"})

    def test_uzhavar_thirunal(self):
        name = "Uzhavar Thirunal"
        dts = (
            "2020-01-17",
            "2021-01-16",
            "2022-01-16",
            "2023-01-17",
            "2024-01-17",
            "2025-01-16",
        )
        self._assertHinduHolidayHelper(name, dts, subdivs={"TN"})

    def test_bathukamma_festival(self):
        name = "Bathukamma Festival"
        dts = (
            "2020-10-16",
            "2021-10-06",
            "2022-09-25",
            "2023-10-14",
            "2024-10-02",
            "2025-09-21",
        )
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TS":
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, range(2010, self.hindu_end_year + 1))
                self.assertNoHolidayName(
                    name,
                    holidays,
                    range(self.start_year, 2010),
                    range(self.hindu_end_year + 1, self.end_year),
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_bonalu(self):
        name = "Bonalu"
        dts = (
            "2018-08-06",
            "2019-07-29",
            "2020-07-20",
            "2021-08-02",
            "2022-07-25",
            "2023-07-17",
            "2024-07-29",
            "2025-07-21",
            "2026-08-10",
            "2027-08-02",
        )
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TS":
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, range(2018, 2028))
                self.assertNoHolidayName(
                    name, holidays, range(self.start_year, 2018), range(2028, self.end_year)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_dr_b_r_ambedkars_jayanti(self):
        name = "Dr. B. R. Ambedkar's Jayanti"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {
                "AN",
                "AP",
                "BR",
                "CG",
                "CH",
                "GA",
                "GJ",
                "HP",
                "HR",
                "JH",
                "JK",
                "KA",
                "KL",
                "LA",
                "MH",
                "MP",
                "OD",
                "PB",
                "PY",
                "RJ",
                "SK",
                "TN",
                "TS",
                "UK",
                "UP",
                "WB",
            }:
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-14" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_andhra_pradesh_foundation_day(self):
        name = "Andhra Pradesh Foundation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AP":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_assam_day(self):
        name = "Assam Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AS":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-02" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_bihar_day(self):
        name = "Bihar Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BR":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-22" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_chhattisgarh_foundation_day(self):
        name = "Chhattisgarh Foundation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "CG":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_goa_liberation_day(self):
        name = "Goa Liberation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "GA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-19" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_gujarat_day(self):
        name = "Gujarat Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "GJ":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sardar_vallabhbhai_patel_jayanti(self):
        name = "Sardar Vallabhbhai Patel Jayanti"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "GJ":
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-31" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_haryana_foundation_day(self):
        name = "Haryana Foundation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "HR":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_himachal_day(self):
        name = "Himachal Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "HP":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-15" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_jharkhand_formation_day(self):
        name = "Jharkhand Formation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "JH":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-15" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_karnataka_rajyotsava(self):
        name = "Karnataka Rajyotsava"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "KA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_kerala_foundation_day(self):
        name = "Kerala Foundation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "KL":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_chhatrapati_shivaji_maharaj_jayanti(self):
        name = "Chhatrapati Shivaji Maharaj Jayanti"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "MH":
                self.assertHolidayName(
                    name, holidays, (f"{year}-02-19" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_maharashtra_day(self):
        name = "Maharashtra Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "MH":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_madhya_pradesh_foundation_day(self):
        name = "Madhya Pradesh Foundation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "MP":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_mizoram_state_day(self):
        name = "Mizoram State Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "MZ":
                self.assertHolidayName(
                    name, holidays, (f"{year}-02-20" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_nagaland_state_inauguration_day(self):
        name = "Nagaland State Inauguration Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NL":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_odisha_day(self):
        name = "Odisha Day (Utkala Dibasa)"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "OD":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_maha_vishuva_sankranti(self):
        name = "Maha Vishuva Sankranti / Pana Sankranti"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "OD":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-15" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_puducherry_de_jure_transfer_day(self):
        name = "Puducherry De Jure Transfer Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PY":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-16" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_puducherry_liberation_day(self):
        name = "Puducherry Liberation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PY":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_lohri(self):
        name = "Lohri"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PB":
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-13" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_new_punjab_day(self):
        name = "New Punjab Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PB":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_rajasthan_day(self):
        name = "Rajasthan Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "RJ":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-30" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sikkim_state_day(self):
        name = "Sikkim State Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SK":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-16" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_puthandu(self):
        name = "Puthandu (Tamil New Year)"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TN":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-14" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_telangana_formation_day(self):
        name = "Telangana Formation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TS":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-02" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_up_formation_day(self):
        name = "UP Formation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "UP":
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-24" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_pohela_boishakh(self):
        name = "Pohela Boishakh"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "WB":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-15" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_rabindra_jayanti(self):
        name = "Rabindra Jayanti"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "WB":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-09" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_2018(self):
        self.assertHolidayDatesInYear(
            2018,
            "2018-01-26",
            "2018-02-13",
            "2018-03-29",
            "2018-03-30",
            "2018-04-30",
            "2018-06-16",
            "2018-08-15",
            "2018-08-22",
            "2018-09-03",
            "2018-09-21",
            "2018-10-02",
            "2018-10-19",
            "2018-11-07",
            "2018-11-21",
            "2018-11-23",
            "2018-12-25",
        )

        subdiv_holidays_mapping = {
            "AN": (
                "2018-03-25",
                "2018-04-14",
                "2018-08-24",
            ),
            "AP": (
                "2018-04-14",
                "2018-11-01",
            ),
            "AS": (
                "2018-01-14",
                "2018-12-02",
            ),
            "BR": (
                "2018-03-22",
                "2018-04-14",
                "2018-11-13",
            ),
            "CG": (
                "2018-04-14",
                "2018-11-01",
            ),
            "CH": ("2018-04-14",),
            "DL": ("2018-11-13",),
            "GA": (
                "2018-04-14",
                "2018-12-19",
            ),
            "GJ": (
                "2018-01-14",
                "2018-04-14",
                "2018-05-01",
                "2018-10-31",
            ),
            "HP": (
                "2018-04-14",
                "2018-04-15",
            ),
            "HR": (
                "2018-04-14",
                "2018-11-01",
            ),
            "JH": (
                "2018-04-14",
                "2018-11-13",
                "2018-11-15",
            ),
            "JK": ("2018-04-14",),
            "KA": (
                "2018-04-14",
                "2018-11-01",
            ),
            "KL": (
                "2018-04-14",
                "2018-08-24",
                "2018-11-01",
            ),
            "LA": ("2018-04-14",),
            "MH": (
                "2018-02-19",
                "2018-03-18",
                "2018-04-14",
                "2018-05-01",
            ),
            "MP": (
                "2018-04-14",
                "2018-11-01",
            ),
            "MZ": ("2018-02-20",),
            "NL": ("2018-12-01",),
            "OD": (
                "2018-04-01",
                "2018-04-14",
                "2018-04-15",
            ),
            "PB": (
                "2018-01-13",
                "2018-04-14",
                "2018-11-01",
            ),
            "PY": (
                "2018-04-14",
                "2018-08-16",
                "2018-11-01",
            ),
            "RJ": (
                "2018-03-30",
                "2018-04-14",
                "2018-06-16",
            ),
            "SK": (
                "2018-04-14",
                "2018-05-16",
            ),
            "TN": (
                "2018-01-14",
                "2018-01-15",
                "2018-01-16",
                "2018-04-14",
            ),
            "TS": (
                "2018-04-14",
                "2018-06-02",
                "2018-10-08",
            ),
            "UK": ("2018-04-14",),
            "UP": (
                "2018-01-24",
                "2018-04-14",
                "2018-11-13",
            ),
            "WB": (
                "2018-04-14",
                "2018-04-15",
                "2018-05-09",
            ),
        }

        for subdiv, dates in subdiv_holidays_mapping.items():
            self.assertHoliday(self.subdiv_holidays[subdiv], dates)

    def test_2018_optional(self):
        self.assertOptionalHolidayDatesInYear(
            2018,
            "2018-01-14",
            "2018-03-02",
            "2018-03-25",
            "2018-04-01",
            "2018-05-01",
            "2018-08-26",
            "2018-09-13",
            "2018-10-10",
            "2018-10-17",
            "2018-10-24",
            "2018-11-08",
            "2018-11-14",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2018-01-13", "Lohri"),
            ("2018-01-14", "Magh Bihu; Makar Sankranti; Pongal; Uttarayan"),
            ("2018-01-15", "Thiruvalluvar Day / Mattu Pongal"),
            ("2018-01-16", "Uzhavar Thirunal"),
            ("2018-01-24", "UP Formation Day"),
            ("2018-01-26", "Republic Day"),
            ("2018-02-13", "Maha Shivaratri"),
            ("2018-02-19", "Chhatrapati Shivaji Maharaj Jayanti"),
            ("2018-02-20", "Mizoram State Day"),
            ("2018-03-02", "Holi"),
            ("2018-03-18", "Gudi Padwa; Ugadi"),
            ("2018-03-22", "Bihar Day"),
            ("2018-03-25", "Palm Sunday; Ram Navami"),
            ("2018-03-29", "Mahavir Jayanti"),
            ("2018-03-30", "Good Friday; Rajasthan Day"),
            ("2018-04-01", "Easter Sunday; Odisha Day (Utkala Dibasa)"),
            ("2018-04-14", "Dr. B. R. Ambedkar's Jayanti; Puthandu (Tamil New Year); Vaisakhi"),
            (
                "2018-04-15",
                "Himachal Day; Maha Vishuva Sankranti / Pana Sankranti; Pohela Boishakh",
            ),
            ("2018-04-30", "Buddha Purnima"),
            ("2018-05-01", "Gujarat Day; Labour Day; Maharashtra Day"),
            ("2018-05-09", "Rabindra Jayanti"),
            ("2018-05-16", "Sikkim State Day"),
            ("2018-06-02", "Telangana Formation Day"),
            ("2018-06-16", "Id-ul-Fitr; Maharana Pratap Jayanti"),
            ("2018-08-06", "Bonalu"),
            ("2018-08-15", "Independence Day"),
            ("2018-08-16", "Puducherry De Jure Transfer Day"),
            ("2018-08-17", "Parsi New Year (Shahenshahi)"),
            ("2018-08-22", "Bakrid"),
            ("2018-08-24", "Onam"),
            ("2018-08-26", "Raksha Bandhan"),
            ("2018-09-03", "Janmashtami"),
            ("2018-09-13", "Ganesh Chaturthi"),
            ("2018-09-21", "Muharram"),
            ("2018-10-02", "Gandhi Jayanti"),
            ("2018-10-08", "Bathukamma Festival"),
            ("2018-10-10", "Navratri / Sharad Navratri"),
            ("2018-10-17", "Maha Navami"),
            ("2018-10-19", "Dussehra"),
            ("2018-10-24", "Maharishi Valmiki Jayanti"),
            ("2018-10-31", "Sardar Vallabhbhai Patel Jayanti"),
            (
                "2018-11-01",
                "Andhra Pradesh Foundation Day; "
                "Chhattisgarh Foundation Day; "
                "Haryana Foundation Day; "
                "Karnataka Rajyotsava; Kerala Foundation Day; "
                "Madhya Pradesh Foundation Day; "
                "New Punjab Day; "
                "Puducherry Liberation Day",
            ),
            ("2018-11-07", "Diwali"),
            ("2018-11-08", "Govardhan Puja"),
            ("2018-11-13", "Chhath Puja"),
            ("2018-11-14", "Children's Day"),
            ("2018-11-15", "Jharkhand Formation Day"),
            ("2018-11-21", "Milad-un-Nabi"),
            ("2018-11-23", "Guru Nanak Jayanti"),
            ("2018-12-01", "Nagaland State Inauguration Day"),
            ("2018-12-02", "Assam Day"),
            ("2018-12-19", "Goa Liberation Day"),
            ("2018-12-25", "Christmas"),
        )

    def test_l10n_bn(self):
        self.assertLocalizedHolidays(
            "bn",
            ("2018-01-13", "লোহরি"),
            ("2018-01-14", "উত্তরায়ণ; পোঙ্গল; মকর সংক্রান্তি; মাঘ বিহু"),
            ("2018-01-15", "তিরুভাল্লুভার দিবস / মাট্টু পোঙ্গল"),
            ("2018-01-16", "উঝাভার থিরুনাল"),
            ("2018-01-24", "উত্তরপ্রদেশ গঠন দিবস"),
            ("2018-01-26", "প্রজাতন্ত্র দিবস"),
            ("2018-02-13", "মহাশিবরাত্রি"),
            ("2018-02-19", "ছত্রপতি শিবাজী মহারাজ জয়ন্তী"),
            ("2018-02-20", "মিজোরাম প্রতিষ্ঠা দিবস"),
            ("2018-03-02", "হোলি"),
            ("2018-03-18", "উগাদি; গুড়ি পাড়ওয়া"),
            ("2018-03-22", "বিহার দিবস"),
            ("2018-03-25", "পাম রবিবার; রাম নবমী"),
            ("2018-03-29", "মহাবীর জয়ন্তী"),
            ("2018-03-30", "গুড ফ্রাইডে; রাজস্থান দিবস"),
            ("2018-04-01", "ইস্টার রবিবার; ওড়িশা দিবস (উৎকল দিবস)"),
            ("2018-04-14", "ড. বি. আর. আম্বেদকর জয়ন্তী; পুত্থান্ডু (তামিল নববর্ষ); বৈশাখী"),
            (
                "2018-04-15",
                "পহেলা বৈশাখ; মহা বিষুব সংক্রান্তি / পানা সংক্রান্তি; হিমাচল দিবস",
            ),
            ("2018-04-30", "বুদ্ধ পূর্ণিমা"),
            ("2018-05-01", "গুজরাট দিবস; মহারাষ্ট্র দিবস; শ্রমিক দিবস"),
            ("2018-05-09", "রবীন্দ্র জয়ন্তী"),
            ("2018-05-16", "সিকিম প্রতিষ্ঠা দিবস"),
            ("2018-06-02", "তেলেঙ্গানা গঠন দিবস"),
            ("2018-06-16", "ঈদ-উল-ফিতর; মহারানা প্রতাপ জয়ন্তী"),
            ("2018-08-06", "বোনালু"),
            ("2018-08-15", "স্বাধীনতা দিবস"),
            ("2018-08-16", "পুদুচেরি আইনি হস্তান্তর দিবস"),
            ("2018-08-17", "পারসি নববর্ষ (শাহেনশাহী)"),
            ("2018-08-22", "বকরিদ"),
            ("2018-08-24", "ওনাম"),
            ("2018-08-26", "রাখি বন্ধন"),
            ("2018-09-03", "জন্মাষ্টমী"),
            ("2018-09-13", "গণেশ চতুর্থী"),
            ("2018-09-21", "মহরম"),
            ("2018-10-02", "গান্ধী জয়ন্তী"),
            ("2018-10-08", "বাথুকাম্মা উৎসব"),
            ("2018-10-10", "নবরাত্রি / শারদ নবরাত্রি"),
            ("2018-10-17", "মহানবমী"),
            ("2018-10-19", "বিজয়া দশমী"),
            ("2018-10-24", "মহার্ষি বাল্মীকি জয়ন্তী"),
            ("2018-10-31", "সরদার বল্লভভাই প্যাটেল জয়ন্তী"),
            (
                "2018-11-01",
                "অন্ধ্রপ্রদেশ প্রতিষ্ঠা দিবস; "
                "কর্ণাটক রাজ্যোৎসব; কেরালা প্রতিষ্ঠা দিবস; "
                "ছত্তিশগড় প্রতিষ্ঠা দিবস; নতুন পাঞ্জাব দিবস; "
                "পুদুচেরি মুক্তি দিবস; মধ্যপ্রদেশ প্রতিষ্ঠা দিবস; "
                "হরিয়ানা প্রতিষ্ঠা দিবস",
            ),
            ("2018-11-07", "দীপাবলি"),
            ("2018-11-08", "গোবর্ধন পূজা"),
            ("2018-11-13", "ছঠ পূজা"),
            ("2018-11-14", "শিশু দিবস"),
            ("2018-11-15", "ঝাড়খণ্ড গঠন দিবস"),
            ("2018-11-21", "মিলাদ-উন-নবী"),
            ("2018-11-23", "গুরু নানক জয়ন্তী"),
            ("2018-12-01", "নাগাল্যান্ড প্রতিষ্ঠা দিবস"),
            ("2018-12-02", "অসম দিবস"),
            ("2018-12-19", "গোয়া মুক্তি দিবস"),
            ("2018-12-25", "বড়দিন"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2018-01-13", "Lohri"),
            ("2018-01-14", "Magh Bihu; Makar Sankranti; Pongal; Uttarayan"),
            ("2018-01-15", "Thiruvalluvar Day / Mattu Pongal"),
            ("2018-01-16", "Uzhavar Thirunal"),
            ("2018-01-24", "UP Formation Day"),
            ("2018-01-26", "Republic Day"),
            ("2018-02-13", "Maha Shivaratri"),
            ("2018-02-19", "Chhatrapati Shivaji Maharaj Jayanti"),
            ("2018-02-20", "Mizoram State Day"),
            ("2018-03-02", "Holi"),
            ("2018-03-18", "Gudi Padwa; Ugadi"),
            ("2018-03-22", "Bihar Day"),
            ("2018-03-25", "Palm Sunday; Ram Navami"),
            ("2018-03-29", "Mahavir Jayanti"),
            ("2018-03-30", "Good Friday; Rajasthan Day"),
            ("2018-04-01", "Easter Sunday; Odisha Day (Utkala Dibasa)"),
            ("2018-04-14", "Dr. B. R. Ambedkar's Jayanti; Puthandu (Tamil New Year); Vaisakhi"),
            (
                "2018-04-15",
                "Himachal Day; Maha Vishuva Sankranti / Pana Sankranti; Pohela Boishakh",
            ),
            ("2018-04-30", "Buddha Purnima"),
            ("2018-05-01", "Gujarat Day; Labor Day; Maharashtra Day"),
            ("2018-05-09", "Rabindra Jayanti"),
            ("2018-05-16", "Sikkim State Day"),
            ("2018-06-02", "Telangana Formation Day"),
            ("2018-06-16", "Eid al-Fitr; Maharana Pratap Jayanti"),
            ("2018-08-06", "Bonalu"),
            ("2018-08-15", "Independence Day"),
            ("2018-08-16", "Puducherry De Jure Transfer Day"),
            ("2018-08-17", "Parsi New Year (Shahenshahi)"),
            ("2018-08-22", "Eid al-Adha"),
            ("2018-08-24", "Onam"),
            ("2018-08-26", "Raksha Bandhan"),
            ("2018-09-03", "Janmashtami"),
            ("2018-09-13", "Ganesh Chaturthi"),
            ("2018-09-21", "Ashura"),
            ("2018-10-02", "Gandhi Jayanti"),
            ("2018-10-08", "Bathukamma Festival"),
            ("2018-10-10", "Navratri / Sharad Navratri"),
            ("2018-10-17", "Maha Navami"),
            ("2018-10-19", "Dussehra"),
            ("2018-10-24", "Maharishi Valmiki Jayanti"),
            ("2018-10-31", "Sardar Vallabhbhai Patel Jayanti"),
            (
                "2018-11-01",
                "Andhra Pradesh Foundation Day; "
                "Chhattisgarh Foundation Day; "
                "Haryana Foundation Day; "
                "Karnataka Rajyotsava; Kerala Foundation Day; "
                "Madhya Pradesh Foundation Day; "
                "New Punjab Day; "
                "Puducherry Liberation Day",
            ),
            ("2018-11-07", "Diwali"),
            ("2018-11-08", "Govardhan Puja"),
            ("2018-11-13", "Chhath Puja"),
            ("2018-11-14", "Children's Day"),
            ("2018-11-15", "Jharkhand Formation Day"),
            ("2018-11-21", "Prophet's Birthday"),
            ("2018-11-23", "Guru Nanak Jayanti"),
            ("2018-12-01", "Nagaland State Inauguration Day"),
            ("2018-12-02", "Assam Day"),
            ("2018-12-19", "Goa Liberation Day"),
            ("2018-12-25", "Christmas"),
        )

    def test_l10n_gu(self):
        self.assertLocalizedHolidays(
            "gu",
            ("2018-01-13", "લોહરી"),
            ("2018-01-14", "ઉત્તરાયણ; પોંગલ; મકરસંક્રાંતિ; માઘ બિહુ"),
            ("2018-01-15", "તિરુવલ્લુવર દિવસ / મટ્ટુ પોંગલ"),
            ("2018-01-16", "ઉઝાવર થિરુનલ"),
            ("2018-01-24", "યુપી સ્થાપના દિવસ"),
            ("2018-01-26", "પ્રજાસત્તાક દિવસ"),
            ("2018-02-13", "મહાશિવરાત્રી"),
            ("2018-02-19", "છત્રપતિ શિવાજી મહારાજ જયંતિ"),
            ("2018-02-20", "મિઝોરમ રાજ્ય દિવસ"),
            ("2018-03-02", "હોળી"),
            ("2018-03-18", "ઉગાડી; ગુડી પડવો"),
            ("2018-03-22", "બિહાર દિવસ"),
            ("2018-03-25", "પામ સન્ડે; રામ નવમી"),
            ("2018-03-29", "મહાવીર જયંતિ"),
            ("2018-03-30", "ગુડ ફ્રાઈડે; રાજસ્થાન દિવસ"),
            ("2018-04-01", "ઈસ્ટર સન્ડે; ઓડિશા દિવસ (ઉત્કલ દિવસ)"),
            ("2018-04-14", "ડૉ. બી. આર. આંબેડકર જયંતિ; પુથંડુ (તમિલ નવું વર્ષ); વૈશાખી"),
            ("2018-04-15", "પોહેલા બોઈશાખ; મહા વિષુવ સંક્રાંતિ / પાના સંક્રાંતિ; હિમાચલ દિવસ"),
            ("2018-04-30", "બુદ્ધ પૂર્ણિમા"),
            ("2018-05-01", "ગુજરાત સ્થાપના દિવસ; મજૂર દિવસ; મહારાષ્ટ્ર દિવસ"),
            ("2018-05-09", "રવીન્દ્ર જયંતિ"),
            ("2018-05-16", "સિક્કિમ રાજ્ય દિવસ"),
            ("2018-06-02", "તેલંગાણા સ્થાપના દિવસ"),
            ("2018-06-16", "ઈદ-ઉલ-ફિત્ર; મહારાણા પ્રતાપ જયંતિ"),
            ("2018-08-06", "બોનાલુ"),
            ("2018-08-15", "સ્વતંત્રતા દિવસ"),
            ("2018-08-16", "પુડુચેરી ડી જ્યુર ટ્રાન્સફર દિવસ"),
            ("2018-08-17", "પારસી નવું વર્ષ (શાહેનશાહી)"),
            ("2018-08-22", "બકરી ઈદ"),
            ("2018-08-24", "ઓણમ"),
            ("2018-08-26", "રક્ષાબંધન"),
            ("2018-09-03", "જન્માષ્ટમી"),
            ("2018-09-13", "ગણેશ ચતુર્થી"),
            ("2018-09-21", "મોહરમ"),
            ("2018-10-02", "ગાંધી જયંતિ"),
            ("2018-10-08", "બથુકમ્મા ઉત્સવ"),
            ("2018-10-10", "નવરાત્રી / શરદ નવરાત્રી"),
            ("2018-10-17", "મહાનવમી"),
            ("2018-10-19", "દશેરા"),
            ("2018-10-24", "મહર્ષિ વાલ્મિકી જયંતિ"),
            ("2018-10-31", "સરદાર વલ્લભભાઈ પટેલ જયંતિ"),
            (
                "2018-11-01",
                "આંધ્ર પ્રદેશ સ્થાપના દિવસ; "
                "કર્ણાટક રાજ્યોત્સવ; કેરળ સ્થાપના દિવસ; "
                "છત્તીસગઢ સ્થાપના દિવસ; નવો પંજાબ દિવસ; "
                "પુડુચેરી મુક્તિ દિવસ; મધ્ય પ્રદેશ સ્થાપના દિવસ; "
                "હરિયાણા સ્થાપના દિવસ",
            ),
            ("2018-11-07", "દિવાળી"),
            ("2018-11-08", "ગોવર્ધન પૂજા"),
            ("2018-11-13", "છઠ પૂજા"),
            ("2018-11-14", "બાળ દિવસ"),
            ("2018-11-15", "ઝારખંડ સ્થાપના દિવસ"),
            ("2018-11-21", "મિલાદ-ઉન-નબી"),
            ("2018-11-23", "ગુરુ નાનક જયંતિ"),
            ("2018-12-01", "નાગાલેન્ડ રાજ્ય ઉદ્ઘાટન દિવસ"),
            ("2018-12-02", "આસામ દિવસ"),
            ("2018-12-19", "ગોવા મુક્તિ દિવસ"),
            ("2018-12-25", "નાતાલ"),
        )

    def test_l10n_hi(self):
        self.assertLocalizedHolidays(
            "hi",
            ("2018-01-13", "लोहड़ी"),
            ("2018-01-14", "उत्तरायण; पोंगल; मकर संक्रांति; माघ बिहू"),
            ("2018-01-15", "तिरुवल्लुवर दिवस / मट्टू पोंगल"),
            ("2018-01-16", "उझावर थिरुनल"),
            ("2018-01-24", "यूपी स्थापना दिवस"),
            ("2018-01-26", "गणतंत्र दिवस"),
            ("2018-02-13", "महाशिवरात्रि"),
            ("2018-02-19", "छत्रपति शिवाजी महाराज जयंती"),
            ("2018-02-20", "मिज़ोरम राज्य दिवस"),
            ("2018-03-02", "होली"),
            ("2018-03-18", "उगादि; गुडी पाडवा"),
            ("2018-03-22", "बिहार दिवस"),
            ("2018-03-25", "पाम रविवार; रामनवमी"),
            ("2018-03-29", "महावीर जयंती"),
            ("2018-03-30", "गुड फ्राइडे; राजस्थान दिवस"),
            ("2018-04-01", "ईस्टर रविवार; ओडिशा दिवस (उत्कल दिवस)"),
            ("2018-04-14", "डॉ. बी.आर. आम्बेडकर जयंती; पुत्ताण्डु (तमिल नव वर्ष); वैसाखी"),
            ("2018-04-15", "पोहेला बोइशाख; महा विषुव संक्रांति / पण संक्रांति; हिमाचल दिवस"),
            ("2018-04-30", "बुद्ध पूर्णिमा"),
            ("2018-05-01", "गुजरात दिवस; मजदूर दिवस; महाराष्ट्र दिवस"),
            ("2018-05-09", "रवींद्र जयंती"),
            ("2018-05-16", "सिक्किम राज्य दिवस"),
            ("2018-06-02", "तेलंगाना स्थापना दिवस"),
            ("2018-06-16", "ईद-उल-फितर; महाराणा प्रताप जयंती"),
            ("2018-08-06", "बोनालु"),
            ("2018-08-15", "स्वतंत्रता दिवस"),
            ("2018-08-16", "पुडुचेरी डी ज्यूर स्थानांतरण दिवस"),
            ("2018-08-17", "पारसी नव वर्ष (शहंशाही)"),
            ("2018-08-22", "बकरीद"),
            ("2018-08-24", "ओणम"),
            ("2018-08-26", "रक्षाबंधन"),
            ("2018-09-03", "जन्माष्टमी"),
            ("2018-09-13", "गणेश चतुर्थी"),
            ("2018-09-21", "मुहर्रम"),
            ("2018-10-02", "गांधी जयंती"),
            ("2018-10-08", "बतुकम्मा महोत्सव"),
            ("2018-10-10", "नवरात्र / शरद नवरात्र"),
            ("2018-10-17", "महानवमी"),
            ("2018-10-19", "दशहरा"),
            ("2018-10-24", "महर्षि वाल्मीकि जयंती"),
            ("2018-10-31", "सरदार वल्लभभाई पटेल जयंती"),
            (
                "2018-11-01",
                "आंध्र प्रदेश स्थापना दिवस; "
                "कर्नाटक राज्योत्सव; केरल स्थापना दिवस; "
                "छत्तीसगढ़ स्थापना दिवस; नया पंजाब दिवस; "
                "पुडुचेरी मुक्ति दिवस; मध्य प्रदेश स्थापना दिवस; "
                "हरियाणा स्थापना दिवस",
            ),
            ("2018-11-07", "दिवाली"),
            ("2018-11-08", "गोवर्धन पूजा"),
            ("2018-11-13", "छठ पूजा"),
            ("2018-11-14", "बाल दिवस"),
            ("2018-11-15", "झारखंड स्थापना दिवस"),
            ("2018-11-21", "मिलाद-उन-नबी"),
            ("2018-11-23", "गुरु नानक जयंती"),
            ("2018-12-01", "नागालैंड राज्य उद्घाटन दिवस"),
            ("2018-12-02", "असम दिवस"),
            ("2018-12-19", "गोवा मुक्ति दिवस"),
            ("2018-12-25", "क्रिसमस"),
        )

    def test_l10n_kn(self):
        self.assertLocalizedHolidays(
            "kn",
            ("2018-01-13", "ಲೋಹ್ರಿ"),
            ("2018-01-14", "ಉತ್ತರಾಯಣ; ಪೊಂಗಲ್; ಮಕರ ಸಂಕ್ರಾಂತಿ; ಮಾಘ್ ಬಿಹು"),
            ("2018-01-15", "ತಿರುವಳ್ಳುವರ್ ದಿನೋತ್ಸವ / ಮಟ್ಟು ಪೊಂಗಲ್"),
            ("2018-01-16", "ಉಳವರ್ ತಿರುನಾಲ್"),
            ("2018-01-24", "ಉತ್ತರ ಪ್ರದೇಶ ಸ್ಥಾಪನಾ ದಿನ"),
            ("2018-01-26", "ಗಣರಾಜ್ಯೋತ್ಸವ"),
            ("2018-02-13", "ಮಹಾ ಶಿವರಾತ್ರಿ"),
            ("2018-02-19", "ಛತ್ರಪತಿ ಶಿವಾಜಿ ಮಹಾರಾಜ್ ಜಯಂತಿ"),
            ("2018-02-20", "ಮಿಜೋರಾಂ ರಾಜ್ಯ ದಿನೋತ್ಸವ"),
            ("2018-03-02", "ಹೋಳಿ ಹಬ್ಬ"),
            ("2018-03-18", "ಗುಡಿ ಪಾಡ್ವ; ಯುಗಾದಿ ಹಬ್ಬ"),
            ("2018-03-22", "ಬಿಹಾರ್ ದಿನೋತ್ಸವ"),
            ("2018-03-25", "ಪಾಮ್ ಭಾನುವಾರ; ಶ್ರೀ ರಾಮನವಮಿ"),
            ("2018-03-29", "ಮಹಾವೀರ ಜಯಂತಿ"),
            ("2018-03-30", "ಗುಡ್ ಫ್ರೈಡೆ; ರಾಜಸ್ಥಾನ ದಿನೋತ್ಸವ"),
            ("2018-04-01", "ಈಸ್ಟರ್ ಭಾನುವಾರ; ಒಡಿಶಾ ದಿನೋತ್ಸವ (ಉತ್ಕಲ ದಿವಸ)"),
            ("2018-04-14", "ಡಾ|| ಬಿ.ಆರ್.ಅಂಬೇಡ್ಕರ್ ಜಯಂತಿ; ಪುತ್ತಾಂಡು (ತಮಿಳು ಹೊಸ ವರ್ಷ); ವೈಶಾಖಿ"),
            (
                "2018-04-15",
                "ಪೊಹೆಲಾ ಬೊಯಿಶಾಖ್; ಮಹಾ ವಿಷುವ ಸಂಕ್ರಾಂತಿ / ಪನ ಸಂಕ್ರಾಂತಿ; ಹಿಮಾಚಲ್ ದಿನೋತ್ಸವ",
            ),
            ("2018-04-30", "ಬುದ್ಧ ಪೂರ್ಣಿಮ"),
            ("2018-05-01", "ಕಾರ್ಮಿಕ ದಿನಾಚರಣೆ; ಗುಜರಾತ್ ದಿನೋತ್ಸವ; ಮಹಾರಾಷ್ಟ್ರ ದಿನೋತ್ಸವ"),
            ("2018-05-09", "ರವೀಂದ್ರ ಜಯಂತಿ"),
            ("2018-05-16", "ಸಿಕ್ಕಿಂ ರಾಜ್ಯ ದಿನೋತ್ಸವ"),
            ("2018-06-02", "ತೆಲಂಗಾಣ ಸ್ಥಾಪನಾ ದಿನ"),
            ("2018-06-16", "ಈದ್-ಉಲ್-ಫಿತರ್; ಮಹಾರಾಣಾ ಪ್ರತಾಪ್ ಜಯಂತಿ"),
            ("2018-08-06", "ಬೋನಾಲು"),
            ("2018-08-15", "ಸ್ವಾತಂತ್ರ್ಯ ದಿನಾಚರಣೆ"),
            ("2018-08-16", "ಪುದುಚ್ಚೇರಿ ಕಾನೂನು ಹಸ್ತಾಂತರ ದಿನೋತ್ಸವ"),
            ("2018-08-17", "ಪಾರ್ಸಿ ಹೊಸ ವರ್ಷ (ಶಹನ್ಶಾಹಿ)"),
            ("2018-08-22", "ಬಕ್ರೀದ್"),
            ("2018-08-24", "ಓಣಂ"),
            ("2018-08-26", "ರಕ್ಷಾ ಬಂಧನ"),
            ("2018-09-03", "ಶ್ರೀ ಕೃಷ್ಣ ಜನ್ಮಾಷ್ಟಮಿ"),
            ("2018-09-13", "ವಿನಾಯಕ ಚತುರ್ಥಿ"),
            ("2018-09-21", "ಮೊಹರಂ ಕಡೆ ದಿನ"),
            ("2018-10-02", "ಗಾಂಧಿ ಜಯಂತಿ"),
            ("2018-10-08", "ಬತುಕಮ್ಮ ಹಬ್ಬ"),
            ("2018-10-10", "ನವರಾತ್ರಿ / ಶರದ್ ನವರಾತ್ರಿ"),
            ("2018-10-17", "ಮಹಾನವಮಿ"),
            ("2018-10-19", "ವಿಜಯದಶಮಿ"),
            ("2018-10-24", "ಮಹರ್ಷಿ ವಾಲ್ಮೀಕಿ ಜಯಂತಿ"),
            ("2018-10-31", "ಸರ್ದಾರ್ ವಲ್ಲಭಭಾಯಿ ಪಟೇಲ್ ಜಯಂತಿ"),
            (
                "2018-11-01",
                "ಆಂಧ್ರ ಪ್ರದೇಶ ಸ್ಥಾಪನಾ ದಿನ; "
                "ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ; "
                "ಕೇರಳ ಸ್ಥಾಪನಾ ದಿನ; "
                "ಛತ್ತೀಸ್‌ಗಢ ಸ್ಥಾಪನಾ ದಿನ; "
                "ಪುದುಚ್ಚೇರಿ ವಿಮೋಚನ ದಿನೋತ್ಸವ; "
                "ಮಧ್ಯ ಪ್ರದೇಶ ಸ್ಥಾಪನಾ ದಿನ; "
                "ಹರ್ಯಾಣ ಸ್ಥಾಪನಾ ದಿನ; "
                "ಹೊಸ ಪಂಜಾಬ್ ದಿನೋತ್ಸವ",
            ),
            ("2018-11-07", "ದೀಪಾವಳಿ"),
            ("2018-11-08", "ಗೋವರ್ಧನ ಪೂಜೆ"),
            ("2018-11-13", "ಛಠ್ ಪೂಜೆ"),
            ("2018-11-14", "ಮಕ್ಕಳ ದಿನಾಚರಣೆ"),
            ("2018-11-15", "ಜಾರ್ಖಂಡ್ ಸ್ಥಾಪನಾ ದಿನ"),
            ("2018-11-21", "ಈದ್-ಮಿಲಾದ್"),
            ("2018-11-23", "ಗುರು ನಾನಕ್ ಜಯಂತಿ"),
            ("2018-12-01", "ನಾಗಾಲ್ಯಾಂಡ್ ರಾಜ್ಯ ಸ್ಥಾಪನಾ ದಿನ"),
            ("2018-12-02", "ಅಸ್ಸಾಂ ದಿನೋತ್ಸವ"),
            ("2018-12-19", "ಗೋವಾ ವಿಮೋಚನ ದಿನೋತ್ಸವ"),
            ("2018-12-25", "ಕ್ರಿಸ್‌ಮಸ್"),
        )

    def test_l10n_ml(self):
        self.assertLocalizedHolidays(
            "ml",
            ("2018-01-13", "ലോഹരി"),
            ("2018-01-14", "ഉത്തരായൻ; പൊങ്കൽ; മകര സംക്രാന്തി; മാഘ് ബിഹു"),
            ("2018-01-15", "തിരുവള്ളുവർ ദിനം / മട്ടു പൊങ്കൽ"),
            ("2018-01-16", "ഉഴവർ തിരുനാൾ"),
            ("2018-01-24", "ഉത്തർപ്രദേശ് രൂപീകരണദിനം"),
            ("2018-01-26", "റിപ്പബ്ലിക് ദിനം"),
            ("2018-02-13", "മഹാ ശിവരാത്രി"),
            ("2018-02-19", "ചത്രപതി ശിവാജി മഹാരാജ ജയന്തി"),
            ("2018-02-20", "മിസോരം സംസ്ഥാനദിനം"),
            ("2018-03-02", "ഹോളി"),
            ("2018-03-18", "ഉഗാദി; ഗുഡി പദ്വ"),
            ("2018-03-22", "ബിഹാർ ദിനം"),
            ("2018-03-25", "ഓശാന ഞായർ; രാമ നവമി"),
            ("2018-03-29", "മഹാവീർ ജയന്തി"),
            ("2018-03-30", "ദുഃഖവെള്ളി; രാജസ്ഥാൻ ദിനം"),
            ("2018-04-01", "ഈസ്റ്റർ; ഉത്കൽ ദിവസ്"),
            ("2018-04-14", "ഡോ. ബി. ആർ. അംബേദ്കർ ജയന്തി; പുത്താണ്ട് (തമിഴ് പുതുവർഷം); വൈശാഖി"),
            (
                "2018-04-15",
                "പൊഹേലാ ബൈശാഖ്; മഹാ വിഷുവ സംക്രാന്തി / പനാ സംക്രാന്തി; ഹിമാചൽ ദിനം",
            ),
            ("2018-04-30", "ബുദ്ധ പൂർണ്ണിമ"),
            ("2018-05-01", "ഗുജറാത്ത് ദിനം; മഹാരാഷ്ട്ര ദിനം; മെയ് ദിനം"),
            ("2018-05-09", "രബീന്ദ്ര ജയന്തി"),
            ("2018-05-16", "സിക്കിം സംസ്ഥാനദിനം"),
            ("2018-06-02", "തെലങ്കാന രൂപീകരണദിനം"),
            ("2018-06-16", "ഈദ്-ഉൽ-ഫിത്തർ; മഹാരാണ പ്രതാപ് ജയന്തി"),
            ("2018-08-06", "ബോനാലു"),
            ("2018-08-15", "സ്വാതന്ത്ര്യദിനം"),
            ("2018-08-16", "പുതുച്ചേരി നിയമപരമായ കൈമാറ്റദിനം"),
            ("2018-08-17", "പാർസി പുതുവർഷം (ഷഹൻഷാഹി)"),
            ("2018-08-22", "ബക്രീദ്"),
            ("2018-08-24", "ഓണം"),
            ("2018-08-26", "രക്ഷാ ബന്ധൻ"),
            ("2018-09-03", "ജന്മാഷ്ടമി"),
            ("2018-09-13", "ഗണേശ് ചതുർത്ഥി"),
            ("2018-09-21", "മുഹറം"),
            ("2018-10-02", "ഗാന്ധി ജയന്തി"),
            ("2018-10-08", "ബത്തുകമ്മ ഉത്സവം"),
            ("2018-10-10", "നവരാത്രി / ശരദ് നവരാത്രി"),
            ("2018-10-17", "മഹാ നവമി"),
            ("2018-10-19", "ദശര"),
            ("2018-10-24", "മഹർഷി വാൽമീകി ജയന്തി"),
            ("2018-10-31", "സർദാർ വല്ലഭായി പട്ടേൽ ജയന്തി"),
            (
                "2018-11-01",
                "ആന്ധ്രാപ്രദേശ് സ്ഥാപനദിനം; "
                "കേരളപ്പിറവി; "
                "കർണാടക രാജ്യോത്സവം; "
                "ഛത്തീസ്ഗഢ് സ്ഥാപനദിനം; "
                "പുതിയ പഞ്ചാബ് ദിനം; "
                "പുതുച്ചേരി മോചനദിനം; "
                "മധ്യപ്രദേശ് സ്ഥാപനദിനം; "
                "ഹരിയാന സ്ഥാപനദിനം",
            ),
            ("2018-11-07", "ദീപാവലി"),
            ("2018-11-08", "ഗോവർധന പൂജ"),
            ("2018-11-13", "ഛഠ് പൂജ"),
            ("2018-11-14", "കുട്ടികളുടെ ദിനം"),
            ("2018-11-15", "ഝാർഖണ്ഡ് രൂപീകരണദിനം"),
            ("2018-11-21", "മിലാദ്-ഉന്നബി"),
            ("2018-11-23", "ഗുരു നാനക് ജയന്തി"),
            ("2018-12-01", "നാഗാലാൻഡ് സംസ്ഥാനാരംഭദിനം"),
            ("2018-12-02", "അസം ദിനം"),
            ("2018-12-19", "ഗോവ മോചനദിനം"),
            ("2018-12-25", "ക്രിസ്തുമസ്"),
        )

    def test_l10n_mr(self):
        self.assertLocalizedHolidays(
            "mr",
            ("2018-01-13", "लोहरी"),
            ("2018-01-14", "उत्तरायण; पोंगल; मकर संक्रांत; माघ बिहू"),
            ("2018-01-15", "तिरुवल्लुवर दिन / मट्टू पोंगल"),
            ("2018-01-16", "उझावर थिरुनल"),
            ("2018-01-24", "यूपी स्थापना दिन"),
            ("2018-01-26", "प्रजासत्ताक दिन"),
            ("2018-02-13", "महाशिवरात्री"),
            ("2018-02-19", "छत्रपती शिवाजी महाराज जयंती"),
            ("2018-02-20", "मिझोराम राज्य दिन"),
            ("2018-03-02", "होळी"),
            ("2018-03-18", "उगाडी; गुढीपाडवा"),
            ("2018-03-22", "बिहार दिन"),
            ("2018-03-25", "पाम रविवार; रामनवमी"),
            ("2018-03-29", "महावीर जन्म कल्याणक"),
            ("2018-03-30", "गुड फ्रायडे; राजस्थान दिन"),
            ("2018-04-01", "ईस्टर रविवार; ओडिशा दिन (उत्कल दिन)"),
            (
                "2018-04-14",
                "डॉ. बाबासाहेब आंबेडकर जयंती; पुथंडू (तमिळ नववर्ष); वैशाखी",
            ),
            (
                "2018-04-15",
                "पोहेला बैशाख; महाविश्व संक्रांती / पण संक्रांती; हिमाचल दिन",
            ),
            ("2018-04-30", "बुध्द पौर्णिमा"),
            ("2018-05-01", "कामगार दिन; गुजरात दिन; महाराष्ट्र दिन"),
            ("2018-05-09", "रवींद्र जयंती"),
            ("2018-05-16", "सिक्कीम राज्य दिन"),
            ("2018-06-02", "तेलंगणा स्थापना दिन"),
            ("2018-06-16", "महाराणा प्रताप जयंती; रमझान ईद (ईद-उल-फितर)"),
            ("2018-08-06", "बोनालू"),
            ("2018-08-15", "स्वातंत्र्य दिन"),
            ("2018-08-16", "पुदुचेरी कायदेशीर हस्तांतरण दिन"),
            ("2018-08-17", "पारसी नवीन वर्ष (शहेनशाही)"),
            ("2018-08-22", "बकरी ईद (ईद-उल-झुआ)"),
            ("2018-08-24", "ओणम"),
            ("2018-08-26", "रक्षाबंधन"),
            ("2018-09-03", "गोकुळाष्टमी"),
            ("2018-09-13", "गणेश चतुर्थी"),
            ("2018-09-21", "मोहरम"),
            ("2018-10-02", "महात्मा गांधी जयंती"),
            ("2018-10-08", "बथुकम्मा उत्सव"),
            ("2018-10-10", "नवरात्र / शारदीय नवरात्र"),
            ("2018-10-17", "महा नवमी"),
            ("2018-10-19", "दसरा"),
            ("2018-10-24", "महर्षी वाल्मिकी जयंती"),
            ("2018-10-31", "सरदार वल्लभभाई पटेल जयंती"),
            (
                "2018-11-01",
                "आंध्र प्रदेश स्थापना दिन; "
                "कर्नाटक राज्योत्सव; केरळ स्थापना दिन; "
                "छत्तीसगड स्थापना दिन; नवीन पंजाब दिन; "
                "पुदुचेरी मुक्ती दिन; मध्य प्रदेश स्थापना दिन; "
                "हरियाणा स्थापना दिन",
            ),
            ("2018-11-07", "दिवाळी (लक्ष्मीपूजन)"),
            ("2018-11-08", "गोवर्धन पूजा"),
            ("2018-11-13", "छठ पूजा"),
            ("2018-11-14", "बाल दिन"),
            ("2018-11-15", "झारखंड स्थापना दिन"),
            ("2018-11-21", "ईद-ए-मिलाद"),
            ("2018-11-23", "गुरुनानक जयंती"),
            ("2018-12-01", "नागालँड राज्य उद्घाटन दिन"),
            ("2018-12-02", "आसाम दिन"),
            ("2018-12-19", "गोवा मुक्ती दिन"),
            ("2018-12-25", "ख्रिसमस"),
        )

    def test_l10n_pa(self):
        self.assertLocalizedHolidays(
            "pa",
            ("2018-01-13", "ਲੋਹੜੀ"),
            ("2018-01-14", "ਉੱਤਰਾਯਣ; ਪੋਂਗਲ; ਮਕਰ ਸੰਕ੍ਰਾਂਤੀ; ਮਾਘ ਬਿਹੂ"),
            ("2018-01-15", "ਤਿਰੂਵੱਲੂਵਰ ਦਿਵਸ / ਮੱਟੂ ਪੋਂਗਲ"),
            ("2018-01-16", "ਉਝਾਵਰ ਥਿਰੂਨਲ"),
            ("2018-01-24", "ਯੂਪੀ ਗਠਨ ਦਿਵਸ"),
            ("2018-01-26", "ਗਣਤੰਤਰ ਦਿਵਸ"),
            ("2018-02-13", "ਮਹਾ ਸ਼ਿਵਰਾਤਰੀ"),
            ("2018-02-19", "ਛਤਰਪਤੀ ਸ਼ਿਵਾਜੀ ਮਹਾਰਾਜ ਜਯੰਤੀ"),
            ("2018-02-20", "ਮਿਜ਼ੋਰਮ ਰਾਜ ਦਿਵਸ"),
            ("2018-03-02", "ਹੋਲੀ"),
            ("2018-03-18", "ਉਗਾਦੀ; ਗੁੜੀ ਪਦਵਾ"),
            ("2018-03-22", "ਬਿਹਾਰ ਦਿਵਸ"),
            ("2018-03-25", "ਪਾਮ ਐਤਵਾਰ; ਰਾਮ ਨੌਮੀ"),
            ("2018-03-29", "ਮਹਾਵੀਰ ਜੈਯੰਤੀ"),
            ("2018-03-30", "ਗੁੱਡ ਫਰਾਈਡੇ; ਰਾਜਸਥਾਨ ਦਿਵਸ"),
            ("2018-04-01", "ਈਸਟਰ ਐਤਵਾਰ; ਓਡੀਸ਼ਾ ਦਿਵਸ (ਉਤਕਲ ਦਿਵਸ)"),
            (
                "2018-04-14",
                "ਜਨਮ ਦਿਨ ਡਾ: ਬੀ.ਆਰ. ਅੰਬੇਡਕਰ; ਪੁਥੰਡੂ (ਤਾਮਿਲ ਨਵਾਂ ਸਾਲ); ਵਿਸਾਖੀ",
            ),
            (
                "2018-04-15",
                "ਪੋਹੇਲਾ ਬੋਸ਼ਾਖ; ਮਹਾਂ ਵਿਸ਼ੁਵ ਸੰਕ੍ਰਾਂਤੀ / ਪਾਨਾ ਸੰਕ੍ਰਾਂਤੀ; ਹਿਮਾਚਲ ਦਿਵਸ",
            ),
            ("2018-04-30", "ਬੁੱਧ ਪੂਰਨਿਮਾ"),
            ("2018-05-01", "ਗੁਜਰਾਤ ਦਿਵਸ; ਮਈ ਦਿਵਸ; ਮਹਾਰਾਸ਼ਟਰ ਦਿਵਸ"),
            ("2018-05-09", "ਰਬਿੰਦਰ ਜੈਅੰਤੀ"),
            ("2018-05-16", "ਸਿੱਕਮ ਰਾਜ ਦਿਵਸ"),
            ("2018-06-02", "ਤੇਲੰਗਾਨਾ ਗਠਨ ਦਿਵਸ"),
            ("2018-06-16", "ਈਦ-ਉੱਲ-ਫਿਤਰ; ਮਹਾਰਾਣਾ ਪ੍ਰਤਾਪ ਜਯੰਤੀ"),
            ("2018-08-06", "ਬੋਨਾਲੂ"),
            ("2018-08-15", "ਸੁਤੰਤਰਤਾ ਦਿਵਸ"),
            ("2018-08-16", "ਪੁਡੂਚੇਰੀ ਡੀ ਜਿਊਰ ਟ੍ਰਾਂਸਫਰ ਦਿਵਸ"),
            ("2018-08-17", "ਪਾਰਸੀ ਨਵਾਂ ਸਾਲ (ਸ਼ਾਹਨਸ਼ਾਹੀ)"),
            ("2018-08-22", "ਈਦ-ਉੱਲ-ਜੂਹਾ (ਬਕਰੀਦ)"),
            ("2018-08-24", "ਓਨਮ"),
            ("2018-08-26", "ਰੱਖੜੀ"),
            ("2018-09-03", "ਜਨਮ ਅਸ਼ਟਮੀ"),
            ("2018-09-13", "ਗਣੇਸ਼ ਚਤੁਰਥੀ"),
            ("2018-09-21", "ਮੁਹੱਰਮ"),
            ("2018-10-02", "ਜਨਮ ਦਿਵਸ ਮਹਾਤਮਾ ਗਾਂਧੀ ਜੀ"),
            ("2018-10-08", "ਬਾਥੁਕੰਮਾ ਤਿਉਹਾਰ"),
            ("2018-10-10", "ਨਵਰਾਤਰੀ / ਸ਼ਰਦ ਨਵਰਾਤਰੀ"),
            ("2018-10-17", "ਮਹਾ ਨਵਮੀ"),
            ("2018-10-19", "ਦੁਸਹਿਰਾ"),
            ("2018-10-24", "ਮਹਾਰਿਸ਼ੀ ਵਾਲਮੀਕੀ ਜਯੰਤੀ"),
            ("2018-10-31", "ਸਰਦਾਰ ਵੱਲਭ ਭਾਈ ਪਟੇਲ ਜਯੰਤੀ"),
            (
                "2018-11-01",
                "ਆਂਧਰਾ ਪ੍ਰਦੇਸ਼ ਸਥਾਪਨਾ ਦਿਵਸ; "
                "ਕਰਨਾਟਕ ਰਾਜਯੋਤਸਵ; ਕੇਰਲ ਸਥਾਪਨਾ ਦਿਵਸ; "
                "ਛੱਤੀਸਗੜ੍ਹ ਸਥਾਪਨਾ ਦਿਵਸ; ਨਵਾਂ ਪੰਜਾਬ ਦਿਵਸ; "
                "ਪੁਡੂਚੇਰੀ ਮੁਕਤੀ ਦਿਵਸ; ਮੱਧ ਪ੍ਰਦੇਸ਼ ਸਥਾਪਨਾ ਦਿਵਸ; "
                "ਹਰਿਆਣਾ ਸਥਾਪਨਾ ਦਿਵਸ",
            ),
            ("2018-11-07", "ਦੀਵਾਲੀ"),
            ("2018-11-08", "ਗੋਵਰਧਨ ਪੂਜਾ"),
            ("2018-11-13", "ਛੱਠ ਪੂਜਾ"),
            ("2018-11-14", "ਬਾਲ ਦਿਵਸ"),
            ("2018-11-15", "ਝਾਰਖੰਡ ਗਠਨ ਦਿਵਸ"),
            ("2018-11-21", "ਮਿਲਾਦ-ਉੱਨ-ਨਬੀ"),
            ("2018-11-23", "ਗੁਰਪੁਰਬ ਸਾਹਿਬ ਸ੍ਰੀ ਗੁਰੂ ਨਾਨਕ ਦੇਵ ਜੀ"),
            ("2018-12-01", "ਨਾਗਾਲੈਂਡ ਰਾਜ ਦਾ ਉਦਘਾਟਨ ਦਿਵਸ"),
            ("2018-12-02", "ਅਸਾਮ ਦਿਵਸ"),
            ("2018-12-19", "ਗੋਆ ਮੁਕਤੀ ਦਿਵਸ"),
            ("2018-12-25", "ਕ੍ਰਿਸਮਿਸ ਦਿਵਸ"),
        )

    def test_l10n_ta(self):
        self.assertLocalizedHolidays(
            "ta",
            ("2018-01-13", "லோஹ்ரி"),
            ("2018-01-14", "உத்தராயண் நாள்; பொங்கல்; மகர சங்கராந்தி; மாக் பிஹூ"),
            ("2018-01-15", "திருவள்ளுவர் நாள் / மாட்டுப் பொங்கல்"),
            ("2018-01-16", "உழவர் திருநாள்"),
            ("2018-01-24", "உத்தரப்பிரதேச உருவாக்க நாள்"),
            ("2018-01-26", "குடியரசு நாள்"),
            ("2018-02-13", "மகா சிவராத்திரி"),
            ("2018-02-19", "சத்ரபதி சிவாஜி மகாராஜ் ஜெயந்தி"),
            ("2018-02-20", "மிசோரம் மாநில நாள்"),
            ("2018-03-02", "ஹோலி"),
            ("2018-03-18", "உகாதி; குடி பாத்வா"),
            ("2018-03-22", "பீகார் நாள்"),
            ("2018-03-25", "பனை ஞாயிறு; ராம நவமி"),
            ("2018-03-29", "மகாவீர் ஜெயந்தி"),
            ("2018-03-30", "புனித வெள்ளி; ராஜஸ்தான் நாள்"),
            ("2018-04-01", "ஈஸ்டர் ஞாயிறு; ஒடிசா நாள் (உத்கல திவசம்)"),
            ("2018-04-14", "டாக்டர் பி. ஆர். அம்பேத்கர் ஜெயந்தி; புத்தாண்டு (தமிழ் புத்தாண்டு); வைசாகி"),
            ("2018-04-15", "இமாச்சல் நாள்; பொஹேலா பொய்ஷாக்; மகா விஷுவ சங்கராந்தி / பானா சங்கராந்தி"),
            ("2018-04-30", "புத்தர் பௌர்ணமி"),
            ("2018-05-01", "குஜராத் நாள்; தொழிலாளர் நாள்; மகாராஷ்டிரா நாள்"),
            ("2018-05-09", "ரபீந்திர ஜெயந்தி"),
            ("2018-05-16", "சிக்கிம் மாநில நாள்"),
            ("2018-06-02", "தெலுங்கானா உருவாக்க நாள்"),
            ("2018-06-16", "ஈத் உல்-பித்ர்; மகாராணா பிரதாப் ஜெயந்தி"),
            ("2018-08-06", "போனாலு"),
            ("2018-08-15", "சுதந்திர தினம்"),
            ("2018-08-16", "புதுச்சேரி சட்டபூர்வ பரிமாற்ற நாள்"),
            ("2018-08-17", "பார்சி புத்தாண்டு (ஷாஹென்ஷாஹி)"),
            ("2018-08-22", "பகரீத்"),
            ("2018-08-24", "ஓணம்"),
            ("2018-08-26", "ரக்ஷா பந்தன்"),
            ("2018-09-03", "கிருஷ்ண ஜெயந்தி"),
            ("2018-09-13", "விநாயகர் சதுர்த்தி"),
            ("2018-09-21", "முஹர்ரம்"),
            ("2018-10-02", "காந்தி ஜெயந்தி"),
            ("2018-10-08", "பதுக்கம்மா திருவிழா"),
            ("2018-10-10", "நவராத்திரி / சரத நவராத்திரி"),
            ("2018-10-17", "மகா நவமி"),
            ("2018-10-19", "விஜயதசமி"),
            ("2018-10-24", "மகரிஷி வால்மீகி ஜெயந்தி"),
            ("2018-10-31", "சர்தார் வல்லபாய் படேல் ஜெயந்தி"),
            (
                "2018-11-01",
                "ஆந்திரப் பிரதேச நாள்; "
                "கர்நாடக ராஜ்யோற்சவம்; "
                "கேரள நாள்; "
                "சத்தீஸ்கர் நாள்; "
                "நியூ பஞ்சாப் நாள்; "
                "புதுச்சேரி விடுதலை நாள்; "
                "மத்திய பிரதேச நாள்; "
                "ஹரியானா நாள்",
            ),
            ("2018-11-07", "தீபாவளி"),
            ("2018-11-08", "கோவர்தன் பூஜை"),
            ("2018-11-13", "சத் பூஜை"),
            ("2018-11-14", "குழந்தைகள் நாள்"),
            ("2018-11-15", "ஜார்கண்ட் உருவாக்க நாள்"),
            ("2018-11-21", "மீலாது உல் நபி"),
            ("2018-11-23", "குரு நானக் ஜெயந்தி"),
            ("2018-12-01", "நாகலாந்து மாநில தொடக்க நாள்"),
            ("2018-12-02", "அஸ்ஸாம் நாள்"),
            ("2018-12-19", "கோவா விடுதலை நாள்"),
            ("2018-12-25", "கிறிஸ்துமஸ்"),
        )

    def test_l10n_te(self):
        self.assertLocalizedHolidays(
            "te",
            ("2018-01-13", "లోహ్రీ"),
            ("2018-01-14", "ఉత్తరాయణం; పొంగల్; భోగాలీ బిహు; మకర సంక్రాంతి"),
            ("2018-01-15", "తిరువళ్ళువర్ దినోత్సవం / మట్టు పొంగల్"),
            ("2018-01-16", "రైతుల పండుగ"),
            ("2018-01-24", "ఉత్తర ప్రదేశ్ అవతరణ దినోత్సవం"),
            ("2018-01-26", "గణతంత్ర దినోత్సవం"),
            ("2018-02-13", "మహాశివరాత్రి"),
            ("2018-02-19", "ఛత్రపతి శివాజీ మహారాజ్ జయంతి"),
            ("2018-02-20", "మిజోరాం రాష్ట్ర దినోత్సవం"),
            ("2018-03-02", "హోలీ"),
            ("2018-03-18", "ఉగాది; గుడి పడ్వా"),
            ("2018-03-22", "బీహార్ దినోత్సవం"),
            ("2018-03-25", "మట్టల ఆదివారం; శ్రీరామనవమి"),
            ("2018-03-29", "మహావీర్ జయంతి"),
            ("2018-03-30", "గుడ్ ఫ్రైడే; రాజస్థాన్ దినోత్సవం"),
            ("2018-04-01", "ఈస్టర్ ఆదివారం; ఒడిశా దినోత్సవం (ఉత్కల దివస)"),
            ("2018-04-14", "డా. బి.ఆర్. అంబేద్కర్ జయంతి; పుతండు (తమిళ నూతన సంవత్సరం); వైశాఖి"),
            ("2018-04-15", "పొహెలా బొయిషాఖ్; మహా విషువ సంక్రాంతి / పానా సంక్రాంతి; హిమాచల్ దినోత్సవం"),
            ("2018-04-30", "బుద్ధ పూర్ణిమ"),
            ("2018-05-01", "కార్మిక దినోత్సవం; గుజరాత్ దినోత్సవం; మహారాష్ట్ర దినోత్సవం"),
            ("2018-05-09", "రవీంద్ర జయంతి"),
            ("2018-05-16", "సిక్కిం రాష్ట్ర దినోత్సవం"),
            ("2018-06-02", "తెలంగాణ అవతరణ దినోత్సవం"),
            ("2018-06-16", "ఈద్-ఉల్-ఫితర్; మహారాణా ప్రతాప్ జయంతి"),
            ("2018-08-06", "బోనాలు"),
            ("2018-08-15", "స్వాతంత్ర దినోత్సవం"),
            ("2018-08-16", "పుదుచ్చేరి చట్టబద్ధ బదిలీ దినోత్సవం"),
            ("2018-08-17", "పార్సీ నూతన సంవత్సరం (షహన్‌షాహీ)"),
            ("2018-08-22", "బక్రీద్"),
            ("2018-08-24", "ఓణం"),
            ("2018-08-26", "రాఖీ పౌర్ణమి"),
            ("2018-09-03", "కృష్ణాష్టమి"),
            ("2018-09-13", "వినాయక చవితి"),
            ("2018-09-21", "మొహర్రం"),
            ("2018-10-02", "గాంధీ జయంతి"),
            ("2018-10-08", "బతుకమ్మ పండుగ"),
            ("2018-10-10", "నవరాత్రి / శరద్ నవరాత్రి"),
            ("2018-10-17", "మహా నవమి"),
            ("2018-10-19", "విజయదశమి"),
            ("2018-10-24", "మహర్షి వాల్మీకి జయంతి"),
            ("2018-10-31", "సర్దార్ వల్లభభాయి పటేల్ జయంతి"),
            (
                "2018-11-01",
                "ఆంధ్రప్రదేశ్ అవతరణ దినోత్సవం; "
                "కర్ణాటక రాజ్యోత్సవం; "
                "కేరళ అవతరణ దినోత్సవం; "
                "కొత్త పంజాబ్ దినోత్సవం; "
                "ఛత్తీస్‌గఢ్ అవతరణ దినోత్సవం; "
                "పుదుచ్చేరి విమోచన దినోత్సవం; "
                "మధ్యప్రదేశ్ అవతరణ దినోత్సవం; "
                "హర్యానా అవతరణ దినోత్సవం",
            ),
            ("2018-11-07", "దీపావళి"),
            ("2018-11-08", "గోవర్ధన పూజ"),
            ("2018-11-13", "ఛఠ్ పూజ"),
            ("2018-11-14", "బాలల దినోత్సవం"),
            ("2018-11-15", "ఝార్ఖండ్ అవతరణ దినోత్సవం"),
            ("2018-11-21", "మిలాద్-ఉన్-నబీ"),
            ("2018-11-23", "గురునానక్ జయంతి"),
            ("2018-12-01", "నాగాలాండ్ రాష్ట్ర ప్రారంభ దినోత్సవం"),
            ("2018-12-02", "అస్సాం దినోత్సవం"),
            ("2018-12-19", "గోవా విమోచన దినోత్సవం"),
            ("2018-12-25", "క్రిస్మస్"),
        )
