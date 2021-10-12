"""
Python version: 3.5.1

https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=251
"""

from sys import stdin, stdout


def main():
    for line in stdin:
        total_nodes = int(line)

        if total_nodes == 0:
            break

        graph = read_graph(total_nodes)

        stdout.write("{}\n".format(articulation_points(graph)))


def read_graph(total_nodes):
    graph = {
        node: {
            "adjacents": set(),
            "visited": False,
            "df_number": None,
            "low": None,
            "father": None,
        }
        for node in range(1, total_nodes + 1)
    }

    for line in stdin:
        start_node, *end_nodes = map(int, line.strip().split())

        if start_node == 0:
            break

        for end_node in end_nodes:
            graph[start_node]["adjacents"].add(end_node)
            graph[end_node]["adjacents"].add(start_node)

    return graph


def articulation_points(graph):
    autoincrement = 1

    def search(v, root, childs, points):
        nonlocal autoincrement

        graph[v]["visited"] = True

        graph[v]["df_number"] = autoincrement
        autoincrement += 1

        graph[v]["low"] = graph[v]["df_number"]

        for w in graph[v]["adjacents"]:

            if not graph[w]["visited"]:
                graph[w]["father"] = v

                if root == v:
                    childs.add(w)

                search(w, root, childs, points)

                if root != v and graph[w]["low"] >= graph[v]["df_number"]:
                    points.add(v)

                graph[v]["low"] = min(graph[v]["low"], graph[w]["low"])

            elif graph[v]["father"] != w:
                graph[v]["low"] = min(graph[v]["low"], graph[w]["df_number"])

    points = set()

    for v in graph:
        if not graph[v]["visited"]:
            root = v
            childs = set()

            search(v, root, childs, points)

            if len(childs) > 1:
                points.add(root)

    return len(points)


if __name__ == "__main__":
    main()
