"""
Python version: 3.5.1

https://vjudge.net/problem/UVA-10131
"""

from sys import stdin, stdout


def main():
    elephants = read_elephants()
    elephants.sort(key=lambda elephant: elephant[0])

    lazy_bigger_elephants = find_lazy_biggers(elephants)

    stdout.write("{}\n".format(len(lazy_bigger_elephants)))
    for elephant in lazy_bigger_elephants:
        stdout.write("{}\n".format(elephant))


def read_elephants():
    weights_iq = [map(int, line.split()) for line in stdin]

    return [(*line, i) for i, line in enumerate(weights_iq, 1)]


def find_lazy_biggers(elephants):
    MEMO = [()] * len(elephants)

    def lis(index):
        max_sequence = ()

        weight, iq, number = elephants[index]

        for i in range(index):
            max_sequence_i = MEMO[i] if MEMO[i] else lis(i)
            weight_i, iq_i, _ = elephants[i]

            if (
                weight_i != weight
                and iq_i > iq
                and len(max_sequence_i) > len(max_sequence)
            ):
                max_sequence = max_sequence_i

        MEMO[index] = max_sequence + (number,)
        return MEMO[index]

    lis(index=len(elephants) - 1)

    total_lazy_biggers = tuple(map(len, MEMO))
    biggest = total_lazy_biggers.index(max(total_lazy_biggers))

    return MEMO[biggest]


if __name__ == "__main__":
    main()
