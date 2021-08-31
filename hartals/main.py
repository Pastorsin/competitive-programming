"""
Python version: 3.5.1

https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=991

Input:
    1º  : Number of test cases to follow
    2º  : Number of days
    3º  : Number of parties
    4º  : Hartals of parties

Output:
    Working days we lose
"""

from sys import stdin, stdout


def main():
    tests = int(stdin.readline())

    for _ in range(tests):
        days = int(stdin.readline())
        parties = int(stdin.readline())
        hartals = [int(stdin.readline()) for _ in range(parties)]

        lost_days = calculate_lost_days(days, hartals)

        stdout.write("{}\n".format(lost_days))


def calculate_lost_days(days, hartals):
    lost_days = [
        day
        for day in range(1, days + 1)
        if not is_weekend(day) and is_hartal_day(day, hartals)
    ]

    return len(lost_days)


def is_weekend(day):
    weekday = day % 7
    return weekday == 0 or weekday == 6


def is_hartal_day(day, hartals):
    return any(day % hartal == 0 for hartal in hartals)


if __name__ == "__main__":
    main()
