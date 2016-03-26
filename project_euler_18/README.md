This is solution for problem #18 from https://projecteuler.net website:

'Find the maximum total from top to bottom of the specified triangle of numbers.'

This was the second problem I worked on and I chose it, because the idea for the efficient solution to the problem came
to me from algorithms used in communication theory. It took me 20 min to come up with idea, 20 min to complete coding,
10 min to write description and about 10 min to create tests.
1 hour total.

The main method in this module is triangle_max_path(triangle). It receives triangle of numbers for which maximum path
from top to bottom should be computed.

The idea is that for the primitive triangle, e.g.

              12
            21  7

... we can determine the maximum path from top to bottom 12+21=33 and discard the other one 12+7=19. We will keep the
survivor path metrics for each element that was processed. So if we start from bottom and work up to the top that way we
will reach the top element where only maximum path will survive. This solution will have linear time complexity since
we processed each triangle element only once.

To run the program you need to have Python installed.

Running from command line:

   > python max_path_sum_1.py

Sample output:

Maximum total from top to bottom: 1074

Execution time: 0.001s

To run unittest, please, make sure you have max_path_sum_1.py in the same directory.


Running from command line:

   > python test_max_path_sum_1.py
