"""
Python version: 3.5.1

https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2737
"""

from sys import stdin, stdout


def main():
    number_of_cases = int(stdin.readline())

    for _ in range(number_of_cases):
        friends, friendships = map(int, stdin.readline().strip().split())

        ufds = UFDS()

        for person, debit in enumerate(range(friends)):
            debit = int(stdin.readline())
            ufds.add(person, debit)

        for _ in range(friendships):
            person_1, person_2 = map(int, stdin.readline().strip().split())
            ufds.union(person_1, person_2)

        if all(debit == 0 for debit in ufds.debit.values()):
            stdout.write("POSSIBLE\n")
        else:
            stdout.write("IMPOSSIBLE\n")


class UFDS:
    def __init__(self):
        self.parents = {}
        self.rank = {}
        self.debit = {}

    def add(self, person, value):
        self.parents[person] = person
        self.rank[person] = 0
        self.debit[person] = value

    def union(self, x, y):
        x_pivot = self.find(x)
        y_pivot = self.find(y)

        if x_pivot == y_pivot:
            return

        if self.rank[x_pivot] > self.rank[y_pivot]:
            parent, child = x_pivot, y_pivot
        else:
            parent, child = y_pivot, x_pivot
            self.rank[parent] += self.rank[parent] == self.rank[child]

        self.parents[child] = parent
        self.debit[parent] += self.debit[child]
        self.debit[child] = 0

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]


if __name__ == "__main__":
    main()
