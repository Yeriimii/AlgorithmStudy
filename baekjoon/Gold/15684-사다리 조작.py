import sys

input = sys.stdin.readline


def check():
    global board

    for i in range(1, N + 1):
        cur_col = i
        for j in range(1, H + 1):
            if board[j][cur_col] == 1:
                cur_col += 1
            elif board[j][cur_col - 1] == 1:
                cur_col -= 1
        if i != cur_col:
            return False
    return True


def dfs(ladder_use_cnt, num):
    global min_res

    if ladder_use_cnt >= min_res:
        return

    if check():
        min_res = ladder_use_cnt
        return

    # combination
    for idx in range(num + 1, len(candidates)):
        r, c = candidates[idx]
        if board[r][c - 1] == 0 and board[r][c + 1] == 0:
            board[r][c] = 1
            dfs(ladder_use_cnt + 1, idx)
            board[r][c] = 0


N, M, H = map(int, input().split())
board = [[0 for _ in range(N + 1)] for _ in range(H + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a][b] = 1

# 사다리를 놓을 수 있는 후보 지점 추출
candidates = []
for i in range(1, H + 1):
    for j in range(1, N):
        if board[i][j] == 0 and board[i][j - 1] == 0 and board[i][j + 1] == 0:
            candidates.append([i, j])

min_res = 4
dfs(0, -1)
if min_res < 4:
    print(min_res)
else:
    print(-1)
