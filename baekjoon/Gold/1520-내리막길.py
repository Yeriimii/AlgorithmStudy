dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]
res = 0


def dfs(r, c):
    if r == N - 1 and c == M - 1:
        return 1

    if dp[r][c] != -1:
        return dp[r][c]

    path = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] < graph[r][c]:
            path += dfs(nr, nc)

    dp[r][c] = path
    return dp[r][c]


print(dfs(0, 0))
