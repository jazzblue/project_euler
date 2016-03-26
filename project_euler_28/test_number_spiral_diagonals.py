__author__ = 'Gregory Ronin'

"""
Unit test for number_spiral_diagonals module.

To run the program you need to have Python installed.
Also, please, make sure you have number_spiral_diagonals.py in the same directory.

Running from command line:

   > python test_number_spiral_diagonals.py

"""

import unittest
import number_spiral_diagonals

class TestEvenFiboNums(unittest.TestCase):

  def test_small_spiral(self):
      """Tests with spiral whose side is of length 5."""
      self.assertEqual(number_spiral_diagonals.spiral_diagonals_sum(5), 101)

if __name__ == '__main__':
    unittest.main()