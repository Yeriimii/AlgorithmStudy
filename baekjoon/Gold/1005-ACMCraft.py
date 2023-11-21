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
