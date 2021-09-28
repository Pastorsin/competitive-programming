"""
Python version: 3.5.1

https://vjudge.net/problem/UVA-10664
"""

from sys import stdin, stdout

YES = "YES\n"
NO = "NO\n"


def knapsack(weights, N, K):
    N, K = N + 1, K + 1

    DP = {(i, 0): 0 for i in range(N)}
    DP.update({(0, j): 0 for j in range(K)})

    for i in range(1, N):
        for j in range(1, K):
            if weights[i - 1] > j:
                DP[i, j] = DP[i - 1, j]
            else:
                DP[i, j] = max(
                    DP[i - 1, j],
                    DP[i - 1, j - weights[i - 1]] + weights[i - 1],
                )

    return DP[N - 1, K - 1]


def main():
    cases = int(stdin.readline())

    for _ in range(cases):
        weights = tuple(map(int, stdin.readline().split()))
        total_weight = sum(weights)

        if total_weight % 2 == 1:
            stdout.write(NO)
        else:
            best_boot_weight = knapsack(
                weights, N=len(weights), K=(total_weight // 2)
            )

            stdout.write(YES if best_boot_weight * 2 == total_weight else NO)


if __name__ == "__main__":
    main()
