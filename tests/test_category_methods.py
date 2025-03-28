#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.constants import GOVERNMENT, OPTIONAL, PUBLIC, SCHOOL, WORKDAY
from tests.common import CommonCountryTests


class TestCategoryMethodSetup(TestCase):
    """Test that category-specific methods are properly generated."""
    
    def test_category_methods_exist(self):
        """Test that category-specific methods exist."""
        self.assertTrue(hasattr(CommonCountryTests, "assertGovernmentHoliday"))
        self.assertTrue(hasattr(CommonCountryTests, "assertGovernmentHolidayName"))
        self.assertTrue(hasattr(CommonCountryTests, "assertNoGovernmentHoliday"))
        self.assertTrue(hasattr(CommonCountryTests, "assertGovernmentNonObservedHoliday"))
        self.assertTrue(hasattr(CommonCountryTests, "assertGovernmentNonObservedHolidayName"))
        self.assertTrue(hasattr(CommonCountryTests, "assertNoGovernmentNonObservedHoliday"))
        
        self.assertTrue(hasattr(CommonCountryTests, "assertOptionalHoliday"))
        self.assertTrue(hasattr(CommonCountryTests, "assertOptionalHolidayName"))
        self.assertTrue(hasattr(CommonCountryTests, "assertNoOptionalHoliday"))
        self.assertTrue(hasattr(CommonCountryTests, "assertOptionalNonObservedHoliday"))
        self.assertTrue(hasattr(CommonCountryTests, "assertOptionalNonObservedHolidayName"))
        self.assertTrue(hasattr(CommonCountryTests, "assertNoOptionalNonObservedHoliday"))
        
        self.assertTrue(hasattr(CommonCountryTests, "assertSchoolHoliday"))
        self.assertTrue(hasattr(CommonCountryTests, "assertSchoolHolidayName"))
        self.assertTrue(hasattr(CommonCountryTests, "assertNoSchoolHoliday"))
        self.assertTrue(hasattr(CommonCountryTests, "assertSchoolNonObservedHoliday"))
        self.assertTrue(hasattr(CommonCountryTests, "assertSchoolNonObservedHolidayName"))
        self.assertTrue(hasattr(CommonCountryTests, "assertNoSchoolNonObservedHoliday"))
        
        self.assertTrue(hasattr(CommonCountryTests, "assertWorkdayHoliday"))
        self.assertTrue(hasattr(CommonCountryTests, "assertWorkdayHolidayName"))
        self.assertTrue(hasattr(CommonCountryTests, "assertNoWorkdayHoliday"))
        self.assertTrue(hasattr(CommonCountryTests, "assertWorkdayNonObservedHoliday"))
        self.assertTrue(hasattr(CommonCountryTests, "assertWorkdayNonObservedHolidayName"))
        self.assertTrue(hasattr(CommonCountryTests, "assertNoWorkdayNonObservedHoliday"))
        
        self.assertTrue(hasattr(CommonCountryTests, "assertBankHoliday"))
        self.assertTrue(hasattr(CommonCountryTests, "assertBankHolidayName"))
        self.assertTrue(hasattr(CommonCountryTests, "assertNoBankHoliday"))
        self.assertTrue(hasattr(CommonCountryTests, "assertBankNonObservedHoliday"))
        self.assertTrue(hasattr(CommonCountryTests, "assertBankNonObservedHolidayName"))
        self.assertTrue(hasattr(CommonCountryTests, "assertNoBankNonObservedHoliday")) 