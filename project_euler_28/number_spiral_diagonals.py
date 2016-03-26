__author__ = 'Gregory Ronin'

"""
This is solution for problem #28 from https://projecteuler.net website:

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

   > python number_spiral_diagonals.py

Sample output:

Sum of the numbers on the diagonals in a 1001 by 1001 is: 669171001
Execution time: 0.001s
"""


import time

TARGET_SIDE_LENGTH = 1001  # Side length we need to compute the result for.

INIT_NUM = 1  # Starting number in gthe spiral.

# 1 2
# 3 4    <-----  1 4  is "left" diagonal,  2 3 is "right even diagonal". the side length is 2, therefore, "even".
#
#  7 8 9
#  6 1 2
#  5 4 3  <--- 7 1 3 is "left" diagonal, 9 1 5 is "right odd diagonal". the side length is 3, therefore, "odd".
#
INIT_LEFT_DIAG_SUM = 1  # Initial Left diagonal sum, it always runs through the first element (INIT_NUM) which is 1.
INIT_RIGHT_EVEN_DIAG_SUM = 0  # Initial Right "even side length" diagonal sum. It does not run through first element,
                              # therefore,initial number is 0.
INIT_RIGHT_ODD_DIAG_SUM = 1   # Initial Right "odd side length" diagonal sum. It always runs through the first element
                              # (INIT_NUM) which is 1.

def spiral_diagonals_sum(target_side_length):

    last_num = INIT_NUM  # The number on which spiral ends, inital spiral has only one number INIT_NUM.
    left_diag_sum = INIT_LEFT_DIAG_SUM               # Initialize Left diagonal sum.
    right_even_diag_sum = INIT_RIGHT_EVEN_DIAG_SUM   # Initialize Right Even diagonal sum.
    right_odd_diag_sum = INIT_RIGHT_ODD_DIAG_SUM     # Initialize Right diagonal diagonal sum.

    # Building target spiral, layer by layer.
    for side_length in xrange(1, target_side_length):
        # In this loop, if side_length reaches target_side_length.
        # It means we have already built the last layer and should exit the loop .

        # We will go and add three new numbers to diagonal sums.
        # Case 1 (going from "even" side_length to "odd" side_length:
        #
        #   Current spiral:
        #                   12
        #                   43
        #                       ... it has "even side_lengths" diagonal
        #
        #  After we increment side_length we add another layer:
        #                   789
        #                   612
        #                   543
        #
        # 1. We add number 7 to left diagonal.
        # 2. We add numbers 5 and 9 to "odd side length" diagonal
        #
        # Case 2 (going from "odd" side_length/diagonal to "even" side_length/diagonal:
        #
        #   Current spiral:
        #                   7  8  9
        #                   6  1  2
        #                   5  4  3
        #                       ... it has "odd side length" diagonal
        #
        #  After we increment side_length we add another layer:
        #                   7  8  9 10
        #                   6  1  2 11
        #                   5  4  3 12
        #                  16 15 14 13
        #
        # 1. We add number 13 to left diagonal
        # 2. We add numbers 10 and 16 to "even side length" diagonal.
        #
        # As we can see in either case we would:
        #   1. add 1 number to left diagonal:
        #          last_num + side_length + 1
        #   2. add two numbers to right "even length" or "odd length" diagonal.
        #          last_num + 1
        #          last_num + 2*(side_length + 1) - 1     <--- this is also going to be our next last number.

        #Computations as described above:
        left_diag_sum += last_num + side_length + 1  # Compute left diagonal as described above
        next_last_num = last_num + 2*(side_length + 1) - 1  # store next last number of the added layer/new spiral
        right_diag_increment = (last_num + 1) + next_last_num  # increment for right diagonal even or odd
        
        if side_length % 2 == 0:  # If side_length is even we are adding on odd side length
            right_odd_diag_sum += right_diag_increment
        else:  # We are adding on even side length
            right_even_diag_sum += right_diag_increment

        last_num = next_last_num  # We used last number in all needed computations, so update it.
            
    if (side_length + 1) % 2 == 0:  # If side has even length
        return left_diag_sum + right_even_diag_sum
    else:  # side has odd length
        return left_diag_sum + right_odd_diag_sum - 1  # We subtract one, since in this case both left and right
                                                       # diagonals share the same number in the center

if __name__ == '__main__':
    time_start = time.time()
    print 'Sum of the numbers on the diagonals in a {0} by {0} is: {1}'.format(
        TARGET_SIDE_LENGTH,
        spiral_diagonals_sum(TARGET_SIDE_LENGTH)
    )
    print 'Execution time: {0:.3f}s'.format(time.time() - time_start)



