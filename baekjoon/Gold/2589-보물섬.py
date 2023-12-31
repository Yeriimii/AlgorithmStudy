from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    distance = [[0] * M for _ in range(N)]
    distance[x][y] = 1
    final_distance = 0
    while Q:
        xx, yy = Q.popleft()
        for k in range(4):
            nx = xx + dx[k]
            ny = yy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 'L' and distance[nx][ny] == 0:
                distance[nx][ny] = distance[xx][yy] + 1
                final_distance = max(final_distance, distance[nx][ny])
                Q.append((nx, ny))

    return final_distance - 1


N, M = map(int, input().split())
board = [' '.join(input()).split() for _ in range(N)]
res = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            res = max(res, bfs(i, j))

print(res)
