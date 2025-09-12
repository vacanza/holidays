@echo off
setlocal enabledelayedexpansion

set TARGET=%1

if "%TARGET%"=="cspell-check" goto cspell-check
if "%TARGET%"=="cspell-install" goto cspell-install
if "%TARGET%"=="cspell-run" goto cspell-run
if "%TARGET%"=="sort-custom-dict" goto sort-custom-dict

echo Usage: make.cmd ^<target^>
echo     cspell-check      run cspell check
echo     cspell-install    install cspell docker image
echo     cspell-run        run cspell (placeholder)
echo     sort-custom-dict  sort and uniquify custom-dict.txt
goto end

:cspell-install
where docker >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: docker not found in PATH. Install Docker Desktop or add docker.exe to PATH.
    goto end
)
set "build_args="
if defined FORCE set "build_args=--no-cache"
set "DOCKER_BUILDKIT=true" && docker build %build_args% -f cspell/Dockerfile -t cspell cspell
goto end

:cspell-run
rem Placeholder for cspell-run
goto end

:sort-custom-dict
python tools/sort_cspell_dict.py
goto end

:cspell-check
set CMD=--no-progress -r /holidays
call :cspell-install
call :cspell-run
docker run --mount type=bind,src="%CD%",dst=/holidays,readonly --rm cspell lint -c cspell/cspell.json %CMD%
goto end

:end
