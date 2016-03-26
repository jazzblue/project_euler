__author__ = 'Gregory Ronin'

"""
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
"""

import time

# Triangle specified by the problem
TRIANGLE_1 = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
]


def triangle_max_path(triangle):
    """
    Computes maximum total from top to bottom of the specified triangle of numbers.
    :param triangle: input triangle
    :return: Maximum total from top to bottom of the input triangle.
    """

    for level in xrange(len(triangle), 0, -1):  # We are working from bottom (last triangle row) to top element
        # Since we need some indexing here, we iterate over indexes using xrange.
        # The level, therefore will run from length of triangle to 1.

        # For each element we want to see which of two children has greater accumulated path metric.
        # We will add that greater path metric to the value of the element to compute that element's
        # accumulated path metric
        if level < len(triangle):  # If not bottom level: we do not process bottom level because it has no children.
            level_elements = triangle[level - 1]

            # The list comprehension computes accumulated path metric for each element in the current level
            # It adds greater path metric of an element's two children and adds it to element's value
            accum_path = [level_elements[idx] + accum_path[idx]
                          if accum_path[idx] > accum_path[idx + 1]
                          else level_elements[idx] + accum_path[idx + 1]
                          for idx in xrange(len(level_elements))]

        # If it is bottom level, initialize accumulated path of each element to element's value, since it has no children.
        else:
            accum_path = triangle[level - 1]

    return accum_path[0]  # The top element list has only one element which is the max path


if __name__ == '__main__':
    time_start = time.time()
    print 'Maximum total from top to bottom: {0}'.format(triangle_max_path(TRIANGLE_1))
    print 'Execution time: {0:.3f}s'.format(time.time() - time_start)
