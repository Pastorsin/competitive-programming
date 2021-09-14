"""
Python version: 3.6

https://www.codechef.com/problems/SPIDY2
"""

from math import log2
from functools import lru_cache
from sys import stdin, stdout

MAX_HEIGHT = 10 ** 9


def main():
    stdin.readline()
    heights = tuple(map(int, stdin.readline().split()))

    last = len(heights) - 1
    stdout.write(f"{minimal_energy(heights, index=last)}\n")


@lru_cache()
def minimal_energy(heights, index):
    """
    f(x) =  0                           if x = 0
            f(x - 1) + (h[i] - h[x])    if x > 0
    """
    energy = 0 if index == 0 else MAX_HEIGHT

    for i in range(index):
        is_power_of_2 = log2(index - i).is_integer()

        if is_power_of_2:
            cost = minimal_energy(heights, i) + abs(heights[i] - heights[index])
            if cost < energy:
                energy = cost

    return energy


if __name__ == "__main__":
    main()
