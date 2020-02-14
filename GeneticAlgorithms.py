from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import numpy as np
from utils.sort_utils import sort_ascent, sort_descent


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

        self._sort_func = sort_ascent()
        if self._go_min == True:
            self._sort_func = sort_descent()

    def __str__(self):
        """

        :return:
        """
        return self._init_pop

    def _selection(self):
        """

        :return:
        """
        # compute cost function
        fitness = np.asarray([self._cost_func(invidual) for invidual in self._init_pop])

        # sort
        fitness, population = self._sort_func(fitness, self._init_pop)

        # remove 50%
        fitness = fitness[:self._num_select]
        population = population[:self._num_select]

    def _cross_over(self, parents):
        """

        :param parents:
        :return:
        """


