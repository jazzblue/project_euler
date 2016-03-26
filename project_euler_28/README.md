This is solution **for problem #28** from https://projecteuler.net website:

'Starting with the number 1 and moving to the right in a clockwise direction a spiral is formed.
 What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in that way?'

This was the third problem I worked on and I chose it, because it seemed like it requires some algorithm design and
has a reasonable amount of challenge.It took me 20 min to come up with algorithm, 50 min to complete coding and
comments, 10 min to write description and about 10 min to create tests.
90 min total.

The main method in this module is spiral_diagonals_sum(target_side_length). It receives triangle of numbers for which
maximum path from top to bottom should be computed.

The idea is to add layers to the spiral iteratively. Each additional layer will result in either odd or even side length
of a spiral. We will only keep and update diagonals' sums. There will be three diagonals to keep track of:

    - left diagonal
    - right diagonal for even side length
    - right diagonal for odd side length

The details of the algorithm are outlined below in the code comments.

To run the program you need to have Python installed.

Running from command line:

*python number_spiral_diagonals.py*

###Sample output:

Sum of the numbers on the diagonals in a 1001 by 1001 is: 669171001<br/>
Execution time: 0.001s

###Testing

To run unittest, please, make sure you have max_path_sum_1.py in the same directory.

Running from command line:

*python test_number_spiral_diagonals.py*
