"""
Python version: 3.5.1

https://vjudge.net/problem/UVA-10282
"""


from sys import stdin, stdout


EOR = ""


def main():
    words = {}

    for line in stdin:
        if line.strip() == EOR:
            break

        english_word, foreign_word = line.split()
        words[foreign_word] = english_word

    for line in stdin:
        foreign_word = line.strip()

        english_word = words.get(foreign_word, "eh")
        stdout.write("{}\n".format(english_word))


if __name__ == "__main__":
    main()
