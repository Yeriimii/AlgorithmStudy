from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
dis = [[0]*m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Q = deque()
Q.append((0, 0))
dis[0][0] = 1
while Q:
    cur = Q.popleft()
    for i in range(4):
        xx = cur[0] + dx[i]
        yy = cur[1] + dy[i]
        if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 1:
            board[xx][yy] = 0
            Q.append((xx, yy))
            dis[xx][yy] = dis[cur[0]][cur[1]] + 1
print(dis[n-1][m-1])
