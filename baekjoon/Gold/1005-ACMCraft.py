import heapq
import sys

input = sys.stdin.readline

T = int(input())

while T:
    T -= 1
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    Building = [[0, [], 0, 0] for i in range(N + 1)]  # 전입차수, 후입목록, 건설소요시간, 누적 건설시간
    for i in range(N):
        Building[i + 1][2] = D[i]

    for i in range(K):
        X, Y = map(int, input().split())
        Building[X][1].append(Y)
        Building[Y][0] += 1

    Q = []
    for i in range(1, N + 1):
        if Building[i][0] == 0:
            Building[i][3] = Building[i][2]
            heapq.heappush(Q, (0, i))

    while len(Q) > 0:
        _, B = heapq.heappop(Q)

        for target in Building[B][1]:
            Building[target][0] -= 1
            if Building[target][3] < Building[target][2] + Building[B][3]:
                Building[target][3] = Building[target][2] + Building[B][3]
            if Building[target][0] == 0:
                heapq.heappush(Q, (Building[target][3], target))
    W = int(input())
    print(Building[W][3])

from collections import deque
import sys

input = sys.stdin.readline


def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        cost = [0] + list(map(int, input().split()))
        link = [[] for _ in range(n + 1)]
        cntLink = [-1] + [0] * (n)
        for _ in range(k):
            a, b = map(int, input().split())
            link[a].append(b)
            cntLink[b] += 1
        end = int(input())

        # 시작 정점들 넣기
        dp = [0] * (n + 1)
        q = deque()
        for i in range(1, n + 1):
            if cntLink[i] == 0:
                q.append(i)
                dp[i] = cost[i]

        # 위상 정렬
        while q:
            curNode = q.popleft()
            for toNode in link[curNode]:
                cntLink[toNode] -= 1
                dp[toNode] = max(dp[toNode], dp[curNode] + cost[toNode])
                if cntLink[toNode] == 0:
                    q.append(toNode)

            # 목표 지점의 값을 구했음
            if cntLink[end] == 0:
                print(dp[end])
                break


solve()