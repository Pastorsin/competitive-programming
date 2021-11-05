"""
Python version: 3.5.1

https://vjudge.net/problem/UVA-10310
"""

from collections import namedtuple
from math import sqrt
from sys import stdin, stdout

Point = namedtuple("Point", ["x", "y"])


def main():
    for line in stdin:
        points = read_points(line)

        # Skip the blank line between sets
        stdin.readline()

        escape_hole = get_escape_hole(*points)

        if escape_hole:
            msg = "The gopher can escape through the hole at ({:.3f},{:.3f})."
            stdout.write(msg.format(*escape_hole))
        else:
            stdout.write("The gopher cannot escape.")

        stdout.write("\n")


def read_points(line):
    total_holes, *positions = line.split()

    total_holes = int(total_holes)
    positions = tuple(map(float, positions))
    
    gopher = Point(*positions[0:2])
    dog = Point(*positions[2:4])

    holes = [
        Point(*map(float, stdin.readline().split())) for _ in range(total_holes)
    ]

    return gopher, dog, holes


def get_escape_hole(gopher, dog, holes):
    for hole in holes:
        gopher_distance = distance(gopher, hole)
        dog_distance = distance(dog, hole)

        if gopher_distance <= (dog_distance / 2):
            return hole


def distance(point_a, point_b):
    diff_x = point_b.x - point_a.x
    diff_y = point_b.y - point_a.y

    return sqrt(diff_x * diff_x + diff_y * diff_y)


if __name__ == "__main__":
    main()
