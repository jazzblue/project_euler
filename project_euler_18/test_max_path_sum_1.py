__author__ = 'Gregory Ronin'

"""
Unit test for max_path_sum_1 module.

To run the program you need to have Python installed.
Also, please, make sure you have test_max_path_sum_1.py in the same directory.

Running from command line:

   > python test_max_path_sum_1.py
"""

import unittest
import max_path_sum_1

class TestEvenFiboNums(unittest.TestCase):

    def test_small_triangle(self):
        """Tests with input triangle of length 3."""
        test_triangle = [
            [3],
            [7, 4],
            [2, 4, 6],
            [8, 5, 9, 3]
        ]

        self.assertEqual(max_path_sum_1.triangle_max_path(test_triangle), 23)

if __name__ == '__main__':
    unittest.main()