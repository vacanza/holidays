@Echo Off
SetLocal EnableDelayedExpansion

Set Target=%~1
Set UV_RUN_CMD=uv run --no-sync

Set Targets=
For /F "Delims=:" %%I in ('FindStr /R "^:" "%~f0"') Do Set Targets=!Targets! %%I
For %%A in (!Targets!) Do (
    If /I "%Target%"=="%%A" Call :%%A & Exit /B
)
GoTo :Help

:Archive-links
    %UV_RUN_CMD% scripts\archive_links.py
    Exit /B

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
    %UV_RUN_CMD% properdocs build -f .properdocs.yml
    Exit /B

:Doc-serve
    %UV_RUN_CMD% properdocs serve -f .properdocs.yml
    Exit /B

:Help
    Echo Usage: make ^<Target^>
    Echo     archive-links update URLs using Wayback Machine
    Echo     check         run pre-commit and tests
    Echo     clean         clean development environment
    Echo     doc           run documentation build process
    Echo     doc-serve     serve documentation locally
    Echo     help          show summary of available commands
    Echo     icalendar     generate JSON and ICS data files
    Echo     l10n          update .pot and .po files
    Echo     package       build package distribution
    Echo     pre-commit    run pre-commit against all files
    Echo     release-notes generate release notes
    Echo     sbom          generate CycloneDX SBOM
    Echo     setup         setup development environment
    Echo     test          run tests (in parallel)
    Echo     upgrade       run dependency upgrade
    Exit /B

:Icalendar
    %UV_RUN_CMD% scripts\l10n\generate_mo_files.py
    %UV_RUN_CMD% scripts\generate_site_assets.py
    Exit /B

:L10n
    %UV_RUN_CMD% scripts\l10n\generate_po_files.py 2>nul >nul
    %UV_RUN_CMD% scripts\l10n\generate_mo_files.py
    Exit /B

:Package
    %UV_RUN_CMD% scripts\l10n\generate_mo_files.py
    uv build
    Exit /B

:Pre-commit
    %UV_RUN_CMD% pre-commit run --all-files
    Exit /B

:Release-notes
    %UV_RUN_CMD% scripts\generate_release_notes.py
    Exit /B

:Sbom
    For /F "Delims=" %%P in ('uv python find') Do Set PYTHON_PATH=%%P
    uv tool run --from cyclonedx-bom cyclonedx-py environment "!PYTHON_PATH!"
    Exit /B

:Setup
    uv venv --clear --python 3.14
    uv sync --all-groups
    %UV_RUN_CMD% pre-commit install --hook-type pre-commit
    %UV_RUN_CMD% pre-commit install --hook-type pre-push
    Call :L10n
    Call :Package
    Exit /B

:Snapshot
    %UV_RUN_CMD% scripts\l10n\generate_mo_files.py
    %UV_RUN_CMD% scripts\generate_snapshots.py
    Exit /B

:Test
    %UV_RUN_CMD% scripts\l10n\generate_mo_files.py
    %UV_RUN_CMD% pytest --cov=. --cov-config=pyproject.toml --cov-report term-missing --cov-report xml --durations 10 --durations-min=0.75 --dist loadscope --no-cov-on-fail --numprocesses auto
    Exit /B

:Upgrade
    uv lock --upgrade
    uv sync --all-groups
