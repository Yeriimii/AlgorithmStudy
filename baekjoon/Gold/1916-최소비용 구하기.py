import sys
import heapq


def djikstra(start):
    q = []
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        now_dist, now_node = heapq.heappop(q)
        if distance[now_node] < now_dist:
            continue
        for next_node, next_dist in graph[now_node]:
            cost = now_dist + next_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return distance


input = sys.stdin.readline

N = int(input())
M = int(input())
INF = float('inf')
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, v = map(int, input().split())
    graph[a].append((b, v))

s, e = map(int, input().split())
s_dist = djikstra(s)
print(s_dist[e])
