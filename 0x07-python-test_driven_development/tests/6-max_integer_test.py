#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_integer_type(self):
        """Test valid integers."""
        self.assertEqual(max_integer([5, 4, 9, 2]), 9)
        self.assertEqual(max_integer([19]), 19)
        self.assertEqual(max_integer([-1, -9, 0, -10]), 0)
        self.assertEqual(max_integer([-5, -1, -6]), -1)

    def test_non_integer_type(self):
        """Tests data types that are not integers."""
        self.assertEqual(max_integer([3.5, 0.8, 2.9, 3.7]), 3.7)
        self.assertEqual(max_integer([5, 10, 15, float('inf')]), float('inf'))
        self.assertEqual(max_integer([90, 100, float('nan')]), 100)
        self.assertEqual(max_integer(['5', '7', '1']), '7')
        self.assertEqual(max_integer("drive"), "v")
        self.assertEqual(max_integer("TEST_DRIVEN"), "_")

    def test_empty_list(self):
        """Tests an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_no_args(self):
        """Tests missing argument."""
        self.assertEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()
