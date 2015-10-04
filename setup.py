#  holidays.py
#  -----------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com>
#  Website: https://github.com/ryanss/holidays.py
#  License: MIT (see LICENSE file)
#  Version: 0.4 (October 4, 2015)


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='holidays',
    version='0.4',
    author='ryanss',
    author_email='ryanssdev@icloud.com',
    url='https://github.com/ryanss/holidays.py',
    bugtrack_url='https://github.com/ryanss/holidays.py/issues',
    license='MIT',
    py_modules=['holidays'],
    description='Generate and work with holidays in Python',
    long_description=open('README.rst').read(),
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
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization',
    ],
)
