"""
Python version: 3.5.1

https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=5372
"""

from sys import stdin, stdout

EOR = "-1"
WRONG = "wrong"
RIGHT = "right"

PENALTY = 20


def main():
    submissions = {}

    for line in stdin:
        minutes, *submission = line.split()

        if minutes == EOR:
            scores = calculate_score(submissions)
            stdout.write("{} {}\n".format(len(scores), sum(scores)))

            submissions.clear()
        else:
            problem, result = submission

            if problem not in submissions:
                submissions[problem] = {WRONG: 0, RIGHT: 0}

            submissions[problem][result] += (
                1 if result == WRONG else int(minutes)
            )


def calculate_score(submissions):
    return [
        result[RIGHT] + result[WRONG] * PENALTY
        for result in submissions.values()
        if result[RIGHT] > 0
    ]


if __name__ == "__main__":
    main()
