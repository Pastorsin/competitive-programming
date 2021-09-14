"""
Python version: 3.7.3

https://www.spoj.com/problems/ELIS/
"""

from functools import lru_cache
from sys import stdin, stdout

LIS_SIZES = []


def main():
    N = int(stdin.readline())
    sequence = tuple(map(int, stdin.readline().split()))

    lis(sequence, index=N - 1)

    stdout.write(f"{max(LIS_SIZES)}\n")


@lru_cache()
def lis(sequence, index):
    sequence_size = 1
    target = sequence[index]

    for i in range(index):
        subsequence_size = lis(sequence, i) + 1

        if sequence[i] < target and sequence_size < subsequence_size:
            sequence_size = subsequence_size

    LIS_SIZES.append(sequence_size)

    return sequence_size


if __name__ == "__main__":
    main()
