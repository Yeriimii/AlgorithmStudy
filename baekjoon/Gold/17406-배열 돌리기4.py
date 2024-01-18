import copy

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
rotate_operations = [list(map(int, input().split())) for _ in range(K)]
used_operation = [False for _ in range(K)]
min_v = 2147000000


def find_v(_arr):
    global min_v
    for row in _arr:
        min_v = min(min_v, sum(row))


def find_s_and_e(o):
    r, c, s = o
    start = (r - s - 1, c - s - 1)
    end = (r + s - 1, c + s - 1)
    return start, end


def execute_rotate(start: tuple, end: tuple, _arr: list[list]):
    if start == end:
        return _arr
    else:
        tmp_1 = _arr[start[0]][end[1]]
        tmp_2 = _arr[end[0]][start[1]]

        # 시작점의 행: 종료점의 열부터 (시작점의 열 - 1)까지
        for i in range(end[1], start[1], -1):
            _arr[start[0]][i] = _arr[start[0]][i - 1]

        # 종료점의 행: 시작점의 열부터 (종료점의 열 - 1)까지
        for i in range(start[1], end[1]):
            _arr[end[0]][i] = _arr[end[0]][i + 1]

        # 시작점의 열: 시점점의 행부터 (종료점의 행 - 2)까지
        for i in range(start[0], end[0] - 1):
            _arr[i][start[1]] = _arr[i + 1][start[1]]
        _arr[end[0] - 1][start[1]] = tmp_2

        # 종료점의 열: 종료점의 행부터 (시작점의 행 - 2)까지
        for i in range(end[0], start[0] + 1, -1):
            _arr[i][end[1]] = _arr[i - 1][end[1]]
        _arr[start[0] + 1][end[1]] = tmp_1

        next_start = (start[0] + 1, start[1] + 1)
        next_end = (end[0] - 1, end[1] - 1)
        return execute_rotate(next_start, next_end, _arr)


def dfs(L, _arr):
    if L == K:
        find_v(_arr)
    else:
        for i in range(K):
            if not used_operation[i]:
                used_operation[i] = True
                operation = rotate_operations[i]
                s, e = find_s_and_e(operation)
                rotated_arr = execute_rotate(s, e, copy.deepcopy(_arr))
                dfs(L + 1, rotated_arr)
                used_operation[i] = False


dfs(0, arr)
print(min_v)
