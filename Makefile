help:
	@echo "Usage: make <target>"
	@echo "    check         run pre-commit and tests"
	@echo "    coverage      identify code not covered with tests"
	@echo "    help          show summary of available commands"
	@echo "    install       install and setup development environment"
	@echo "    pot           create or update holidays/locale/pot/*.pot files"
	@echo "    pre-commit    run pre-commit against all files"
	@echo "    test          run tests (in parallel)"
	@echo "    tox           run tox (in parallel)"

check:
	make pre-commit
	make test

coverage:
	pytest --cov=. --cov-config=pyproject.toml --cov-report term-missing --no-cov-on-fail --numprocesses auto

install:
	pip install -U pip
	pip install --requirement requirements/dev.txt
	pip install --requirement requirements/docs.txt
	pre-commit install --hook-type pre-commit
	pre-commit install --hook-type pre-push
	mkdir -p holidays/locale/pot

pot:
	scripts/i18n/generate_po_templates.py

pre-commit:
	pre-commit run --all-files

test:
	pytest --cov=. --cov-config=pyproject.toml --cov-report term --cov-report xml --durations 10 --durations-min=0.75 --no-cov-on-fail --numprocesses auto

tox:
	tox --parallel auto
