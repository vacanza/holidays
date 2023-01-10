============
Contributing
============

.. _prs: https://github.com/dr-prodigy/python-holidays/pulls
.. _`beta branch`: https://github.com/dr-prodigy/python-holidays/tree/beta
.. |contributors| image:: https://img.shields.io/github/contributors/dr-prodigy/python-holidays
    :target: https://www.github.com/dr-prodigy/python-holidays
    :alt: contributors

|contributors|


Basics
------

When contributing with fixes and new features, please start forking/branching
from the `beta branch`_ to work on the latest code and reduce merging issues.

Contributed PRs_ are required to include valid test coverage **(95% minimum,
100% whenever possible)** in order to be merged.

Thanks a lot for your support.


Running tests
-------------

First step is installing all the required dependencies with:

.. code-block:: bash

    $ pip install -r requirements_dev.txt

The project provides automated tests and coverage checks with tox; just run:

.. code-block:: bash

    $ tox

Alternatively, you can run pytest to run tests and coverage:

.. code-block:: bash

    $ python -m pytest .
    # if you want to retrieve uncovered lines too:
    $ python -m pytest --cov-report term-missing .

In addition to pytest, you need to ensure that all staged files are up to
standard.

.. _pre-commit: https://github.com/dr-prodigy/python-holidays/issues

Install `pre-commit`_ and its git hook script so that the quality assurance
tests will run on all staged files before they are committed:

.. code-block:: bash

    $ pip install pre-commit
    $ pre-commit install

To manually run the quality assurance tests on all tracked files:

.. code-block:: bash

    $ pre-commit run -a


Internationalization
--------------------------
.. _ISO 639-1 codes: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

In order to add or update existing holiday names translation you'll need to
generate pygettext .pot file first:

.. code-block:: bash

    $ mkdir holidays/locale/pot
    $ pygettext -k 'tr' -o holidays/locale/pot/AR.pot holidays/countries/argentina.py

If the template file is empty make sure that the holiday names are wrapped
with ``tr``/``self.tr`` helpers. Use `ISO 639-1 codes`_ when adding new
languages. Copy the generated template to all locale folders you're going to
translate this country holiday names into (e.g. for Argentina:
holidays/locale/en/LC_MESSAGES/AR.po - note the file extension difference here).
Also copy the template to a default country language folder (e.g. for Argentina
holidays/locale/es/LC_MESSAGES) and leave it as is. After copying the .po file open
them with your favorite .po file editor and translate accordingly. Don't
forget to fill in the translation file header fields.

If the translation already exists you'll just need to update it with the new
template entries (your .po file editor may help you to do that with no hassle).
In case it's a new translation please also add tests (see already translated
countries tests for examples). Update the list of country supported
translations in README.rst file.

The .mo files are generated automatically for the tests (don't forget to
initialize the ``setUpClass`` properly) and the python-holidays package so you
shouldn't worry about it.

Build sphinx documentation
--------------------------

.. _readthedocs.io: https://python-holidays.readthedocs.io/

The project provides a Sphinx documentation source under ``./docs/source``,
published online on `readthedocs.io`_.

Great documentation is absolutely key in any a project. If you are not familiar
with reStructuredText for Sphinx you can read a primer
`here`__.

__ https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
