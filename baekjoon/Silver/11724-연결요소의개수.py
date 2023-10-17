from collections import deque
import sys

n, m = map(int, input().split())
if m == 0:
    print(n)
else:
    graph = [[] for _ in range(n+1)]
    visit = [0] * (n+1)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    Q = deque()
    res = 0
    for i in range(1, n+1):
        if len(graph[i]) != 0 and visit[i] == 0:
            visit[i] = 1
            for x in graph[i]:
                Q.append(x)
            while Q:
                node = Q.popleft()
                if visit[node] == 0:
                    visit[node] = 1
                    for x in graph[node]:
                        Q.append(x)
            res += 1
    tmp = 0
    for i in visit[1:]:
        if i == 0:
            tmp += 1

    print(res + tmp)
