"""
Python version: 3.5.1

https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=737
"""

from sys import stdin, stdout


def main():
    for line in stdin:
        total_nodes = int(line)

        graph = read_graph(total_nodes)

        links = critical_links(graph)
        write_critical_links(links)

        # Skip the line between the graphs
        stdin.readline()


def read_graph(total_nodes):
    graph = {
        node: {
            "adjacents": set(),
            "visited": False,
            "df_number": None,
            "low": None,
            "father": None,
        }
        for node in range(total_nodes)
    }

    for _ in range(total_nodes):
        start_node, _, *end_nodes = stdin.readline().strip().split()

        graph[int(start_node)]["adjacents"].update(map(int, end_nodes))

    return graph


def critical_links(graph):
    autoincrement = 1

    def search(v, bridges):
        nonlocal autoincrement

        graph[v]["visited"] = True

        graph[v]["df_number"] = autoincrement
        autoincrement += 1

        graph[v]["low"] = graph[v]["df_number"]

        for w in graph[v]["adjacents"]:

            if not graph[w]["visited"]:
                graph[w]["father"] = v

                search(w, bridges)

                if graph[w]["low"] > graph[v]["df_number"]:
                    bridges.append((v, w))

                graph[v]["low"] = min(graph[v]["low"], graph[w]["low"])

            elif graph[v]["father"] != w:
                graph[v]["low"] = min(graph[v]["low"], graph[w]["df_number"])

    bridges = []

    for v in graph:
        if not graph[v]["visited"]:
            search(v, bridges)

    return bridges


def write_critical_links(links):
    stdout.write("{} critical links\n".format(len(links)))

    ordered_links = sorted([sorted(link) for link in links])

    for link in ordered_links:
        stdout.write("{} - {}\n".format(*link))

    stdout.write("\n")


if __name__ == "__main__":
    main()
