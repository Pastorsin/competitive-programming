"""
Python version: 3.5.1

https://vjudge.net/problem/UVA-627
"""

from sys import stdin, stdout


def main():
    for line in stdin:
        total_routers = int(line)
        graph = read_graph(total_routers)

        total_querys = int(stdin.readline())

        stdout.write("-" * 5 + "\n")

        for _ in range(total_querys):
            start, end = stdin.readline().strip().split()
            path = bfs(graph, start, end)

            write_query_response(path, end)


def read_graph(total_routers):
    graph = {}

    for _ in range(total_routers):
        router, *connections = filter(
            bool, stdin.readline().strip().replace("-", ",").split(",")
        )

        graph[router] = connections

    return graph


def bfs(graph, start, end):
    roots = [start]
    path = {start: None}

    while len(roots) > 0 and end not in path:
        root = roots.pop(0)

        for adjacent in graph[root]:
            if adjacent not in path:
                path[adjacent] = root
                roots.append(adjacent)

    return path


def write_query_response(path, end):
    if end in path:
        response = []
        root = end

        while root is not None:
            response.append(root)
            root = path[root]

        stdout.write(" ".join(response[::-1]))
    else:
        stdout.write("connection impossible")

    stdout.write("\n")


if __name__ == "__main__":
    main()
