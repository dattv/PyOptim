from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np


class Particle():
    def __init__(self, x0):
        """

        :param x0:
        """
        self._position_i = x0
        self._velocity_i = []
        self._pos_best_i = []
        self._err_best_i = []
        self._err_i = -1.
        self._num_dimension = len(x0)
        self._velocity_i = np.random.uniform(-1., 1., size=self._num_dimension)

    def _evaluate(self, costFunc):
        """

        :param costFunc:
        :return:
        """
        self._err_i = costFunc(self._position_i)

        # check to see if current position is an individual best
        if self._err_i <= self._err_best_i or self._err_best_i == -1.
            self._pos_best_i = self._position_i
            self._err_best_i = self._err_i

    def _update_velocity(self, pos_best_g):
        """

        :param pos_best_g:
        :return:
        """
        _w = 0.5  # constant inertia weight (how much to weigh the previous velocity)
        _c1 = 1.  # cognative constant
        _c2 = 2.  # social constant

        for i in range(self._num_dimension):
            r1 = np.random.random()
            r2 = np.random.random()

            vel_coginitive = _c1 * r1 * (self._pos_best_i[i] - self._position_i[i])
            vel_social = _c2 * r2 * (pos_best_g[i] - self._position_i[i])
            self._velocity_i[i] = _w * self._velocity_i[i] + vel_coginitive + vel_social

    def _update_position(self, bounds):
        """

        :param bounds:
        :return:
        """

