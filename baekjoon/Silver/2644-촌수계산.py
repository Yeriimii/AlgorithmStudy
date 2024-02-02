from collections import deque

N = int(input())
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
A, B = map(int, input().split())

M = int(input())
for _ in range(M):
    parent, child = map(int, input().split())
    graph[parent][child] = 1

res = -1
visited = [False for _ in range(N + 1)]
visited[A] = True
Q = deque()
Q.append((A, 0))
while Q:
    node, relation = Q.popleft()
    if node == B:
        res = relation
    else:
        for i in range(1, N + 1):
            if not visited[i] and graph[i][node] == 1:
                visited[i] = True
                Q.append((i, relation + 1))

        for i in range(1, N + 1):
            if not visited[i] and graph[node][i] == 1:
                visited[i] = True
                Q.append((i, relation + 1))

print(res)
