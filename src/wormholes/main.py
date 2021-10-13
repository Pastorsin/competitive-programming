"""
Python version: 3.5.1

https://vjudge.net/problem/UVA-558
"""

from sys import stdin, stdout

START_VERTEX = 0
MAX_DISTANCE = 1000


def main():
    total_cases = int(stdin.readline())

    for _ in range(total_cases):
        stars, wormholes = map(int, stdin.readline().split())

        graph = read_graph(stars, wormholes)

        if has_negative_cycle(graph):
            stdout.write("possible")
        else:
            stdout.write("not possible")

        stdout.write("\n")


def read_graph(stars, wormholes):
    graph = {vertex: [] for vertex in range(stars)}

    for _ in range(wormholes):
        start, end, weight = map(int, stdin.readline().split())
        graph[start].append((end, weight))

    return graph


def has_negative_cycle(graph):
    distances = relax(graph)

    for vertex, edges in graph.items():
        for adjacent, weight in edges:
            if distances[vertex] > (distances[adjacent] + weight):
                return True

    return False


def relax(graph):
    distances = {
        vertex: 0 if vertex == START_VERTEX else MAX_DISTANCE
        for vertex in graph
    }

    for _ in range(len(graph) - 1):
        for vertex, edges in graph.items():
            for adjacent, weight in edges:
                if distances[vertex] > (distances[adjacent] + weight):
                    distances[vertex] = distances[adjacent] + weight

    return distances


if __name__ == "__main__":
    main()
