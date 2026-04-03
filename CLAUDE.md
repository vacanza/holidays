# holidays

A fast, efficient Python library for generating country, province and state specific sets of
holidays on the fly. It aims to make determining whether a specific date is a holiday as fast
and flexible as possible.

## Project Overview

- **Primary Language:** Python
- **Other Languages:** JavaScript
- **Package Manager:** uv

## Project Structure

```text
.github/
docs/
holidays/
scripts/
snapshots/
tests/
```

## Key Commands

- **Setup:** `make setup`
- **Install:** `uv sync`
- **Test:** `make test` (runs `uv run pytest` in parallel)
- **Lint & Format:** `make pre-commit` (runs all pre-commit hooks: ruff, isort, mypy, license headers)
- **Full Check:** `make check` (l10n + pre-commit + docs + tests)

## Code Style

- Follow PEP 8 style guidelines
- Line length limit: 99 characters
- Use f-strings for string formatting
- Use type hints for function parameters and return values
- Country `_populate_*` methods omit explicit `-> None` return annotations (project convention)
- Primary linter: **ruff** (configured in `pyproject.toml` under `[tool.ruff]`)
- Import sorting: **isort** with `profile = "black"` and `known_first_party = ["holidays", "tests"]`
- Type checking: **mypy**

## License Header

All `.py` and `.po` files must include the standard license header at the top (enforced by
pre-commit via `insert-license`). The header template is in `docs/file_header.txt`:

```text
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
```

Do NOT add module-level docstrings to country files (`holidays/countries/`), calendar files
(`holidays/calendars/`), or test files (`tests/`). The license header serves as the file header.

## Conventions

### Country Implementations

- Each country is a class inheriting from `HolidayBase` plus mixin groups (e.g., `ChristianHolidays`, `InternationalHolidays`, `StaticHolidays`)
- Holiday logic lives in `_populate_public_holidays()`, `_populate_subdiv_<code>_public_holidays()`, etc.
- Use `self._year` for the current year being populated
- Use `tr()` (from `gettext`) for translatable holiday names
- Import month/day constants from `holidays.calendars.gregorian` (e.g., `JAN`, `FEB`, `MAR`)
- Import holiday categories from `holidays.constants` (e.g., `PUBLIC`, `CATHOLIC`)
- Do NOT define `__all__` in country modules
- Include references to official sources (government sites, archived web pages) in class docstrings

### Test Files

- Use direct imports: `from holidays.countries.<country> import <CountryClass>`
- Import shared test infrastructure: `from tests.common import CommonCountryTests`
- Test classes inherit from both `CommonCountryTests` and `unittest.TestCase`
- PRs require 100% test coverage to be merged

### General

- All PRs must pass CI before merging
- Run `make pre-commit` before committing to catch formatting and linting issues
- Write tests for new features and bug fixes
- Read CONTRIBUTING.md before making changes
- Update documentation when changing public APIs
- Keep commits focused and atomic
- Write clear commit messages describing the "why"
- Branch from `dev` (not `main`) for contributions

## Architecture

- `holidays/holiday_base.py` — Core `HolidayBase` class with `_populate()` method
- `holidays/countries/` — One file per country, each defining a `HolidayBase` subclass
- `holidays/calendars/` — Calendar systems (Gregorian, Islamic, Hindu, etc.)
- `holidays/groups/` — Mixin classes for holiday groups (Christian, Islamic, International, etc.)
- `holidays/financial/` — Financial market holidays
- `tests/countries/` — One test file per country
- `snapshots/` — Holiday data snapshots for regression testing

## Important Notes

- Read existing code before making changes to understand patterns
- Follow the existing project structure and naming conventions
- Run `make pre-commit` after making changes to ensure code passes all checks
- Ensure code passes linting before committing
- All changes must pass CI checks
