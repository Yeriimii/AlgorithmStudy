from collections import deque

# board = [[1] + list(map(int, input().split())) + [1] for _ in range(7)]
# board.insert(0, [1] * 9)
# board.insert(8, [1] * 9)
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# Q = deque()
# now = (1, 1)
# board[1][1] = 1
# Q.append(now)
# end = (7, 7)
# L = 0
# while now != end:
#     if not Q:
#         L = -1
#         break
#     size = len(Q)
#     for i in range(size):
#         now = Q.popleft()
#         if now == end:
#             break
#         for j in range(4):
#             x = now[0] + dx[j]
#             y = now[1] + dy[j]
#             if board[x][y] == 0:
#                 board[x][y] = 1
#                 Q.append((x, y))
#     else:
#         L += 1
# print(L)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = [list(map(int, input().split()))for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]
Q = deque()
Q.append((0, 0))
board[0][0] = 1
while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0:
            board[x][y] = 1  # 방문시 체크
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1  # 시작점에서 +1씩 증가 -> 시작점으로부터의 거리를 입력
            Q.append((x, y))
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])


