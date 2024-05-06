""" Generic unit tests for the module. """
import unittest
import holidays

class TestModuleGeneric(unittest.TestCase):
    """ Generic tests of the module for python 3.6 """
    def test_nyse(self):
        """Test saving security items and loading them from the repository"""

        test_cases = {
            "success": {
                "year": 2021,
                "expectedErr": None,
            }
        }
        
        for key, case in test_cases.items():
            with self.subTest(key=key):
                if case["expectedErr"]:
                    with self.assertRaises(case["expectedErr"]):
                        holidays.NYSE(years=case.get("year"))
                        
                else:
                    holidays.NYSE(years=case.get("year"))
                    
    def test_us(self):
        """Test saving security items and loading them from the repository"""

        test_cases = {
            "success": {
                "year": 2021,
                "expectedErr": None,
            }
        }
        
        for key, case in test_cases.items():
            with self.subTest(key=key):
                if case["expectedErr"]:
                    with self.assertRaises(case["expectedErr"]):
                        holidays.US(years=case.get("year"))
                        
                else:
                    holidays.US(years=case.get("year"))
                    
    def test_india(self):
        """Test saving security items and loading them from the repository"""

        test_cases = {
            "success": {
                "year": 2021,
                "expectedErr": None,
            }
        }
        
        for key, case in test_cases.items():
            with self.subTest(key=key):
                if case["expectedErr"]:
                    with self.assertRaises(case["expectedErr"]):
                        holidays.India(years=case.get("year"))
                        
                else:
                    holidays.India(years=case.get("year"))
                    
    def test_bolivia(self):
        """Test saving security items and loading them from the repository"""

        test_cases = {
            "success": {
                "year": 2021,
                "expectedErr": None,
            }
        }
        
        for key, case in test_cases.items():
            with self.subTest(key=key):
                if case["expectedErr"]:
                    with self.assertRaises(case["expectedErr"]):
                        holidays.Bolidvia(years=case.get("year"))
                        
                else:
                    holidays.Bolivia(years=case.get("year"))
                    
        
    def test_Tunisia(self):
        """Test saving security items and loading them from the repository"""

        test_cases = {
            "success": {
                "year": 2021,
                "expectedErr": None,
            }
        }
        
        for key, case in test_cases.items():
            with self.subTest(key=key):
                if case["expectedErr"]:
                    with self.assertRaises(case["expectedErr"]):
                        holidays.Tunisia(years=case.get("year"))
                        
                else:
                    holidays.Tunisia(years=case.get("year"))