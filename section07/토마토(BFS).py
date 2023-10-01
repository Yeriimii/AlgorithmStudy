from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
Q = deque()
fx = 0
fy = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            Q.append((i, j))
if len(Q) == 0:
    print(-1)
else:
    while Q:
        size = len(Q)
        for _ in range(size):
            cur = Q.popleft()
            for k in range(4):
                x = cur[0] + dx[k]
                y = cur[1] + dy[k]
                if 0 <= x < n and 0 <= y < m and board[x][y] == 0:
                    board[x][y] = board[cur[0]][cur[1]] + 1
                    Q.append((x, y))
                    fx = x
                    fy = y
    for i in range(n):
        if 0 in board[i]:
            print(-1)
            break
    else:
        print(board[fx][fy]-1)

'''
최적화 풀이
'''
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dis = [[0] * m for _ in range(n)]
Q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            Q.append((i, j))
while Q:
    tmp = Q.popleft()
    for i in range(4):
        xx = tmp[0] + dx[i]
        yy = tmp[1] + dy[i]
        if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 0:
            board[xx][yy] = 1
            dis[xx][yy] = dis[tmp[0]][tmp[1]] + 1
            Q.append((xx, yy))
flag = 1
for i in range(n):  # 익지 않은 토마토가 하나라도 있다면 -> -1
    for j in range(m):
        if board[i][j] == 0:
            flag = 0
result = 0
if flag == 1:  # 다 익은 토마토 중 걸린 시간의 최대값 찾기
    for i in range(n):
        for j in range(m):
            if dis[i][j] > result:
                result = dis[i][j]  # 최대값 저장
    print(result)
else:
    print(-1)
