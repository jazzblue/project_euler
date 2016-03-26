__author__ = 'Gregory Ronin'
"""
This is solution for problem #2 from https://projecteuler.net website:

'Find the sum of the even-valued Fibonacci terms whose values do not exceed 4000000.'

This was the first problem I worked on and I chose it as a warm-up since it is fairly straightforward and simple.
It took me 20 min to complete coding and debug, 10 min to write description and about 10 min to create tests.
40 min total.

The main method in this module is fibo_sum_even(max_value). It receives maximum Fibonacci value which is 4000000 in our
case and computes the solution to the problem.

To run the program you need to have Python installed.

Running from command line:

   > python even_fibo_numbers.py

Sample output:

Sum of even-valued Fibonacci that do not exceed 4000000 is: 4613732
Execution time: 0.001s

"""


import time

# Constants
MAX_FIBO_VALUE = 4000000  # maxmum Fibonacci value specified by the problem.
FIBO_INIT = (1, 2)  # First two Fibonacci values secified by the problem.


def is_even(n):
    """
    Checks if number is even.
    :param n: input number
    :return: True if n is even, otherwise, return False.
    """
    if n % 2 == 0:
        return True
    else:
        return False

def fibo_sum_even(max_value):
    """
    Computes the sum of the even-valued Fibonacci terms whose values do not exceed specified max_value.
    :param max_value: maximum Fibonacci value
    :return: Sum of the even-valued Fibonacci terms whose values do not exceed specified max_value.
    """

    # Initialize two running Fibonacci values
    fib_1, fib_2 = FIBO_INIT

    # Initialize running sum accumulator for even numbers:it should be set to the second initial Fibonacci value if
    # it is even, otherwise it should be set to 0, as we ignore odd values during summation.
    if is_even(fib_1):
        even_sum = fib_1
    else:
        even_sum = 0

    while fib_2 <= max_value:  # Run loop until the most recently computed number exceeds max_value0000000000
        # In each iteration we compute the new Fibonacci number and it gets "pushed" into fib_2 as the last computed
        # number.

        if is_even(fib_2):  # Update the running sum of even terms only if the newly computed number is even.00000000000
            even_sum += fib_2

        # Compute next Fibonacci number, "shift left" fib_2 to fib_1, and assign fib_2 new computed number
        fib_1, fib_2 = fib_2, fib_1 + fib_2

    return even_sum

if __name__ == '__main__':
    time_start = time.time()
    print 'Sum of even-valued Fibonacci that do not exceed {0} is: {1}'.format(MAX_FIBO_VALUE, fibo_sum_even(MAX_FIBO_VALUE))
    print 'Execution time: {0:.3f}s'.format(time.time() - time_start)



