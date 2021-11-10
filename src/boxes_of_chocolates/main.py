"""
Python version: 3.5.1

https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1430
"""

from sys import stdin, stdout
from functools import reduce
from operator import mul


def main():
    total_cases = int(stdin.readline())

    for _ in range(total_cases):
        total_friends, total_boxes = read_integers()

        boxes_of_chocolates = [read_integers()[1:] for _ in range(total_boxes)]

        total_chocolates = sum(reduce(mul, box) for box in boxes_of_chocolates)

        residue = total_chocolates % total_friends
        stdout.write("{}\n".format(residue))


def read_integers():
    return tuple(map(int, stdin.readline().split()))


if __name__ == "__main__":
    main()
