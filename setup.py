#  holidays.py
#  -----------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com>
#  Website: https://github.com/ryanss/holidays.py
#  License: MIT (see LICENSE file)
#  Version: 0.5 (September 5, 2016)


import codecs
import os
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


base_dir = os.path.dirname(os.path.abspath(__file__))

def get_version(filename="holidays.py"):
    with codecs.open(os.path.join(base_dir, filename), encoding="utf-8") as initfile:
        for line in initfile.readlines():
            m = re.match("__version__ *= *['\"](.*)['\"]", line)
            if m:
                return m.group(1)


setup(
    name='holidays',
    version=get_version(),
    author='ryanss',
    author_email='ryanssdev@icloud.com',
    url='https://github.com/ryanss/holidays.py',
    bugtrack_url='https://github.com/ryanss/holidays.py/issues',
    license='MIT',
    py_modules=['holidays'],
    description='Generate and work with holidays in Python',
    long_description=codecs.open('README.rst', encoding='utf-8').read(),
    install_requires=['python-dateutil'],
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization',
    ],
)
