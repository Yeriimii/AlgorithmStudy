import sys
sys.setrecursionlimit(10**6)


def dfs(x, y, is_abnormal):
    cur = board[x][y]  # 현재 좌표의 색
    visit[x][y][is_abnormal] = 1

    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0 <= xx < n and 0 <= yy < n and visit[xx][yy][is_abnormal] == 0:
            if cur == board[xx][yy]:
                dfs(xx, yy, is_abnormal)


if __name__ == "__main__":
    n = int(input())
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    board = [' '.join(input()).split() for _ in range(n)]
    visit = [[[0, 0] for _ in range(n)] for _ in range(n)]
    res_normal = 0
    res_abnormal = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j][0] == 0:
                dfs(i, j, 0)
                res_normal += 1

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'G':
                board[i][j] = 'R'

    for i in range(n):
        for j in range(n):
            if visit[i][j][1] == 0:
                dfs(i, j, 1)
                res_abnormal += 1

    print(res_normal, res_abnormal)
