============
Contributing
============

.. _prs: https://github.com/vacanza/python-holidays/pulls
.. _`dev branch`: https://github.com/vacanza/python-holidays/tree/dev


Basics
------

When contributing with fixes and new features, please start forking/branching
from the `dev branch`_ to work on the latest code and reduce merging issues.
If you add/change holiday official dates or names you must include references to
all sources (government sites, archived web pages, wiki pages, etc) you've used
while working on this PR. Contributed PRs_ are required to include valid test
coverage in order to be merged. Please don't hesitate to ask for help if you
need one with the tests.

Thanks a lot for your support.


Running tests
-------------

First step is setting up development environment and installing all the required dependencies with:

.. code-block:: shell

    $ virtualenv -p python3 venv
    $ source venv/bin/activate

    $ make setup

The project provides automated style, tests and coverage checks:

.. code-block:: shell

    $ make check

You can run them separately:

.. code-block:: shell

    $ make pre-commit
    $ make test

If you want to retrieve uncovered lines too:

.. code-block:: shell

    $ make coverage

You can specific tests using ``pytest`` command:

.. code-block:: shell

    $ pytest tests/countries/test_argentina.py

Or even more granular:

.. code-block:: shell

    $ pytest tests/countries/test_argentina.py::TestArgentina::test_country_aliases

Due to how pytest-xdist is implemented, the -s/--capture=no option
`doesn't work <https://pytest-xdist.readthedocs.io/en/latest/known-limitations.html#output-stdout-and-stderr-from-workers>`_.
Use pytest directly if you need ``-s`` option:

.. code-block:: shell

    $ pytest -s tests/countries/test_argentina.py


Localization
------------
.. _ISO 639-1 codes: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

In order to add or update existing holiday names translation you'll need to
generate pygettext .pot file first:

.. code-block:: shell

    $ make l10n

If the template file is empty make sure that the country/market entity has the
``default_language`` attribute set and all holiday names are wrapped
with ``tr``/``self.tr`` helpers. Use `ISO 639-1 codes`_ when adding new
languages. Copy the generated template to all locale folders you're going to
translate this country holiday names into (e.g., for Argentina:
holidays/locale/en/LC_MESSAGES/AR.po - note the file extension difference here).
Also copy the template to a default country language folder (e.g., for Argentina
holidays/locale/es/LC_MESSAGES) and leave it as is. After copying the .po files
open them with your favorite .po file editor and translate accordingly. Don't
forget to fill in the translation file headers. Finally, update the list of
supported translations for the country in the README.rst.

If the translation already exists you'll just need to update it with the new
template entries (your .po file editor may help you to do that with no hassle).

Please also add tests (see already translated countries tests for examples).
The .mo files are generated automatically for the tests and the python-holidays
package so you shouldn't worry about it. Just don't forget to
initialize the ``setUpClass`` properly:

.. code-block:: python

    @classmethod
    def setUpClass(cls):
        super().setUpClass(Argentina)


Build sphinx documentation
--------------------------

.. _readthedocs.io: https://python-holidays.readthedocs.io/

The project provides a Sphinx documentation source under ``./docs/source``,
published online on `readthedocs.io`_.

Great documentation is absolutely key in any a project. If you are not familiar
with reStructuredText for Sphinx you can read a primer
`here`__.

__ https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html


Contributors
------------

.. __: https://github.com/vacanza/python-holidays/blob/dev/AUTHORS
.. |contributors| image:: https://img.shields.io/github/contributors/vacanza/python-holidays
    :target: https://github.com/vacanza/python-holidays/graphs/contributors
    :alt: contributors

In order to keep the list of contributors up to date we encourage you add your
name (in alphabetical order) to the `AUTHORS`__ file if it's not there yet.
Thanks for your contribution!

|contributors|
