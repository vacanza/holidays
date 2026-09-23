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
import subprocess
import sys
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
    def test_countries_imports(self):
        warnings.simplefilter("ignore")

        loader_entities = set()
        for module, entities in registry.COUNTRIES.items():
            module = importlib.import_module(f"holidays.countries.{module}")
            for entity in entities:
                countries_cls = getattr(countries, entity)
                loader_cls = getattr(holidays, entity)
                module_cls = getattr(module, entity)

                self.assertIsNotNone(countries_cls, entity)
                self.assertIsNotNone(loader_cls, entity)
                self.assertIsNotNone(module_cls, entity)
                self.assertEqual(countries_cls, module_cls)
                self.assertIsInstance(loader_cls, registry.EntityLoader)
                self.assertIsInstance(loader_cls(), countries_cls)
                self.assertIsInstance(loader_cls(), module_cls)

                loader_entities.add(loader_cls.__name__)

        countries_entities = {
            entity[0] for entity in inspect.getmembers(countries, inspect.isclass)
        }
        self.assertEqual(
            countries_entities,
            loader_entities,
            "Registry entities and countries entities don't match: "
            f"{countries_entities.difference(loader_entities)}",
        )

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
        loader_entities = set()
        for module, entities in registry.FINANCIAL.items():
            module = importlib.import_module(f"holidays.financial.{module}")
            for entity in entities:
                financial_cls = getattr(financial, entity)
                loader_cls = getattr(holidays, entity)
                module_cls = getattr(module, entity)

                self.assertIsNotNone(financial_cls, entity)
                self.assertIsNotNone(loader_cls, entity)
                self.assertIsNotNone(module_cls, entity)
                self.assertEqual(financial_cls, module_cls)
                self.assertIsInstance(loader_cls, registry.EntityLoader)
                self.assertIsInstance(loader_cls(), financial_cls)
                self.assertIsInstance(loader_cls(), module_cls)

                loader_entities.add(loader_cls.__name__)

        financial_entities = {
            entity[0] for entity in inspect.getmembers(financial, inspect.isclass)
        }
        self.assertEqual(
            financial_entities,
            loader_entities,
            "Registry entities and financial entities don't match: "
            f"{financial_entities.difference(loader_entities)}",
        )

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
            class SubClass(parent):
                pass

            return SubClass()

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

    def test_lazy_package_attributes(self):
        for package, container in (
            (countries, registry.COUNTRIES),
            (financial, registry.FINANCIAL),
        ):
            module_name, entities = next(iter(container.items()))
            module = importlib.import_module(f"{package.__name__}.{module_name}")

            # Entity modules are resolved on attribute access too.
            delattr(package, module_name)
            try:
                self.assertEqual(getattr(package, module_name), module)
            finally:
                setattr(package, module_name, module)

            for entity in entities:
                self.assertEqual(getattr(package, entity), getattr(module, entity))
                self.assertIn(entity, package.__all__)
                self.assertIn(entity, dir(package))
            self.assertIn(module_name, package.__all__)

            with self.assertRaises(AttributeError):
                package.NonExistentEntity

    def test_lazy_package_loading(self):
        code = (
            "import sys, holidays; holidays.country_holidays('CA', subdiv='QC'); "
            "holidays.financial_holidays('XNYS'); "
            "print(sorted(m for m in sys.modules "
            "if m.startswith(('holidays.countries.', 'holidays.financial.'))))"
        )
        self.assertEqual(
            subprocess.check_output([sys.executable, "-c", code], text=True).strip(),  # noqa: S603
            "['holidays.countries.canada', 'holidays.financial.ny_stock_exchange']",
        )
