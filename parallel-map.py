import csv
from multiprocessing import Pool

from calc import solve, parameters_gen
from cmd_args import parse_arguments


def simulate_pendulum(theta_resolution, L1, L2, m1, m2, tmax, dt, results_path):
    with open(results_path, 'w') as csvfile:
        fieldnames = ['theta1_init', 'theta2_init', 'theta1', 'theta2', 'x1', 'y1', 'x2', 'y2']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()

        p = Pool()
        results = p.map(solve, parameters_gen(L1, L2, m1, m1, tmax, dt, theta_resolution), chunksize=theta_resolution)
        p.close()

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
