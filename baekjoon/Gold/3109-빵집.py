import sys

# 왼쪽 대각선 위, 왼쪽, 왼쪽 대각선 아래
drc = [(-1, 1), (0, 1), (1, 1)]


def put_pipe(r, c):
    global board, cnt, flag

    if c == C - 1:
        cnt += 1
        flag = True
    else:
        for k in range(3):
            nr = r + drc[k][0]
            nc = c + drc[k][1]
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == '.':
                board[nr][nc] = 'x'
                put_pipe(nr, nc)
                if flag:
                    break


input = sys.stdin.readline

R, C = map(int, input().strip().split())
flag = False
board = [' '.join(input().strip()).split() for _ in range(R)]
cnt = 0

for i in range(R):
    put_pipe(i, 0)
    flag = False
print(cnt)
