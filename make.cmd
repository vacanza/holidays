@Echo Off
SetLocal EnableDelayedExpansion

Set Target=%~1

If Exist .venv\Scripts\uv.exe (
    Set "UV=.venv\Scripts\uv.exe"
) Else (
    Set "UV=uv"
)
Set "UV_RUN_CMD=!UV! run --no-sync"

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
    Echo     sbom          generate CycloneDX SBOM from the built wheel
    Echo     setup         setup development environment
    Echo     snapshot      generate project snapshots
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
    %UV% build
    Exit /B

:Pre-commit
    %UV_RUN_CMD% pre-commit run --all-files
    Exit /B

:Release-notes
    %UV_RUN_CMD% scripts\generate_release_notes.py
    Exit /B

:Sbom
    Set /P VERSION=<VERSION
    Set "WHEEL=dist\holidays-!VERSION!-py3-none-any.whl"
    If Not Exist "!WHEEL!" (
        Echo No wheel for version !VERSION! in dist/; run 'make package' first. 1>&2
        Exit /B 1
    )
    Set "TOOLS_ENV=%TEMP%\holidays-sbom-tools-%RANDOM%"
    Set "SBOM_ENV=%TEMP%\holidays-sbom-%RANDOM%"
    Set "SBOM_ERROR=0"

    Set "UV_PROJECT_ENVIRONMENT=!TOOLS_ENV!"
    %UV% sync --frozen --no-default-groups --only-group ci --no-install-project --no-build >nul
    Set "SBOM_ERROR=!ErrorLevel!"
    Set "UV_PROJECT_ENVIRONMENT="
    If Not "!SBOM_ERROR!"=="0" Goto :SbomDone

    %UV% venv "!SBOM_ENV!" >nul
    Set "SBOM_ERROR=!ErrorLevel!"
    If Not "!SBOM_ERROR!"=="0" Goto :SbomDone

    %UV% pip install --python "!SBOM_ENV!" "!WHEEL!" >nul
    Set "SBOM_ERROR=!ErrorLevel!"
    If Not "!SBOM_ERROR!"=="0" Goto :SbomDone

    Set "UV_PROJECT_ENVIRONMENT=!TOOLS_ENV!"
    %UV% run --frozen --no-sync -- cyclonedx-py environment "!SBOM_ENV!"
    Set "SBOM_ERROR=!ErrorLevel!"
    Set "UV_PROJECT_ENVIRONMENT="

:SbomDone
    Set "UV_PROJECT_ENVIRONMENT="
    If Exist "!TOOLS_ENV!" RD /S /Q "!TOOLS_ENV!"
    If Exist "!SBOM_ENV!" RD /S /Q "!SBOM_ENV!"
    Exit /B !SBOM_ERROR!

:Setup
    where uv >nul 2>&1
    If ErrorLevel 1 (
        Echo uv is required to bootstrap the environment:
        Echo   https://docs.astral.sh/uv/getting-started/installation/
        Exit /B 1
    )
    Rem Bootstrap with PATH uv, then switch to the lockfile-pinned uv in .venv.
    uv venv --clear --python 3.14
    uv sync --frozen --only-group ci --no-install-project
    Set "UV=.venv\Scripts\uv.exe"
    Set "UV_RUN_CMD=!UV! run --no-sync"
    !UV! sync --all-groups
    !UV_RUN_CMD! pre-commit install --hook-type pre-commit
    If ErrorLevel 1 Echo warning: could not install pre-commit hooks (check git core.hooksPath) 1>&2
    !UV_RUN_CMD! pre-commit install --hook-type pre-push
    If ErrorLevel 1 Echo warning: could not install pre-push hooks (check git core.hooksPath) 1>&2
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
    %UV_RUN_CMD% pre-commit autoupdate
    %UV% lock --upgrade
    %UV% sync --all-groups
    Exit /B
