from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np


class sort_ascent():
    def __init__(self):
        pass

    def __call__(self, fitness, population):
        """

        :param fitness:
        :param population:
        :return:
        """
        index_sorted = np.argsort(fitness)  # ascent
        return fitness[index_sorted], population[index_sorted]


class sort_descent():
    def __init__(self):
        pass

    def __call__(self, fitness, population):
        """

        :param fitness:
        :param population:
        :return:
        """
        index_sorted = np.argsort(fitness)[::-1]  # descent
        return fitness[index_sorted], population[index_sorted]


if __name__ == '__main__':
    fitness = np.array([2, 4, 86, 3, 5, 54, 45, 4, 5, 346, 67, 34, 234, 34])
    population = np.random.random([len(fitness), 10])

    print(fitness)
    print(population)

    sort = sort_descent()
    sorted_fitness, sorted_population = sort(fitness, population)

    print(sorted_fitness)
    print(sorted_population)

    sort = sort_ascent()
    sorted_fitness, sorted_population = sort(fitness, population)

    print(sorted_fitness)
    print(sorted_population)

