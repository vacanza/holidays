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
    Del /S /Q *.pot
    Del /S /Q *.pyc
    RD /S /Q .mypy_cache
    RD /S /Q .pytest_cache
    RD /S /Q dist
    Exit /B

:Doc
    uv run --no-sync mkdocs build
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
    Echo     upgrade       run dependency upgrade
    Exit /B

:L10n
    uv run --no-sync scripts\l10n\generate_po_files.py 2>nul >nul
    uv run --no-sync scripts\l10n\generate_mo_files.py
    Exit /B

:Package
    uv run --no-sync scripts\l10n\generate_mo_files.py
    uv build
    Exit /B

:Pre-commit
    uv run --no-sync pre-commit run --all-files
    Exit /B

:Release-notes
    uv run --no-sync scripts\generate_release_notes.py
    Exit /B

:Sbom
    For /F "Delims=" %%P in ('uv python find') Do Set PYTHON_PATH=%%P
    uv tool run --from cyclonedx-bom cyclonedx-py environment "!PYTHON_PATH!"
    Exit /B

:Setup
    uv venv --clear --python 3.14
    uv sync --all-groups
    uv run --no-sync pre-commit install --hook-type pre-commit
    uv run --no-sync pre-commit install --hook-type pre-push
    Call :L10n
    Call :Package
    Exit /B

:Snapshot
    uv run --no-sync scripts\l10n\generate_mo_files.py
    uv run --no-sync scripts\generate_snapshots.py
    Exit /B

:Test
    uv run --no-sync scripts\l10n\generate_mo_files.py
    uv run --no-sync pytest --cov=. --cov-config=pyproject.toml --cov-report term-missing --cov-report xml --durations 10 --durations-min=0.75 --dist loadscope --no-cov-on-fail --numprocesses auto
    Exit /B

Upgrade:
    uv lock --upgrade
    uv sync --all-groups
