import copy
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
directions = [LEFT, RIGHT, UP, DOWN]


def has_meet_student(_board: list[list]):
    global T_pos_list
    Q = deque()
    flag = False
    for direction in directions:
        visited = [[False for _ in range(N)] for _ in range(N)]
        for r, c in T_pos_list:
            Q.append((r, c, direction))
            visited[r][c] = True
        while Q:
            cur_r, cur_c, direction = Q.popleft()
            if _board[cur_r][cur_c] == 'S':
                flag = True
            else:
                nc, nr = calc_next_pos(cur_c, cur_r, direction)
                if (0 <= nr < N and 0 <= nc < N and not visited[nr][nc]
                        and (_board[nr][nc] == 'X' or _board[nr][nc] == 'S')):
                    visited[nr][nc] = True
                    Q.append((nr, nc, direction))
    return flag


def calc_next_pos(cur_c, cur_r, direction):
    nr = None
    nc = None
    if direction == LEFT:
        nr = cur_r
        nc = cur_c - 1
    elif direction == RIGHT:
        nr = cur_r
        nc = cur_c + 1
    elif direction == UP:
        nr = cur_r - 1
        nc = cur_c
    elif direction == DOWN:
        nr = cur_r + 1
        nc = cur_c
    return nc, nr


def put_obstacle(L, _board: list[list]):
    global has_meet
    if has_meet is False:
        return

    if L == 3:
        result = has_meet_student(_board)
        if not result:
            has_meet = False
    else:
        for r in range(N):
            for c in range(N):
                if _board[r][c] == "X" and not obstacle_visited[r][c]:
                    _board[r][c] = "O"
                    obstacle_visited[r][c] = True
                    put_obstacle(L + 1, copy.deepcopy(_board))
                    obstacle_visited[r][c] = False
                    _board[r][c] = "X"


N = int(input())
board = [input().split() for _ in range(N)]
obstacle_visited = [[False for _ in range(N)] for _ in range(N)]
has_meet = True

# 선생님들 좌표 저장
T_pos_list = []
for i in range(N):
    for j in range(N):
        if board[i][j] == "T":
            T_pos_list.append((i, j))

put_obstacle(0, copy.deepcopy(board))
if has_meet is False:
    print("YES")
elif has_meet:
    print("NO")
