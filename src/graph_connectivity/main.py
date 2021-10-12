"""
Python version: 3.5.1

https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=400
"""

import string
from sys import stdin, stdout


def main():
    total_cases = int(stdin.readline())

    # Skip the first blank line
    stdin.readline()

    for case in range(total_cases):
        graph = read_graph(identifiers=string.ascii_uppercase)

        stdout.write("{}\n".format(max_connected_subgraphs(graph)))

        if case != total_cases - 1:
            stdout.write("\n")


def read_graph(identifiers):
    last_node = stdin.readline().strip()
    nodes = identifiers[: identifiers.index(last_node) + 1]

    graph = {node: {"adjacents": set(), "visited": False} for node in nodes}

    for line in stdin:
        if line.strip() == "":
            break

        node_a, node_b = line.strip()

        graph[node_a]["adjacents"].add(node_b)
        graph[node_b]["adjacents"].add(node_a)

    return graph


def max_connected_subgraphs(graph):
    connected_subgraphs = 0

    for v in graph:
        if not graph[v]["visited"]:
            dfs(graph, v)
            connected_subgraphs += 1

    return connected_subgraphs


def dfs(graph, v):
    graph[v]["visited"] = True

    for w in graph[v]["adjacents"]:
        if not graph[w]["visited"]:
            dfs(graph, w)


if __name__ == "__main__":
    main()
