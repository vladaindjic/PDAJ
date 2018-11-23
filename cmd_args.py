import argparse


def parse_arguments():
    # Setup command line option parser
    parser = argparse.ArgumentParser(
        description='Double pendulum simulation '
    )

    parser.add_argument(
        '-tr',
        '--theta-resolution',
        metavar='THETA_RESOLUTION',
        help="Theta resolution",
        type=int,
        default=10
    )

    parser.add_argument(
        '-L1',
        '--L1',
        metavar='L1',
        help="Length of the first",
        type=float,
        default=1.0
    )

    parser.add_argument(
        '-L2',
        '--L2',
        metavar='L2',
        help="Length of the second",
        type=float,
        default=1.0
    )

    parser.add_argument(
        '-m1',
        '--m1',
        metavar='m1',
        help="Mass of the first",
        type=float,
        default=1.0
    )

    parser.add_argument(
        '-m2',
        '--m2',
        metavar='m2',
        help="Mass of the second",
        type=float,
        default=1.0
    )

    parser.add_argument(
        '-tmax',
        '--tmax',
        metavar='TMAX',
        help="Time for simulation",
        type=float,
        default=30.0
    )

    parser.add_argument(
        '-dt',
        '--dt',
        metavar='DT',
        help="Dt",
        type=float,
        default=0.01
    )

    parser.add_argument(
        '-rpath',
        '--results-path',
        metavar='RESULTS PATH',
        help="Path for results",
        default="results.csv"
    )

    args = parser.parse_args()
    theta_resolution = args.theta_resolution
    L1 = args.L1
    L2 = args.L2
    m1 = args.m1
    m2 = args.m2
    tmax = args.tmax
    dt = args.dt
    results_path = args.results_path

    return theta_resolution, L1, L2, m1, m2, tmax, dt, results_path


def main():
    print parse_arguments()


if __name__ == '__main__':
    main()
