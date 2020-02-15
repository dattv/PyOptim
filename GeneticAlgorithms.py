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
        self._num_select = int(len(self._init_pop) / 2)

        self._len = len(init_pop[0])

        self._sort_func = sort_descent()
        if self._go_min == True:
            self._sort_func = sort_ascent()

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
        population = population[:self._num_select, :]

        return fitness, population

    def _cross_over(self, parents):
        """

        :param parents:
        :return:
        """
        random_parent_idx = np.random.randint(0, self._num_select - 1, size=self._num_select)
        for i in range(0, self._num_select, 2):
            cross_point = np.random.randint(1, self._len - 2)


            temp = np.concatenate([parents[random_parent_idx[i], :cross_point], parents[random_parent_idx[i + 1], cross_point:]], axis=0)
            parents = np.concatenate([parents, np.reshape(temp, newshape=[1, -1])], axis=0)

        return parents

    def _mutation(self, childrent, num_mutations=1):
        """

        :param parents:
        :return:
        """
        mutation_counter = np.uint8(childrent.shape[1] / num_mutations)
        for idx in range(childrent.shape[0]):
            gene_idx = np.random.randint(0, childrent.shape[1])
            for mutation_num in range(num_mutations):
                random_value = np.random.uniform(-1., 1., 1)
                childrent[idx, gene_idx] = childrent[idx, gene_idx] + random_value

        return childrent

    def __call__(self):

        # do selection operator
        fitness, parent = self._selection()
        print("finess", fitness)
        print("best_fitness", fitness[0])
        print("best_solution", parent[0, :])

        # do cross_over operator
        new_population = self._cross_over(parent)

        # do mutation operator
        self._init_pop = self._mutation(new_population, num_mutations=2)


import numpy

def cal_pop_fitness(equation_inputs, pop):
    # Calculating the fitness value of each solution in the current population.
    # The fitness function calulates the sum of products between each input and its corresponding weight.
    fitness = numpy.sum(pop*equation_inputs, axis=1)
    return fitness

def select_mating_pool(pop, fitness, num_parents):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    parents = numpy.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999999
    return parents

def crossover(parents, offspring_size):
    offspring = numpy.empty(offspring_size)
    # The point at which crossover takes place between two parents. Usually, it is at the center.
    crossover_point = numpy.uint8(offspring_size[1]/2)

    for k in range(offspring_size[0]):
        # Index of the first parent to mate.
        parent1_idx = k%parents.shape[0]
        # Index of the second parent to mate.
        parent2_idx = (k+1)%parents.shape[0]
        # The new offspring will have its first half of its genes taken from the first parent.
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        # The new offspring will have its second half of its genes taken from the second parent.
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring

def mutation(offspring_crossover, num_mutations=1):
    mutations_counter = numpy.uint8(offspring_crossover.shape[1] / num_mutations)
    # Mutation changes a number of genes as defined by the num_mutations argument. The changes are random.
    for idx in range(offspring_crossover.shape[0]):
        gene_idx = mutations_counter - 1
        for mutation_num in range(num_mutations):
            # The random value to be added to the gene.
            random_value = numpy.random.uniform(-1.0, 1.0, 1)
            offspring_crossover[idx, gene_idx] = offspring_crossover[idx, gene_idx] + random_value
            gene_idx = gene_idx + mutations_counter
    return offspring_crossover