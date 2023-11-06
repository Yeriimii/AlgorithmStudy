import sys

sys.setrecursionlimit(10 ** 6)


def dfs(L, s):
    global res
    if L == n // 2:
        teamStartStat = 0
        teamLinkStat = 0

        for i in range(n):
            for j in range(i+1, n):
                if visited[i] == 1 and visited[j] == 1:
                    teamStartStat += S[i][j] + S[j][i]
                elif visited[i] == 0 and visited[j] == 0:
                    teamLinkStat += S[i][j] + S[j][i]
        cha = abs(teamStartStat - teamLinkStat)
        if res > cha:
            res = cha
    else:
        for i in range(s, n):
            if visited[i] == 0:
                visited[i] = 1
                dfs(L + 1, i + 1)
                visited[i] = 0


if __name__ == '__main__':
    n = int(input())
    S = [list(map(int, input().split())) for _ in range(n)]
    res = 2147000000
    visited = [0] * n
    visited[0] = 1
    dfs(1, 1)
    print(res)
