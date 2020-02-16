import numpy
import GeneticAlgorithms as ga
import ParticalSwarmOptm as PSO
import sys

"""
The y=target is to maximize this equation ASAP:
    y = w1x1+w2x2+w3x3+w4x4+w5x5+6wx6
    where (x1,x2,x3,x4,x5,x6)=(4,-2,3.5,5,-11,-4.7)
    What are the best values for the 6 weights w1 to w6?
    We are going to use the genetic algorithm for the best possible values after a number of generations.
"""

# Inputs of the equation.
equation_inputs = [4, -2, 3.5, 5, -11, -4.7]

# Number of the weights we are looking to optimize.
num_weights = len(equation_inputs)

"""
Genetic algorithm parameters:
    Mating pool size
    Population size
"""
sol_per_pop = 8
# sol_per_pop = 15
num_parents_mating = 4

# Defining the population size.
pop_size = (sol_per_pop,
            num_weights)  # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
# Creating the initial population.
new_population = numpy.random.uniform(low=-4.0, high=4.0, size=pop_size)
print(new_population)


def cost_func(input):
    x = numpy.array([4, -2, 3.5, 5, -11, -4.7])
    return numpy.sum(x*input)


genetic_algs = ga.GA(new_population, cost_func=cost_func, go_min=False)


bounds = []
for i in range(sol_per_pop):
    bounds.append([-1.e10, 1.e10])

PSO_algs = PSO.PSO(new_population, costFunc=cost_func, bounds=bounds, num_particles=sol_per_pop, go_min=False)


fit = []
for i in range(1000):
    fit.append(PSO_algs())
    #
    # fitness, solution = genetic_algs()
    #
    # fit.append(fitness)

import matplotlib.pyplot

matplotlib.pyplot.plot(fit)
matplotlib.pyplot.xlabel("Iteration")
matplotlib.pyplot.ylabel("Fitness")
matplotlib.pyplot.show()
