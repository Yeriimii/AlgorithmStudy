import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
    n, m, r = map(int, input().split())
    graph = [list() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    q = deque()
    q.append(r)
    visited = [0 for _ in range(n + 1)]
    visited[0] = 1
    visited[r] = 1
    seq = 1
    while q:
        number = q.popleft()
        for node in sorted(graph[number]):
            if visited[node] == 0:
                seq += 1
                visited[node] = seq
                q.append(node)

    for i in range(1, n + 1):
        print(visited[i])
