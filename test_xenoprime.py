# test_xenoprime.py
"""
Tests for XenoPrime module.
"""

import unittest
from xenoprime import XenoPrime

class TestXenoPrime(unittest.TestCase):
    """Test cases for XenoPrime class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = XenoPrime()
        self.assertIsInstance(instance, XenoPrime)
        
    def test_run_method(self):
        """Test the run method."""
        instance = XenoPrime()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
