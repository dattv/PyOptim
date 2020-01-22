from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
from matplotlib import pyplot
from PolyCur import polynomial_curvel

from GeneticAlgorithms import GA

def main():
    """

    :return:
    """
    poly = polynomial_curvel()

    minimum = -11.
    maximum = 11.
    x = np.arange(minimum, maximum, 0.05)
    y = poly.poly(x)

    optim = GA(10, poly.poly, minimum, maximum, width=32)
    optim()

    pyplot.plot(x, y, 'g-')
    pyplot.ylabel('polynomial_func')
    pyplot.show()

if __name__ == '__main__':
    main()