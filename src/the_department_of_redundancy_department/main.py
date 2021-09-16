"""
Python version: 3.5.1

https://vjudge.net/problem/UVA-484
"""


from collections import Counter
from sys import stdin, stdout


def main():
    sequence = []
    for line in stdin:
        sequence += list(map(int, line.split()))

    counter = Counter(sequence)

    ordered_counter = sorted(
        counter.items(), key=lambda pair: sequence.index(pair[0])
    )

    for number, occurences in ordered_counter:
        stdout.write("{} {}\n".format(number, occurences))


if __name__ == "__main__":
    main()
