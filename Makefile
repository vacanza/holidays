help:
	@echo "Usage: make <target>"
	@echo "    check         run pre-commit and tests"
	@echo "    doc           run documentation build process"
	@echo "    help          show summary of available commands"
	@echo "    l10n          update .pot and .po files"
	@echo "    package       build package distribution"
	@echo "    pre-commit    run pre-commit against all files"
	@echo "    setup         setup development environment"
	@echo "    test          run tests (in parallel)"
	@echo "    upgrade       run dependency upgrade"

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
	uv run --no-sync mkdocs build

l10n:
	find . -type f -name "*.pot" -delete
	uv run --no-sync scripts/l10n/generate_po_files.py 2>/dev/null
	uv run --no-sync scripts/l10n/generate_mo_files.py

package:
	uv run --no-sync scripts/l10n/generate_mo_files.py
	uv build

pre-commit:
	uv run --no-sync pre-commit run --all-files

release-notes:
	uv run --no-sync scripts/generate_release_notes.py

sbom:
	uv tool run --from cyclonedx-bom cyclonedx-py environment "$(uv python find)"

setup:
	uv venv --clear --python 3.14
	uv sync --all-groups
	uv run --no-sync pre-commit install --hook-type pre-commit
	uv run --no-sync pre-commit install --hook-type pre-push
	make l10n
	make package

snapshot:
	uv run --no-sync scripts/l10n/generate_mo_files.py
	uv run --no-sync scripts/generate_snapshots.py

test:
	uv run --no-sync scripts/l10n/generate_mo_files.py
	uv run --no-sync pytest --cov=. --cov-config=pyproject.toml --cov-report term-missing --cov-report xml --durations 10 --durations-min=0.75 --dist loadscope --no-cov-on-fail --numprocesses auto

upgrade:
	uv lock --upgrade
	uv sync --all-groups
