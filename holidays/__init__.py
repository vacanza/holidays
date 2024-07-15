#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

# flake8: noqa: F403

import warnings

from holidays.constants import *
from holidays.deprecation import (
    FUTURE_INCOMPATIBILITY_WARNING_TEMPLATE,
    FutureIncompatibilityWarning,
)
from holidays.holiday_base import *
from holidays.registry import EntityLoader
from holidays.utils import *

__version__ = "0.53"


EntityLoader.load("ISO_3166", globals())
EntityLoader.load("ISO_10383", globals())

warnings.warn(
    FUTURE_INCOMPATIBILITY_WARNING_TEMPLATE.format(version=__version__),
    FutureIncompatibilityWarning,
)
