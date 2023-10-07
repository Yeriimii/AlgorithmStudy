import heapq as hq
import sys

a = list()
n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(a) == 0:
            print(0)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, x)
