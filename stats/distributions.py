import numpy as np


class Contaminated:
    def __init__(self, proportion, gen1, gen2):
        self.proportion = proportion
        self.gen1 = gen1
        self.gen2 = gen2

    def __call__(self, size):
        samples = []
        for i in range(size):
            if np.random.uniform() < self.proportion:
                samples.append(self.gen1())
            else:
                samples.append(self.gen2())
        return samples
