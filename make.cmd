@Echo Off
SetLocal EnableDelayedExpansion

Set Target=%1

If "!Target!"=="" (
    GoTo :Help
) Else If "!Target!"=="check" (
    GoTo :Check
) Else If "!Target!"=="clean" (
    GoTo :Clean
) Else If "!Target!"=="coverage" (
    GoTo :Coverage
) Else If "!Target!"=="doc" (
    GoTo :Doc
) Else If "!Target!"=="help" (
    GoTo :Help
) Else If "!Target!"=="l10n" (
    GoTo :L10n
) Else If "!Target!"=="package" (
    GoTo :Package
) Else If "!Target!"=="pre-commit" (
    GoTo :Precommit
) Else If "!Target!"=="release-notes" (
    GoTo :Releasenotes
) Else If "!Target!"=="sbom" (
    GoTo :Sbom
) Else If "!Target!"=="setup" (
    GoTo :Setup
) Else If "!Target!"=="snapshot" (
    GoTo :Snapshot
) Else If "!Target!"=="test" (
    GoTo :Test
) Else If "!Target!"=="tox" (
    GoTo :Tox
) Else (
    GoTo :Help
)

:Check
    Call :L10n
    Call :Precommit
    Call :Doc
    Call :Test
    GoTo :EOF

:Clean
    Del /S /Q *.mo
    Del /S /Q *.pyc
    RD /S /Q .mypy_cache
    RD /S /Q .pytest_cache
    RD /S /Q dist
    RD /S /Q docs\build
    RD /S /Q docs\source\_autosummary
    GoTo :EOF

:Coverage
    pytest --cov=. --cov-config=pyproject.toml --cov-report term-missing --dist loadscope --no-cov-on-fail --numprocesses auto
    GoTo :EOF

:Doc
    sphinx-build -E -T -W -b html -D language=en -j auto -q docs\source docs\build
    GoTo :EOF

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
    GoTo :EOF

:L10n
    python scripts\l10n\generate_po_files.py 2>nul >nul
    python scripts\l10n\generate_mo_files.py
    pre-commit run mixed-line-ending >nul
    GoTo :EOF

:Package
    python scripts\l10n\generate_mo_files.py
    python -m build
    GoTo :EOF

:Precommit
    pre-commit run --all-files
    GoTo :EOF

:Releasenotes
    python scripts\generate_release_notes.py
    GoTo :EOF

:Sbom
    python -m cyclonedx_py requirements requirements\runtime.txt
    GoTo :EOF

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
    GoTo :EOF

:Snapshot
    python scripts\l10n\generate_mo_files.py
    python scripts\generate_snapshots.py
    GoTo :EOF

:Test
    python scripts\l10n\generate_mo_files.py
    pytest --cov=. --cov-config=pyproject.toml --cov-report term --cov-report xml --durations 10 --durations-min=0.75 --dist loadscope --no-cov-on-fail --numprocesses auto
    GoTo :EOF

:Tox
    tox --parallel auto
    GoTo :EOF
