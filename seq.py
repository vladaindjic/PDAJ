import sys

import numpy as np
from scipy.integrate import odeint

# The gravitational acceleration (m.s-2).
g = 9.81


# based on https://scipython.com/blog/the-double-pendulum/
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


def calc_E(y):
    """Return the total energy of the system."""

    th1, th1d, th2, th2d = y.T
    V = -(m1 + m2) * L1 * g * np.cos(th1) - m2 * L2 * g * np.cos(th2)
    T = 0.5 * m1 * (L1 * th1d) ** 2 + 0.5 * m2 * ((L1 * th1d) ** 2 + (L2 * th2d) ** 2 +
                                                  2 * L1 * L2 * th1d * th2d * np.cos(th1 - th2))
    return T + V


def solve(L1, L2, m1, m2, tmax, dt, y0):
    t = np.arange(0, tmax + dt, dt)

    # Do the numerical integration of the equations of motion
    y = odeint(deriv, y0, t, args=(L1, L2, m1, m2))

    # Unpack z and theta as a function of time
    theta1, theta2 = y[:, 0], y[:, 2]

    # Convert to Cartesian coordinates of the two bob positions.
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)

    return theta1, theta2, x1, y1, x2, y2


def simulate_pendulum(theta_resolution):
    # Pendulum rod lengths (m), bob masses (kg).
    L1, L2 = 1.0, 1.0
    m1, m2 = 1.0, 1.0

    for theta1_init in np.linspace(0, 2 * np.pi, theta_resolution):
        for theta2_init in np.linspace(0, 2 * np.pi, theta_resolution):
            # Maximum time, time point spacings and the time grid (all in s).
            tmax, dt = 30.0, 0.01
            # Initial conditions: theta1, dtheta1/dt, theta2, dtheta2/dt.
            y0 = np.array([
                theta1_init,
                0.0,
                theta2_init,
                0.0
            ])

            theta1, theta2, x1, y1, x2, y2 = solve(L1, L2, m1, m2, tmax, dt, y0)
            print theta1_init, theta2_init, theta1[-1], theta2[-1]


def main():
    simulate_pendulum(10)


if __name__ == '__main__':
    main()
