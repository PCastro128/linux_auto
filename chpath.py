#!/usr/bin/env python3.6
import argparse
import os
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--to-linux", action="store_true",
                        help="Convert a windows path into a linux path.")
    parser.add_argument("-w", "--to-windows", action="store_true",
                        help="Convert a linux path into a windows path.")
    parser.add_argument("path", help="Path to convert.")
    return parser.parse_args()


def win_to_linux(path):
    if path.startswith("C:"):
        return path.replace("C:", "/mnt/c").replace("\\", "/")
    else:
        return path.replace("\\", "/")


def linux_to_win(path):
    if path.startswith("/mnt/c"):
        return path.replace("/mnt/c", "C:").replace("/", "\\")
    else:
        return path.replace("/", "\\")


def main():
    args = parse_args()
    if args.to_linux:
        print(win_to_linux(args.path))
    elif args.to_windows:
        print(linux_to_win(args.path))
    else:
        print("Pick either linux or windows. Use chpath -h for more info.")


if __name__ == '__main__':
    main()

