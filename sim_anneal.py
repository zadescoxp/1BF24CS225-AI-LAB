import random
import math

def simulated_annealing(x, T, cooling):
    while T > 0.001:
        new_x = x + random.uniform(-1, 1)
        delta = -(new_x**2) - (-(x**2))

        if delta > 0 or random.random() < math.exp(delta / T):
            x = new_x

        T *= cooling

    return x

print(simulated_annealing(5, 100, 0.95))
