import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
Q = []
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        heapq.heappush(Q, i)

while Q:
    x = heapq.heappop(Q)
    print(x, end=' ')
    graph[x].sort()
    for i in graph[x]:
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(Q, i)
