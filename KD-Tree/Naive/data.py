import numpy as np
import random
import matplotlib.pyplot as plt
RANGE_MAX = 100
random.seed(3009)


def generate_data_points(num_dimensions, num_datapoint, range_max=RANGE_MAX):
    return np.random.randint(0, range_max, (num_datapoint, num_dimensions))


if __name__ == '__main__':
    data = generate_data_points(2, 10)
    plt.scatter(data[:, 0], data[:, 1])
    plt.show()
