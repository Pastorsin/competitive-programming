"""
Python version: 3.5.1

https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2949
"""


from sys import stdin, stdout

EOR = (0, 0)


def main():
    for line in stdin:
        total_jack, total_jill = map(int, line.split())

        if (total_jack, total_jill) == EOR:
            break

        jack_cds = read_cds(total_jack)
        jill_cds = read_cds(total_jill)

        copies = jack_cds.intersection(jill_cds)
        cds_to_sell = len(copies)

        stdout.write("{}\n".format(cds_to_sell))


def read_cds(total):
    return {int(stdin.readline()) for _ in range(total)}


if __name__ == "__main__":
    main()
