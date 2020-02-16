from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import numpy as np

def random_neighbour(x, bounds, fraction=1.):
    """

    :param x:
    :param fraction:
    :return:
    """
    size = len(x)
    amplitude = (max(bounds) - min(bounds)) * fraction / 10.
    delta = (-amplitude/2.) + amplitude * np.random.random(size=size)
    return np.clip(x + delta, a_max=max(bounds), a_min=min(bounds))


class SA():
    def __init__(self, state, costFunc, temperature, bounds):
        """

        :param random_start:
        :param costFunc:
        :param temperature:
        """
        self._state = state
        self._costFunc = costFunc
        self._temperature = temperature
        self._bounds = bounds

    def __call__(self, step_id, max_step):
        """

        :return:
        """
        cost = self._costFunc(self._state)

        fraction = step_id / float(max_step)
        T = self._temperature(fraction)
        new_state = random_neighbour(self._state, self._bounds)
