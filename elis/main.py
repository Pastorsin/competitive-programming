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
    sequence_lis = 1
    sequence_target = sequence[index]

    for i in range(index):
        subsequence_lis = lis(sequence, index=i) + 1

        if sequence[i] < sequence_target and sequence_lis < subsequence_lis:
            sequence_lis = subsequence_lis

    LIS_SIZES.append(sequence_lis)

    return sequence_lis


if __name__ == "__main__":
    main()
