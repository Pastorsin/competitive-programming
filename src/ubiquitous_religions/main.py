"""
Python version: 3.5.1

https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1524
"""

from sys import stdin, stdout


def main():
    for case_number, line in enumerate(stdin, start=1):
        N, M = map(int, line.strip().split())

        if (N, M) == (0, 0):
            break

        ufds = UFDS(N)

        for _ in range(M):
            student_1, student_2 = map(int, stdin.readline().strip().split())
            ufds.union(student_1, student_2)

        ufds.compression()
        differents_religions = len(set(ufds.parents.values()))

        stdout.write("Case {}: {}\n".format(case_number, differents_religions))


class UFDS:
    def __init__(self, N):
        sequence = range(1, N + 1)

        self.parents = {i: i for i in sequence}
        self.rank = {i: 0 for i in sequence}

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

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def compression(self):
        for student in self.parents:
            self.find(student)


if __name__ == "__main__":
    main()
