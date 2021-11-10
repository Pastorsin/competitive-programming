"""
Python version: 3.7.3

https://www.spoj.com/problems/GCD2/
"""

from sys import stdin, stdout


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def main():
    total_cases = int(stdin.readline())

    for _ in range(total_cases):
        a, b = map(int, stdin.readline().split())

        stdout.write(f"{gcd(a, b)}\n")


if __name__ == "__main__":
    main()
