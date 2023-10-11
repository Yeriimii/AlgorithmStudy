# import sys
#
# n, m = map(int, sys.stdin.readline().split())
# board = [[0] * (n+1)]
#
# for _ in range(n):
#     row = [0] + list(map(int, sys.stdin.readline().split()))
#     for j in range(1, n+1):
#         row[j] += row[j-1]
#     board.append(row)
#
# for _ in range(m):
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#     res = 0
#
#     for i in range(x1, x2+1):
#         res += board[i][y2] - board[i][y1-1]
#     print(res)

import sys

n, m = map(int, sys.stdin.readline().split())
board = [[0] * (n + 1)]

for _ in range(n):
    row = [0] + list(map(int, sys.stdin.readline().split()))
    board.append(row)

# 부분 합 계산
for i in range(1, n + 1):
    for j in range(1, n + 1):
        board[i][j] += board[i - 1][j] + board[i][j - 1] - board[i - 1][j - 1]

# 쿼리 처리
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    res = board[x2][y2] - board[x2][y1 - 1] - board[x1 - 1][y2] + board[x1 - 1][y1 - 1]

    print(res)
