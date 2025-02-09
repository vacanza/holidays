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
    RD /S /Q docs\build
    RD /S /Q docs\source\_autosummary
    Exit /B

:Coverage
    pytest --cov=. --cov-config=pyproject.toml --cov-report term-missing --dist loadscope --no-cov-on-fail --numprocesses auto
    Exit /B

:Doc
    sphinx-build -E -T -W -b html -D language=en -j auto -q docs\source docs\build
    Exit /B

:Help
    Echo Usage: make ^<Target^>
    Echo     check         run pre-commit and tests
    Echo     coverage      identify code not covered with tests
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
    python scripts\l10n\generate_po_files.py 2>nul >nul
    python scripts\l10n\generate_mo_files.py
    pre-commit run mixed-line-ending >nul
    Exit /B

:Package
    python scripts\l10n\generate_mo_files.py
    python -m build
    Exit /B

:Pre-commit
    pre-commit run --all-files
    Exit /B

:Release-notes
    python scripts\generate_release_notes.py
    Exit /B

:Sbom
    python -m cyclonedx_py requirements requirements\runtime.txt
    Exit /B

:Setup
    pip install --upgrade pip
    pip install --requirement requirements\dev.txt
    pip install --requirement requirements\docs.txt
    pip install --requirement requirements\runtime.txt
    pip install --requirement requirements\tests.txt
    pre-commit install --hook-type pre-commit
    pre-commit install --hook-type pre-push
    Call :L10n
    Call :Package
    Exit /B

:Snapshot
    python scripts\l10n\generate_mo_files.py
    python scripts\generate_snapshots.py
    Exit /B

:Test
    python scripts\l10n\generate_mo_files.py
    pytest --cov=. --cov-config=pyproject.toml --cov-report term --cov-report xml --durations 10 --durations-min=0.75 --dist loadscope --no-cov-on-fail --numprocesses auto
    Exit /B

:Tox
    tox --parallel auto
    Exit /B
