"""
Python version: 3.5.1

https://vjudge.net/problem/UVA-10048
"""

from collections import defaultdict
from sys import stdin, stdout


class UFDS:
    def __init__(self, total_elements):
        self.parents = list(range(total_elements + 1))
        self.rank = [0] * len(self.parents)

    def union(self, x, y):
        x_pivot = self.find(x)
        y_pivot = self.find(y)

        if x_pivot == y_pivot:
            return False

        if self.rank[x_pivot] > self.rank[y_pivot]:
            parent, child = x_pivot, y_pivot
        else:
            parent, child = y_pivot, x_pivot
            self.rank[parent] += self.rank[parent] == self.rank[child]

        self.parents[child] = parent

        return True

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]


class MST:
    NOT_FOUND = -1

    def __init__(self, graph, total_nodes):
        self.tree = self._build_tree(graph, total_nodes)

    def _build_tree(self, graph, total_nodes):
        ufds = UFDS(total_nodes)
        tree = defaultdict(list)

        graph.sort(key=lambda edge: edge[2])

        for vi, vj, w in graph:
            if ufds.union(vi, vj):
                tree[vi].append((vj, w))
                tree[vj].append((vi, w))

        return dict(tree)

    def _dfs(self, start, end, visited):
        if start not in self.tree:
            return self.NOT_FOUND

        visited.append(start)

        for child, weight in self.tree[start]:
            if child == end:
                return weight

            if child not in visited:
                child_max_weight = self._dfs(child, end, visited)

                if child_max_weight != self.NOT_FOUND:
                    return max(weight, child_max_weight)

        return self.NOT_FOUND

    def max_weight(self, start, end):
        return self._dfs(start, end, visited=[])


def main():
    for case, line in enumerate(stdin, start=1):
        total_crossings, total_streets, total_queries = map(int, line.split())

        if (total_crossings, total_streets, total_queries) == (0, 0, 0):
            break

        graph = read_graph(total_streets)
        mst = MST(graph, total_crossings)

        write_queries_response(mst, case, total_queries)


def read_graph(total_streets):
    graph = []

    for _ in range(total_streets):
        streets = tuple(map(int, stdin.readline().split()))
        graph.append(streets)

    return graph


def write_queries_response(mst, case, queries):
    if case != 1:
        stdout.write("\n")

    stdout.write("Case #{}\n".format(case))

    for _ in range(queries):
        query = map(int, stdin.readline().split())

        max_weight = mst.max_weight(*query)

        if max_weight == mst.NOT_FOUND:
            stdout.write("no path\n")
        else:
            stdout.write("{}\n".format(max_weight))


if __name__ == "__main__":
    main()
