@ECHO OFF
setlocal EnableDelayedExpansion
pushd %~dp0

REM Command file to generate Sphinx documentation

if "%SPHINXBUILD%" == "" (
    set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=_build

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
    echo.-
    echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
    echo.installed, then set the SPHINXBUILD environment variable to point
    echo.to the full path of the 'sphinx-build' executable. Alternatively you
    echo.may add the Sphinx directory to PATH.
    echo.
    echo.If you don't have Sphinx installed, grab it from
    echo.http://sphinx-doc.org/
    exit /b 1
)

:sphinxbuild
%SPHINXBUILD% -b html %SOURCEDIR% %BUILDDIR% -E -W -j auto -v %SPHINXOPTS% %O%

if %errorlevel% equ 0 (
  start "" "file://%~dp0_build\index.html"
  popd
) else (
  set /p r=Do you want to try again? [Y/n]? || set r=y
  if !r! EQU Y i=y
  echo.
  if !r! EQU y goto sphinxbuild
  popd
  exit /b %errorlevel%
)

:end
exit
