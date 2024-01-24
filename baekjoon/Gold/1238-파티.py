import sys
import heapq

input = sys.stdin.readline


def dijkstra(start):
    q = []
    distance = [INF for _ in range(N + 1)]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리에 있는 노드 정보 꺼내기
        now_dist, now_node = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드면 무시
        if distance[now_node] < now_dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next_node, next_dist in graph[now_node]:
            cost = now_dist + next_dist
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 갱신
            if cost < distance[next_node]:
                distance[next_node] = cost
                # 인접한 노드를 우선순위 큐에 삽입
                heapq.heappush(q, (cost, next_node))
    return distance


if __name__ == '__main__':
    INF = float('inf')
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, val = map(int, input().split())
        graph[a].append((b, val))

    res = 0
    for i in range(1, N + 1):
        i_distance = dijkstra(i)
        back = dijkstra(X)
        res = max(res, i_distance[X] + back[i])
    print(res)