"""
Python version: 3.5.1

https://vjudge.net/problem/UVA-270
"""
from collections import namedtuple, Counter
from sys import stdin, stdout

MAX_VALUE = float("Inf")

Point = namedtuple("Point", ["x", "y"])


def main():
    total_cases = int(stdin.readline())

    # Skip the first blank line
    stdin.readline()

    for case in range(total_cases):
        points = read_points()
        max_points_on_line = get_max_points_on_line(points)

        write_response(max_points_on_line, end=(case == total_cases - 1))


def read_points():
    points = []

    for line in stdin:
        if line.strip() == "":
            break

        coords = map(int, line.split())
        points.append(Point(*coords))

    return points


def get_max_points_on_line(points):
    max_points = 0

    for i, point_i in enumerate(points[:-1]):
        remaining_points = points[i + 1 :]

        slopes = [slope(point_i, point_j) for point_j in remaining_points]

        _, max_equals_slopes = Counter(slopes).most_common(1)[0]
        max_points = max(max_points, max_equals_slopes)

    return max_points + 1


def slope(point_a, point_b):
    if point_a.x == point_b.x:
        return MAX_VALUE

    return (point_a.y - point_b.y) / (point_a.x - point_b.x)


def write_response(max_points_on_line, end):
    stdout.write("{}\n".format(max_points_on_line))

    if not end:
        stdout.write("\n")


if __name__ == "__main__":
    main()
