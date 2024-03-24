import copy
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
research_map = [list(map(int, input().split())) for _ in range(N)]
viruses = list()
res_time = float('inf')
infect_time = []

# virus 좌표들
for i in range(N):
    for j in range(N):
        if research_map[i][j] == 2:
            viruses.append((i, j))


def dfs(L: int, start: int, virus_pos: list):
    global res_time

    if L == M:
        infected_board, infection_time = infect(virus_pos, copy.deepcopy(research_map))
        if check(infected_board):
            res_time = min(res_time, infection_time)
    else:
        for i in range(start, len(viruses)):
            virus_pos.append(viruses[i])
            dfs(L + 1, i + 1, virus_pos)
            virus_pos.pop()


def infect(virus_pos_list: list, board: list[list[int]]):
    _infect_time = [[-1 for _ in range(N)] for _ in range(N)]
    for _x, _y in virus_pos_list:
        _infect_time[_x][_y] = 0
    Q = deque(virus_pos_list)
    total_time = 0
    while Q:
        x, y = Q.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if board[nx][ny] == 0 and _infect_time[nx][ny] == -1:
                board[nx][ny] = 2
                _infect_time[nx][ny] = _infect_time[x][y] + 1
                total_time = max(total_time, _infect_time[x][y] + 1)
                Q.append((nx, ny))
            if board[nx][ny] == 2 and _infect_time[nx][ny] == -1:
                _infect_time[nx][ny] = _infect_time[x][y] + 1
                Q.append((nx, ny))
    return board, total_time


def check(board: list[list[int]]):
    return all(0 not in row for row in board)


virus_use = [False for _ in range(len(viruses))]
dfs(0, 0, [])
if res_time == float('inf'):
    print(-1)
else:
    print(res_time)
