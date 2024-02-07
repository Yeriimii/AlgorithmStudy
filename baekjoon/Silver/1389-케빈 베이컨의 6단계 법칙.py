from collections import deque


def bfs(start):
    score = [0] * (N + 1)
    Q = deque()
    Q.append(start)
    visited = [False] * (N + 1)
    visited[start] = True

    while Q:
        curr = Q.popleft()
        for i in graph[curr]:
            if not visited[i]:
                visited[i] = True
                score[i] = score[curr] + 1
                Q.append(i)
    return sum(score)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

res = []
for i in range(1, N + 1):
    res.append(bfs(i))

print(res.index(min(res)) + 1)
