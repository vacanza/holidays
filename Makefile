.DEFAULT_GOAL := help

.PHONY: archive-links check clean doc doc-serve help icalendar l10n package \
        pre-commit release-notes sbom setup snapshot test upgrade

UV_RUN_CMD = uv run --no-sync

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
	@echo "    sbom          generate CycloneDX SBOM"
	@echo "    setup         setup development environment"
	@echo "    test          run tests (in parallel)"
	@echo "    upgrade       run dependency upgrade"

archive-links:
	$(UV_RUN_CMD) scripts/archive_links.py

check:
	make l10n
	make pre-commit
	make doc
	make test

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
	uv build

pre-commit:
	$(UV_RUN_CMD) pre-commit run --all-files

release-notes:
	$(UV_RUN_CMD) scripts/generate_release_notes.py

sbom:
	uv tool run --from cyclonedx-bom cyclonedx-py environment "$(uv python find)"

setup:
	uv venv --clear --python 3.14
	uv sync --all-groups
	$(UV_RUN_CMD) pre-commit install --hook-type pre-commit
	$(UV_RUN_CMD) pre-commit install --hook-type pre-push
	make l10n
	make package

snapshot:
	$(UV_RUN_CMD) scripts/l10n/generate_mo_files.py
	$(UV_RUN_CMD) scripts/generate_snapshots.py

test:
	$(UV_RUN_CMD) scripts/l10n/generate_mo_files.py
	$(UV_RUN_CMD) pytest --cov=. --cov-config=pyproject.toml --cov-report term-missing --cov-report xml --durations 10 --durations-min=0.75 --dist loadscope --no-cov-on-fail --numprocesses auto

upgrade:
	pre-commit autoupdate
	uv lock --upgrade
	uv sync --all-groups
