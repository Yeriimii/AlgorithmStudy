import copy
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    global res

    copy_board = copy.deepcopy(board)
    Q = deque()
    for i in range(n):
        for j in range(m):
            if copy_board[i][j] == 2:
                Q.append((i, j))

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and copy_board[xx][yy] == 0:
                copy_board[xx][yy] = 2
                Q.append((xx, yy))

    cnt = 0
    for i in range(n):
        cnt += copy_board[i].count(0)

    res = max(res, cnt)


def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    else:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    board[i][j] = 1
                    make_wall(cnt + 1)
                    board[i][j] = 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = -2147000000
    make_wall(0)
    print(res)
