#!/usr/bin/env python3.6
import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--all", action="store_true",
                        help="Runs all tests found in 'path'")
    parser.add_argument("path", help="Path to test(s)")
    return parser.parse_args()


def get_all_tests(path):
    paths = []
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if not os.path.isfile(filepath):
            continue
        if filename.startswith("test_") and filename.endswith(".py"):
            paths.append(filepath)
    return paths


def main():
    args = parse_args()
    if args.all:
        paths = get_all_tests(args.path)
    else:
        paths = [args.path]

    os.system("coverage erase")
    for path in paths:
        os.system("coverage run -a --omit=/home/paolo/.local/lib/python3.6/site-packages/pcutils.py {}".format(path))
    os.system("coverage report")


if __name__ == '__main__':
    main()

