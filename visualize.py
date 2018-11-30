from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.backends.backend_pdf

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

from cmd_args import parse_args_visualize

fonts = {
    'label': 8,
    'plt': 8,
    'title': 10
}

cmaps = {
    'pcolor': 'RdBu',
    '3D': 'viridis'
}

FIGURE_SIZE = (11.7, 8.3) # In inches


def read_results(path):
    # read results from .csv file
    return np.genfromtxt(path, delimiter=',', skip_header=1)


def visualize_parameter_pcolor(xx, yy, z, title, fig, position):
    # visualize one parameter using pcolor
    zz = np.reshape(z, np.shape(xx))
    ax = fig.add_subplot(position)
    ax.set_title(title, fontsize=fonts['title'])
    ax.set_xlabel('theta2_init', fontsize=fonts['label'])
    ax.set_ylabel('theta1_init', fontsize=fonts['label'])
    im = ax.pcolor(xx, yy, zz, cmap=cmaps['pcolor'])
    fig.colorbar(im, ax=ax)


# def visualize_pcolor(xx, yy, x1, y1, x2, y2, theta1, theta2):
#     # visualize all parameters using pcolor
#     fig = plt.figure(1)
#
#     visualize_parameter_pcolor(xx, yy, x1, 'x1', fig, 321)
#     visualize_parameter_pcolor(xx, yy, y1, 'y1', fig, 322)
#     visualize_parameter_pcolor(xx, yy, x2, 'x2', fig, 323)
#     visualize_parameter_pcolor(xx, yy, y2, 'y2', fig, 324)
#     visualize_parameter_pcolor(xx, yy, theta1, 'theta1', fig, 325)
#     visualize_parameter_pcolor(xx, yy, theta2, 'theta2', fig, 326)
#     #
#     fig.tight_layout()
#
#     plt.savefig('results/pcolor.png')


def visualize_parameter_3D(xx, yy, z, title, fig, position):
    # visualize one parameter in 3D
    zz = np.reshape(z, np.shape(xx))
    ax = fig.add_subplot(position, projection='3d')
    ax.set_title(title, fontsize=fonts['title'])
    # ax.contour3D(xx, yy, zz, 50, cmap='binary')
    ax.plot_surface(xx, yy, zz, rstride=1, cstride=1,
                    cmap=cmaps['3D'], edgecolor='none')

    ax.set_xlabel('theta2_init', fontsize=fonts['label'])
    ax.set_ylabel('theta1_init', fontsize=fonts['label'])
    ax.set_zlabel(title, fontsize=fonts['label'])


# def visualize_3D(xx, yy, x1, y1, x2, y2, theta1, theta2):
#     # visualize parameters in 3D
#     fig = plt.figure(2, figsize=plt.figaspect(0.5))
#
#     visualize_parameter_3D(xx, yy, x1, 'x1', fig, 321)
#     visualize_parameter_3D(xx, yy, y1, 'y1', fig, 322)
#     visualize_parameter_3D(xx, yy, x2, 'x2', fig, 323)
#     visualize_parameter_3D(xx, yy, y2, 'y2', fig, 324)
#     visualize_parameter_3D(xx, yy, theta1, 'theta1', fig, 325)
#     visualize_parameter_3D(xx, yy, theta2, 'theta2', fig, 326)
#     #
#     fig.tight_layout()
#
#     plt.savefig('results/3D.png')


def visualize_figure(xx, yy, x1, y1, x2, y2, theta1, theta2):
    pdf = matplotlib.backends.backend_pdf.PdfPages("results/output.pdf")

    # fig = plt.figure(1, figsize=plt.figaspect(0.5))
    fig = plt.figure(1)

    # x1
    visualize_parameter_pcolor(xx, yy, x1, 'x1', fig, 221)
    visualize_parameter_3D(xx, yy, x1, 'x1', fig, 222)
    # y1
    visualize_parameter_pcolor(xx, yy, y1, 'y1', fig, 223)
    visualize_parameter_3D(xx, yy, y1, 'y1', fig, 224)
    fig.tight_layout()
    # plt.savefig('results/tmp1.png')
    pdf.savefig(fig)

    # fig = plt.figure(2, figsize=plt.figaspect(0.5))
    fig = plt.figure(2)

    # x1
    visualize_parameter_pcolor(xx, yy, x2, 'x2', fig, 221)
    visualize_parameter_3D(xx, yy, x2, 'x2', fig, 222)
    # y1
    visualize_parameter_pcolor(xx, yy, y2, 'y2', fig, 223)
    visualize_parameter_3D(xx, yy, y2, 'y2', fig, 224)
    fig.tight_layout()
    # plt.savefig('results/tmp2.png')
    pdf.savefig(fig)

    # fig = plt.figure(3, figsize=plt.figaspect(0.5))
    fig = plt.figure(3)

    # x1
    visualize_parameter_pcolor(xx, yy, theta1, 'theta1', fig, 221)
    visualize_parameter_3D(xx, yy, theta1, 'theta1', fig, 222)
    # y1
    visualize_parameter_pcolor(xx, yy, theta2, 'theta2', fig, 223)
    visualize_parameter_3D(xx, yy, theta2, 'theta2', fig, 224)
    fig.tight_layout()
    # plt.savefig('results/tmp3.png')
    pdf.savefig(fig)
    pdf.close()




def visualize(results):
    matplotlib.rc('figure',
                  figsize=FIGURE_SIZE,
                  titlesize='xx-large'
                  )


    # set font for values on plot
    plt.rcParams.update({'font.size': fonts['plt']})
    # extracting parameters
    theta1_init = results[:, 0]
    theta2_init = results[:, 1]
    theta1 = results[:, 2]
    theta2 = results[:, 3]
    x1 = results[:, 4]
    y1 = results[:, 5]
    x2 = results[:, 6]
    y2 = results[:, 7]
    # setting axes
    x = theta2_init
    y = theta1_init
    # dim is equal to theta resolution
    dim = int(sqrt(np.shape(x)[0]))
    # reshape 1d arrays in 2d arrays with shape (dim, dim)
    xx = np.reshape(x, (dim, dim))
    yy = np.reshape(y, (dim, dim))
    # create pcolor plot
    # visualize_pcolor(xx, yy, x1, y1, x2, y2, theta1, theta2)
    # create 3D plot
    # visualize_3D(xx, yy, x1, y1, x2, y2, theta1, theta2)
    visualize_figure(xx, yy, x1, y1, x2, y2, theta1, theta2)


def main():
    # get value of -rpath parameter
    results_path = parse_args_visualize()
    results = read_results(results_path)
    visualize(results)


if __name__:
    # accept cmd_arg -rpath which is the path to the *.csv file with results
    main()
