"""
Python version: 3.5.1

https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1051
"""

from sys import stdin, stdout
from math import sqrt


def main():
    for line in stdin:
        total_bulbs = int(line)

        if total_bulbs == 0:
            break

        # if the number of divisors is odd => the bulb is ON
        # 4 => 1 [ON], 2 [OFF], 4 [ON]
        # 5 => 1 [ON], 5 [OFF]
        if sqrt(total_bulbs).is_integer():
            stdout.write("yes\n")
        else:
            stdout.write("no\n")


if __name__ == "__main__":
    main()
