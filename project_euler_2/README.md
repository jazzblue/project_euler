This is solution for problem #2 from https://projecteuler.net website:

'Find the sum of the even-valued Fibonacci terms whose values do not exceed 4000000.'

This was the first problem I worked on and I chose it as a warm-up since it is fairly straightforward and simple. It took me 20 min to complete coding and debug, 10 min to write description and about 10 min to create tests. 40 min total.

The main method in this module is fibo_sum_even(max_value). It receives maximum Fibonacci value which is 4000000 in our case and computes the solution to the problem.

To run the program you need to have Python installed.

Running from command line:

   > python even_fibo_numbers.py

Sample output:

Sum of even-valued Fibonacci that do not exceed 4000000 is: 4613732

Execution time: 0.001s


To test you can run unittest by invoking:

   > python test_even_fibo_numbers.py

Also, please, make sure you have even_fibo_numbers.py in the same directory.
