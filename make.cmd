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
    Set CMD=find . -type f \( -name "*.mo" -o -name "*.pot" -o -name "*.pyc" \) -delete ^&^& ^
        rm -rf .cache .mypy_cache .pytest_cache .ruff_cache build dist site
    Call :Docker-run
    Exit /B

:Clean-docker
    docker image rm -f holidays >nul 2>&1
    Exit /B

:Coverage
    Set CMD=pytest --cov-report term-missing --no-cov-on-fail
    Call :Docker-run
    Exit /B

:Doc
    Set CMD=mkdocs build
    Call :Docker-run
    Exit /B

:Docker-build
    Set DOCKER_BUILDKIT=1
    docker buildx use holidays-builder >nul 2>&1 || (
        docker buildx create --use --name holidays-builder
    )
    docker buildx build ^
        --cache-from=type=local,src=./.buildx-cache ^
        --cache-to=type=local,dest=./.buildx-cache ^
        --load ^
        -t holidays ^
        . >nul 2>&1
    Exit /B

:Docker-run
    docker run --rm ^
        --mount type=bind,src=%CD%,dst=/home/user ^
        --platform=linux/amd64 ^
        holidays sh -c "!CMD!"
    Exit /B

:Docker-shell
    docker run --rm ^
	    -it ^
        --mount type=bind,src=%CD%,dst=/home/user ^
        --platform=linux/amd64 ^
        holidays /bin/sh
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
    Exit /B

:L10n
    Set CMD=find . -type f -name "*.pot" -delete ^&^& ^
        scripts/l10n/generate_po_files.py ^> /dev/null 2^>^&1 ^&^& ^
        scripts/l10n/generate_mo_files.py
    Call :Docker-run
    Exit /B

:Package
    Set CMD=scripts/l10n/generate_mo_files.py ^&^& python -m build
    Call :Docker-run
    Exit /B

:Pre-commit
    Set CMD=pre-commit run --all-files
    Call :Docker-run
    Exit /B

:Release-notes
    Set CMD=scripts/generate_release_notes.py
    Call :Docker-run
    Exit /B

:Sbom
    Set CMD=python -m cyclonedx_py requirements requirements/runtime.txt
    Call :Docker-run
    Exit /B

:Setup
    Call :L10n
    Call :Package
    Exit /B

:Snapshot
    Set CMD=scripts/l10n/generate_mo_files.py ^&^& scripts/generate_snapshots.py
    Call :Docker-run
    Exit /B

:Test
    Set CMD=scripts/l10n/generate_mo_files.py ^&^& pytest
    Call :Docker-run
    Exit /B
