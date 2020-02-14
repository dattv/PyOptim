from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import numpy

class GA():
    def __init__(self, init_pop, cost_func, go_min=True):
        """

        :param init_pop:
        :param cost_func:
        :param go_min:
        """

        self._init_pop = init_pop
        self._cost_func = cost_func
        self._go_min = go_min
        self._num_select = len(self._init_pop) / 2

    def __str__(self):
        """

        :return:
        """
        return self._init_pop

    def _selection(self):
        """

        :return:
        """
        fitness = [self._cost_func(invidual) for invidual in self._init_pop]

        