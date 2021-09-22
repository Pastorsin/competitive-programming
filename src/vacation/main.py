"""
Python version: 3.5.1

https://vjudge.net/problem/UVA-10192
"""

from sys import stdin, stdout


def main():
    for case_number, line in enumerate(stdin, 1):
        if line.strip() == "#":
            break

        mom_cities = line.strip("\n")
        dad_cities = stdin.readline().strip("\n")
        
        cities_to_visit = calculate_cities_to_visit(mom_cities, dad_cities)

        stdout.write(
            "Case #{}: you can visit at most {} cities.\n".format(
                case_number, cities_to_visit
            )
        )


def calculate_cities_to_visit(mom_cities, dad_cities):
    N, M = len(mom_cities) + 1, len(dad_cities) + 1

    MEMO = {(i, 0): 0 for i in range(N)}
    MEMO.update({(0, j): 0 for j in range(M)})

    for i in range(1, N):
        for j in range(1, M):
            if mom_cities[i - 1] == dad_cities[j - 1]:
                MEMO[i, j] = MEMO[i - 1, j - 1] + 1
            else:
                MEMO[i, j] = max(MEMO[i - 1, j], MEMO[i, j - 1])

    return MEMO[N - 1, M - 1]


if __name__ == "__main__":
    main()
