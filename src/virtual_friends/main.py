"""
Python version: 3.5.1

https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2498
"""

from sys import stdin, stdout


def main():
    number_of_cases = int(stdin.readline())

    for _ in range(number_of_cases):
        friendships = int(stdin.readline())
        ufds = UFDS()

        for _ in range(friendships):
            person_1, person_2 = stdin.readline().strip().split()

            ufds.add(person_1)
            ufds.add(person_2)

            total_friendships = ufds.union(person_1, person_2)

            stdout.write("{}\n".format(total_friendships))


class UFDS:
    def __init__(self):
        self.parents = {}
        self.rank = {}
        self.sizes = {}

    def add(self, person):
        if person not in self.parents:
            self.parents[person] = person
            self.rank[person] = 0
            self.sizes[person] = 1

    def union(self, x, y):
        x_pivot = self.find(x)
        y_pivot = self.find(y)

        if x_pivot == y_pivot:
            return self.sizes[x_pivot]

        if self.rank[x_pivot] > self.rank[y_pivot]:
            parent, child = x_pivot, y_pivot
        else:
            parent, child = y_pivot, x_pivot
            self.rank[parent] += self.rank[parent] == self.rank[child]

        self.parents[child] = parent

        self.sizes[parent] += self.sizes[child]
        self.sizes[child] = self.sizes[parent]

        return self.sizes[parent]

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]


if __name__ == "__main__":
    main()
