"""
Python version: 3.5.1

https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=216
"""

from sys import stdin, stdout


def main():
    for line in stdin:
        total_nodes = int(line)

        if total_nodes == 0:
            break

        graph = read_graph(total_nodes)

        _, *start_nodes = map(int, stdin.readline().strip().split())

        for start_node in start_nodes:
            innacesibles = get_innacesibles_nodes(graph, start_node)
            write_innacesibles_nodes(innacesibles)


def read_graph(total_nodes):
    graph = {
        node: {"adjacents": set(), "visited": False}
        for node in range(1, total_nodes + 1)
    }

    add_edges(graph)

    return graph


def add_edges(graph):
    edges = stdin.readline().strip()

    while edges != "0":
        start_node, *end_nodes, _ = map(int, edges.split())
        graph[start_node]["adjacents"].update(end_nodes)

        edges = stdin.readline().strip()


def get_innacesibles_nodes(graph, start_node):
    dfs(graph, start_node)

    innacesibles = []

    for v in graph:
        if not graph[v]["visited"]:
            innacesibles.append(v)
        else:
            graph[v]["visited"] = False

    return innacesibles


def dfs(graph, v, root=None):
    graph[v]["visited"] = root is not None

    for w in graph[v]["adjacents"]:
        if not graph[w]["visited"]:
            dfs(graph, w, root=v)


def write_innacesibles_nodes(innacesibles):
    stdout.write("{}".format(len(innacesibles)))
    for i in innacesibles:
        stdout.write(" {}".format(i))
    stdout.write("\n")


if __name__ == "__main__":
    main()
