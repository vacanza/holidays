#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import importlib
import inspect
import warnings
from unittest import TestCase

from holidays import countries, financial, registry


class TestEntityLoader(TestCase):
    def test_countries_imports(self):
        warnings.simplefilter("ignore")

        import holidays

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
                self.assertTrue(isinstance(loader_cls, registry.EntityLoader))
                self.assertTrue(isinstance(loader_cls(), countries_cls))
                self.assertTrue(isinstance(loader_cls(), module_cls))

                loader_entities.add(loader_cls.__name__)

        countries_entities = set(
            entity[0]
            for entity in inspect.getmembers(countries, inspect.isclass)
        )
        self.assertEqual(
            countries_entities,
            loader_entities,
            "Registry entities and countries entities don't match: %s"
            % countries_entities.difference(loader_entities),
        )

    def test_country_str(self):
        self.assertEqual(
            str(
                registry.EntityLoader(
                    "holidays.countries.united_states.US",
                )
            ),
            "A lazy loader for "
            "<class 'holidays.countries.united_states.US'>. For class "
            "inheritance please use 'holidays.countries' entities directly.",
        )

    def test_financial_imports(self):
        import holidays

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
                self.assertTrue(isinstance(loader_cls, registry.EntityLoader))
                self.assertTrue(isinstance(loader_cls(), financial_cls))
                self.assertTrue(isinstance(loader_cls(), module_cls))

                loader_entities.add(loader_cls.__name__)

        financial_entities = set(
            entity[0]
            for entity in inspect.getmembers(financial, inspect.isclass)
        )
        self.assertEqual(
            financial_entities,
            loader_entities,
            "Registry entities and financial entities don't match: %s"
            % financial_entities.difference(loader_entities),
        )

    def test_financial_str(self):
        self.assertEqual(
            str(
                registry.EntityLoader(
                    "holidays.financial.ny_stock_exchange.NYSE"
                )
            ),
            "A lazy loader for "
            "<class 'holidays.financial.ny_stock_exchange.NYSE'>. For class "
            "inheritance please use 'holidays.financial' entities directly.",
        )
