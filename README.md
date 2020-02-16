# PyOptim
Implement Some Optimization Algorithm For Finding Minimal Point of Polynomial Curvel

problem:
maximizing equation 
<img src="https://latex.codecogs.com/svg.latex?\Large&space;Y=\overrightarrow{W}\cdot\overrightarrow{X}" title="\Large Y=\overrightarrow{W}\cdot\overrightarrow{X}" />


## [Genetic Algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm)
In this document, I try to re-implement [GA](https://en.wikipedia.org/wiki/Genetic_algorithm),
based on my understanding about this method and [Genetic Algorithm Implementation in Python](https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6).

My fitness history             |  [Ahmed Grad fitness history](https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6)
:-------------------------:|:-------------------------:
<img src="https://github.com/dattv/PyOptim/blob/master/results/GA/my/my_fitness.png" width="400" height="400"> |<img src="https://github.com/dattv/PyOptim/blob/master/results/GA/references/Ahmed%20Gad_fitness.png" width="400" height="400">


comparison between my result and [Ahmed Gad](https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6) after 1000 step.
easy to realize that after 1000 step my implementation can reach higher value of equation above.

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
| best solution [Ahmed Gad](https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6)  |x1 = 1.67171573e+00  |x2 = -3.71316424e+00 |x3 = 3.05233306e+02   |x4 = 2.11299501e+00 |x5 = -2.00224839e-01   |x6 = -3.27807311e+02 |  
| best solution fitness [Ahmed Gad](https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6)  | 2635.8915725  |   |   |   |   |   |
| best solution [my]()  |x1 = 109.35142938  |x2 = -58.62868893 |x3 = 60.66640886  |x4 = 105.50072658 |x5 = -171.52134765  |x6 = -81.86705169  |
| best solution fitness [my]()  | 3566.0091264521807  |   |   |   |   |   |


## [Partical Swarm Optimization](https://en.wikipedia.org/wiki/Particle_swarm_optimization)
My fitness history             | 
:-------------------------:|
<img src="https://github.com/dattv/PyOptim/blob/master/results/PSO/my/My_fitness.png" width="400" height="400"> |

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
| best solution [my]()  |x1 = 1.e+10  |x2 = -1.e+10 |x3 = 1.e+10  |x4 =  1.e+10 |x5 = -1.e+10  |x6 = -1.e+10  |
| best solution fitness [my]()  | 302000000000.0  |   |   |   |   |   |

