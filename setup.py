#  holidays.py
#  -----------
#  A fast, efficient Python library for generating country-specific lists of
#  holidays on the fly which aims to make determining whether a specific date
#  is a hoiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com>
#  Website: https://github.com/ryanss/holidays.py
#  License: MIT (see LICENSE file)


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import holidays


setup(
    name='holidays',
    version=holidays.__version__,
    author='ryanss',
    author_email='ryanssdev@icloud.com',
    url='https://github.com/ryanss/holidays.py',
    license='MIT',
    py_modules=['holidays'],
    description='Generates country-specific lists of statutory holidays',
    long_description=open('README.rst').read(),
    install_requires=['python-dateutil'],
    platforms='any',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization',
    ],
)
