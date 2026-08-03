.DEFAULT_GOAL := help

.PHONY: archive-links check clean doc doc-serve help icalendar l10n package \
        pre-commit release-notes sbom setup snapshot test upgrade

# Prefer the project-local uv (pinned via the ci dependency group) when present.
UV = $(if $(wildcard .venv/bin/uv),.venv/bin/uv,uv)
UV_RUN_CMD = $(UV) run --no-sync

help:
	@echo "Usage: make <target>"
	@echo "    archive-links update URLs using Wayback Machine"
	@echo "    check         run pre-commit and tests"
	@echo "    clean         clean development environment"
	@echo "    doc           run documentation build process"
	@echo "    doc-serve     serve documentation locally"
	@echo "    help          show summary of available commands"
	@echo "    icalendar     generate JSON and ICS data files"
	@echo "    l10n          update .pot and .po files"
	@echo "    package       build package distribution"
	@echo "    pre-commit    run pre-commit against all files"
	@echo "    release-notes generate release notes"
	@echo "    sbom          generate CycloneDX SBOM from the built wheel"
	@echo "    setup         setup development environment"
	@echo "    snapshot      generate project snapshots"
	@echo "    test          run tests (in parallel)"
	@echo "    upgrade       run dependency upgrade"

archive-links:
	$(UV_RUN_CMD) scripts/archive_links.py

check:
	$(MAKE) l10n
	$(MAKE) pre-commit
	$(MAKE) doc
	$(MAKE) test

clean:
	@for ext in mo pot pyc; do \
		find . -type f -name "*.$$ext" -delete; \
	done
	@rm -rf .mypy_cache .pytest_cache dist

doc:
	$(UV_RUN_CMD) properdocs build -f .properdocs.yml

doc-serve:
	$(UV_RUN_CMD) properdocs serve -f .properdocs.yml

icalendar:
	$(UV_RUN_CMD) scripts/l10n/generate_mo_files.py
	$(UV_RUN_CMD) scripts/generate_site_assets.py

l10n:
	find . -type f -name "*.pot" -delete
	$(UV_RUN_CMD) scripts/l10n/generate_po_files.py 2>/dev/null
	$(UV_RUN_CMD) scripts/l10n/generate_mo_files.py

package:
	$(UV_RUN_CMD) scripts/l10n/generate_mo_files.py
	$(UV) build

pre-commit:
	$(UV_RUN_CMD) pre-commit run --all-files

release-notes:
	$(UV_RUN_CMD) scripts/generate_release_notes.py

sbom:
	@set -e; \
	version="$$(tr -d '[:space:]' < VERSION)"; \
	wheel="dist/holidays-$${version}-py3-none-any.whl"; \
	if [ ! -f "$$wheel" ]; then \
		echo "No wheel for version $${version} in dist/; run 'make package' first." >&2; \
		exit 1; \
	fi; \
	tools_env="$$(mktemp -d)"; \
	sbom_env="$$(mktemp -d)"; \
	trap 'rm -rf "$$tools_env" "$$sbom_env"' EXIT; \
	UV_PROJECT_ENVIRONMENT="$$tools_env" $(UV) sync --frozen --no-default-groups --only-group ci --no-install-project --no-build >/dev/null; \
	$(UV) venv "$$sbom_env" >/dev/null; \
	$(UV) pip install --python "$$sbom_env" "$$wheel" >/dev/null; \
	UV_PROJECT_ENVIRONMENT="$$tools_env" $(UV_RUN_CMD) -- cyclonedx-py environment "$$sbom_env"

setup:
	@command -v uv >/dev/null 2>&1 || { \
		echo "uv is required to bootstrap the environment:" >&2; \
		echo "  https://docs.astral.sh/uv/getting-started/installation/" >&2; \
		exit 1; \
	}
	# Bootstrap with PATH uv, then switch to the lockfile-pinned uv in .venv.
	uv venv --clear --python 3.14
	uv sync --frozen --only-group ci --no-install-project
	.venv/bin/uv sync --all-groups
	.venv/bin/uv run --no-sync pre-commit install --hook-type pre-commit \
		|| echo "warning: could not install pre-commit hooks (check git core.hooksPath)" >&2
	.venv/bin/uv run --no-sync pre-commit install --hook-type pre-push \
		|| echo "warning: could not install pre-push hooks (check git core.hooksPath)" >&2
	$(MAKE) l10n
	$(MAKE) package

snapshot:
	$(UV_RUN_CMD) scripts/l10n/generate_mo_files.py
	$(UV_RUN_CMD) scripts/generate_snapshots.py

test:
	$(UV_RUN_CMD) scripts/l10n/generate_mo_files.py
	$(UV_RUN_CMD) pytest --cov=. --cov-config=pyproject.toml --cov-report term-missing --cov-report xml --durations 10 --durations-min=0.75 --dist loadscope --no-cov-on-fail --numprocesses auto

upgrade:
	$(UV_RUN_CMD) pre-commit autoupdate
	$(UV) lock --upgrade
	$(UV) sync --all-groups
