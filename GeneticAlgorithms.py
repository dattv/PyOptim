from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np


class GA():
    def __init__(self, population_num, object_func, minimum, maximum, width=64):
        """

        """
        self.population_num = population_num
        self.object_func = object_func
        self.minimum = minimum
        self.maximum = maximum
        self.population = None
        self.width = width

    def selection(self):
        self.population = np.random.uniform(self.minimum, self.maximum, self.population_num)

        y = self.object_func(self.population)

        out_array = np.argsort(y)

        return self.population[out_array[-int(self.population_num / 2):]]

    def mutation(self, string):
        index_mutation = np.random.randint(0, self.width)
        temp = string[index_mutation]
        temp = str(int(np.logical_not(bool(int(temp)))))


        return string[:index_mutation] + temp + string[index_mutation+1:]

    def cross_over(self, childeren_float):
        if self.population is not None:
            if self.width == 32:
                iiwidth = np.iinfo(np.int32)
            else:
                iiwidth = np.iinfo(np.int64)

            max_int = iiwidth.max
            min_int = iiwidth.min
            childeren_int = np.rint(
                np.interp(childeren_float, (self.minimum, self.maximum), (min_int, max_int))).astype(iiwidth.dtype)
            str_array = [np.binary_repr(sample, width=self.width) for sample in childeren_int]

            np.random.shuffle(str_array)

            for i in range(0, int(self.population_num / 2), 2):
                index = np.random.randint(1, self.width - 1)

                string1 = str_array[i]
                string2 = str_array[i + 1]
                str_array.append(string1[:index] + string2[index:])
                self.mutation(str_array[-1])
                str_array.append(string2[:index] + string1[index:])
                self.mutation(str_array[-1])

            np.random.shuffle(str_array)

            new_pop_int = [int(string, 2) for string in str_array]

            new_pop_float = np.interp(new_pop_int, (min_int, max_int), (self.minimum, self.maximum)).astype(np.float32)

        return new_pop_float

    def __call__(self):
        """

        :return:
        """
        childeren_float = self.selection()

        new_prop = self.cross_over(childeren_float)

