# Contributing

## Basics

When contributing with fixes and new features, please start forking/branching from the [dev
branch](https://github.com/vacanza/holidays/tree/dev) to work on the latest code and reduce merging
issues. If you add/change holiday official dates or names, your code must include references to all
sources (government sites, archived web pages, wiki pages, etc.) you've used while working on this
PR. That could be done either as a `References` section update or as a comment on the relevant part
of the code. Contributed [PRs](https://github.com/vacanza/holidays/pulls) are required to include
100% test coverage in order to be merged. Please don't hesitate to ask for help if you need one
with the tests.

Thanks a lot for your support.

## Running tests

First step is setting up the development environment and installing all the required dependencies
with, once you have [`uv`](https://docs.astral.sh/uv/getting-started/installation/#installation-methods) setup:

``` shell
make setup
```

!!! note "WSL Windows File Permission Fix"

    If you're a Windows-based developer setting this up via WSL for the first time and encounter
    file permission errors (e.g., `[Errno 1] Operation not permitted`) where `ls -l` shows files
    owned by root like `-rwxrwxrwx 1 root root ...`, follow these steps:

    **Step 1**: Edit the WSL configuration file:

    ``` shell
    sudo nano /etc/wsl.conf
    ```

    **Step 2**: Add the following section at the bottom of `wsl.conf`, then save (Ctrl+O, Enter) and exit (Ctrl+X):

    ``` ini
    [automount]
    enabled = true
    options = "metadata,umask=22,fmask=11"
    ```

    **Step 3**: Close your WSL session, open PowerShell, then restart WSL:

    ``` powershell
    wsl --shutdown
    wsl ~
    ```

    After this, running `ls -l` on your local `holidays` installation should show:

    ``` console
    drwxr-xr-x 1 username username ...
    ```
    - you're good to go!

The project provides automated style, tests and coverage checks:

``` shell
make check
```

You can run them separately:

``` shell
make pre-commit
make test
```

It'll retrieve uncovered lines too.

You can run specific tests using the `pytest` command:

``` shell
pytest tests/countries/test_argentina.py
```

Or even more granular:

``` shell
pytest tests/countries/test_argentina.py::TestArgentina::test_country_aliases
```

Due to how pytest-xdist is implemented, the -s/--capture=no option [doesn't
work](https://pytest-xdist.readthedocs.io/en/latest/known-limitations.html#output-stdout-and-stderr-from-workers).
Use pytest directly if you need `-s` option:

``` shell
pytest -s tests/countries/test_argentina.py
```

## Localization

In order to add or update existing holiday names translation you'll need to generate pygettext
.pot file first:

``` shell
make l10n
```

If the template file is empty, make sure that the country/market entity has the `default_language`
attribute set, and all holiday names are wrapped with `tr`/`self.tr` helpers. Use [ISO 639-1
codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) when adding new languages. Copy the
generated template to all locale folders you're going to translate this country holiday names into
(e.g., for Argentina: holidays/locale/en/LC_MESSAGES/AR.po - note the file extension difference
here). Also copy the template to a default country language folder (e.g., for Argentina
holidays/locale/es/LC_MESSAGES) and leave it as is. After copying the .po files, open them with
your favorite .po file editor and translate accordingly. Don't forget to fill in the translation
file headers. Finally, update the list of supported translations for the country in the README.md.

If the translation already exists you'll just need to update it with the new template entries
(your .po file editor may help you to do that with no hassle).

Please also add tests (see already translated countries tests for examples). The .mo files are
generated automatically for the tests and the holidays package, so you shouldn't worry about it.
Just don't forget to initialize the `setUpClass` properly:

``` python
@classmethod
def setUpClass(cls):
    super().setUpClass(Argentina)
```

## Build MkDocs Documentation

The project provides MkDocs documentation under `./docs`, published online on
[readthedocs.io](https://holidays.readthedocs.io/).

Great documentation is absolutely key in any project. If you are not familiar with Markdown for
MkDocs, you can read a primer [here](https://www.mkdocs.org/user-guide/writing-your-docs/).

## GitHub Actions

All new GitHub actions must use commit SHAs instead of version tags. When updating an action, contributors should explicitly use the commit SHA from the latest release.

### Example

Allowed:

```yaml
uses: actions/checkout@8fdb40e56baf9c5dc24e3ab5bc2a91db65f39f21
```

Not allowed:

```yaml
uses: actions/checkout@v4
```

## Contributors

In order to keep the list of contributors up to date, we encourage you add your name (in
alphabetical order) to the [CONTRIBUTORS](https://github.com/vacanza/holidays/blob/dev/CONTRIBUTORS)
file if it's not there yet. Thanks for your contribution!

[![contributors](https://img.shields.io/github/contributors/vacanza/holidays)](https://github.com/vacanza/holidays/graphs/contributors)
