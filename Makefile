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
	@echo "    tox           run tox (in parallel)"

check:
	make l10n
	make pre-commit
	make doc
	make test

clean:
	@for ext in mo pot pyc; do \
		find . -type f -name "*.$$ext" -delete; \
	done
	@rm -rf .mypy_cache .pytest_cache dist .tox

doc:
	uv run mkdocs build

l10n:
	find . -type f -name "*.pot" -delete
	uv run scripts/l10n/generate_po_files.py 2>/dev/null
	uv run scripts/l10n/generate_mo_files.py

package:
	uv run scripts/l10n/generate_mo_files.py
	uv build

pre-commit:
	uv run pre-commit run --all-files

release-notes:
	uv run scripts/generate_release_notes.py

sbom:
	uv sync --extra build --link-mode=copy
	uv tool run --from cyclonedx-bom cyclonedx-py environment "$(uv python find)"

setup:
	uv venv --clear --python 3.14
	uv sync --extra build --extra dev --extra docs --extra tests --link-mode=copy
	uv run pre-commit install --hook-type pre-commit
	uv run pre-commit install --hook-type pre-push
	make l10n
	make package

snapshot:
	uv run scripts/l10n/generate_mo_files.py
	uv run scripts/generate_snapshots.py

test:
	uv run scripts/l10n/generate_mo_files.py
	uv run pytest --cov=. --cov-config=pyproject.toml --cov-report term-missing --cov-report xml --durations 10 --durations-min=0.75 --dist loadscope --no-cov-on-fail --numprocesses auto

tox:
	uv run tox --parallel auto
