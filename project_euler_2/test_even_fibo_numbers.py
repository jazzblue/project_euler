__author__ = 'Gregory Ronin'

"""
Unit test for even_fibo_numbers module.

To run the program you need to have Python installed.
Also, please, make sure you have even_fibo_numbers.py in the same directory.

Running from command line:

   > python test_even_fibo_numbers.py

"""

import unittest
import even_fibo_numbers

class TestEvenFiboNums(unittest.TestCase):

  def test_small_num_1(self):
      """Tests with maximum Fibonacci term value of 10."""
      self.assertEqual(even_fibo_numbers.fibo_sum_even(10), 10)

  def test_small_num_2(self):
      """Tests with maximum Fibonacci term value of 20."""
      self.assertEqual(even_fibo_numbers.fibo_sum_even(20), 10)

  def test_small_num_3(self):
      """Tests with maximum Fibonacci term value of 40."""
      self.assertEqual(even_fibo_numbers.fibo_sum_even(40), 44)

if __name__ == '__main__':
    unittest.main()
