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

import importlib
import inspect
import warnings
from unittest import TestCase

import pytest

import holidays
from holidays import countries, financial, registry
from tests.common import PYTHON_LATEST_SUPPORTED_VERSION, PYTHON_VERSION


class TestEntityLoader(TestCase):
    @pytest.mark.skipif(
        PYTHON_VERSION != PYTHON_LATEST_SUPPORTED_VERSION,
        reason="Run once on the latest Python version only",
    )

    def _assert_entities_importable(
        self, registry_entities, entity_namespace, namespace
    ):
        loader_entities = set()
        for module, entities in registry_entities.items():
            module = importlib.import_module(f"holidays.{namespace}.{module}")
            for entity in entities:
                entity_cls = getattr(entity_namespace, entity)
                loader_cls = getattr(holidays, entity)
                module_cls = getattr(module, entity)

                self.assertIsNotNone(entity_cls, entity)
                self.assertIsNotNone(loader_cls, entity)
                self.assertIsNotNone(module_cls, entity)
                self.assertEqual(entity_cls, module_cls)
                self.assertIsInstance(loader_cls, registry.EntityLoader)
                self.assertIsInstance(loader_cls(), entity_cls)
                self.assertIsInstance(loader_cls(), module_cls)

                loader_entities.add(loader_cls.__name__)

        entities = {
            entity[0]
            for entity in inspect.getmembers(entity_namespace, inspect.isclass)
        }
        self.assertEqual(
            entities,
            loader_entities,
            f"Registry entities and {namespace} entities don't match: "
            f"{entities.difference(loader_entities)}",
        )
    def test_countries_imports(self):
        warnings.simplefilter("ignore")
        self._assert_entities_importable(registry.COUNTRIES, countries, "countries")

    def test_country_str(self):
        self.assertEqual(
            str(registry.EntityLoader("holidays.countries.united_states.US")),
            "A lazy loader for <class 'holidays.countries.united_states.US'>. "
            "For inheritance please use the "
            "'holidays.countries.united_states.US' class directly.",
        )

    @pytest.mark.skipif(
        PYTHON_VERSION != PYTHON_LATEST_SUPPORTED_VERSION,
        reason="Run once on the latest Python version only",
    )
    def test_financial_imports(self):
        self._assert_entities_importable(registry.FINANCIAL, financial, "financial")

    def test_financial_str(self):
        self.assertEqual(
            str(registry.EntityLoader("holidays.financial.ny_stock_exchange.NYSE")),
            "A lazy loader for "
            "<class 'holidays.financial.ny_stock_exchange.NYSE'>. "
            "For inheritance please use the "
            "'holidays.financial.ny_stock_exchange.NYSE' class directly.",
        )

    def test_get_country_codes(self):
        country_codes = set(registry.EntityLoader.get_country_codes(include_aliases=False))
        for entity_classes in registry.COUNTRIES.values():
            self.assertNotIn(entity_classes[0], country_codes)
            self.assertIn(entity_classes[1], country_codes)
            for code in entity_classes[2:]:
                self.assertNotIn(code, country_codes)

    def test_get_country_codes_aliases(self):
        country_codes = set(registry.EntityLoader.get_country_codes(include_aliases=True))
        for entity_classes in registry.COUNTRIES.values():
            self.assertNotIn(entity_classes[0], country_codes)
            for code in entity_classes[1:]:
                if code.isupper():
                    self.assertIn(code, country_codes)
                else:
                    self.assertNotIn(code, country_codes)

    def test_get_financial_codes(self):
        financial_codes = set(registry.EntityLoader.get_financial_codes(include_aliases=False))
        for entity_classes in registry.FINANCIAL.values():
            self.assertNotIn(entity_classes[0], financial_codes)
            self.assertIn(entity_classes[1], financial_codes)
            for code in entity_classes[2:]:
                self.assertNotIn(code, financial_codes)

    def test_get_financial_codes_aliases(self):
        financial_codes = set(registry.EntityLoader.get_financial_codes(include_aliases=True))
        for entity_classes in registry.FINANCIAL.values():
            self.assertNotIn(entity_classes[0], financial_codes)
            for code in entity_classes[1:]:
                if code.isupper():
                    self.assertIn(code, financial_codes)
                else:
                    self.assertNotIn(code, financial_codes)

    def test_inheritance(self):
        def create_instance(parent):
            subclass = type("SubClass", (parent,), {})
            return subclass()

        for cls in (holidays.UnitedStates, holidays.US, holidays.USA):
            self.assertIsInstance(cls, holidays.registry.EntityLoader)
            with self.assertRaises(TypeError):
                create_instance(cls)

        for cls in (
            holidays.countries.UnitedStates,
            holidays.countries.US,
            holidays.countries.USA,
        ):
            self.assertIsInstance(create_instance(cls), holidays.countries.UnitedStates)
