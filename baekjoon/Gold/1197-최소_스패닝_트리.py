import sys
import heapq

'''Prim 알고리즘: 전체 노드들을 연결할 때 사용한다. (간선이 많을 때)
1. 임의의 정점을 선택
2. 해당 정점에서 갈 수 있는 간선을 minheap에 넣는다.
3. 최소값을 뽑아 해당 정점을 방문 안했다면 선택한다.
'''
input = sys.stdin.readline

V, E = map(int, input().split())
visited = [False] * (V + 1)  # 방문 여부 확인
Elist = [[] for _ in range(V + 1)]  # 간선 저장
# 1번 노드는 자기 자신으로 가는 거리가 0 임을 우선순위 큐에 삽입
heap = [[0, 1]]
for _ in range(E):
    start_node, end_node, weight = map(int, input().split())
    Elist[start_node].append([weight, end_node])  # s -> e 연결(가중치 w)
    Elist[end_node].append([weight, start_node])  # e -> s 연결(가중치 w)

answer = 0
cnt = 0
while heap:
    if cnt == V:  # 중단점: 모든 노드에 방문한 횟수 == 모든 노드 개수
        break
    weight, start_node = heapq.heappop(heap)  # 가중치, 현재 노드
    if not visited[start_node]:  # 각 노드당 한 번씩만 방문
        visited[start_node] = True
        answer += weight  # 연결 거리 누적 합
        cnt += 1  # 노드 방문 추가
        # 현재 노드와 연결된 노드들을 우선순위 큐에 삽입
        for next_node in Elist[start_node]:
            heapq.heappush(heap, next_node)

print(answer)
