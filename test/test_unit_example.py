# tests/test_unit_example.py

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest

from app import add_numbers


class TestAddNumbers(unittest.TestCase):
    """Test case for the add_numbers function."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        result = add_numbers(-3, -5)
        self.assertEqual(result, -8)

    def test_add_mixed_numbers(self):
        """Test adding a positive and a negative number."""
        result = add_numbers(3, -5)
        self.assertEqual(result, -2)

    def test_add_zero(self):
        """Test adding zero."""
        result = add_numbers(0, 5)
        self.assertEqual(result, 5)
        result = add_numbers(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
