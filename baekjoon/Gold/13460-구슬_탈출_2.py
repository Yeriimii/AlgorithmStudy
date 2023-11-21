# import copy
# from collections import deque
#
#
# def is_game_over(x: int, y: int):
#     if x == hall_pos[0] and y == hall_pos[1]:
#         return True
#     else:
#         return False
#
#
# def has_goal(x: int, y: int):
#     return x == hall_pos[0] and y == hall_pos[1]
#
#
# def can_move(x: int, y: int, color: str, board):
#     if 0 > x or n <= x or 0 > y or m <= y:
#         return False
#     if color == 'R' and board[x][y][1] is True:
#         return False
#     return board[x][y][0] == 'O' or board[x][y][0] == '.'
#
#
# def move(x: int, direction_x: int, y: int, direction_y: int, color: str, copied_board):
#     nx = x + direction_x
#     ny = y + direction_y
#     copied_board[x][y][0] = '.'
#     if not can_move(x, y, color, copied_board):
#         return x, y, copied_board
#
#     if color == 'R' and copied_board[nx][ny][0] == '.':
#         copied_board[nx][ny][1] = True
#
#     if copied_board[nx][ny][0] == '.':
#         copied_board[nx][ny][0] = color
#
#     if copied_board[nx][ny][0] == 'O':
#         return nx, ny, copied_board
#
#     if can_move(nx + direction_x, ny + direction_y, color, copied_board):
#         nx, ny, copied_board = move(nx, direction_x, ny, direction_y, color, copied_board)
#         return nx, ny, copied_board
#
#     return nx, ny, copied_board
#
#
# n, m = map(int, input().split())
# r_board = [[['', False] for _ in range(m)] for _ in range(n)]
#
# r_pos = (0, 0)
# b_pos = (0, 0)
# hall_pos = (0, 0)
#
# for i in range(n):
#     info = ' '.join(input()).split()
#     for j in range(m):
#         r_board[i][j][0] = info[j]
#         if info[j] == 'R':
#             r_pos = (i, j)
#         elif info[j] == 'B':
#             b_pos = (i, j)
#         elif info[j] == 'O':
#             hall_pos = (i, j)
#
# r_board[r_pos[0]][r_pos[1]][1] = True
#
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
#
# res = 2147000000
#
# Q = deque()
# Q.append((r_pos[0], r_pos[1], b_pos[0], b_pos[1], r_board, 0))
# ban = set()
# while Q:
#     rx, ry, bx, by, board, movement = Q.popleft()
#     if is_game_over(bx, by):
#         continue
#     if has_goal(rx, ry):
#         res = min(res, movement)
#         continue
#
#     for i in range(4):
#         nrx = rx + dx[i]
#         nry = ry + dy[i]
#
#         nbx = bx + dx[i]
#         nby = by + dy[i]
#
#         # 빨강 먼저 움직일 수 있을 때
#         tmp_copied_board = copy.deepcopy(board)
#         if can_move(nrx, nry, 'R', tmp_copied_board):
#             after_moved_nrx, after_moved_nry, tmp_copied_board = move(rx, nrx - rx, ry, nry - ry, 'R', tmp_copied_board)
#             after_moved_nbx, after_moved_nby = bx, by
#             if can_move(nbx, nby, 'B', tmp_copied_board):
#                 after_moved_nbx, after_moved_nby, tmp_copied_board = move(bx, nbx - bx, by, nby - by, 'B', tmp_copied_board)
#             Q.append((after_moved_nrx, after_moved_nry, after_moved_nbx, after_moved_nby, tmp_copied_board, movement + 1))
#
#         # 파랑을 먼저 움직일 때
#         tmp_copied_board = copy.deepcopy(board)
#         if can_move(nbx, nby, 'B', tmp_copied_board):
#             after_moved_nbx, after_moved_nby, tmp_copied_board = move(bx, nbx - bx, by, nby - by, 'B', tmp_copied_board)
#             if is_game_over(after_moved_nbx, after_moved_nby):
#                 ban
#             if not is_game_over(after_moved_nbx, after_moved_nby):
#                 after_moved_nrx, after_moved_nry = rx, ry
#                 if can_move(nrx, nry, 'R', tmp_copied_board):  # 게임 오버가 아니면 일단 같은 방향으로 빨강을 움직여보기
#                     after_moved_nrx, after_moved_nry, tmp_copied_board = move(rx, nrx - rx, ry, nry - ry, 'R', tmp_copied_board)
#                 for j in range(4):
#                     nrx = rx + dx[j]
#                     nry = ry + dy[j]
#                     if can_move(nrx, nry, 'R', tmp_copied_board):  # 빨강이 이동가능한 범위가 나오면 저장
#                         Q.append((after_moved_nrx, after_moved_nry, after_moved_nbx, after_moved_nby, tmp_copied_board, movement + 1))
#
#
# if res == 2147000000:
#     print(-1)
# else:
#     print(res)


from collections import deque
import sys

# n = 세로 크기, m = 가로 크기
# 목표는 빨간 구슬 구멍으로 빼내기 / 파란 구슬이 들어가면 안됨!
# 공은 동시에 움직인다.
# n = 세로 / m = 가로
n, m = map(int, input().split())

# . = 빈칸 / # = 장애물, 벽 / o = 구멍
# 그래프 입력받기
graph = []
R = [0, 0]
B = [0, 0]
target = [0, 0]
for a in range(n):
    sub = list(input())
    graph.append(sub)
    for b in range(m):
        if sub[b] == 'R':
            R = [a, b]
        elif sub[b] == 'B':
            B = [a, b]
        elif sub[b] == 'O':
            target = [a, b]

answer_mark = False

# 상, 하, 좌, 우
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()

# R 좌표, B 좌표
q.append((R[0], R[1], B[0], B[1], 0))

visited = set()
visited.add((R[0], R[1], B[0], B[1]))

while q:
    rx, ry, bx, by, cnt = q.popleft()

    if graph[rx][ry] == 'O':
        print(cnt)
        answer_mark = True
        break

    if cnt >= 10:
        continue

    # r, b 움직이기
    for k in range(4):
        r_move = 0
        b_move = 0

        # r 움직이기
        nrx = rx + dx[k]
        nry = ry + dy[k]

        while 1:
            if graph[nrx][nry] == '#':
                nrx -= dx[k]
                nry -= dy[k]
                break
            elif graph[nrx][nry] == 'O':
                break

            nrx += dx[k]
            nry += dy[k]

            r_move += 1

        # b 움직이기
        nbx = bx + dx[k]
        nby = by + dy[k]
        while 1:
            if graph[nbx][nby] == '#':
                nbx -= dx[k]
                nby -= dy[k]
                break
            elif graph[nbx][nby] == 'O':
                break
            nbx += dx[k]
            nby += dy[k]
            b_move += 1

        # B 빠지면 안됨
        if graph[nbx][nby] == 'O':
            continue

        # r, b가 같은 경우 / O일때 아닐때
        if nrx == nbx and nry == nby:

            if r_move > b_move:
                nrx -= dx[k]
                nry -= dy[k]
            else:
                nbx -= dx[k]
                nby -= dy[k]

        if not (nrx, nry, nbx, nby) in visited:
            visited.add((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, cnt + 1))

if answer_mark == False:
    print(-1)
