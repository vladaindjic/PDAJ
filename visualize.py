import numpy as np
import matplotlib.pyplot as plt


def read_results():
    return np.genfromtxt('res-parallel-map.csv', delimiter=',', skip_header=1)


def visualize(results):

    theta1 = results[:, 2]
    theta2 = results[:, 3]
    x1 = results[:, 4]
    y1 = results[:, 5]
    x2 = results[:, 6]
    y2 = results[:, 7]

    # TODO: implement propper code for visualization
    plt.plot(x1, y1, '.')
    plt.plot(x2, y2, 'x')
    plt.savefig("res.png")


def main():
    results = read_results()
    visualize(results)


if __name__:
    main()


# pcolor pcolor mash matplotlib 3d SeaBorn
