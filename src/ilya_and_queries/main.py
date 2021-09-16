"""
Python version: 3.8

http://codeforces.com/problemset/problem/313/B
"""

from sys import stdin, stdout


def main():
    chars = stdin.readline().strip()

    Q = int(stdin.readline())
    queries = [map(int, stdin.readline().split()) for _ in range(Q)]

    counter = get_counter(chars)

    for query in queries:
        stdout.write(f"{rsq(counter, *query)}\n")


def get_counter(chars):
    counter = [0]

    for i in range(1, len(chars)):
        same_chars = chars[i] == chars[i - 1]
        total_equal_chars = counter[i - 1] + same_chars

        counter.append(total_equal_chars)

    return counter


def rsq(counter, left, right):
    return counter[right - 1] - counter[left - 1]


if __name__ == "__main__":
    main()
