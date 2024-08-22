# import sys
#
# if __name__ == '__main__':
#     q = list()
#     n, m = map(int, input().split())
#     degree = [0 for _ in range(n + 1)]
#
#     for i in range(m):
#         a, b = map(int, sys.stdin.readline().rstrip().split())
#         degree[a] += 1
#
#     answer = list()
#
#     min_v = min(degree[1:])
#     for i in range(1, n + 1):
#         if degree[i] == min_v:
#             answer.append(i)
#
#     print(*answer)

# 위상 정렬로 풀면 안되는 이유: 순환이 생기면 문제가 생김. 위상 정렬은 비순환 방향 그래프에서만 사용 가능.

# 아래 방법은 pypy3 만 통과 가능
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(start):
    visited = [False for _ in range(n + 1)]
    visited[start] = True

    queue = deque([start])
    count = 1

    while queue:
        x = queue.popleft()
        for next_node in graph[x]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                count += 1
    return count


max_cnt = 1
for i in range(1, n + 1):  # 컴퓨터 건건으로 탐색
    cnt = bfs(i)
    if cnt > max_cnt:  # 최장 길이 갱신
        max_cnt = cnt
        answer.clear()
        answer.append(i)
    elif cnt == max_cnt:
        answer.append(i)

print(*answer)
