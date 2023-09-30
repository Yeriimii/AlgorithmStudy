from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
Q = deque()
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:  # 1로 시작하는 x, y 좌표
            board[i][j] = 0  # 방문 체크
            Q.append((i, j))  # Queue 추가
            while Q:
                tmp = Q.popleft()  # 탐색 시작점
                for k in range(8):  # 8 방향 탐색
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
                        board[x][y] = 0  # 방문 체크
                        Q.append((x, y))  # 탐색 시작점으로부터 다음 탐색 좌표 추가
            cnt += 1  # 탐색 종료시 섬 개수 카운트
print(cnt)
