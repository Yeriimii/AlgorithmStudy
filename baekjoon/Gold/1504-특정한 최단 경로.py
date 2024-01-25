import sys
import heapq

input = sys.stdin.readline


def dijkstra(start):
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


INF = float('INF')
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

first_node_dist = dijkstra(1)
v1_node_dist = dijkstra(v1)
v2_node_dist = dijkstra(v2)
min_v1 = first_node_dist[v1] + v1_node_dist[v2] + v2_node_dist[N]
min_v2 = first_node_dist[v2] + v2_node_dist[v1] + v1_node_dist[N]
res = min(min_v1, min_v2)
if res != INF:
    print(res)
else:
    print(-1)
