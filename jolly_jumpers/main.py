"""
Python version: 3.5.1

https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=979
"""

from sys import stdin, stdout


def main():
    for line in stdin:
        N, *numbers = list(map(int, line.split()))

        if is_jolly(N, numbers):
            stdout.write("Jolly\n")
        else:
            stdout.write("Not jolly\n")


def is_jolly(N, numbers):
    sequence = set(range(1, N))
    differences = {abs(numbers[i] - numbers[i + 1]) for i in range(N - 1)}

    return sequence == differences


if __name__ == "__main__":
    main()
