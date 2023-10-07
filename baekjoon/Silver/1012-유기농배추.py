from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    board = [[0]*m for _ in range(n)]
    res = 0
    for _ in range(k):
        a, b = map(int, input().split())
        board[b][a] = 1
    for i in range(n):
        for j in range(m):
            Q = deque()
            if board[i][j] == 1:
                Q.append((i, j))
                while Q:
                    cur = Q.popleft()
                    for t in range(4):
                        xx = cur[0] + dx[t]
                        yy = cur[1] + dy[t]
                        if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 1:
                            board[xx][yy] = 0
                            Q.append((xx, yy))
                res += 1
    print(res)
