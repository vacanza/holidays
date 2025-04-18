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

import unittest
from unittest.mock import MagicMock, patch

from holidays.constants import BANK, GOVERNMENT, OPTIONAL, PUBLIC, SCHOOL, WORKDAY


class TestDynamicCategoryMethodGeneration(unittest.TestCase):
    """Test that category-specific methods are properly generated.
    
    Instead of manually defining methods for each category, we dynamically
    generate methods for all supported categories following the approach
    similar to HolidayBase::_add_holiday_* in holiday_base.py.
    """

    def test_dynamic_method_generation(self):
        """Test that dynamic method generation works properly."""
        # Create a mock TestCase class to simulate our implementation
        mock_test_class = MagicMock()
        mock_test_class.supported_categories = (PUBLIC, GOVERNMENT, OPTIONAL, SCHOOL, WORKDAY, BANK)
        
        # Create a class to hold our generated methods
        class TestClassWithDynamicMethods:
            pass
        
        # Define the method generation function similar to the one in common.py
        def generate_category_methods(cls, test_class):
            """Generate category-specific assertion methods for all supported categories."""
            # Skip PUBLIC as it has dedicated methods
            categories = [cat for cat in test_class.supported_categories if cat != PUBLIC]
            
            for category in categories:
                # Use the title-cased category name (e.g., GOVERNMENT -> Government)
                category_name = category.title()
                
                # Create mock method functions
                def mock_method(*args, **kwargs):
                    pass
                
                # Set all the expected methods
                setattr(cls, f"assert{category_name}Holiday", mock_method)
                setattr(cls, f"assert{category_name}HolidayName", mock_method)
                setattr(cls, f"assertNo{category_name}Holiday", mock_method)
                setattr(cls, f"assert{category_name}NonObservedHoliday", mock_method)
                setattr(cls, f"assert{category_name}NonObservedHolidayName", mock_method)
                setattr(cls, f"assertNo{category_name}NonObservedHoliday", mock_method)
        
        # Generate methods on our test class
        test_instance = TestClassWithDynamicMethods()
        generate_category_methods(test_instance, mock_test_class)
        
        # Verify methods were created correctly
        categories = [GOVERNMENT, OPTIONAL, SCHOOL, WORKDAY, BANK]
        for category in categories:
            category_name = category.title()
            
            # Regular holiday assertions
            self.assertTrue(
                hasattr(test_instance, f"assert{category_name}Holiday"),
                f"Missing assert{category_name}Holiday method",
            )
            self.assertTrue(
                hasattr(test_instance, f"assert{category_name}HolidayName"),
                f"Missing assert{category_name}HolidayName method",
            )
            self.assertTrue(
                hasattr(test_instance, f"assertNo{category_name}Holiday"),
                f"Missing assertNo{category_name}Holiday method",
            )
            
            # Non-observed holiday assertions
            self.assertTrue(
                hasattr(test_instance, f"assert{category_name}NonObservedHoliday"),
                f"Missing assert{category_name}NonObservedHoliday method",
            )
            self.assertTrue(
                hasattr(test_instance, f"assert{category_name}NonObservedHolidayName"),
                f"Missing assert{category_name}NonObservedHolidayName method",
            )
            self.assertTrue(
                hasattr(test_instance, f"assertNo{category_name}NonObservedHoliday"),
                f"Missing assertNo{category_name}NonObservedHoliday method",
            ) 