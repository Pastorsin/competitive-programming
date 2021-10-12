"""
Python version: 3.5.1

https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1867
"""

from sys import stdin, stdout


def main():
    for line in stdin:
        total_tasks = int(line)

        if total_tasks == 0:
            break

        graph = read_graph(tasks=range(1, total_tasks + 1))

        task = task_with_more_dependencies(graph)
        stdout.write("{}\n".format(task))


def read_graph(tasks):
    graph = {}

    for task in tasks:
        _, *dependencies = map(int, stdin.readline().strip().split())

        graph[task] = {"adjacents": dependencies, "total_dependencies": None}

    return graph


def task_with_more_dependencies(graph):
    max_task = max_dependencies = -1

    for v in graph:
        total_dependencies = dfs(graph, v)

        if len(total_dependencies) > max_dependencies:
            max_dependencies = len(total_dependencies)
            max_task = v

    return max_task


def dfs(graph, v):
    if graph[v]["total_dependencies"] is not None:
        return graph[v]["total_dependencies"]

    total_dependencies = set()

    for w in graph[v]["adjacents"]:
        total_dependencies.add(w)
        total_dependencies.update(dfs(graph, w))

    graph[v]["total_dependencies"] = total_dependencies
    return total_dependencies


if __name__ == "__main__":
    main()
