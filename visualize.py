import numpy as np
import matplotlib.pyplot as plt


def read_results():
    return np.genfromtxt('results.csv', delimiter=',', skip_header=1)


def visualize(results):
    theta1 = results[:, 0]
    theta2 = results[:, 1]
    x1 = results[:, 2]
    y1 = results[:, 3]
    x2 = results[:, 4]
    y2 = results[:, 5]

    # TODO: implement propper code for visualization
    plt.plot(x1, y1)
    plt.show()


def main():
    results = read_results()
    visualize(results)


if __name__:
    main()
