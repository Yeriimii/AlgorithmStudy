import sys
from collections import deque

input = sys.stdin.readline

queue = deque()
N = int(input())
for _ in range(N):
    command = input()
    if command.startswith("push"):
        queue.append(command.split()[1])
    elif command.startswith("pop"):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command.startswith("front"):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command.startswith("back"):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif command.startswith("empty"):
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command.startswith("size"):
        print(len(queue))
