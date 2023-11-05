import heapq
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, K = map(int, input().split())
board = [[0] + list(map(int, input().split())) for _ in range(N)]
board.insert(0, [0] * (N + 1))
S, X, Y = map(int, input().split())
heap = list()
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if board[i][j] != 0:
            heapq.heappush(heap, (board[i][j], i, j))
Q = deque()
while S >= 0:
    while heap:
        Q.append(heapq.heappop(heap))
    while Q:
        virus, x, y = Q.popleft()
        if S == 0:
            break
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 < xx <= N and 0 < yy <= N and board[xx][yy] == 0:
                board[xx][yy] = virus
                heapq.heappush(heap, (virus, xx, yy))
    S -= 1
print(board[X][Y])
