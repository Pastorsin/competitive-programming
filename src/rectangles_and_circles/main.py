"""
Python version: 3.5.1

https://vjudge.net/problem/UVA-477
"""

from collections import namedtuple
from math import sqrt
from sys import stdin, stdout

Point = namedtuple("Point", ["x", "y"])
END_POINT = Point(9999.9, 9999.9)


class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def includes(self, point):
        x_coords = self.top_left.x, self.bottom_right.x
        is_between_x = min(x_coords) < point.x < max(x_coords)

        y_coords = self.top_left.y, self.bottom_right.y
        is_between_y = min(y_coords) < point.y < max(y_coords)

        return is_between_x and is_between_y


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def includes(self, point):
        return self._distance(point, self.center) < self.radius

    def _distance(self, point_a, point_b):
        diff_x = point_b.x - point_a.x
        diff_y = point_b.y - point_a.y

        return sqrt(diff_x * diff_x + diff_y * diff_y)


def main():
    figures = read_figures()
    solve_queries(figures)


def read_figures():
    figures = []

    for line in stdin:
        if line.strip() == "*":
            break

        name, *positions = line.strip().split()
        positions = tuple(map(float, positions))

        if name == "r":
            figure = Rectangle(
                top_left=Point(*positions[0:2]),
                bottom_right=Point(*positions[2:4]),
            )
        else:
            figure = Circle(center=Point(*positions[0:2]), radius=positions[2])

        figures.append(figure)

    return figures


def solve_queries(figures):
    for point_number, line in enumerate(stdin, start=1):
        point = Point(*map(float, line.strip().split()))

        if point == END_POINT:
            break

        contained = False

        for figure_number, figure in enumerate(figures, start=1):
            if figure.includes(point):
                contained = True
                msg = "Point {} is contained in figure {}\n"
                stdout.write(msg.format(point_number, figure_number))

        if not contained:
            msg = "Point {} is not contained in any figure\n"
            stdout.write(msg.format(point_number))


if __name__ == "__main__":
    main()
