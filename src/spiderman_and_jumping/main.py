"""
Python version: 3.6

https://www.codechef.com/problems/SPIDY2
"""

from math import log2
from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200_000)


def main():
    stdin.readline()
    heights = tuple(map(int, stdin.readline().split()))

    stdout.write(f"{minimal_energy(heights)}\n")


def minimal_energy(heights):
    MAX_HEIGHT = 10 ** 9
    MEMO = [-1] * len(heights)

    def lis(index):
        if index == 0:
            min_cost = 0
        else:
            min_cost = MAX_HEIGHT
            iterations = int(log2(index) + 1)

            for k in range(iterations):
                i = index - 2 ** k

                previous_cost = lis(i) if MEMO[i] == -1 else MEMO[i]
                new_cost = previous_cost + abs(heights[i] - heights[index])

                if new_cost < min_cost:
                    min_cost = new_cost

        MEMO[index] = min_cost
        return min_cost

    return lis(index=len(heights) - 1)


if __name__ == "__main__":
    main()
