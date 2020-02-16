from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np


class Particle():
    def __init__(self, x0):
        """

        :param x0:
        """
        self._num_dimension = len(x0)
        self._position_i = x0
        self._velocity_i = np.random.uniform(-1., 1., size=self._num_dimension)
        self._pos_best_i = x0
        self._err_best_i = -1.
        self._err_i = -1.

    def _evaluate(self, costFunc):
        """

        :param costFunc:
        :return:
        """
        self._err_i = costFunc(self._position_i)

        # check to see if current position is an individual best
        if self._err_i <= self._err_best_i or self._err_best_i == -1.:
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
        for i in range(self._num_dimension):
            self._position_i[i] += self._velocity_i[i]

            # adjust maximum position if necessary
            if self._position_i[i] > bounds[i][1]:
                self._position_i[i] = bounds[i][1]

            # adjust minimum position if neseccary
            if self._position_i[i] < bounds[i][0]:
                self._position_i[i] = bounds[i][0]


class PSO():
    def __init__(self, x0, costFunc, bounds, num_particles, go_min=True):
        """

        :param x0:
        :param costFunc:
        :param bounds:
        :param num_particles:
        """
        self._costFunc = costFunc
        if go_min == False:
            def _new_costFunc(input):
                return -costFunc(input)

            self._costFunc = _new_costFunc

        self._bounds = bounds
        self._num_particles = num_particles
        self._num_dimension = len(x0)

        self._err_best_g = -1  # best error for group
        self._pos_best_g = []  # best position for group

        self._go_min = go_min
        # establish the swarm
        self._swarm = []
        for i in range(num_particles):
            self._swarm.append(Particle(x0[i,:]))

    def __call__(self):
        """

        :return:
        """
        for j in range(self._num_particles):
            self._swarm[j]._evaluate(self._costFunc)

            # determine if current particle is the best (globally)
            if self._swarm[j]._err_best_i < self._err_best_g or self._err_best_g == -1.:
                self._pos_best_g = self._swarm[j]._pos_best_i
                self._err_best_g = self._swarm[j]._err_best_i

        for j in range(self._num_particles):
            self._swarm[j]._update_velocity(self._pos_best_g)
            self._swarm[j]._update_position(self._bounds)

        if self._go_min == False:
            self._err_best_g = -self._err_best_g

        print(self._err_best_g)
        # print(self._pos_best_g)
        return self._err_best_g
