import sys
import heapq

input = sys.stdin.readline


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    heapq.heappush(dist[start], 0)

    while q:
        # 가장 최단 거리에 있는 노드 정보 꺼내기
        now_dist, now_node = heapq.heappop(q)

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next_node, next_dist in graph[now_node]:
            cost = now_dist + next_dist
            if (len(dist[next_node]) <= K):  # 인접 노드와 연결된 개수가 K개 보다 같거나 작으면
                heapq.heappush(q, (cost, next_node))  # 인접한 노드를 큐에 삽입
                heapq.heappush(dist[next_node], -cost)  # 인접한 노드의 경로에 비용 삽입(최대 힙)
            else:  # 이미 인접 노드의 경로가 K개 있을 때
                if (dist[next_node][0] < -cost):  # 인접 노드의 경로의 0번째 바용이 현재 비용보다 크면
                    heapq.heappop(dist[next_node])  # 인접 노드가 갖는 경로 중 가장 비용이 큰 경로 버리고
                    heapq.heappush(q, (cost, next_node))  # 인접한 노드를 큐에 삽입
                    heapq.heappush(dist[next_node], -cost)  # 인접한 노드의 경로에 비용 삽입(최대 힙)


if __name__ == '__main__':
    INF = float('inf')
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    dist = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, val = map(int, input().split())
        graph[a].append((b, val))

    res = 0
    result = dijkstra(1)
    for node in range(1, N + 1):
        if len(dist[node]) < K:
            print(-1)
        else:
            dist[node].sort()  # -25 -20 -15 -10 -5 ...
            print(-dist[node][-K])  # K 번째 작은 경로의 비용
