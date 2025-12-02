@Echo Off
SetLocal EnableDelayedExpansion

Set Target=%~1

Set Targets=
For /F "Delims=:" %%I in ('FindStr /R "^:" "%~f0"') Do Set Targets=!Targets! %%I
For %%A in (!Targets!) Do (
    If /I "%Target%"=="%%A" Call :%%A & Exit /B
)
GoTo :Help

:Check
    Call :L10n
    Call :Pre-commit
    Call :Doc
    Call :Test
    Exit /B

:Clean
    Del /S /Q *.mo
    Del /S /Q *.pyc
    RD /S /Q .mypy_cache
    RD /S /Q .pytest_cache
    RD /S /Q dist
    Exit /B

:Doc
    uv run mkdocs build
    Exit /B

:Help
    Echo Usage: make ^<Target^>
    Echo     check         run pre-commit and tests
    Echo     doc           run documentation build process
    Echo     help          show summary of available commands
    Echo     l10n          update .pot and .po files
    Echo     package       build package distribution
    Echo     pre-commit    run pre-commit against all files
    Echo     setup         setup development environment
    Echo     test          run tests (in parallel)
    Echo     tox           run tox (in parallel)
    Exit /B

:L10n
    uv run python scripts\l10n\generate_po_files.py 2>nul >nul
    uv run python scripts\l10n\generate_mo_files.py
    Exit /B

:Package
    uv run python scripts\l10n\generate_mo_files.py
    uv build
    Exit /B

:Pre-commit
    uv run pre-commit run --all-files
    Exit /B

:Release-notes
    uv run python scripts\generate_release_notes.py
    Exit /B

:Sbom
    uv sync --extra build
    uv run python -m cyclonedx_py
    Exit /B

:Setup
    uv venv --clear
    uv sync --extra build --extra dev --extra docs --extra tests --link-mode=copy
    uv run pre-commit install --hook-type pre-commit
    uv run pre-commit install --hook-type pre-push
    Call :L10n
    Call :Package
    Exit /B

:Snapshot
    uv run python scripts\l10n\generate_mo_files.py
    uv run python scripts\generate_snapshots.py
    Exit /B

:Test
    uv run python scripts\l10n\generate_mo_files.py
    uv run pytest --cov=. --cov-config=pyproject.toml --cov-report term-missing --cov-report xml --durations 10 --durations-min=0.75 --dist loadscope --no-cov-on-fail --numprocesses auto
    Exit /B

:Tox
    uv run tox --parallel auto
    Exit /B
