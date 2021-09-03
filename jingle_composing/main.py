"""
Python version: 3.8

https://www.urionlinejudge.com.br/judge/en/problems/view/1430
"""


from sys import stdin, stdout

DURATIONS = {
    "W": 1,
    "H": 1 / 2,
    "Q": 1 / 4,
    "E": 1 / 8,
    "S": 1 / 16,
    "T": 1 / 32,
    "X": 1 / 64,
}

EOR = "*"


def main():
    while (line := stdin.readline().strip()) and line != EOR:
        measures = line.split("/")[1:-1]

        total_duration = calculate_duration(measures)
        stdout.write(f"{total_duration:.0f}\n")


def calculate_duration(measures):
    total = 0

    for measure in measures:
        measures_duration = sum([DURATIONS[duration] for duration in measure])

        if measures_duration == 1:
            total += measures_duration

    return total


if __name__ == "__main__":
    main()
