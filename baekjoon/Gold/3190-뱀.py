from collections import deque

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
RIGHT = 'r'
DOWN = 'd'
LEFT = 'l'
UP = 'u'


def rotate(_direction, _c):
    if _direction == RIGHT:
        if _c == 'L':
            return UP
        else:
            return DOWN
    if _direction == LEFT:
        if _c == 'L':
            return DOWN
        else:
            return UP
    if _direction == UP:
        if _c == 'L':
            return LEFT
        else:
            return RIGHT
    if _direction == DOWN:
        if _c == 'L':
            return RIGHT
        else:
            return LEFT


def move_rc(_r, _c, _direction):
    if _direction == RIGHT:
        _r = _r
        _c = _c + 1
    elif _direction == LEFT:
        _r = _r
        _c = _c - 1
    elif _direction == UP:
        _r = _r - 1
        _c = _c
    elif _direction == DOWN:
        _r = _r + 1
        _c = _c

    return _r, _c


K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 9

L = int(input())
move_list = []
head_move_pointer = 0
tail_move_pointer = 0
for _ in range(L):
    X, C = input().split()
    move_list.append([int(X), C])

time = 0
board[0][0] = 1
Q = deque()
Q.append((0, 0, 0, 0, 1, RIGHT, RIGHT))
while Q:
    hr, hc, tr, tc, length, head_direction, tail_direction = Q.popleft()
    # 방향에 따른 머리 좌표 계산
    hr, hc = move_rc(hr, hc, head_direction)

    # 시간 증가
    time += 1

    if not (0 <= hr < N and 0 <= hc < N and board[hr][hc] != 1):
        break

    if board[hr][hc] != 9:
        # 꼬리 좌표 계산
        board[tr][tc] = 0
        tr, tc = move_rc(tr, tc, tail_direction)
        board[tr][tc] = 1
    else:
        length += 1

    board[hr][hc] = 1

    # 머리만 회전
    if head_move_pointer < L:
        X, C = move_list[head_move_pointer]
        if time == X:
            head_direction = rotate(head_direction, C)
            head_move_pointer += 1
    if tail_move_pointer < L:
        X, C = move_list[tail_move_pointer]
        # 꼬리만 회전
        if time - length + 1 == X:
            tail_direction = rotate(tail_direction, C)
            tail_move_pointer += 1

    Q.append((hr, hc, tr, tc, length, head_direction, tail_direction))

print(time)
