#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

import importlib
from unittest import TestCase

import pytest

import holidays
from holidays.registry import ISO_10383, ISO_3166, EntityLoader
from tests.common import PYTHON_LATEST_SUPPORTED_VERSION, PYTHON_VERSION


class TestEntityLoader(TestCase):
    def test_get_entity_codes(self):
        registry_container = {"A": ("A", "AA", "AAA"), "B": ("B", "BB")}

        codes = set(
            EntityLoader._get_entity_codes(container=registry_container, include_aliases=False)
        )
        codes_aliases = set(
            EntityLoader._get_entity_codes(container=registry_container, include_aliases=True)
        )

        for item in ("A", "B"):
            self.assertIn(item, codes)
            self.assertIn(item, codes_aliases)

        for item in ("AA", "AAA", "BB"):
            self.assertNotIn(item, codes)
            self.assertIn(item, codes_aliases)

    @pytest.mark.skipif(
        PYTHON_VERSION != PYTHON_LATEST_SUPPORTED_VERSION,
        reason="Run once on the latest Python version only",
    )
    def test_iso_3166_imports(self):
        for code, aliases in ISO_3166.items():
            module = importlib.import_module(f"holidays.entities.ISO_3166.{code}")
            entity_cls = getattr(module, f"{code.capitalize()}Holidays", None)
            self.assertIsNotNone(entity_cls, code)

            for alias in aliases:
                loader_cls = getattr(holidays, alias, None)
                self.assertIsNotNone(loader_cls, alias)
                self.assertIsInstance(loader_cls, EntityLoader)
                self.assertIsInstance(loader_cls(), entity_cls)

    def test_iso_3166_str(self):
        self.assertEqual(
            str(EntityLoader("holidays.entities.ISO_3166.US.UsHolidays")),
            "A lazy loader for <class 'holidays.entities.ISO_3166.US.UsHolidays'>. "
            "For inheritance please use the "
            "'holidays.entities.ISO_3166.US.UsHolidays' class directly.",
        )

    @pytest.mark.skipif(
        PYTHON_VERSION != PYTHON_LATEST_SUPPORTED_VERSION,
        reason="Run once on the latest Python version only",
    )
    def test_iso_10383_imports(self):
        for code, aliases in ISO_10383.items():
            module = importlib.import_module(f"holidays.entities.ISO_10383.{code}")
            entity_cls = getattr(module, f"{code.capitalize()}Holidays", None)
            self.assertIsNotNone(entity_cls, code)

            for alias in aliases:
                loader_cls = getattr(holidays, alias)
                self.assertIsNotNone(loader_cls, alias)
                self.assertIsInstance(loader_cls, EntityLoader)
                self.assertIsInstance(loader_cls(), entity_cls)

    def test_iso_10383_str(self):
        self.assertEqual(
            str(EntityLoader("holidays.entities.ISO_10383.XNYS.XnysHolidays")),
            "A lazy loader for "
            "<class 'holidays.entities.ISO_10383.XNYS.XnysHolidays'>. "
            "For inheritance please use the "
            "'holidays.entities.ISO_10383.XNYS.XnysHolidays' class directly.",
        )

    def test_inheritance(self):
        def create_instance(parent):
            class SubClass(parent):
                pass

            return SubClass()

        for cls in (holidays.US, holidays.USA):
            self.assertIsInstance(cls, holidays.registry.EntityLoader)
            with self.assertRaises(TypeError):
                create_instance(cls)

        self.assertIsInstance(
            create_instance(holidays.entities.ISO_3166.US.UsHolidays),
            holidays.entities.ISO_3166.US.UsHolidays,
        )

    def test_load(self):
        scope = {}

        EntityLoader.load(prefix="invalid", scope=scope)
        self.assertDictEqual(scope, {})

        EntityLoader.load(prefix="ISO_10383", scope=scope)
        self.assertIn("IFEU", scope)

        EntityLoader.load(prefix="ISO_3166", scope=scope)
        self.assertIn("UA", scope)
