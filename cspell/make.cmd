@echo off
setlocal enabledelayedexpansion

set TARGET=%1

if "%TARGET%"=="cspell-check" goto cspell-check
if "%TARGET%"=="cspell-install" goto cspell-install
if "%TARGET%"=="cspell-run" goto cspell-run

echo Usage: make.cmd ^<target^>
echo     cspell-check    run cspell check
echo     cspell-install  install cspell docker image
echo     cspell-run      run cspell (placeholder)
goto end

:cspell-install
where docker-credential-desktop >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: docker-credential-desktop not found in PATH.
    echo Please add Docker's bin directory to your PATH.
    echo Typically: set PATH=%%PATH%%;C:\Program Files\Docker\Docker\resources\bin
    echo Or reinstall Docker Desktop to fix credential helper.
    goto end
)
set "DOCKER_BUILDKIT=true" && docker build -f cspell/Dockerfile cspell -t cspell
goto end

:cspell-run
rem Placeholder for cspell-run
goto end

:cspell-check
call :cspell-install
call :cspell-run
docker run --mount type=bind,src="%CD%",dst=/holidays --rm cspell lint -c cspell/cspell.json --no-progress -r /holidays
goto end

:end
