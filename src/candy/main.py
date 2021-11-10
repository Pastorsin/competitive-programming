"""
Python version: 3.5.1

https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=3298
"""

from sys import stdin, stdout


def main():
    for line in stdin:
        # N: Number of rows
        # M: Number of columns
        N, M = map(int, line.split())

        if (N, M) == (0, 0):
            break

        # Read the matrix
        boxes = [read_row() for _ in range(N)]

        max_candies = calculate_max_candies(boxes)
        stdout.write("{}\n".format(max_candies))


def calculate_max_candies(boxes):
    N, M = len(boxes), len(boxes[0])

    # DP: (N + 2) x (M + 3)
    # Fill first 2 rows and 2 columns with zeros for the base cases
    # The last column is the max number of candies
    # The others cells are the max number of candies for the subproblems
    DP = [[0 for _ in range(M + 3)] for _ in range(N + 2)]

    # Fill DP starting from 2nd row and 2nd column
    # until the last row and the penultimate column
    for row, box in enumerate(boxes, start=2):
        for col, candies in enumerate(box, start=2):
            DP[row][col] = max(
                # Alternative 1: Don't take the candy
                DP[row][col - 1],
                # Alternative 2: Take the candy
                candies + DP[row][col - 2],
            )

        DP[row][-1] = max(
            # Alternative 1: Don't take the row
            DP[row - 1][-1],
            # Alternative 2: Take the row
            DP[row][-2] + DP[row - 2][-1],
        )

    # The result at the last corner is the max number of candies
    return DP[-1][-1]


def read_row():
    return list(map(int, stdin.readline().split()))


if __name__ == "__main__":
    main()
