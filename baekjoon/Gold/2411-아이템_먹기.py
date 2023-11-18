import sys
from collections import deque

# sys.setrecursionlimit(10 ** 6)
#
input = sys.stdin.readline
#
#
# def dfs(x, y, level_pointer):
#     global res
#
#     if board[x][y] == 2:
#         level_pointer += 1
#
#     if x == n - 1 and y == m - 1:
#         res += 1
#     else:
#         if level_pointer < a:
#             ix, iy = item_level[level_pointer]
#         else:
#             ix, iy = n - 1, m - 1
#
#         for i in range(2):
#             xx = x + dx[i]
#             yy = y + dy[i]
#             if 0 <= xx < n and 0 <= yy < m and board[xx][yy] != 1 and xx <= ix and yy <= iy:
#                 dfs(xx, yy, level_pointer)
#
#     if board[x][y] == 2:
#         level_pointer -= 1
#
#
# def bfs(tx, ty):
#     global res
#
#     Q = deque()
#     Q.append((tx, ty, 0))
#     while Q:
#         x, y, level_pointer = Q.popleft()
#         if board[x][y] == 2:
#             level_pointer += 1
#         if x == n - 1 and y == m - 1:
#             # res += 1
#             break
#         if level_pointer < a:
#             ix, iy = item_level[level_pointer]
#         else:
#             ix, iy = n - 1, m - 1
#         cnt = 0
#         for i in range(2):
#             xx = x + dx[i]
#             yy = y + dy[i]
#             if 0 <= xx < n and 0 <= yy < m and board[xx][yy] != 1 and xx <= ix and yy <= iy:
#                 if not visited[xx][yy]:
#                     visited[xx][yy] = True
#                     Q.append((xx, yy, level_pointer))
#                     cnt += 1
#         if cnt == 2:
#             res += 2


if __name__ == '__main__':
    n, m, a, b = map(int, input().split())
    dx = [1, 0]
    dy = [0, 1]

    board = [[0] * (m + 1) for _ in range(n + 1)]
    visited = [[0] * (m + 1) for _ in range(n + 1)]
    item_level = list()

    for k in range(a):
        x, y = map(int, input().split())
        board[x][y] = 2  # item
        item_level.append((x, y))

    for k in range(b):
        x, y = map(int, input().split())
        board[x][y] = -1

    item_level.sort(key=lambda x: (x[0], x[1]))

    res = 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    visited[1][1] = True
    pointer = 0
    Q = deque()
    Q.append((1, 1))
    while Q:
        i, j = Q.popleft()

        if board[i][j] == 2:
            pointer += 1

        if pointer < a:
            ix = item_level[pointer][0]
            iy = item_level[pointer][1]
        else:
            ix = n
            iy = m

        for k in range(2):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx <= n and ny <= m and board[nx][ny] != -1:
                if nx <= ix and ny <= iy and (not visited[nx][ny] or dp[nx][ny] <= dp[nx][ny] + dp[i][j]):
                    dp[nx][ny] += dp[i][j]
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        Q.append((nx, ny))

    res = dp[n][m]
    print(res)
