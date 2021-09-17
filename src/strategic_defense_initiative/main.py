"""
Python version: 3.5.1

https://vjudge.net/problem/UVA-497
"""

from sys import stdin, stdout


def main():
    tests = int(stdin.readline())

    # Skip the first blank line
    stdin.readline()

    for t in range(tests):
        heights = read_heights()

        max_hits, best_hits_sequence = calculate_best_hits_sequence(heights)

        write_hits(max_hits, best_hits_sequence, end=(t == tests - 1))


def read_heights():
    heights = []

    for line in stdin:
        if line.strip() == "":
            break

        heights.append(int(line))

    return heights


def write_hits(max_hits, best_hits_sequence, end):
    stdout.write("Max hits: {}\n".format(max_hits))

    for hit in best_hits_sequence:
        stdout.write("{}\n".format(hit))

    if not end:
        stdout.write("\n")


def calculate_best_hits_sequence(HEIGHTS):
    TOTAL_BEST_HITS = [()] * len(HEIGHTS)  # Output array

    def lis(index):
        height = HEIGHTS[index]
        best_hits = ()

        for i in range(index):
            best_previous_hits = (
                TOTAL_BEST_HITS[i] if TOTAL_BEST_HITS[i] else lis(i)
            )

            is_higher = height > HEIGHTS[i]

            if len(best_previous_hits) > len(best_hits) and is_higher:
                best_hits = best_previous_hits

        TOTAL_BEST_HITS[index] = best_hits + (height,)
        return TOTAL_BEST_HITS[index]

    lis(len(HEIGHTS) - 1)

    total_best_hits = tuple(map(len, TOTAL_BEST_HITS))

    max_hits = max(total_best_hits)
    max_pos = total_best_hits.index(max_hits)

    return max_hits, TOTAL_BEST_HITS[max_pos]


if __name__ == "__main__":
    main()
