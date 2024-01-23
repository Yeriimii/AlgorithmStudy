from collections import deque

INF = float('inf')
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
now_time = 0

init_size = 2
shark = [init_size, 0]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def size_up():
    global shark
    size, exp = shark
    if size == exp:
        shark = [size + 1, 0]


def calculate_distance_and_pos(r, c):
    candidates = []
    for _i in range(N):
        for _j in range(N):
            if board[_i][_j] != 9 and board[_i][_j] != 0 and board[_i][_j] < shark[0]:
                _dist = abs(_i - r) + abs(_j - c)
                candidates.append([_dist, _i, _j])
    candidates.sort(key=lambda x: (x[0], x[1], x[2]))
    return candidates


def move(r, c, _target_pos):
    visited = [[False for _ in range(N)] for _ in range(N)]
    Q = deque()
    Q.append((r, c, 0))
    visited[r][c] = True
    while Q:
        cur_r, cur_c, time = Q.popleft()
        if cur_r == _target_pos[0] and cur_c == _target_pos[1]:
            return time
        for k in range(4):
            nr = cur_r + dr[k]
            nc = cur_c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and board[nr][nc] <= shark[0]:
                visited[nr][nc] = True
                Q.append((nr, nc, time + 1))
    return -1


def eat(r, c, time, _target_r, _target_c):
    global now_time, shark
    now_time += time
    shark[1] += 1
    size_up()
    board[r][c] = 0
    board[_target_r][_target_c] = 9


dQ = deque()
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            dQ.append((i, j))
            break

while dQ:
    now_r, now_c = dQ.popleft()
    targets = calculate_distance_and_pos(now_r, now_c)
    eat_candidates = []
    min_time = INF
    for target in targets:
        dist, target_r, target_c = target
        spend_time = move(now_r, now_c, (target_r, target_c))
        if spend_time != -1 and spend_time < min_time:
            min_time = spend_time
            eat_candidates.append([spend_time, target_r, target_c])
    if eat_candidates:
        eat_candidates.sort(reverse=True, key=lambda x: (x[0], x[1], x[2]))
        spend_time, target_r, target_c = eat_candidates.pop()
        eat(now_r, now_c, spend_time, target_r, target_c)
        dQ.append((target_r, target_c))
print(now_time)

