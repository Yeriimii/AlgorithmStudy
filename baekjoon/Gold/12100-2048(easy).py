import sys
import copy

N = int(input())
board = []
res = 0

for _ in range(N):
    board.append([int(x) for x in sys.stdin.readline().rstrip().split()])


def left(copied_board):
    for i in range(N):
        cursor = 0
        for j in range(1, N):
            if copied_board[i][j] != 0:  # 0이 아닌 값이
                tmp = copied_board[i][j]
                copied_board[i][j] = 0  # 일단 비워질꺼니까 0으로 바꿈

                if copied_board[i][cursor] == 0:  # 비어있으면
                    copied_board[i][cursor] = tmp  # 옮긴다

                elif copied_board[i][cursor] == tmp:  # 같으면
                    copied_board[i][cursor] *= 2  # 합친다
                    cursor += 1
                else:  # 비어있지도 않고 다른 값일때
                    cursor += 1  # pass
                    copied_board[i][cursor] = tmp  # 바로 옆에 붙임

    return copied_board


def right(copied_board):
    for i in range(N):
        cursor = N - 1
        for j in range(N - 1, -1, -1):

            if copied_board[i][j] != 0:
                tmp = copied_board[i][j]
                copied_board[i][j] = 0

                if copied_board[i][cursor] == 0:
                    copied_board[i][cursor] = tmp

                elif copied_board[i][cursor] == tmp:
                    copied_board[i][cursor] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    copied_board[i][cursor] = tmp
    return copied_board


def up(copied_board):
    for j in range(N):
        cursor = 0
        for i in range(N):
            if copied_board[i][j] != 0:
                tmp = copied_board[i][j]
                copied_board[i][j] = 0

                if copied_board[cursor][j] == 0:
                    copied_board[cursor][j] = tmp

                elif copied_board[cursor][j] == tmp:
                    copied_board[cursor][j] *= 2
                    cursor += 1

                else:
                    cursor += 1
                    copied_board[cursor][j] = tmp
    return copied_board


def down(copied_board):
    for j in range(N):
        cursor = N - 1
        for i in range(N - 1, -1, -1):
            if copied_board[i][j] != 0:
                tmp = copied_board[i][j]
                copied_board[i][j] = 0

                if copied_board[cursor][j] == 0:
                    copied_board[cursor][j] = tmp

                elif copied_board[cursor][j] == tmp:
                    copied_board[cursor][j] *= 2
                    cursor -= 1

                else:
                    cursor -= 1
                    copied_board[cursor][j] = tmp
    return copied_board


def dfs(n, arr):
    global res
    if n == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j] > res:
                    res = arr[i][j]
        return

    for i in range(4):
        copy_arr = copy.deepcopy(arr)
        if i == 0:
            dfs(n + 1, left(copy_arr))
        elif i == 1:
            dfs(n + 1, right(copy_arr))
        elif i == 2:
            dfs(n + 1, up(copy_arr))
        else:
            dfs(n + 1, down(copy_arr))


dfs(0, board)
print(res)
