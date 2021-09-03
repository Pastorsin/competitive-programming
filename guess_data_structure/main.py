"""
Python version: 3.5.1

https://vjudge.net/problem/UVA-11995
"""


from sys import stdin, stdout
import heapq

PUSH = 1
POP = 2


def main():
    for line in stdin:
        total_actions = int(line)
        actions = [
            map(int, stdin.readline().split()) for _ in range(total_actions)
        ]

        result = guess_structure(actions)

        if not any(result):
            stdout.write("impossible\n")
        elif sum(result) > 1:
            stdout.write("not sure\n")
        elif result[0]:
            stdout.write("queue\n")
        elif result[1]:
            stdout.write("stack\n")
        elif result[2]:
            stdout.write("priority queue\n")


def guess_structure(actions):
    queue = []
    stack = []
    max_heap = []

    is_queue = is_stack = is_max_heap = True

    for action, number in actions:
        if action == PUSH:
            queue.append(number)
            stack.append(number)
            heapq.heappush(max_heap, number * -1)
        elif len(queue) == 0:
            is_queue = is_stack = is_max_heap = False
        else:
            if number != queue.pop(0):
                is_queue = False

            if number != stack.pop():
                is_stack = False

            if number != heapq.heappop(max_heap) * -1:
                is_max_heap = False

    return is_queue, is_stack, is_max_heap


if __name__ == "__main__":
    main()
