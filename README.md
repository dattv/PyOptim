# PyOptim
Implement Some Optimization Algorithm For Finding Minimal Point of Polynomial Curvel

## [Genetic Algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm)
In this document, I try to re-implement [GA](https://en.wikipedia.org/wiki/Genetic_algorithm),
based on my understanding about this method and [Genetic Algorithm Implementation in Python](https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6).

problem:
maximizing equation 
<img src="https://latex.codecogs.com/svg.latex?\Large&space;Y=\overrightarrow{W}\cdot\overrightarrow{X}" title="\Large Y=\overrightarrow{W}\cdot\overrightarrow{X}" />

![My_Fitness_history](https://github.com/dattv/PyOptim/blob/master/results/GA/my/my_fitness.png&s=200)
<img src="https://github.com/dattv/PyOptim/blob/master/results/GA/my/my_fitness.png" width="400" height="790">
![Ahmed_Grad_Fitness_history](https://github.com/dattv/PyOptim/blob/master/results/GA/references/Ahmed%20Gad_fitness.png)

comparison between my result and [Ahmed Gad](https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6) after 1000 step.
easy to realize that after 1000 step my implementation can reach higher value of equation above.

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
| best solution [Ahmed Gad](https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6)  | 1.67171573e+00  | -3.71316424e+00 | 3.05233306e+02   | 2.11299501e+00 | -2.00224839e-01   | -3.27807311e+02 |  
| best solution fitness [Ahmed Gad](https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6)  | 2635.8915725  |   |   |   |   |   |
| best solution [my]()  | 108.18044766  | -48.89323501  | 104.3551271  |  88.57507076 | -143.86504601  | -86.99125212  |
| best solution fitness [my]()  | 3330.000950447867  |   |   |   |   |   |