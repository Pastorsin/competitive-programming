"""
PyPy version: 2.7.13

https://www.spoj.com/problems/EDIST/
"""

from sys import stdin, stdout


def main():
    total_cases = int(stdin.readline())

    for _ in range(total_cases):
        word_a, word_b = (stdin.readline().strip() for _ in range(2))

        minimal_operations = edit_distance(word_a, word_b)
        stdout.write("%d\n" % minimal_operations)


def edit_distance(word_a, word_b):
    if word_a == word_b:
        return 0

    if len(word_a) == 0:
        return len(word_b)

    if len(word_b) == 0:
        return len(word_a)

    N, M = len(word_a) + 1, len(word_b) + 1

    COSTS = [list(range(M))] + [[i] for i in range(1, N)]

    for i in range(1, N):
        for j in range(1, M):
            replace = COSTS[i - 1][j - 1] + (word_a[i - 1] != word_b[j - 1])
            delete = COSTS[i - 1][j] + 1
            insert = COSTS[i][j - 1] + 1

            COSTS[i].append(min(replace, delete, insert))

    return COSTS[N - 1][M - 1]


if __name__ == "__main__":
    main()
