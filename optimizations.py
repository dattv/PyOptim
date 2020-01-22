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

    x_err = []
    min_err = []
    for i in range(100):
        x_error, min_error = optim()
        print(x_error, min_error)

        x_err.append(x_error)
        min_err.append(min_error)



    pyplot.plot(x, y, 'g-')
    pyplot.plot(x_err, min_err, 'ro')
    pyplot.ylabel('polynomial_func')
    pyplot.show()

if __name__ == '__main__':
    main()