import numpy as np
import csv
import sys
import time
from scipy.integrate import odeint

# The gravitational acceleration (m.s-2).
g = 9.81


def deriv(y, t, L1, L2, m1, m2):
    """Return the first derivatives of y = theta1, z1, theta2, z2."""
    theta1, z1, theta2, z2 = y

    c, s = np.cos(theta1 - theta2), np.sin(theta1 - theta2)

    theta1dot = z1
    z1dot = (m2 * g * np.sin(theta2) * c - m2 * s * (L1 * z1 ** 2 * c + L2 * z2 ** 2) -
             (m1 + m2) * g * np.sin(theta1)) / L1 / (m1 + m2 * s ** 2)
    theta2dot = z2
    z2dot = ((m1 + m2) * (L1 * z1 ** 2 * s - g * np.sin(theta2) + g * np.sin(theta1) * c) +
             m2 * L2 * z2 ** 2 * s * c) / L2 / (m1 + m2 * s ** 2)
    return theta1dot, z1dot, theta2dot, z2dot


def solve(L1, L2, m1, m2, tmax, dt, y0):
    t = np.arange(0, tmax + dt, dt)

    # Do the numerical integration of the equations of motion
    y = odeint(deriv, y0, t, args=(L1, L2, m1, m2))
    theta1, theta2 = y[:, 0], y[:, 2]

    # Convert to Cartesian coordinates of the two bob positions.
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)

    return theta1, theta2, x1, y1, x2, y2


def y0_gen(theta_resolution):
    for theta1_init in np.linspace(0, 2 * np.pi, theta_resolution):
        for theta2_init in np.linspace(0, 2 * np.pi, theta_resolution):
            # Initial conditions: theta1, dtheta1/dt, theta2, dtheta2/dt.
            y0 = np.array([
                theta1_init,
                0.0,
                theta2_init,
                0.0
            ])
            yield y0


def simulate_pendulum(theta_resolution, write_results=True):
    # Pendulum rod lengths (m), bob masses (kg).
    L1, L2 = 1.0, 1.0
    m1, m2 = 1.0, 1.0

    # Maximum time, time point spacings (all in s).
    tmax, dt = 30.0, 0.01

    with open('results.csv', 'w') as csvfile:
        fieldnames = ['theta1', 'theta2', 'x1', 'y1', 'x2', 'y2']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()

        start_time = time.time()
        for y0 in y0_gen(theta_resolution):
            theta1, theta2, x1, y1, x2, y2 = solve(L1, L2, m1, m2, tmax, dt, y0)
            if write_results:
                theta1_init, theta2_init = y0[0], y0[2]
                print theta1_init, theta2_init, theta1[-1], theta2[-1]
                csvwriter.writerow({'theta1': theta1[-1],
                                    'theta2': theta2[-1],
                                    'x1': x1[-1],
                                    'y1': y1[-1],
                                    'x2': x2[-1],
                                    'y2': y2[-1]
                                    })
        end_time = time.time()
        print 'Time elapsed (sequential): %f' % (end_time - start_time)


def main():
    write_results = sys.argv[1] == 'write-results' if len(sys.argv) > 1 else False
    simulate_pendulum(10, write_results=write_results)


if __name__ == "__main__":
    main()
