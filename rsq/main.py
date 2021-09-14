"""
Python version: 3.8

“Dado un arreglo A[ ] con N números y una cantidad de consultas M imprimir 
la respuesta a cada una de ellas. Las consultas están compuestas por un par
de números L y R, donde 0 <= L <= R < N, y lo que se pide es la suma de los
elementos de A en el rango [L, R]”
"""

from sys import stdin, stdout


def main():
    N = int(stdin.readline())
    numbers = [int(stdin.readline()) for _ in range(N)]

    M = int(stdin.readline())
    queries = [map(int, stdin.readline().split()) for _ in range(M)]

    total_sum = build_rsq(N, numbers)

    for query in queries:
        stdout.write(f"{rsq(total_sum, *query)}\n")


def build_rsq(N, numbers):
    return [sum(numbers[:i]) for i in range(N + 1)]


def rsq(total_sum, left, right):
    return total_sum[right + 1] - total_sum[left]


if __name__ == "__main__":
    main()
