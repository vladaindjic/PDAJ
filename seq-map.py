import csv

from calc import y0_gen, solve
from cmd_args import parse_arguments

from simple_plugins import AttrDict

_pool_data = None


def _init_pool(*data):
    global _pool_data

    data_keys = 'L1, L2, m1, m2, tmax, dt'.split(', ')
    _pool_data = AttrDict(zip(data_keys, data))


def _worker(args):
    y0 = args
    c = _pool_data

    return solve(c.L1, c.L2, c.m1, c.m2, c.tmax, c.dt, y0)


def simulate_pendulum(theta_resolution, L1, L2, m1, m2, tmax, dt, results_path):
    with open(results_path, 'w') as csvfile:
        fieldnames = ['theta1_init', 'theta2_init', 'theta1', 'theta2', 'x1', 'y1', 'x2', 'y2']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()

        _init_pool(L1, L2, m1, m2, tmax, dt)

        results = map(_worker, y0_gen(theta_resolution))

        for theta1_init, theta2_init, theta1, theta2, x1, y1, x2, y2 in results:
            csvwriter.writerow({'theta1_init': theta1_init,
                                'theta2_init': theta2_init,
                                'theta1': theta1[-1],
                                'theta2': theta2[-1],
                                'x1': x1[-1],
                                'y1': y1[-1],
                                'x2': x2[-1],
                                'y2': y2[-1]
                                })


def main():
    theta_resolution, L1, L2, m1, m2, tmax, dt, results_path = parse_arguments()
    simulate_pendulum(theta_resolution, L1, L2, m1, m2, tmax, dt, results_path)


if __name__ == "__main__":
    main()
