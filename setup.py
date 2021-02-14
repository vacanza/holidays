#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import codecs
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with codecs.open('holidays/__init__.py', 'r', 'utf-8') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='holidays',
    version=version,
    author='ryanss',
    author_email='ryanssdev@icloud.com',
    maintainer='dr-prodigy',
    maintainer_email='maurizio.montel@gmail.com',
    url='https://github.com/dr-prodigy/python-holidays',
    packages=['holidays', 'holidays/countries'],
    license='MIT',
    description='Generate and work with holidays in Python',
    long_description=codecs.open('README.rst', encoding='utf-8').read(),
    install_requires=['python-dateutil', 'six', 'convertdate>=2.3.0',
                      'korean_lunar_calendar', 'hijri_converter'],
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization',
    ],
)
