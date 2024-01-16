import copy


def is_game_over(_board):
    for i in range(N):
        for j in range(M):
            if _board[i][j] == 1:
                return False
    return True


def hunt(_hunt_cnt, _hunters, _board):
    hunt_set = set()
    for hunter in _hunters:
        remove_candidate = set()
        range_r = hunter[0]
        range_c = hunter[1]
        for i in range(N - 1, - 1, -1):
            for j in range(M):
                if _board[i][j] == 1:
                    dist = (abs(range_r - i) + abs(range_c - j))
                    if dist <= D:
                        remove_candidate.add((dist, i, j))
        if remove_candidate:
            dist, r, c = min(remove_candidate, key=lambda x: (x[0], x[2], x[1]))
            hunt_set.add((r, c))
    for r, c in hunt_set:
        _hunt_cnt += 1
        _board[r][c] = 0
    return _hunt_cnt


def move_for_enemy(_board):
    for i in range(N - 1, -1, -1):
        for j in range(M):
            if i == N - 1:
                if _board[i][j] == 1:
                    _board[i][j] = 0
            elif 0 <= i < N - 1:
                if _board[i][j] == 1:
                    _board[i][j] = 0
                    _board[i + 1][j] = 1
    return _board


def put_hunter(L, s):
    global max_hunt_cnt, visited, hunters

    if L == 3:
        hunt_cnt = 0
        copy_board = copy.deepcopy(board)
        while not is_game_over(copy_board):
            hunt_cnt = hunt(hunt_cnt, hunters, copy_board)
            copy_board = move_for_enemy(copy_board)
        max_hunt_cnt = max(max_hunt_cnt, hunt_cnt)
    else:
        for i in range(s, M):
            if i < M and not visited[i]:
                visited[i] = True
                hunters.append((N, i))
                put_hunter(L + 1, i + 1)
                hunters.pop()
                visited[i] = False


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
hunters = []
max_hunt_cnt = 0
visited = [False for _ in range(M + 1)]
put_hunter(0, 0)
print(max_hunt_cnt)
