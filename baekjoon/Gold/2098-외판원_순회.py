# https://velog.io/@dltmdrl1244/알고리즘-외판원-순회TSP-알고리즘
# https://velog.io/@e_juhee/python-백준-2098-외판원-순회-DP-비트마스킹-lso2bk58
import sys

n = int(sys.stdin.readline())
INF = 2147000000

# 노드 i에서 노드 j로 가는 비용(거리) 입력
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 점 좌표
# dp[i][j] : i = 내 위치, j : 아직 방문하지 않은, 방문해야 할 노드 정보
# 들어가는 값은 남은 점들을 최적 경로로 돌았을 때의 총 거리
# dp = [[INF] * (1 << n) for _ in range(n)]

dp = dict()


def dfs(now, visited):
    # start : 현재 내 위치
    # visited : 방문 여부 정보를 담고 있음. 해당 비트가 0이면 방문하지 않은 것, 1이면 방문한 것
    if visited == (1 << n) - 1:  # 모든 정점을 방문한 상태라면
        if graph[now][0] != 0:  # 시작점에서 0번 노드(최초 출발점)으로 돌아갈 수 있으면
            # dp[start][visited] = graph[start][0]  # 시작점에서 0번 노드(최초 출발점)으로 돌아가는 비용 저장
            return graph[now][0]  # 시작점에서 0번 노드(최초 출발점)으로 돌아가는 비용 반환
        else:
            return INF  # 못 돌아가면 무한대 반환

    # 메모이제이션 활용
    if (now, visited) in dp:
        return dp[(now, visited)]  # now까지 방문한 최소 비용

    min_cost = INF
    for i in range(1, n):  # 0번 노드는 최초 입력값이므로 1번 노드부터 시작
        if graph[now][i] == 0 or visited & (1 << i):  # 비용이 0이어서 갈 수 없거나, 방문한 점이라면 건너뛴다
            continue
        # 현재 노드에서 그 다음 노드까지의 거리 + 그 다음 노드에 방문하고 나서 남은 점들을 최적 경로로 돌았을 때의 거리
        # 의 합이 가장 작은 점이 현재 visited 상태 최적 경로 상의 다음 점이 될 것이다.
        startToiCost = graph[now][i] + dfs(i, visited | (1 << i))
        min_cost = min(min_cost, startToiCost)

    dp[(now, visited)] = min_cost
    return min_cost  # 현재 노드까지 방문하는 비용 반환


print(dfs(0, 1))
