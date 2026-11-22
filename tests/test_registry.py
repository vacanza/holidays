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

import ast
import importlib
import inspect
import os
import subprocess
import sys
import warnings
from pathlib import Path
from unittest import TestCase, mock

import pytest

import holidays
from holidays import calendars, countries, financial, groups, registry
from tests.common import PYTHON_LATEST_SUPPORTED_VERSION, PYTHON_VERSION


class TestEntityLoader(TestCase):
    @staticmethod
    def lazy_load_modules(path: Path) -> dict[str, tuple[str, ...]]:
        """Return the `modules` mapping passed to `_load_lazily` in a package `__init__`."""
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in tree.body:
            if not isinstance(node, ast.If):
                continue
            test = node.test
            if not (isinstance(test, ast.Name) and test.id == "TYPE_CHECKING"):
                continue
            for statement in node.orelse:
                if not isinstance(statement, ast.Expr) or not isinstance(
                    statement.value, ast.Call
                ):
                    continue
                call = statement.value
                if not isinstance(call.func, ast.Name) or call.func.id != "_load_lazily":
                    continue
                if len(call.args) < 2:
                    break
                mapping = ast.literal_eval(call.args[1])
                return {str(module): tuple(names) for module, names in mapping.items()}
        raise AssertionError(f"No _load_lazily mapping found in {path}")

    @staticmethod
    def type_checking_imports(path: Path) -> set[tuple[str, str]]:
        """Return `(module, name)` pairs from a package's `TYPE_CHECKING` import block."""
        imported: set[tuple[str, str]] = set()
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in tree.body:
            if not isinstance(node, ast.If):
                continue
            test = node.test
            if not (isinstance(test, ast.Name) and test.id == "TYPE_CHECKING"):
                continue
            for statement in node.body:
                # Pair each name with its module so a wrong import path fails.
                if isinstance(statement, ast.ImportFrom) and statement.module is not None:
                    imported.update(
                        (statement.module, alias.asname or alias.name) for alias in statement.names
                    )
        return imported

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

    def test_type_checking_imports_match_lazy_maps(self):
        # Calendars/groups have no registry: keep TYPE_CHECKING imports aligned with
        # the runtime `_load_lazily` map. Empty-export modules (submodule access only)
        # are runtime-only and must not appear in TYPE_CHECKING name imports.
        for package in (calendars, groups):
            path = Path(package.__file__)
            imported = self.type_checking_imports(path)
            lazy_modules = self.lazy_load_modules(path)
            registered = {
                (f"{package.__name__}.{module}", name)
                for module, names in lazy_modules.items()
                for name in names
            }
            module_only = {module for module, names in lazy_modules.items() if not names}

            differences = []
            if missing := sorted(registered - imported):
                differences.append(f"missing {missing}")
            if extra := sorted(imported - registered):
                differences.append(f"extra {extra}")
            if unexpected := sorted(
                {
                    module_path.rsplit(".", 1)[-1]
                    for module_path, _name in imported
                    if module_path.rsplit(".", 1)[-1] in module_only
                }
            ):
                differences.append(f"TYPE_CHECKING imports from module-only {unexpected}")
            on_disk = {file.stem for file in Path(package.__path__[0]).glob("[!_]*.py")}
            if missing_modules := sorted(module_only - on_disk):
                differences.append(f"module-only not on disk {missing_modules}")

            if differences:
                self.fail(
                    f"{package.__name__} TYPE_CHECKING vs lazy map: {', '.join(differences)}."
                )

    def test_type_checking_imports_match_registry(self):
        for package, container in (
            (countries, registry.COUNTRIES),
            (financial, registry.FINANCIAL),
        ):
            imported = self.type_checking_imports(Path(package.__file__))
            registered = {
                (f"{package.__name__}.{module}", name)
                for module, entities in container.items()
                for name in entities
            }
            differences = []
            if missing := sorted(registered - imported):
                differences.append(f"missing {missing}")
            if extra := sorted(imported - registered):
                differences.append(f"extra {extra}")

            if differences:
                self.fail(f"{package.__name__} TYPE_CHECKING imports: {', '.join(differences)}.")


class TestLazyPackage(TestCase):
    @staticmethod
    def _holidays_subprocess_env() -> tuple[str, dict[str, str]]:
        root = str(Path(holidays.__file__).resolve().parent.parent)
        env = {
            **os.environ,
            "PYTHONPATH": os.pathsep.join(filter(None, (root, os.environ.get("PYTHONPATH")))),
        }
        return root, env

    @staticmethod
    def run_holidays_code(code: str) -> str:
        """Run `code` in a new interpreter that imports the holidays package under test."""
        root, env = TestLazyPackage._holidays_subprocess_env()
        return subprocess.check_output(  # noqa: S603
            [sys.executable, "-c", code], cwd=root, env=env, text=True
        ).strip()

    @staticmethod
    def run_holidays_script(script: Path) -> str:
        """Run `script` in a new interpreter that imports the holidays package under test."""
        root, env = TestLazyPackage._holidays_subprocess_env()
        return subprocess.check_output(  # noqa: S603
            [sys.executable, str(script)], cwd=root, env=env, text=True
        ).strip()

    def test_lazy_calendars_and_groups_namespaces(self):
        for package, not_imported_submodules in (
            # The school calendars are imported by their countries only.
            (calendars, {"australia_school", "germany_school"}),
            (groups, set()),
        ):
            exported = set(package.__all__)
            public_names = {name for name in dir(package) if not name.startswith("_")}
            # Other public names are only the submodules that were imported directly.
            self.assertLessEqual(exported, public_names)
            self.assertLessEqual(public_names - exported, not_imported_submodules)
            self.assertNotIn("TYPE_CHECKING", dir(package))
            self.assertNotIn("_load_lazily", dir(package))
            submodules = {path.stem for path in Path(package.__path__[0]).glob("[!_]*.py")}
            self.assertEqual(exported & submodules, submodules - not_imported_submodules)
            for name in package.__all__:
                self.assertIsNotNone(getattr(package, name))

    def test_lazy_imports_do_not_deadlock(self):
        script = Path(__file__).parent / "lazy_loading" / "import_deadlock.py"
        self.assertEqual(self.run_holidays_script(script), "ok")

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

            # Already cached: `__getattr__` is not called by normal lookup.
            self.assertEqual(package.__getattr__(module_name), module)
            self.assertEqual(package.__getattr__(entities[0]), getattr(module, entities[0]))

            with self.assertRaises(AttributeError):
                package.NonExistentEntity

    def test_lazy_package_imports_hold_import_lock(self):
        original_import_module = importlib.import_module
        lock_owned = []

        def import_module(name, package=None):
            if name.startswith(("holidays.countries.", "holidays.financial.")):
                lock_owned.append(registry.IMPORT_LOCK._is_owned())
            return original_import_module(name, package)

        for package, container in (
            (countries, registry.COUNTRIES),
            (financial, registry.FINANCIAL),
        ):
            module_name, entities = next(iter(container.items()))
            entity = entities[0]
            # Restore the package namespace as it was, whether the names were cached or not.
            cached = {name: vars(package).get(name) for name in (module_name, entity)}
            module = original_import_module(f"{package.__name__}.{module_name}")
            vars(package).pop(module_name, None)
            vars(package).pop(entity, None)
            lock_owned.clear()
            try:
                with mock.patch("importlib.import_module", side_effect=import_module):
                    # Module-name access (e.g. holidays.countries.canada).
                    self.assertEqual(getattr(package, module_name), module)
                    # Entity access (e.g. holidays.countries.Canada).
                    self.assertEqual(getattr(package, entity), getattr(module, entity))
            finally:
                for name, value in cached.items():
                    if value is None:
                        vars(package).pop(name, None)
                    else:
                        setattr(package, name, value)
            self.assertEqual(lock_owned, [True, True])

    def test_lazy_package_loading(self):
        code = (
            "import sys, holidays; holidays.country_holidays('CA', subdiv='QC'); "
            "holidays.financial_holidays('XNYS'); "
            "dir(holidays); holidays.__all__; dir(holidays.calendars); dir(holidays.groups); "
            "print(sorted(m for m in sys.modules if m.startswith(('holidays.calendars.', "
            "'holidays.countries.', 'holidays.financial.', 'holidays.groups.', "
            "'importlib.metadata'))))"
        )
        self.assertEqual(
            self.run_holidays_code(code),
            str(
                [
                    "holidays.calendars.ethiopian",
                    "holidays.calendars.gregorian",
                    "holidays.calendars.julian",
                    "holidays.calendars.julian_revised",
                    "holidays.countries.canada",
                    "holidays.financial.ny_stock_exchange",
                    "holidays.groups.christian",
                    "holidays.groups.custom",
                    "holidays.groups.international",
                ]
            ),
        )

    def test_lazy_package_loading_attributes_first(self):
        code = (
            "import sys, holidays.countries, holidays.financial; "
            "holidays.countries.Canada; holidays.financial.NYSE; "
            "holidays.country_holidays('CA'); holidays.financial_holidays('XNYS'); "
            "print(sorted(m for m in sys.modules "
            "if m.startswith(('holidays.countries.', 'holidays.financial.'))))"
        )
        self.assertEqual(
            self.run_holidays_code(code),
            str(["holidays.countries.canada", "holidays.financial.ny_stock_exchange"]),
        )
