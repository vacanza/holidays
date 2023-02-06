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

Contributed PRs_ are required to include valid test coverage **(the goal is
100% coverage)** in order to be merged. Please don't hesitate to ask for
help if you'read struggling with tests.

Thanks a lot for your support.


Running tests
-------------

First step is setting up development environment and installing all the required dependencies with:

.. code-block:: shell

    $ virtualenv -p python3 venv
    $ source venv/bin/activate

    $ make install

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

    $ pytest tests/countries/test_albania.py

Or even more granular:

.. code-block:: shell

    $ pytest tests/countries/test_albania.py::TestAlbania::test_country_aliases

Due to how pytest-xdist is implemented, the -s/--capture=no option
`doesn't work <https://pytest-xdist.readthedocs.io/en/latest/known-limitations.html#output-stdout-and-stderr-from-workers>`_.
Use pytest directly if you need ``-s`` option:

.. code-block:: shell

    $ pytest -s tests/countries/test_albania.py


Build sphinx documentation
--------------------------

.. _readthedocs.io: https://python-holidays.readthedocs.io/

The project provides a Sphinx documentation source under ``./docs/source``,
published online on `readthedocs.io`_.

Great documentation is absolutely key in any a project. If you are not familiar
with reStructuredText for Sphinx you can read a primer
`here`__.

__ https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
