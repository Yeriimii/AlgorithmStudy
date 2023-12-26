import copy

up = 0
right = 1
down = 2
left = 3
directions = [up, right, down, left]

# 입력 받기
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# cctv의 좌표 저장
cctv_pos_list = []
for i in range(N):
    for j in range(M):
        if board[i][j] != 0 and board[i][j] != 6:
            cctv_pos_list.append([board[i][j], (i, j)])


def change(cctv_pos, _board, direction):
    nr = None
    nc = None

    r, c = cctv_pos

    # direction: 0 up / 1 right / 2 down / 3 left
    if direction == up:
        nr = r - 1
        nc = c
    elif direction == right:
        nr = r
        nc = c + 1
    elif direction == down:
        nr = r + 1
        nc = c
    elif direction == left:
        nr = r
        nc = c - 1

    if 0 <= nr < N and 0 <= nc < M and _board[nr][nc] != 6:
        _board[nr][nc] = '#'
        change((nr, nc), _board, direction)


def find_zero(_board):
    cnt = 0
    for x in range(N):
        for y in range(M):
            if _board[x][y] == 0:
                cnt += 1
    return cnt


def dfs(L, _board):
    global res

    if L == len(cctv_pos_list):
        res = min(res, find_zero(_board))
    else:
        cctv_type = cctv_pos_list[L][0]
        cctv_pos = cctv_pos_list[L][1]

        if cctv_type == 1:
            for i in range(4):
                _copied_board = copy.deepcopy(_board)
                change(cctv_pos, _copied_board, directions[i])
                dfs(L + 1, _copied_board)
        elif cctv_type == 2:
            for i in range(2):
                _copied_board = copy.deepcopy(_board)
                change(cctv_pos, _copied_board, directions[i])
                change(cctv_pos, _copied_board, directions[i + 2])
                dfs(L + 1, _copied_board)
        elif cctv_type == 3:
            for i in range(4):
                _copied_board = copy.deepcopy(_board)
                change(cctv_pos, _copied_board, directions[i % 4])
                change(cctv_pos, _copied_board, directions[(i + 1) % 4])
                dfs(L + 1, _copied_board)
        elif cctv_type == 4:
            for i in range(4):
                _copied_board = copy.deepcopy(_board)
                change(cctv_pos, _copied_board, directions[i % 4])
                change(cctv_pos, _copied_board, directions[(i + 1) % 4])
                change(cctv_pos, _copied_board, directions[(i + 2) % 4])
                dfs(L + 1, _copied_board)
        elif cctv_type == 5:
            _copied_board = copy.deepcopy(_board)
            for i in range(4):
                change(cctv_pos, _copied_board, directions[i])
            dfs(L + 1, _copied_board)


res = 64
dfs(0, board)
print(res)
