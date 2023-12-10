# 최소 신장 트리 = 최소 스패닝 트리 : 크루스칼
import sys

input = sys.stdin.readline


def find(n):
    if parent[n] != n:  # 노드 n의 부모 노드가 자기 자신이 아니면
        parent[n] = find(parent[n])  # 노드 n의 부모 노드 = 최상위 부모 노드 탐색 재귀함수
    return parent[n]  # 현재 노드 n의 최상위 부모 노드 return


def union(a, b):
    a = find(a)  # 노드 a의 최상위 노드 탐색
    b = find(b)  # 노드 b의 최상위 노드 탐색

    if a < b:
        parent[b] = a  # 노드b의 부모 노드 a로 갱신
    else:  # a > b 이면
        parent[a] = b  # 노드a의 부모 노드 b로 갱신


N, M = map(int, input().split())

edges = []
parent = list(range(N + 1))  # 부모를 저장
for _ in range(M):
    A, B, cost = map(int, input().split())
    edges.append((A, B, cost))
edges.sort(key=lambda x: x[2])  # 유지비용을 기준으로 오름차순으로 정렬

answer = 0
last_edge = 0  # 마지막에 연결된 마을의 유지비용을 저장
for a, b, cost in edges:
    if find(a) != find(b):  # 각 노드의 최상위 부모가 다르다면
        union(a, b)  # 하나의 집합에 추가한다
        answer += cost  # 마을의 연결 비용을 계속 더해준다
        last_edge = cost  # 마지막에 연결된 마을의 연결 비용을 저장
print(answer - last_edge)  # 마지막에 연결된 마을의 유지비용을 빼주면 정답
