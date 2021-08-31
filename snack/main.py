"""
Python version: 3.8

https://www.urionlinejudge.com.br/judge/en/problems/view/1038
"""

from sys import stdin, stdout


prices = (4.0, 4.5, 5.0, 2.0, 1.5)


def main():
    code, quantity = map(int, stdin.readline().split())
    total = prices[code - 1] * quantity

    stdout.write("Total: R$ {:.2f}\n".format(total))


if __name__ == "__main__":
    main()
