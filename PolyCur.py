from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np


class polynomial_curvel():
    """

    """

    def __init__(self, order=None):
        """

        """
        if order is None:
            self.poly = default_polynomial_curvel()

        else:
            self.poly = None


class default_polynomial_curvel():

    def __call__(self, input):
        """

        :return:
        """

        x = input
        return 0.1*x - 3*np.power((np.sin(x)-3*np.cos(x)), 4)+\
               10.*(np.power(np.sin(x), 6)+3*np.power(np.cos(x), 6))+\
               6*np.power((6*np.sin(x)+np.cos(x)), 2) + 0.01*(np.power(x, 3) + 3*np.power(x, 4))
