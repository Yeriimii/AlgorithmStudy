import sys
import heapq

input = sys.stdin.readline

# 오름차순 힙 정렬 (최소 힙 = 우선순위 큐)
def heapsort(iterable):
    '''
    단계마다 방문하지 않은 노드 중에서
    최단거리가 가장 짧은 노드를 선택하기 위해
    heap 자료구조 선택
    '''
    h = []  # 최소 힙
    result = []  # 결과 반환 리스트
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내서 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result

def dijkstra(src: int):
    q = []  # 우선순위 큐
    # Queue에 시작 노드로 가기 위한 최단 경로는 0 삽입
    heapq.heappush(q, (0, src))  # (자기 자신과의 거리, 자기 노드)
    distance[src] = 0
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


if __name__ == '__main__':
    INF = 2147000000
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    distance = [INF for _ in range(v + 1)]
    start = int(input())
    for _ in range(e):
        a, b, val = map(int, input().split())
        graph[a].append((b, val))
    dijkstra(start)

    # 모든 노드로 가기 위한 최단 거리를 출력
    for i in range(1, v+1):
        # 도달할 수 없는 경우 INF 출력
        if distance[i] == INF:
            print("INF")
        # 도달할 수 있으면 거리 출력
        else:
            print(distance[i])
